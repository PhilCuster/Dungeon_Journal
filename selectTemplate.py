# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './selectTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectTemplate(object):
    def setupUi(self, selectTemplate):
        selectTemplate.setObjectName("selectTemplate")
        selectTemplate.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(selectTemplate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(selectTemplate)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(selectTemplate)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okayButton = QtWidgets.QPushButton(selectTemplate)
        self.okayButton.setObjectName("okayButton")
        self.horizontalLayout.addWidget(self.okayButton)
        self.cancelButton = QtWidgets.QPushButton(selectTemplate)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(selectTemplate)
        QtCore.QMetaObject.connectSlotsByName(selectTemplate)

    def retranslateUi(self, selectTemplate):
        _translate = QtCore.QCoreApplication.translate
        selectTemplate.setWindowTitle(_translate("selectTemplate", "Form"))
        self.label.setText(_translate("selectTemplate", "Select a template:"))
        self.okayButton.setText(_translate("selectTemplate", "Okay"))
        self.cancelButton.setText(_translate("selectTemplate", "Cancel"))

