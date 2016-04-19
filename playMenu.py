# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './playMenu.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_playMenu(object):
    def setupUi(self, playMenu):
        playMenu.setObjectName("playMenu")
        playMenu.resize(255, 264)
        self.verticalLayout = QtWidgets.QVBoxLayout(playMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(playMenu)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.newGroupButton = QtWidgets.QPushButton(playMenu)
        self.newGroupButton.setObjectName("newGroupButton")
        self.verticalLayout.addWidget(self.newGroupButton)
        self.openGroupButton = QtWidgets.QPushButton(playMenu)
        self.openGroupButton.setObjectName("openGroupButton")
        self.verticalLayout.addWidget(self.openGroupButton)
        self.returnButton = QtWidgets.QPushButton(playMenu)
        self.returnButton.setObjectName("returnButton")
        self.verticalLayout.addWidget(self.returnButton)

        self.retranslateUi(playMenu)
        QtCore.QMetaObject.connectSlotsByName(playMenu)

    def retranslateUi(self, playMenu):
        _translate = QtCore.QCoreApplication.translate
        playMenu.setWindowTitle(_translate("playMenu", "Play"))
        self.label.setText(_translate("playMenu", "Play"))
        self.newGroupButton.setText(_translate("playMenu", "Create New Group"))
        self.openGroupButton.setText(_translate("playMenu", "Open Group"))
        self.returnButton.setText(_translate("playMenu", "Return to Main Menu"))

