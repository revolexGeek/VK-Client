from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QPropertyAnimation, QRect, QPoint, QEasingCurve
import sys
from time import sleep
import getpass
import pathlib
import vk_api
import json
from PyQt5.QtGui import QPixmap, QIcon
from urllib import request
from PyQt5.QtCore import Qt
import datetime

token__ = "vkhost.github.io --> kate_mobile"
assetspath = str(pathlib.Path().absolute()) + "\\assets"
username = getpass.getuser()


class ImageViewer(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1353, 894)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: \"#222222\"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(assetspath + "\\warning.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", "VKMANAGER | Image-viewer | Coded by revolex 30.03.2021"))


class MainWindow_(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1018, 738)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 101, 741))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: \"#767676\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 95, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(99, 300))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("color: \"#222222\";")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(99, 16777215))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: \"#222222\";")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(99, 16777215))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: \"#222222\";")
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(80, 0, 20, 251))
        self.frame_4.setStyleSheet("color: \"#222222\";\n"
                                   "background-color: \"#222222\";\n"
                                   "border: 1px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 260, 21, 251))
        self.frame_5.setStyleSheet("color: \"#222222\";\n"
                                   "background-color: \"#222222\";\n"
                                   "border: 1px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setEnabled(True)
        self.frame_6.setGeometry(QtCore.QRect(80, 250, 21, 251))
        self.frame_6.setStyleSheet("color: \"#222222\";\n"
                                   "background-color: \"#222222\";\n"
                                   "border: 1px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setGeometry(QtCore.QRect(0, 260, 21, 251))
        self.frame_8.setStyleSheet("color: \"#222222\";\n"
                                   "background-color: \"#222222\";\n"
                                   "border: 1px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setEnabled(True)
        self.frame_9.setGeometry(QtCore.QRect(80, 500, 21, 251))
        self.frame_9.setStyleSheet("color: \"#222222\";\n"
                                   "background-color: \"#222222\";\n"
                                   "border: 1px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(0, 260, 21, 251))
        self.frame_10.setStyleSheet("color: \"#222222\";\n"
                                    "background-color: \"#222222\";\n"
                                    "border: 1px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(100, 39, 921, 701))
        self.frame_2.setStyleSheet("background-color: \"#444444\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 921, 701))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 921, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: \"#111111\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(210, 110, 102, 542))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(100, 100))
        self.label_8.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_8.setBaseSize(QtCore.QSize(200, 200))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("border: 3px solid gray;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(100, 100))
        self.label_10.setStyleSheet("border: 3px solid gray;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(100, 100))
        self.label_12.setStyleSheet("border: 3px solid gray;")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(100, 100))
        self.label_11.setStyleSheet("border: 3px solid gray;")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(100, 100))
        self.label_9.setStyleSheet("border: 3px solid gray;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(320, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: \"#111111\";\n"
                                   "border-radius: 13px;\n"
                                   "background-color: \"#797979\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(320, 160, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: \"#111111\";\n"
                                   "border-radius: 13px;\n"
                                   "background-color: \"#767676\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(320, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(320, 270, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(320, 330, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(320, 380, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(320, 490, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(320, 440, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(320, 600, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(320, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(580, 110, 101, 101))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_21.setScaledContents(False)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(False)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(580, 220, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.page)
        self.label_23.setGeometry(QtCore.QRect(580, 330, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.page)
        self.label_24.setGeometry(QtCore.QRect(580, 440, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.page)
        self.label_25.setGeometry(QtCore.QRect(580, 550, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page)
        self.label_26.setGeometry(QtCore.QRect(470, 110, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.page)
        self.label_27.setGeometry(QtCore.QRect(470, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.page)
        self.label_28.setGeometry(QtCore.QRect(470, 330, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.page)
        self.label_29.setGeometry(QtCore.QRect(470, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page)
        self.label_30.setGeometry(QtCore.QRect(470, 550, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(0, 30, 921, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: \"#111111\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_59 = QtWidgets.QLabel(self.page_2)
        self.label_59.setGeometry(QtCore.QRect(380, 470, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.page_2)
        self.label_60.setGeometry(QtCore.QRect(380, 530, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.page_2)
        self.label_61.setGeometry(QtCore.QRect(530, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.page_2)
        self.label_62.setGeometry(QtCore.QRect(380, 250, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.page_2)
        self.label_63.setGeometry(QtCore.QRect(530, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.page_2)
        self.label_64.setGeometry(QtCore.QRect(380, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.page_2)
        self.label_65.setGeometry(QtCore.QRect(380, 420, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.page_2)
        self.label_66.setGeometry(QtCore.QRect(530, 530, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.page_2)
        self.label_67.setGeometry(QtCore.QRect(380, 140, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.page_2)
        self.label_68.setGeometry(QtCore.QRect(530, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.page_2)
        self.label_69.setGeometry(QtCore.QRect(380, 580, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_4.setGeometry(
            QtCore.QRect(270, 90, 102, 542))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_70 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMaximumSize(QtCore.QSize(100, 100))
        self.label_70.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_70.setBaseSize(QtCore.QSize(200, 200))
        self.label_70.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_70.setAutoFillBackground(False)
        self.label_70.setStyleSheet("border: 3px solid gray;")
        self.label_70.setText("")
        self.label_70.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_70.setScaledContents(False)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setWordWrap(False)
        self.label_70.setOpenExternalLinks(False)
        self.label_70.setObjectName("label_70")
        self.verticalLayout_4.addWidget(self.label_70)
        self.label_71 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMaximumSize(QtCore.QSize(100, 100))
        self.label_71.setStyleSheet("border: 3px solid gray;")
        self.label_71.setText("")
        self.label_71.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_71.setScaledContents(False)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setWordWrap(False)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_4.addWidget(self.label_71)
        self.label_72 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMaximumSize(QtCore.QSize(100, 100))
        self.label_72.setStyleSheet("border: 3px solid gray;")
        self.label_72.setText("")
        self.label_72.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_72.setScaledContents(False)
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setWordWrap(False)
        self.label_72.setObjectName("label_72")
        self.verticalLayout_4.addWidget(self.label_72)
        self.label_73 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMaximumSize(QtCore.QSize(100, 100))
        self.label_73.setStyleSheet("border: 3px solid gray;")
        self.label_73.setText("")
        self.label_73.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_73.setScaledContents(False)
        self.label_73.setAlignment(QtCore.Qt.AlignCenter)
        self.label_73.setWordWrap(False)
        self.label_73.setObjectName("label_73")
        self.verticalLayout_4.addWidget(self.label_73)
        self.label_74 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMaximumSize(QtCore.QSize(100, 100))
        self.label_74.setStyleSheet("border: 3px solid gray;")
        self.label_74.setText("")
        self.label_74.setPixmap(QtGui.QPixmap(
            assetspath + "\\users\\nophoto.png"))
        self.label_74.setScaledContents(False)
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setWordWrap(False)
        self.label_74.setObjectName("label_74")
        self.verticalLayout_4.addWidget(self.label_74)
        self.label_75 = QtWidgets.QLabel(self.page_2)
        self.label_75.setGeometry(QtCore.QRect(380, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.page_2)
        self.label_76.setGeometry(QtCore.QRect(380, 360, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std Book")
        font.setPointSize(10)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#767676\";")
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.page_2)
        self.label_77.setGeometry(QtCore.QRect(530, 420, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.page_2)
        self.label_78.setGeometry(QtCore.QRect(380, 310, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 13px;\n"
                                    "background-color: \"#797979\";")
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(270, 640, 321, 31))
        self.lineEdit.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 10px;\n"
                                    "background-color: \"#767676\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_79 = QtWidgets.QLabel(self.page_2)
        self.label_79.setGeometry(QtCore.QRect(600, 640, 31, 31))
        self.label_79.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 10px;\n"
                                    "background-color: \"#767676\";")
        self.label_79.setText("")
        self.label_79.setPixmap(QtGui.QPixmap(assetspath + "\\send.png"))
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setObjectName("label_79")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.radioButton = QtWidgets.QRadioButton(self.page_3)
        self.radioButton.setGeometry(QtCore.QRect(260, 350, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: \"#111111\";")
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 300, 921, 41))
        font = QtGui.QFont()
        font.setFamily("Circular Std Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: \"#111111\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_2.setGeometry(QtCore.QRect(370, 350, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: \"#111111\";")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_3.setGeometry(QtCore.QRect(460, 350, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: \"#111111\";")
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_4.setGeometry(QtCore.QRect(580, 350, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Circular Std Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: \"#111111\";")
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.stackedWidget.addWidget(self.page_3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(100, 0, 921, 41))
        self.frame_3.setStyleSheet("background-color: \"#222222\";")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(50, -5, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: gray;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            assetspath + "\\command-window.png"))
        self.label_2.setObjectName("label_2")
        self.label_80 = QtWidgets.QLabel(self.frame_3)
        self.label_80.setGeometry(QtCore.QRect(870, 10, 41, 21))
        self.label_80.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 10px;\n"
                                    "background-color: \"#767676\";")
        self.label_80.setText("")
        self.label_80.setPixmap(QtGui.QPixmap(assetspath + "\\close.png"))
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.frame_3)
        self.label_81.setGeometry(QtCore.QRect(800, 10, 61, 21))
        self.label_81.setStyleSheet("color: \"#111111\";\n"
                                    "border-radius: 10px;\n"
                                    "background-color: \"#767676\";")
        self.label_81.setText("")
        self.label_81.setPixmap(QtGui.QPixmap(assetspath + "\\hide.png"))
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        MainWindow.setCentralWidget(self.centralwidget)

        self.frame_4.setStyleSheet("background-color: #222222")
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''def Mainclicked():
                                    self.frame_4.setStyleSheet("color: \"#222222\";\n"
                                    "background-color: \"#222222\";\n"
                                    "border: 1px;")
                                    self.frame_5.setStyleSheet("background-color: #767676;")
                                    self.frame_6.setStyleSheet("background-color: #767676;")
                                    self.label.setText("Main")
                                def Settingsclicked():
                                    self.frame_5.setStyleSheet("color: \"#222222\";\n"
                                    "background-color: \"#222222\";\n"
                                    "border: 1px;")
                                    self.frame_4.setStyleSheet("background-color: #767676;")
                                    self.frame_6.setStyleSheet("background-color: #767676;")
                                    self.label.setText("Settings")
                                def Themeclicked():
                                    self.frame_6.setStyleSheet("color: \"#222222\";\n"
                                    "background-color: \"#222222\";\n"
                                    "border: 1px;")
                                    self.frame_4.setStyleSheet("background-color: #767676;")
                                    self.frame_5.setStyleSheet("background-color: #767676;")
                                    self.label.setText("Theme")'''

        # from main to settings
        # self.anim.setStartValue(QPoint(80,0))
        # self.anim.setEndValue(QPoint(80,250))
        # from main to themes
        # self.anim.setStartValue(QPoint(80,0))
        # self.anim.setEndValue(QPoint(80,500))
        # from themes to main
        #
        #
        lastseen = "Users"

        #        self.frame_4.setGeometry(QtCore.QRect(79, 0, 21, 251))

        try:
            token = token__
            vk = vk_api.VkApi(token=token).get_api()
            vk_ = vk_api.VkApi(token=token)
            id__ = 239652629
            req = json.dumps(vk_.method("users.get"))
            req_ = json.loads(req)
            __id = req_[0]['id']
            print("Got my id: " + str(__id))
        except Exception as e:
            print("Error! Maybe token is broken!", ' ', e)

        #def draculatheme():

        def getlastmsgtime(id_):
            pretty_json = json.dumps(vk_.method("messages.getHistory", {
                                     'user_id': id_, 'count': '1'}), indent=2)
            ppretty_json = json.loads(pretty_json)
            timestamp = int(ppretty_json['items'][0]['date'])
            value = datetime.datetime.fromtimestamp(timestamp)
            x = (value.strftime('%H:%M \n %d-%m'))
            return x

        def getlastmsg(id_):
            pretty_json = json.dumps(vk_.method("messages.getHistory", {
                                     'user_id': id_, 'count': '1'}), indent=2)
            ppretty_json = json.loads(pretty_json)
            print(ppretty_json)
            x = ppretty_json['items'][0]['text']
            if len(x) >= 40:
                x = str(ppretty_json['items'][0]['text'])[0:40] + ' ...'
            else:
                if x == '':
                    x = "[Image]"
            return x

        def getidsfromconversation():
            global lastconvs
            lastconvs = []
            global lastconvs__
            lastconvs__ = []
            global images
            images = []
            global online
            online = []
            try:
                try:
                    fr = json.dumps(vk_.method(
                        "messages.getConversations", {'count': '5'}))
                    frr = json.loads(fr)
                    for i in range(0, 5+1):
                        lastconvs.append(
                            frr['items'][i]['conversation']['peer']['id'])
                        print(frr['items'][i]['conversation']['peer']['id'])
                    print(lastconvs, " lastconvs")
                    print(lastconvs__, " lastconvs__")
                    gr = json.dumps(vk_.method("users.get", {'user_ids': '%s, %s, %s, %s, %s' % (
                        lastconvs[0], lastconvs[1], lastconvs[2], lastconvs[3], lastconvs[4]),
                        'fields': 'photo_100, online'}))
                    grr = json.loads(gr)

                except Exception as e:
                    print(str(e) + ' Line: 1102')

                try:
                    for s in range(0, 5):
                        if grr[s]['first_name'] == "DELETED":
                            lastconvs__.append("Group")
                            images.append(
                                "https://image.flaticon.com/icons/png/128/681/681494.png")
                            online.append('-')
                        else:
                            lastconvs__.append(
                                grr[s]['first_name'] + ' ' + grr[s]['last_name'])
                            images.append(grr[s]['photo_100'])
                        print(grr[s]['first_name'])
                        if grr[s]['online'] == 1:
                            online.append("Online")
                        elif grr[s]['online'] == 0 and grr[s]['first_name'] != "DELETED":
                            online.append("Offline")
                        else:
                            online.append("-")
                except Exception as f:
                    print(str(f) + ' Line: 1122')
                # print(images)
                print(online)
                # print(lastconvs__)

                # Name
                try:
                    self.label_6.setText(lastconvs__[0])
                    self.label_13.setText(lastconvs__[1])
                    self.label_16.setText(lastconvs__[2])
                    self.label_18.setText(lastconvs__[3])
                    self.label_20.setText(lastconvs__[4])
                    # Status 26 30

                    if online[0] == "Online":
                        self.label_26.setText(online[0])
                        self.label_26.setStyleSheet("color: green;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    elif online[0] == "Offline":
                        self.label_26.setText(online[0])
                        self.label_26.setStyleSheet("color: red;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    else:
                        self.label_26.setText("-")

                    if online[1] == "Online":
                        self.label_27.setText(online[1])
                        self.label_27.setStyleSheet("color: green;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    elif online[1] == "Offline":
                        self.label_27.setText(online[1])
                        self.label_27.setStyleSheet("color: red;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    else:
                        self.label_27.setText("-")

                    if online[2] == "Online":
                        self.label_28.setText(online[2])
                        self.label_28.setStyleSheet("color: green;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    elif online[2] == "Offline":
                        self.label_28.setText(online[2])
                        self.label_28.setStyleSheet("color: red;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    else:
                        self.label_28.setText("-")

                    if online[3] == "Online":
                        self.label_29.setText(online[3])
                        self.label_29.setStyleSheet("color: green;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    elif online[3] == "Offline":
                        self.label_29.setText(online[3])
                        self.label_29.setStyleSheet("color: red;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    else:
                        self.label_29.setText("-")

                    if online[4] == "Online":
                        self.label_30.setText(online[4])
                        self.label_30.setStyleSheet("color: green;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    elif online[4] == "Offline":
                        self.label_30.setText(online[4])
                        self.label_30.setStyleSheet("color: red;\n"
                                                    "border-radius: 13px;\n"
                                                    "background-color: \"#797979\";")
                    else:
                        self.label_30.setText("-")

                    # Image
                    for i in range(0, 5):
                        url = images[i]
                        data = request.urlopen(url).read()
                        pixmap = QPixmap()
                        pixmap.loadFromData(data)
                        if i == 0:
                            self.label_8.setPixmap(pixmap)
                        if i == 1:
                            self.label_10.setPixmap(pixmap)
                        if i == 2:
                            self.label_12.setPixmap(pixmap)
                        if i == 3:
                            self.label_11.setPixmap(pixmap)
                        if i == 4:
                            self.label_9.setPixmap(pixmap)
                    # Last messages

                    self.label_7.setText(getlastmsg(lastconvs[0]))
                    self.label_14.setText(getlastmsg(lastconvs[1]))
                    self.label_15.setText(getlastmsg(lastconvs[2]))
                    self.label_17.setText(getlastmsg(lastconvs[3]))
                    self.label_19.setText(getlastmsg(lastconvs[4]))
                    self.frame_6.setVisible(False)
                    self.frame_9.setVisible(False)

                    # Lastmsg time
                    for i in range(0, 5):
                        f = getlastmsgtime(lastconvs[i])
                        if i == 0:
                            self.label_21.setText(f)
                        if i == 1:
                            self.label_22.setText(f)
                        if i == 2:
                            self.label_23.setText(f)
                        if i == 3:
                            self.label_24.setText(f)
                        if i == 4:
                            self.label_25.setText(f)
                except Exception as q:
                        print(str(q) + ' Line: 1241')

            except Exception as a:
                print(str(a) + ' Line: 1235' + str(Exception))

        getidsfromconversation()

        def switchtomain():
            if self.frame_4.isVisible() == True:
                self.frame_6.setVisible(False)
                self.frame_9.setVisible(False)
                self.frame_4.setVisible(True)
                self.stackedWidget.setCurrentIndex(0)
                lastseen = "Users"
                self.label.setText(lastseen)
            if self.frame_6.isVisible() == True:
                self.frame_6.setVisible(False)
                self.frame_9.setVisible(False)
                self.frame_4.setVisible(True)
                self.stackedWidget.setCurrentIndex(0)
                lastseen = "Users"
                self.label.setText(lastseen)
            if self.frame_9.isVisible() == True:
                self.frame_6.setVisible(False)
                self.frame_9.setVisible(False)
                self.frame_4.setVisible(True)
                self.stackedWidget.setCurrentIndex(0)
                lastseen = "Users"
                self.label.setText(lastseen)
            getidsfromconversation()

        def switchtosettings():
            if self.frame_4.isVisible() == True:
                self.frame_6.setVisible(True)
                self.frame_9.setVisible(False)
                self.frame_4.setVisible(False)
                self.stackedWidget.setCurrentIndex(1)
                lastseen = "Chat"
                self.label.setText(lastseen)
            if self.frame_6.isVisible() == True:
                self.frame_6.setVisible(True)
                self.frame_9.setVisible(False)
                self.frame_4.setVisible(False)
                self.stackedWidget.setCurrentIndex(1)
                lastseen = "Chat"
                self.label.setText(lastseen)
            if self.frame_9.isVisible() == True:
                self.frame_6.setVisible(True)
                self.frame_9.setVisible(False)
                self.frame_4.setVisible(False)
                self.stackedWidget.setCurrentIndex(1)
                lastseen = "Chat"
                self.label.setText(lastseen)
            getmsghistory()

        def switchtothemes():
            if self.frame_4.isVisible() == True:
                self.frame_6.setVisible(False)
                self.frame_9.setVisible(True)
                self.frame_4.setVisible(False)
                self.stackedWidget.setCurrentIndex(2)
                lastseen = "Themes"
                self.label.setText(lastseen)
            if self.frame_6.isVisible() == True:
                self.frame_6.setVisible(False)
                self.frame_9.setVisible(True)
                self.frame_4.setVisible(False)
                self.stackedWidget.setCurrentIndex(2)
                lastseen = "Themes"
                self.label.setText(lastseen)
            if self.frame_9.isVisible() == True:
                self.frame_6.setVisible(False)
                self.frame_9.setVisible(True)
                self.frame_4.setVisible(False)
                self.stackedWidget.setCurrentIndex(2)
                lastseen = "Themes"
                self.label.setText(lastseen)

            #        self.frame_4.setGeometry(QtCore.QRect(79, 0, 21, 251))

        # 3m 4s 2t
        self.pushButton_3.clicked.connect(switchtomain)
        self.pushButton_4.clicked.connect(switchtosettings)
        self.pushButton_2.clicked.connect(switchtothemes)

        def getchatid(i):
            global chatid
            global selected
            chatid = lastconvs[i]
            selected = i
            print(chatid)
            print(selected)
            switchtosettings()

        self.label_6.mousePressEvent = (lambda x: getchatid(0))
        self.label_13.mousePressEvent = (lambda x: getchatid(1))
        self.label_16.mousePressEvent = (lambda x: getchatid(2))
        self.label_18.mousePressEvent = (lambda x: getchatid(3))
        self.label_20.mousePressEvent = (lambda x: getchatid(4))

        def sendmsg():
            try:
                if self.lineEdit.text() != '':
                    vk.messages.send(user_id=int(chatid), message=self.lineEdit.text(),
                                     random_id=0)
                    getmsghistory()
                    self.lineEdit.setText('')
                else:
                    print("Text is empty!")
            except Exception as o:
                print(o)

        self.label_79.mousePressEvent = (lambda x: sendmsg())
        self.label_80.mousePressEvent = (lambda x: self.close())  # close btn
        self.label_81.mousePressEvent = (
            lambda x: print("Not working by the way!"))  # hide btn

        # def sendImage():

        def getmsghistory():
            '''
            1. Сделать запрос getHistory
            2. Из него спарсить 
                - profiles --> photo_100, first_name, last_name
                - items --> text [i], date [i]
            '''
            try:
                me = ""
                partner = ""
                try:
                    if chatid != __id:
                        getuserphotos = json.dumps(vk_.method("users.get",
                                                              {'user_ids': '%s, %s' % (str(chatid), str(__id)),
                                                               'fields': 'photo_100'}))
                        getuserphotos_ = json.loads(getuserphotos)
                        if getuserphotos_[0]['id'] == str(__id):
                            me = str(getuserphotos_[0]['photo_100'])
                            partner = str(getuserphotos_[1]['photo_100'])
                        else:
                            me = str(getuserphotos_[1]['photo_100'])
                            partner = str(getuserphotos_[0]['photo_100'])
                    else:
                        getuserphotos = json.dumps(vk_.method("users.get",
                                                              {'user_ids': '%s' % (str(__id)),
                                                               'fields': 'photo_100'}))
                        getuserphotos_ = json.loads(getuserphotos)
                        me = str(getuserphotos_[0]['photo_100'])
                        partner = str(getuserphotos_[0]['photo_100'])

                except Exception as q:
                    print("getuserphotos " + str(q))

                images = []
                global messagesImg
                messagesImg = []
                names = []
                messages = []
                dates = []

                # Создаем запрос к Api
                fr = json.dumps(vk_.method("messages.getHistory", {
                                'count': '30', 'user_id': chatid, 'extended': True}))
                frr = json.loads(fr)

                # Скапливаем смски и их дату написания
                for i in range(0, 5):
                    if frr['items'][i]['text'] != '':
                        if len(str(frr['items'][i]['text'])) >= 35:
                            messages.append(
                                str(frr['items'][i]['text'])[0:35] + ' ...')
                        else:
                            messages.append(frr['items'][i]['text'])

                        if frr['items'][i]['from_id'] == chatid:
                            names.append(lastconvs__[selected])
                            images.append(partner)

                        if frr['items'][i]['from_id'] == __id:
                            names.append("Viktor Pospelov")
                            images.append(me)

                        if frr['items'][i]['from_id'] != __id and frr['items'][i]['from_id'] != chatid:
                            names.append("Unknown User")
                        messagesImg.append(
                            "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/20080306152140-interrogacion1.png/120px-20080306152140-interrogacion1.png")
                    else:
                        if frr['items'][i]['from_id'] == chatid:
                            names.append(lastconvs__[selected])
                            images.append(partner)
                        elif frr['items'][i]['from_id'] == __id:
                            names.append("Viktor Pospelov")
                            images.append(me)
                        else:
                            names.append("Unknown user")
                            images.append(
                                "https://img.icons8.com/wired/2x/anonymous-mask.png")

                        # Errors

                        if frr['items'][i]['attachments'][0]['type'] != "photo" and frr['items'][i]['attachments'][0][
                                'type'] != "sticker":
                            messages.append("[WallRepost/VoiceMessage]")
                            messagesImg.append(
                                "https://www.freeiconspng.com/uploads/the-error-of-a-frown-the-red-circular-plate-photos-24.png")

                        if frr['items'][i]['attachments'][0]['type'] == "photo":
                            messages.append("[Image] (click to open!)")
                            messagesImg.append(
                                frr['items'][i]['attachments'][0]['photo']['sizes'][6]['url'])

                        if frr['items'][i]['attachments'][0]['type'] == "sticker":
                            messages.append("[Sticker] (Click to open!)")
                            messagesImg.append(
                                frr['items'][i]['attachments'][0]['sticker']['images'][1]['url'])

                    dates.append(frr['items'][i]['date'])

                # Расставляем время сообщениям
                for s in reversed(range(0, 5)):
                    timestamp = int(dates[s])
                    value = datetime.datetime.fromtimestamp(timestamp)
                    x = (value.strftime('%H:%M'))
                    if s == 4:
                        self.label_68.setText(x)
                    if s == 3:
                        self.label_63.setText(x)
                    if s == 2:
                        self.label_61.setText(x)
                    if s == 1:
                        self.label_77.setText(x)
                    if s == 0:
                        self.label_66.setText(x)

                # Расставляем текст сообщений
                for i in reversed(range(0, 5)):
                    if i == 4:
                        self.label_67.setText(messages[i])
                    if i == 3:
                        self.label_62.setText(messages[i])
                    if i == 2:
                        self.label_76.setText(messages[i])
                    if i == 1:
                        self.label_59.setText(messages[i])
                    if i == 0:
                        self.label_69.setText(messages[i])

                # Расставляем имена
                for i in reversed(range(0, 5)):
                    if i == 4:
                        self.label_64.setText(names[i])
                    if i == 3:
                        self.label_75.setText(names[i])
                    if i == 2:
                        self.label_78.setText(names[i])
                    if i == 1:
                        self.label_65.setText(names[i])
                    if i == 0:
                        self.label_60.setText(names[i])

                # Расставляем картинки
                for i in reversed(range(0, 5)):
                    url = images[i]
                    data = request.urlopen(url).read()
                    pixmap = QPixmap()
                    pixmap.loadFromData(data)
                    if i == 4:
                        self.label_70.setPixmap(pixmap)
                    if i == 3:
                        self.label_71.setPixmap(pixmap)
                    if i == 2:
                        self.label_72.setPixmap(pixmap)
                    if i == 1:
                        self.label_73.setPixmap(pixmap)
                    if i == 0:
                        self.label_74.setPixmap(pixmap)

                print(images, ' ', names, ' ', messages, ' ', dates)
                print()
                print(messages)
                print(messagesImg)
            except Exception as a:
                print(a)

        self.frame.setStyleSheet("background-color: #767676;")

        def getImageUrl(i):
            try:
                url_ = messagesImg[i]
                openImageView(url_)
            except Exception as a:
                print(a)

        self.label_67.mousePressEvent = (lambda x: getImageUrl(4))
        self.label_62.mousePressEvent = (lambda x: getImageUrl(3))
        self.label_76.mousePressEvent = (lambda x: getImageUrl(2))
        self.label_59.mousePressEvent = (lambda x: getImageUrl(1))
        self.label_69.mousePressEvent = (lambda x: getImageUrl(0))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Users"))
        self.pushButton_4.setText(_translate("MainWindow", "Chat"))
        self.pushButton_2.setText(_translate("MainWindow", "Themes"))
        self.label_4.setText(_translate("MainWindow", "Conversations"))
        self.label_6.setText(_translate("MainWindow", "{Name}"))
        self.label_7.setText(_translate("MainWindow", "{LastMessage}"))
        self.label_13.setText(_translate("MainWindow", "{Name}"))
        self.label_14.setText(_translate("MainWindow", "{LastMessage}"))
        self.label_16.setText(_translate("MainWindow", "{Name}"))
        self.label_15.setText(_translate("MainWindow", "{LastMessage}"))
        self.label_17.setText(_translate("MainWindow", "{LastMessage}"))
        self.label_18.setText(_translate("MainWindow", "{Name}"))
        self.label_19.setText(_translate("MainWindow", "{LastMessage}"))
        self.label_20.setText(_translate("MainWindow", "{Name}"))
        self.label_21.setText(_translate("MainWindow", "{Date}"))
        self.label_22.setText(_translate("MainWindow", "{Date}"))
        self.label_23.setText(_translate("MainWindow", "{Date}"))
        self.label_24.setText(_translate("MainWindow", "{Date}"))
        self.label_25.setText(_translate("MainWindow", "{Date}"))
        self.label_26.setText(_translate("MainWindow", "{Status}"))
        self.label_27.setText(_translate("MainWindow", "{Status}"))
        self.label_28.setText(_translate("MainWindow", "{Status}"))
        self.label_29.setText(_translate("MainWindow", "{Status}"))
        self.label_30.setText(_translate("MainWindow", "{Status}"))
        self.label_5.setText(_translate("MainWindow", "Chat"))
        self.label_59.setText(_translate("MainWindow", "{Message}"))
        self.label_60.setText(_translate("MainWindow", "{Name}"))
        self.label_61.setText(_translate("MainWindow", "{Time}"))
        self.label_62.setText(_translate("MainWindow", "{Message}"))
        self.label_63.setText(_translate("MainWindow", "{Time}"))
        self.label_64.setText(_translate("MainWindow", "{Name}"))
        self.label_65.setText(_translate("MainWindow", "{Name}"))
        self.label_66.setText(_translate("MainWindow", "{Time}"))
        self.label_67.setText(_translate("MainWindow", "{Message}"))
        self.label_68.setText(_translate("MainWindow", "{Time}"))
        self.label_69.setText(_translate("MainWindow", "{Message}"))
        self.label_75.setText(_translate("MainWindow", "{Name}"))
        self.label_76.setText(_translate("MainWindow", "{Message}"))
        self.label_77.setText(_translate("MainWindow", "{Time}"))
        self.label_78.setText(_translate("MainWindow", "{Name}"))
        self.lineEdit.setText(_translate("MainWindow", "Write a message..."))
        self.radioButton.setText(_translate("MainWindow", "Light"))
        self.label_3.setText(_translate("MainWindow", "Available Themes"))
        self.radioButton_2.setText(_translate("MainWindow", "Dark"))
        self.radioButton_3.setText(_translate("MainWindow", "Midnight"))
        self.radioButton_4.setText(_translate("MainWindow", "Dracula"))
        self.label.setText(_translate("MainWindow", "Users"))


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(398, 300)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("../../back.gif"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: violet;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Circular Std")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie(r"C:\Users\revolex\Desktop\back.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "LOADING..."))
        self.label_3.setText(_translate(
            "MainWindow", "We will make your day!"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#ee82ee;\">MY</span>MANAGER</p></body></html>"))


def loadscreen():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sleep(3)
    MainWindow.hide()

    # sys.exit(app.exec_())


def proga():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow_()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def openImageView(url):
    try:
        data = request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        dlg = QtWidgets.QDialog()
        ui = ImageViewer()
        ui.setupUi(dlg)
        ui.label.setPixmap(pixmap)
        dlg.exec_()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # loadscreen()
    proga()

# Day 2: 1493
# Day 3: ?
'''
ToDo:
1. Доделать темы
2. Пофиксить долгую загрузку / Сделать loading форму исправной
3. Исправить отображение сообщений группы
4. Логин в программу
'''
