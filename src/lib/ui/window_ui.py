# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 220, 781, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 771, 301))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 761, 191))
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(70, 40, 251, 121))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.progress_bar = QProgressBar(self.widget_2)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.gridLayout_3.addWidget(self.progress_bar, 2, 0, 1, 2)

        self.clean_count = QLabel(self.widget_2)
        self.clean_count.setObjectName(u"clean_count")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clean_count.sizePolicy().hasHeightForWidth())
        self.clean_count.setSizePolicy(sizePolicy)
        self.clean_count.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.clean_count, 0, 0, 1, 1)

        self.path_count = QLabel(self.widget_2)
        self.path_count.setObjectName(u"path_count")
        sizePolicy.setHeightForWidth(self.path_count.sizePolicy().hasHeightForWidth())
        self.path_count.setSizePolicy(sizePolicy)
        self.path_count.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.path_count, 0, 1, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.last_clean = QLabel(self.widget_2)
        self.last_clean.setObjectName(u"last_clean")
        sizePolicy.setHeightForWidth(self.last_clean.sizePolicy().hasHeightForWidth())
        self.last_clean.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.last_clean, 3, 1, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(380, 40, 381, 111))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clean_btn = QToolButton(self.horizontalLayoutWidget)
        self.clean_btn.setObjectName(u"clean_btn")
        self.clean_btn.setIconSize(QSize(22, 22))
        self.clean_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.clean_btn.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.clean_btn)

        self.theme_btn = QToolButton(self.horizontalLayoutWidget)
        self.theme_btn.setObjectName(u"theme_btn")
        icon = QIcon()
        iconThemeName = u"style"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.theme_btn.setIcon(icon)
        self.theme_btn.setIconSize(QSize(22, 22))
        self.theme_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.theme_btn.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.theme_btn)

        self.refresh_btn = QToolButton(self.horizontalLayoutWidget)
        self.refresh_btn.setObjectName(u"refresh_btn")
        icon1 = QIcon()
        iconThemeName = u"reload"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.refresh_btn.setIcon(icon1)
        self.refresh_btn.setIconSize(QSize(22, 22))
        self.refresh_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.refresh_btn.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.refresh_btn)

        self.path_btn = QToolButton(self.horizontalLayoutWidget)
        self.path_btn.setObjectName(u"path_btn")
        icon2 = QIcon()
        iconThemeName = u"folder"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.path_btn.setIcon(icon2)
        self.path_btn.setIconSize(QSize(22, 22))
        self.path_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.path_btn.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.path_btn)

        self.about_btn = QToolButton(self.horizontalLayoutWidget)
        self.about_btn.setObjectName(u"about_btn")
        icon3 = QIcon()
        iconThemeName = u"info"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.about_btn.setIcon(icon3)
        self.about_btn.setIconSize(QSize(22, 22))
        self.about_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.about_btn.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.about_btn)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.search_btn = QToolButton(self.page_2)
        self.search_btn.setObjectName(u"search_btn")
        icon4 = QIcon()
        iconThemeName = u"search"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.search_btn.setIcon(icon4)

        self.gridLayout_2.addWidget(self.search_btn, 1, 1, 1, 1)

        self.search_line = QLineEdit(self.page_2)
        self.search_line.setObjectName(u"search_line")

        self.gridLayout_2.addWidget(self.search_line, 1, 0, 1, 1)

        self.add_btn = QToolButton(self.page_2)
        self.add_btn.setObjectName(u"add_btn")
        icon5 = QIcon()
        iconThemeName = u"add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.add_btn.setIcon(icon5)

        self.gridLayout_2.addWidget(self.add_btn, 3, 1, 1, 1)

        self.path_list = QListWidget(self.page_2)
        self.path_list.setObjectName(u"path_list")

        self.gridLayout_2.addWidget(self.path_list, 2, 0, 1, 2)

        self.home_btn = QToolButton(self.page_2)
        self.home_btn.setObjectName(u"home_btn")
        icon6 = QIcon()
        iconThemeName = u"home"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.home_btn.setIcon(icon6)

        self.gridLayout_2.addWidget(self.home_btn, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_4 = QWidget(self.page_3)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.about_icon = QLabel(self.widget_4)
        self.about_icon.setObjectName(u"about_icon")
        self.about_icon.setMinimumSize(QSize(140, 140))
        self.about_icon.setMaximumSize(QSize(140, 140))
        self.about_icon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.about_icon, 0, 0, 1, 1)

        self.about_app_name = QLabel(self.widget_4)
        self.about_app_name.setObjectName(u"about_app_name")
        sizePolicy.setHeightForWidth(self.about_app_name.sizePolicy().hasHeightForWidth())
        self.about_app_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.about_app_name.setFont(font1)
        self.about_app_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.about_app_name, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_4, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.widget_3 = QWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.widget_3.setFont(font2)
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.label_6, 3, 1, 1, 3)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout_5.addWidget(self.widget_5, 4, 1, 1, 3)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.label_4, 1, 1, 1, 3)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 3)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.label_10, 2, 1, 1, 2)


        self.gridLayout_6.addWidget(self.widget_3, 2, 0, 1, 3)

        self.home_btn_2 = QToolButton(self.page_3)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setIcon(icon6)

        self.gridLayout_6.addWidget(self.home_btn_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clean_count.setText("")
        self.path_count.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Last Clean:", None))
        self.last_clean.setText("")
        self.clean_btn.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.theme_btn.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.path_btn.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.search_btn.setText("")
        self.search_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.add_btn.setText("")
        self.home_btn.setText("")
        self.about_icon.setText("")
        self.about_app_name.setText(QCoreApplication.translate("MainWindow", u"OctuClean.beta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"+(967) 776973923", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Accounts: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<a href=\"mail:omamkaz@gmail.com\">omamkaz@gmail.com</a>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Osama Alzabidi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dev by: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"User ID:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"omamkaz", None))
        self.home_btn_2.setText("")
    # retranslateUi

