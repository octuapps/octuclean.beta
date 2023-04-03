from PySide6.QtWidgets import (QWidget, QGridLayout, QGraphicsBlurEffect, 
                               QGraphicsOpacityEffect, QLabel, QProgressBar)
from PySide6.QtCore import Qt


class AlertWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QGridLayout(self)
        
        self.setWindowFlags(Qt.WindowType.Widget)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedSize(self.parent().size())
        self.setStyleSheet(
            f"background: {'#262721' if self.parent().is_dark else '#dddddd'};")

        self.set_parent_blur()
        self.set_widget_opacity()

        self.title = QLabel(self)
        self.title.setObjectName("load_title")
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setObjectName("load_progress_bar")
        self.progress_bar.setFixedWidth(350)
        self.subtitle = QLabel(self)
        self.subtitle.setObjectName("load_subtitle")
        
        self.title.setAlignment(Qt.AlignCenter)
        self.subtitle.setAlignment(Qt.AlignCenter)

        self.grid_layout.addWidget(self.title)
        self.grid_layout.addWidget(self.progress_bar)
        self.grid_layout.addWidget(self.subtitle)

        self.setLayout(self.grid_layout)
    
    def set_widget_opacity(self) -> None:
        # Opacity child self
        effect = QGraphicsOpacityEffect(self)
        effect.setOpacity(0.8)
        self.setGraphicsEffect(effect)

    def set_parent_blur(self) -> None:
        # Blur the main window
        effect = QGraphicsBlurEffect(self.parent().centralWidget())
        effect.setBlurRadius(0)
        self.parent().centralWidget().setGraphicsEffect(effect)

    def show_ui(self):
        self.parent().centralWidget().graphicsEffect().setBlurRadius(2)
        self.show()
    
    def hide_ui(self) -> None:
        self.parent().centralWidget().graphicsEffect().setBlurRadius(0)
        self.hide()