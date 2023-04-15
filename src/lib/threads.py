from PySide6.QtCore import Signal, QThread
from .base_dir import Assets
from datetime import datetime

import json
import os


class DeletingFilesThread(QThread):
    progress = Signal(int)

    def __init__(self, parent: object):
        super().__init__(parent)
        self.parent = parent

    def delete_files_in_folder(self, folder_path: str) -> None:
        for fp in os.listdir(folder_path):
            fp = os.path.join(folder_path, fp)
            # I think that is danger for some files
            # if os.path.islink(fp):
            #     os.unlink(fp)
            try:
                if os.path.isdir(fp):
                    self.delete_files_in_folder(fp)
                    os.rmdir(fp)
                else:
                    os.remove(fp)
            except Exception:
                ...

    def run(self) -> None:
        paths = self.parent._data.get("paths", [])
        self.parent._alert_widget.title.setText("Deleting files...")
        self.parent._alert_widget.progress_bar.setRange(0, paths.__len__())
        for index, fp in enumerate(paths, 1):
            self.delete_files_in_folder(fp)
            self.progress.emit(index)


class FinishingFilesThread(QThread):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        with open(Assets.assets_dir("settings.json"), "w") as fw:
            self.parent._data["last_clean"] = datetime.now().timestamp()
            self.parent._data["clean_count"] += 1
            json.dump(self.parent._data, fw, indent=4)
            self.parent.set_last_state()
