# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.createTemplateButton = QtWidgets.QPushButton(self.centralwidget)
        self.createTemplateButton.setObjectName("createTemplateButton")
        self.verticalLayout.addWidget(self.createTemplateButton)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout.addWidget(self.quitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dungeon Journal"))
        self.createTemplateButton.setText(_translate("MainWindow", "Create Template"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))

