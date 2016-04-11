# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './newEntry.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newEntry(object):
    def setupUi(self, newEntry):
        newEntry.setObjectName("newEntry")
        newEntry.resize(638, 343)
        self.verticalLayout = QtWidgets.QVBoxLayout(newEntry)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(newEntry)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(newEntry)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 270))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submitButton = QtWidgets.QPushButton(newEntry)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout.addWidget(self.submitButton)
        self.cancelButton = QtWidgets.QPushButton(newEntry)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(newEntry)
        QtCore.QMetaObject.connectSlotsByName(newEntry)

    def retranslateUi(self, newEntry):
        _translate = QtCore.QCoreApplication.translate
        newEntry.setWindowTitle(_translate("newEntry", "New Entry"))
        self.label.setText(_translate("newEntry", "Add Entry Below:"))
        self.submitButton.setText(_translate("newEntry", "Submit"))
        self.cancelButton.setText(_translate("newEntry", "Cancel"))

