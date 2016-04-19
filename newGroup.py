# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './newGroup.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newGroup(object):
    def setupUi(self, newGroup):
        newGroup.setObjectName("newGroup")
        newGroup.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(newGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(newGroup)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameEdit = QtWidgets.QLineEdit(newGroup)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_2 = QtWidgets.QLabel(newGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.librarySelector = QtWidgets.QComboBox(newGroup)
        self.librarySelector.setObjectName("librarySelector")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.librarySelector)
        self.verticalLayout.addLayout(self.formLayout)
        self.createButton = QtWidgets.QPushButton(newGroup)
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(newGroup)
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout.addWidget(self.cancelButton)

        self.retranslateUi(newGroup)
        QtCore.QMetaObject.connectSlotsByName(newGroup)

    def retranslateUi(self, newGroup):
        _translate = QtCore.QCoreApplication.translate
        newGroup.setWindowTitle(_translate("newGroup", "New Group"))
        self.label.setText(_translate("newGroup", "Name: "))
        self.label_2.setText(_translate("newGroup", "Library: "))
        self.createButton.setText(_translate("newGroup", "Create Group"))
        self.cancelButton.setText(_translate("newGroup", "Cancel"))

