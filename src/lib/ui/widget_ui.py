# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(266, 133)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.remove_btn = QToolButton(Form)
        self.remove_btn.setObjectName(u"remove_btn")
        icon = QIcon()
        iconThemeName = u"delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../", QSize(), QIcon.Normal, QIcon.Off)

        self.remove_btn.setIcon(icon)
        self.remove_btn.setAutoRaise(True)

        self.gridLayout.addWidget(self.remove_btn, 2, 2, 1, 1)

        self.refresh_btn = QToolButton(Form)
        self.refresh_btn.setObjectName(u"refresh_btn")
        icon1 = QIcon()
        iconThemeName = u"reload"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../../../../../", QSize(), QIcon.Normal, QIcon.Off)

        self.refresh_btn.setIcon(icon1)
        self.refresh_btn.setAutoRaise(True)

        self.gridLayout.addWidget(self.refresh_btn, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.progress_bar = QProgressBar(Form)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.gridLayout.addWidget(self.progress_bar, 1, 0, 1, 3)

        self.path_name = QLabel(Form)
        self.path_name.setObjectName(u"path_name")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_name.sizePolicy().hasHeightForWidth())
        self.path_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.path_name.setFont(font)

        self.gridLayout.addWidget(self.path_name, 0, 0, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.remove_btn.setText("")
        self.refresh_btn.setText("")
        self.path_name.setText("")
    # retranslateUi

