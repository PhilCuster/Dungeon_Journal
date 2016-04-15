# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './createTable.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createTable(object):
    def setupUi(self, createTable):
        createTable.setObjectName("createTable")
        createTable.resize(670, 489)
        self.verticalLayout = QtWidgets.QVBoxLayout(createTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(createTable)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.tableName = QtWidgets.QLineEdit(createTable)
        self.tableName.setObjectName("tableName")
        self.horizontalLayout_2.addWidget(self.tableName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(createTable)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.addButton = QtWidgets.QPushButton(createTable)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptButton = QtWidgets.QPushButton(createTable)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.acceptButton.setFont(font)
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout.addWidget(self.acceptButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(createTable)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(createTable)
        QtCore.QMetaObject.connectSlotsByName(createTable)

    def retranslateUi(self, createTable):
        _translate = QtCore.QCoreApplication.translate
        createTable.setWindowTitle(_translate("createTable", "Create Table"))
        self.label.setText(_translate("createTable", "Table Name:"))
        self.addButton.setText(_translate("createTable", "Add Table Entry"))
        self.acceptButton.setText(_translate("createTable", "Accept"))
        self.cancelButton.setText(_translate("createTable", "Cancel"))

