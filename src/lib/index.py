from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, 
                               QToolButton, QSpacerItem, QSizePolicy)
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtCore import QDir, QUrl, QSize

from .base_dir import Assets
from .ui.window_ui import Ui_MainWindow
from .path_page import PathPage
from .utils import get_dir_size
from .alert_widget import AlertWidget
from .threads import DeletingFilesThread, FinishingFilesThread
from datetime import datetime

import os
import sys
import json
import psutil


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.load_data()
        self.setFixedSize(800, 550)

        self.is_dark = True
        self._path_page = PathPage(self)
        self._alert_widget = AlertWidget(self)
        self._alert_widget.hide()

        self.init()
        self.about_page()
        self.buttons_event()
        
        self.check_for_paths()

    def update_status_widget(self):
        self.load_data()
        self.get_path_count()
        self.state_widget()
        self.set_last_state()

    def init(self) -> None:
        self.theme_btn.setIcon(QIcon(Assets.icons("light.png")))
        self.clean_btn.setIcon(QIcon(Assets.icons("clean.svg")))
        self.theme_btn.setText("Light")
        self.set_theme("dark.qss")

    def get_path_count(self) -> None:
        """
        path not cleaning/of all paths
        """
        _len = str(self._data.get("paths", []).__len__())
        total = 0
        for fp in self._data.get("paths", []):
            if os.path.exists(fp) and get_dir_size(fp) > 1024:
                total += 1
        self.path_count.setText(f"{total}/{_len} not cleaning")

    def show_ui(self) -> None:
        self.show()
        self.update_status_widget()

    def load_data(self) -> None:
        with open(Assets.assets_dir("settings.json"), "r") as fr:
            self._data = json.load(fr)

    def about_page(self) -> None:
        self.about_icon.setPixmap(QIcon(Assets.icons("profile.png")).pixmap(140, 140))
        for i in self._data.get("accounts", []):
            btn = QToolButton(self)
            btn.setIconSize(QSize(32, 32))
            btn.setIcon(QIcon(Assets.icons("accounts", i.get("icon"))))
            btn.setObjectName("account_btn")
            btn.setText(i.get("url", ""))
            btn.setToolTip(i.get("name"))
            btn.clicked.connect(self.on_open_url)
            self.horizontalLayout.addWidget(btn)
        self.horizontalLayout.addSpacerItem(QSpacerItem(40, 40, QSizePolicy.Expanding))

    def on_open_url(self) -> None:
        QDesktopServices.openUrl(QUrl.fromUserInput(self.sender().text()))

    def buttons_event(self) -> None:
        self.home_btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.home_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.about_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.path_btn.clicked.connect(self.open_path_page)
        self.theme_btn.clicked.connect(self.switch_theme)
        self.add_btn.clicked.connect(self.on_add_path)
        self.clean_btn.clicked.connect(self.on_clean)
        self.stackedWidget.currentChanged.connect(self.check_for_paths)
        self.refresh_btn.clicked.connect(self.update_status_widget)

    def switch_theme(self) -> None:
        icon = Assets.icons("dark.png") if self.is_dark else Assets.icons("light.png")
        name = "Dark" if self.is_dark else "Light"
        
        self.theme_btn.setIcon(QIcon(icon))
        self.theme_btn.setText(name)
        self.set_theme(("light" if self.is_dark else "dark") + ".qss")

        self.is_dark = not self.is_dark

    def set_theme(self, name: str) -> None:
        with open(Assets.themes(name), "r") as fr:
            self.setStyleSheet(fr.read())

    def open_path_page(self) -> None:
        self.load_data()
        self._path_page.list_paths()
        self.stackedWidget.setCurrentIndex(1)

    def on_add_path(self) -> None:
        path = str(QFileDialog.getExistingDirectory(self, 
                                                    "Select Directory", 
                                                    QDir.homePath()))
        if path.strip():
            self.load_data()
            self._path_page.add_path(path)

    def state_widget(self) -> None:
        obj_Disk = psutil.disk_usage(QDir.rootPath())
        folders_size = 0
        for fp in self._data.get("paths", []):
            folders_size += get_dir_size(fp)

        disk_size = int(obj_Disk.total / (1024 ** 2))
        path_size = int(folders_size / (1024 ** 2))
        self.progress_bar.setValue((path_size / disk_size) * 100)

    def set_last_state(self) -> None:
        last_clean = self._data["last_clean"]
        if int(last_clean) != 0:
            self.last_clean.setText(
                datetime.fromtimestamp(last_clean).strftime("%r %m/%d/%Y"))
        else:
            self.last_clean.setText("PC not clean yet")
        self.clean_count.setText(str(self._data["clean_count"]))

    def on_clean(self) -> None:
        self._alert_widget.show_ui()
        
        with open(Assets.assets_dir("settings.json"), "w") as fw:
            folders_size = 0
            for fp in self._data.get("paths", []):
                folders_size += get_dir_size(fp)
            self._data["clean_size"] += folders_size
            json.dump(self._data, fw, indent=4)

        self._deleting_files()

    def _deleting_files(self) -> None:
        def update_progress(value):
            self._alert_widget.progress_bar.setValue(value)
            self._alert_widget.subtitle.setText(
                f"{value} of the {self._data.get('paths', []).__len__()} files completed.")

        rm_files = DeletingFilesThread(self)
        rm_files.progress.connect(update_progress)
        rm_files.finished.connect(self._finishing_files)
        rm_files.start()

    def _finishing_files(self) -> None:
        def on_finish():
            self._alert_widget.hide_ui()
            self.update_status_widget()

        finish_files = FinishingFilesThread(self)
        finish_files.finished.connect(on_finish)
        finish_files.start()

    def check_for_paths(self):
        self.clean_btn.setEnabled(bool(self._data.get("paths", [])))


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    
    app_name = "OctuClean.beta"
    
    app.setApplicationName(app_name)
    app.setApplicationDisplayName(app_name)
    app.setApplicationVersion("0.0")

    window.setWindowTitle(app_name)
    window.setWindowIcon(QIcon(Assets.icons("clean.svg")))

    window.show_ui()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()