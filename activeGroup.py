# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './activeGroup.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_activeGroup(object):
    def setupUi(self, activeGroup):
        activeGroup.setObjectName("activeGroup")
        activeGroup.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(activeGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(activeGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.groupLabel = QtWidgets.QLabel(activeGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupLabel.setFont(font)
        self.groupLabel.setObjectName("groupLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupLabel)
        self.label_3 = QtWidgets.QLabel(activeGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.libraryLabel = QtWidgets.QLabel(activeGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.libraryLabel.setFont(font)
        self.libraryLabel.setObjectName("libraryLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.libraryLabel)
        self.verticalLayout.addLayout(self.formLayout)
        self.exitButton = QtWidgets.QPushButton(activeGroup)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)

        self.retranslateUi(activeGroup)
        QtCore.QMetaObject.connectSlotsByName(activeGroup)

    def retranslateUi(self, activeGroup):
        _translate = QtCore.QCoreApplication.translate
        activeGroup.setWindowTitle(_translate("activeGroup", "Form"))
        self.label.setText(_translate("activeGroup", "Current Group: "))
        self.groupLabel.setText(_translate("activeGroup", "TextLabel"))
        self.label_3.setText(_translate("activeGroup", "Group Library: "))
        self.libraryLabel.setText(_translate("activeGroup", "TextLabel"))
        self.exitButton.setText(_translate("activeGroup", "Exit"))

