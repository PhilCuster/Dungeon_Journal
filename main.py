from PyQt5.QtWidgets import *
from mainWindow import Ui_MainWindow
from newTemplate import Ui_newTemplate
from editLibrary import Ui_editLibrary
from selectTemplate import Ui_selectTemplate
from PyQt5 import uic
import os
import sys
import sqlite3

def compileUIC():
    uic.compileUiDir('./')

def setupDirs():
    if not os.path.exists("libraries"):
        os.makedirs("libraries")

    if not os.path.exists("templates"):
        os.makedirs("templates")

def cleanse(text):
    return ''.join( c for c in text if c.isalnum())

def getColumn(lst, x):
    i = 0
    for item in lst:
        if item == x:
            return i
        i += 1


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
        self.selectedTemplate = library
        self.importTemplate()

    def importTemplate(self):
        fields = {}
        field_list = []
        table_columns = []

        with open('templates/' + self.selectedTemplate + '.csv', 'r') as file:
            count = 1
            for line in file:
                line = line.rstrip('\n')
                if count < 3:
                    count += 1
                else:
                    if line.endswith("(text),"):
                        fields[line[:-8]] = line[-6:-2]
                        field_list.append(line[:-8])
                    else:
                        fields[line[:-11]] = line[-9:-2]
                        field_list.append(line[:-11])
                    count += 1

        self.ui.tableWidget.setColumnCount(len(fields))
        self.ui.tableWidget.setRowCount(1)

        i = 0
        for item in field_list:
            self.ui.tableWidget.setItem(0, i, QTableWidgetItem(item))
            i += 1

        conn = sqlite3.connect('libraries/' + self.selectedTemplate + '.db')
        table_name = cleanse(self.selectedTemplate)
        c = conn.cursor()
        c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name=?''', (cleanse(self.selectedTemplate),))
        if c.fetchone() is None:
            count = 0
            for key in fields:
                if count == 0:
                    if fields[key] == "real":
                        query = "CREATE TABLE " + table_name + " (" + cleanse(key) + " INTEGER)"
                    else:
                        query = "CREATE TABLE " + table_name + " (" + cleanse(key) + " TEXT)"
                    c.execute(query)
                    count += 1
                else:
                    query = "ALTER TABLE " + table_name + " ADD COLUMN " + \
                            cleanse(key) + " " + fields[key]
                    c.execute(query)
                    count += 1

        c.execute('''PRAGMA TABLE_INFO(''' + table_name + ''')''')
        for item in c:
            table_columns.append(item[1])

        row_count = 1
        for row in c.execute('''SELECT * FROM ''' + table_name):
            i = 0
            self.ui.tableWidget.setRowCount(row_count + 1)
            for item in row:
                self.ui.tableWidget.setItem(row_count, getColumn(field_list,
                                                                 table_columns[i]), QTableWidgetItem(str(item)))
                i += 1
            row_count += 1

        conn.commit()
        conn.close()


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
    setupDirs()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
