# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './activeTable.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_activeTable(object):
    def setupUi(self, activeTable):
        activeTable.setObjectName("activeTable")
        activeTable.resize(473, 132)
        self.verticalLayout = QtWidgets.QVBoxLayout(activeTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(activeTable)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tableLabel = QtWidgets.QLabel(activeTable)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableLabel.setFont(font)
        self.tableLabel.setObjectName("tableLabel")
        self.horizontalLayout.addWidget(self.tableLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.supriseButton = QtWidgets.QPushButton(activeTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supriseButton.sizePolicy().hasHeightForWidth())
        self.supriseButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.supriseButton.setFont(font)
        self.supriseButton.setObjectName("supriseButton")
        self.verticalLayout.addWidget(self.supriseButton)

        self.retranslateUi(activeTable)
        QtCore.QMetaObject.connectSlotsByName(activeTable)

    def retranslateUi(self, activeTable):
        _translate = QtCore.QCoreApplication.translate
        activeTable.setWindowTitle(_translate("activeTable", "Random Table"))
        self.label.setText(_translate("activeTable", "Table: "))
        self.tableLabel.setText(_translate("activeTable", "TextLabel"))
        self.supriseButton.setText(_translate("activeTable", "Suprise Me!"))

