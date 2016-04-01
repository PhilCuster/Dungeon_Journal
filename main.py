from PyQt5.QtWidgets import *
from mainWindow import Ui_MainWindow
from newTemplate import Ui_newTemplate
from PyQt5 import uic
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
        self.w = None

    # Create the widget to make a new template.  Hide the main window and pass a reference of itself to the
    # constructor for the newTemplate widget.
    def createNewTemplate(self):
        self.hide()
        self.w = newTemplate(self)
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
        # As long as it is not blank, add it to the list and clear the field.
        if text != "":
            self.ui.fieldList.addItem(QListWidgetItem(self.ui.fieldToAdd.text(), self.ui.fieldList))
            self.ui.fieldToAdd.clear()

    def createTemplate(self):
        templateName = self.ui.templateName.text()
        gameSystem = self.ui.gameSystem.text()
        fields = []
        for i in range(self.ui.fieldList.count()):
            fields.append(self.ui.fieldList.item(i).text())
        filename = "templates/" + templateName + "_" + gameSystem + ".csv"
        with open(filename, "w") as f:
            f.write(templateName + ",\n")
            f.write(gameSystem + ",\n")
            for entry in fields:
                f.write(entry + ",\n")
        self.ui.templateName.clear()
        self.ui.gameSystem.clear()
        self.ui.fieldList.clear()


if __name__ == '__main__':
    compileUIC()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
