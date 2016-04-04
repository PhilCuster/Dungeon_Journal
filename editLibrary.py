# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './editLibrary.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editLibrary(object):
    def setupUi(self, editLibrary):
        editLibrary.setObjectName("editLibrary")
        editLibrary.resize(400, 300)
        self.returnButton = QtWidgets.QPushButton(editLibrary)
        self.returnButton.setGeometry(QtCore.QRect(130, 220, 161, 28))
        self.returnButton.setObjectName("returnButton")

        self.retranslateUi(editLibrary)
        QtCore.QMetaObject.connectSlotsByName(editLibrary)

    def retranslateUi(self, editLibrary):
        _translate = QtCore.QCoreApplication.translate
        editLibrary.setWindowTitle(_translate("editLibrary", "Form"))
        self.returnButton.setText(_translate("editLibrary", "Return to Main Menu"))

