# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './newTemplateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newTemplateDialog(object):
    def setupUi(self, newTemplateDialog):
        newTemplateDialog.setObjectName("newTemplateDialog")
        newTemplateDialog.resize(377, 124)
        newTemplateDialog.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(newTemplateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(newTemplateDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(newTemplateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(newTemplateDialog)
        self.buttonBox.accepted.connect(newTemplateDialog.accept)
        self.buttonBox.rejected.connect(newTemplateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newTemplateDialog)

    def retranslateUi(self, newTemplateDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("newTemplateDialog", "Template Created!"))

