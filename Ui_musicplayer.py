# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\TestCode\music_player\musicplayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(100, 20, 400, 350))
        self.frame.setStyleSheet("QFrame{\n"
"    border:2px solid black;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(70, 30, 256, 201))
        self.listWidget.setObjectName("listWidget")
        self.btn_1 = QtWidgets.QPushButton(self.frame)
        self.btn_1.setGeometry(QtCore.QRect(50, 280, 41, 23))
        self.btn_1.setObjectName("btn_1")
        self.slider_music = QtWidgets.QSlider(self.frame)
        self.slider_music.setGeometry(QtCore.QRect(70, 240, 251, 22))
        self.slider_music.setOrientation(QtCore.Qt.Horizontal)
        self.slider_music.setObjectName("slider_music")
        self.btn_2 = QtWidgets.QPushButton(self.frame)
        self.btn_2.setGeometry(QtCore.QRect(110, 280, 41, 23))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.frame)
        self.btn_3.setGeometry(QtCore.QRect(170, 280, 41, 23))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.frame)
        self.btn_4.setGeometry(QtCore.QRect(230, 280, 41, 23))
        self.btn_4.setObjectName("btn_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 280, 31, 21))
        self.label.setObjectName("label")
        self.slider_vol = QtWidgets.QSlider(self.frame)
        self.slider_vol.setGeometry(QtCore.QRect(330, 270, 20, 41))
        self.slider_vol.setOrientation(QtCore.Qt.Vertical)
        self.slider_vol.setObjectName("slider_vol")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_1.setText(_translate("MainWindow", "last"))
        self.btn_2.setText(_translate("MainWindow", "play"))
        self.btn_3.setText(_translate("MainWindow", "pause"))
        self.btn_4.setText(_translate("MainWindow", "next"))
        self.label.setText(_translate("MainWindow", "Vol"))