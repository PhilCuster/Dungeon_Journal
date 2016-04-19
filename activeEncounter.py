# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './activeEncounter.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_activeEncounter(object):
    def setupUi(self, activeEncounter):
        activeEncounter.setObjectName("activeEncounter")
        activeEncounter.resize(1419, 827)
        self.verticalLayout = QtWidgets.QVBoxLayout(activeEncounter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.encounterLabel = QtWidgets.QLabel(activeEncounter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.encounterLabel.setFont(font)
        self.encounterLabel.setObjectName("encounterLabel")
        self.verticalLayout.addWidget(self.encounterLabel)
        self.encounterTable = QtWidgets.QTableWidget(activeEncounter)
        self.encounterTable.setObjectName("encounterTable")
        self.encounterTable.setColumnCount(0)
        self.encounterTable.setRowCount(0)
        self.verticalLayout.addWidget(self.encounterTable)
        self.exitButton = QtWidgets.QPushButton(activeEncounter)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)

        self.retranslateUi(activeEncounter)
        QtCore.QMetaObject.connectSlotsByName(activeEncounter)

    def retranslateUi(self, activeEncounter):
        _translate = QtCore.QCoreApplication.translate
        activeEncounter.setWindowTitle(_translate("activeEncounter", "Encounter"))
        self.encounterLabel.setText(_translate("activeEncounter", "TextLabel"))
        self.exitButton.setText(_translate("activeEncounter", "Exit"))

