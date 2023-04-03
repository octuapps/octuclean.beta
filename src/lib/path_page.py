#!/usr/bin/python3

from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QToolButton, QListWidgetItem, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from .base_dir import Assets

import json


class ItemWidget(QWidget):
    def __init__(self, path: str, index: int, remove_callback: object = None):
        super().__init__(None)

        self.path = path
        self.index = index
        self.remove_callback = remove_callback

        self.grid_layout = QGridLayout(self)
        self.icon = QLabel(self)
        self.icon.setFixedSize(32, 32)
        self.icon.setPixmap(QIcon.fromTheme("folder").pixmap(32, 32))

        self.label = QLabel(self.path, self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.btn = QToolButton(self)
        self.btn.setIcon(QIcon.fromTheme("delete"))
        self.btn.clicked.connect(lambda: self.remove_callback(self.path))

        self.grid_layout.addWidget(self.icon, 0, 0)
        self.grid_layout.addWidget(self.label, 0, 1)
        self.grid_layout.addWidget(self.btn, 0, 2)

        self.setLayout(self.grid_layout)


class PathPage:
    def __init__(self, parent: object = None) -> None:
        self.ui = parent
        self.ui.path_list.setSpacing(1.5)
        self.ui.search_line.textChanged.connect(self.list_paths)

    def list_paths(self, search: str = "") -> None:
        self.ui.path_list.clear()
        for path in self.ui._data.get("paths", []):
            if search.lower().strip() in path.lower().strip() or not search.strip():
                item = QListWidgetItem(self.ui.path_list)
                item.setSizeHint(QSize(40, 40))
                widget = ItemWidget(path, self.ui.path_list.currentRow(), self.remove_path)
                self.ui.path_list.setItemWidget(item, widget)

    def add_path(self, path: str) -> None:
        with open(Assets.assets_dir("settings.json"), "w") as fw:
            data = self.ui._data
            if not path in data["paths"]:
                data["paths"].append(path)
            json.dump(data, fw, indent=4)
        self.list_paths()

    def remove_path(self, path: str) -> None:
        with open(Assets.assets_dir("settings.json"), "w") as fw:
            data = self.ui._data
            data["paths"].remove(path)
            json.dump(data, fw, indent=4)
        self.list_paths()