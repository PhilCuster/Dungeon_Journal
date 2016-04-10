# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './editLibrary.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editLibrary(object):
    def setupUi(self, editLibrary):
        editLibrary.setObjectName("editLibrary")
        editLibrary.resize(800, 435)
        self.verticalLayout = QtWidgets.QVBoxLayout(editLibrary)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(editLibrary)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.currentLIbrary = QtWidgets.QLabel(editLibrary)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentLIbrary.setFont(font)
        self.currentLIbrary.setObjectName("currentLIbrary")
        self.horizontalLayout.addWidget(self.currentLIbrary)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(editLibrary)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.selectTemplateButton = QtWidgets.QPushButton(editLibrary)
        self.selectTemplateButton.setObjectName("selectTemplateButton")
        self.verticalLayout_2.addWidget(self.selectTemplateButton)
        self.returnButton = QtWidgets.QPushButton(editLibrary)
        self.returnButton.setObjectName("returnButton")
        self.verticalLayout_2.addWidget(self.returnButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(editLibrary)
        QtCore.QMetaObject.connectSlotsByName(editLibrary)

    def retranslateUi(self, editLibrary):
        _translate = QtCore.QCoreApplication.translate
        editLibrary.setWindowTitle(_translate("editLibrary", "Edit Library"))
        self.label.setText(_translate("editLibrary", "Selected Template/Library:"))
        self.currentLIbrary.setText(_translate("editLibrary", "None"))
        self.selectTemplateButton.setText(_translate("editLibrary", "Select Library/Template"))
        self.returnButton.setText(_translate("editLibrary", "Return to Main Menu"))

