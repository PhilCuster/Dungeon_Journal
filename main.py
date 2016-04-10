from PyQt5.QtWidgets import *
from mainWindow import Ui_MainWindow
from newTemplate import Ui_newTemplate
from editLibrary import Ui_editLibrary
from selectTemplate import Ui_selectTemplate
from PyQt5 import uic
import os
import sys

def compileUIC():
    uic.compileUiDir('./')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quitButton.clicked.connect(self.close)
        self.ui.createTemplateButton.clicked.connect(self.createNewTemplate)
        self.ui.editLibraryButton.clicked.connect(self.openEditLibrary)
        self.w = None

    # Create the widget to make a new template.  Hide the main window and pass a reference of itself to the
    # constructor for the newTemplate widget.
    def createNewTemplate(self):
        self.hide()
        self.w = newTemplate(self)
        self.w.show()

    def openEditLibrary(self):
        self.hide()
        self.w = editLibrary(self)
        self.w.show()


class newTemplate(QWidget):
    def __init__(self, mainW):
        super(newTemplate, self).__init__()

        self.ui = Ui_newTemplate()
        self.ui.setupUi(self)
        self.mainW = mainW

        self.ui.returnButton.clicked.connect(self.returnToMain)
        self.ui.addFieldButton.clicked.connect(self.addField)
        self.ui.createTemplateButton.clicked.connect(self.createTemplate)

    # Closes itself and re-shows the main window.
    def returnToMain(self):
        self.close()
        self.mainW.show()

    def addField(self):
        # Get text from field.
        text = self.ui.fieldToAdd.text()
        # Check which radio button is selected.
        isItText = False
        if self.ui.textButton.isChecked():
            isItText = True
        # As long as it is not blank, add it to the list and clear the field.
        if text != "" and (self.ui.textButton.isChecked() or self.ui.intButton.isChecked()):
            text_to_add = self.ui.fieldToAdd.text()
            if isItText:
                text_to_add += " (text)"
            else:
                text_to_add += " (integer)"
            self.ui.fieldList.addItem(QListWidgetItem(text_to_add, self.ui.fieldList))
            self.ui.fieldToAdd.clear()

    def createTemplate(self):
        templateName = self.ui.templateName.text()
        gameSystem = self.ui.gameSystem.text()
        fields = []
        for i in range(self.ui.fieldList.count()):
            fields.append(self.ui.fieldList.item(i).text())
        if templateName != "" and gameSystem != "" and len(fields) != 0:
            filename = "templates/" + templateName + "_" + gameSystem + ".csv"
            with open(filename, "w") as f:
                f.write(templateName + ",\n")
                f.write(gameSystem + ",\n")
                for entry in fields:
                    f.write(entry + ",\n")
            self.ui.templateName.clear()
            self.ui.gameSystem.clear()
            self.ui.fieldList.clear()


class editLibrary(QWidget):
    def __init__(self, mainW):
        super(editLibrary, self).__init__()

        self.ui = Ui_editLibrary()
        self.ui.setupUi(self)
        self.mainW = mainW

        self.d = None
        self.selectedTemplate = None

        self.ui.returnButton.clicked.connect(self.returnToMain)
        self.ui.selectTemplateButton.clicked.connect(self.selectTemplateWindow)

    def returnToMain(self):
        self.close()
        self.mainW.show()

    def selectTemplateWindow(self):
        self.d = selectTemplate(self)
        self.d.show()

    def changeLibrary(self, library):
        self.ui.currentLIbrary.setText(library)


class selectTemplate(QWidget):
    def __init__(self, ref):
        super(selectTemplate, self).__init__()

        self.ui = Ui_selectTemplate()
        self.ui.setupUi(self)
        self.ref = ref

        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.okayButton.clicked.connect(self.submit)

        # Scan template directory for list of templates.
        for file in os.listdir("templates"):
            if file.endswith(".csv"):
                file = file[:-4]
                self.ui.listWidget.addItem(QListWidgetItem(file, self.ui.listWidget))


    def cancel(self):
        self.close()

    def submit(self):
        # Code to be added here...
        if not len(self.ui.listWidget.selectedItems()) == 0:
            self.ref.changeLibrary(self.ui.listWidget.selectedItems()[0].text())
            self.close()

if __name__ == '__main__':
    compileUIC()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
