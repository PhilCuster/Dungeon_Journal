from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QVariant
from mainWindow import Ui_MainWindow
from newTemplate import Ui_newTemplate
from editLibrary import Ui_editLibrary
from selectTemplate import Ui_selectTemplate
from newTemplateDialog import Ui_newTemplateDialog
from activeGroup import Ui_activeGroup
from playMenu import Ui_playMenu
from newEntry import Ui_newEntry
from newGroup import Ui_newGroup
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

    if not os.path.exists("groups"):
        os.makedirs("groups")

def cleanse(text):
    return ''.join( c for c in text if c.isalnum())

def getColumn(lst, x):
    i = 0
    for item in lst:
        if item == x:
            return i
        i += 1

def checkInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quitButton.clicked.connect(self.close)
        self.ui.createTemplateButton.clicked.connect(self.createNewTemplate)
        self.ui.editLibraryButton.clicked.connect(self.openEditLibrary)
        self.ui.playMenuButton.clicked.connect(self.openPlayMenu)
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

    def openPlayMenu(self):
        self.hide()
        self.w = playMenu(self)
        self.w.show()


class playMenu(QWidget):
    def __init__(self, mainW):
        super(playMenu, self).__init__()
        self.ui = Ui_playMenu()
        self.ui.setupUi(self)
        self.mainW = mainW
        self.w = None

        self.ui.returnButton.clicked.connect(self.returnToMenu)
        self.ui.newGroupButton.clicked.connect(self.newGroupWindow)
        self.ui.openGroupButton.clicked.connect(self.selectGroup)

    def returnToMenu(self):
        self.close()
        self.mainW.show()

    def newGroupWindow(self):
        self.w = newGroup(self)
        self.w.show()
        self.hide()

    def selectGroup(self):
        filename = QFileDialog.getOpenFileName(self, "Select Group", 'groups', '*.group')
        if filename:
            n = activeGroup(self, filename[0])
            n.show()
            self.hide()


class newGroup(QWidget):
    def __init__(self, ref):
        super(newGroup, self).__init__()
        self.ui = Ui_newGroup()
        self.ui.setupUi(self)
        self.ref = ref

        self.ui.createButton.clicked.connect(self.createGroup)
        self.ui.cancelButton.clicked.connect(self.cancel)

        # Populate the library names.
        self.library_list = []
        for file in os.listdir('libraries'):
            if file.endswith('.db'):
                self.library_list.append(file[:-3])
        for library in self.library_list:
            self.ui.librarySelector.addItem(library)

    def createGroup(self):
        if self.ui.nameEdit.text() == "":
            return
        filename = 'groups/' + self.ui.nameEdit.text() + ".group"
        with open(filename, 'w') as file:
            file.write("library:" + self.ui.librarySelector.currentText())

        n = activeGroup(self.ref, filename)
        n.show()
        self.close()

    def cancel(self):
        self.close()
        self.ref.show()


class activeGroup(QWidget):
    def __init__(self, ref, filename):
        super(activeGroup, self).__init__()

        self.ui = Ui_activeGroup()
        self.ui.setupUi(self)
        self.ref = ref
        self.filename = filename

        self.ui.exitButton.clicked.connect(self.cancel)

    def cancel(self):
        self.close()
        self.ref.show()


class newTemplate(QWidget):

    # To Do:
    #
    # 1. Ensure that when a template is made an identical template does not already exist.
    #

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

            d = newTemplateDialog(self, self.mainW)
            d.show()


class newTemplateDialog(QDialog):
    def __init__(self, parent=None, super_parent=None):
        super(newTemplateDialog, self).__init__(parent)

        self.parent = parent
        self.super_parent = super_parent
        self.ui = Ui_newTemplateDialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Create New Template")
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText("Return to Main Menu")

        self.ui.buttonBox.accepted.connect(self.close)
        self.ui.buttonBox.rejected.connect(self.closeParent)

    def closeParent(self):
        self.parent.close()
        self.close()
        self.super_parent.show()


class NumericTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        if isinstance(other, QTableWidgetItem):
            my_value = self.data(Qt.EditRole)
            other_value = other.data(Qt.EditRole)

            if my_value and other_value:
                return my_value < other_value

        return super(NumericTableWidgetItem, self).__lt__(other)


class editLibrary(QWidget):

    # To Do:
    # 1. When creating a new entry check to make sure an entry with that name does not already exists,
    #    as the name is the unique identifier.
    #
    # 2. Allow a user to edit an attribute for an individual field.
    #
    # 3. Allow a user to delete an entry.

    def __init__(self, mainW):
        super(editLibrary, self).__init__()

        self.ui = Ui_editLibrary()
        self.ui.setupUi(self)
        self.mainW = mainW

        self.d = None
        self.selectedTemplate = None
        self.field_list = []
        self.fields = {}
        self.table_columns = []

        self.ui.tableWidget.setSortingEnabled(True)

        self.ui.returnButton.clicked.connect(self.returnToMain)
        self.ui.selectTemplateButton.clicked.connect(self.selectTemplateWindow)
        self.ui.addButton.clicked.connect(self.newEntryWindow)

    def returnToMain(self):
        self.close()
        self.mainW.show()

    def selectTemplateWindow(self):
        self.d = selectTemplate(self)
        self.d.show()

    def newEntryWindow(self):
        if self.selectedTemplate is not None:
            self.d = newEntry(self, cleanse(self.selectedTemplate), self.selectedTemplate, self.fields, self.field_list, self.table_columns)
            self.d.show()

    def changeLibrary(self, library):
        self.ui.currentLIbrary.setText(library)
        self.selectedTemplate = library
        self.importTemplate()

    def importTemplate(self):

        self.field_list = []

        with open('templates/' + self.selectedTemplate + '.csv', 'r') as file:
            count = 1
            for line in file:
                line = line.rstrip('\n')
                if count < 3:
                    count += 1
                else:
                    if line.endswith("(text),"):
                        self.fields[line[:-8]] = line[-6:-2]
                        self.field_list.append(line[:-8])
                    else:
                        self.fields[line[:-11]] = line[-9:-2]
                        self.field_list.append(line[:-11])
                    count += 1

        self.ui.tableWidget.setColumnCount(len(self.fields))
        self.ui.tableWidget.setRowCount(1)

        i = 0
        for item in self.field_list:
            self.ui.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(item))
            i += 1

        conn = sqlite3.connect('libraries/' + self.selectedTemplate + '.db')
        table_name = cleanse(self.selectedTemplate)
        c = conn.cursor()
        c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name=?''', (cleanse(self.selectedTemplate),))
        if c.fetchone() is None:
            count = 0
            for key in self.fields:
                if count == 0:
                    if self.fields[key] == "real":
                        query = "CREATE TABLE " + table_name + " (" + cleanse(key) + " INTEGER)"
                    else:
                        query = "CREATE TABLE " + table_name + " (" + cleanse(key) + " TEXT)"
                    c.execute(query)
                    count += 1
                else:
                    query = "ALTER TABLE " + table_name + " ADD COLUMN " + \
                            cleanse(key) + " " + self.fields[key]
                    c.execute(query)
                    count += 1

        c.execute('''PRAGMA TABLE_INFO(''' + table_name + ''')''')
        for item in c:
            self.table_columns.append(item[1])

        row_count = 0
        for row in c.execute('''SELECT * FROM ''' + table_name):
            i = 0
            self.ui.tableWidget.setRowCount(row_count + 1)
            for item in row:
                if self.fields[self.table_columns[i]] == "integer":
                    newItem = NumericTableWidgetItem()
                    newItem.setData(Qt.EditRole, QVariant(item))
                else:
                    newItem = QTableWidgetItem()
                    newItem.setData(Qt.EditRole, QVariant(item))
                self.ui.tableWidget.setItem(row_count, getColumn(self.field_list, self.table_columns[i]), newItem)
                i += 1
            row_count += 1

        conn.commit()
        conn.close()


    def refresh(self, newEntry):
        self.ui.tableWidget.setSortingEnabled(False)
        row_count = self.ui.tableWidget.rowCount() + 1
        self.ui.tableWidget.setRowCount(row_count)
        i = 0
        for field in self.field_list:
            if self.fields[field] == "integer":
                newItem = NumericTableWidgetItem()
                newItem.setData(Qt.EditRole, QVariant(int(newEntry[field])))
            else:
                newItem = QTableWidgetItem()
                newItem.setData(Qt.EditRole, QVariant(str(newEntry[field])))
            self.ui.tableWidget.setItem(row_count-1, i, newItem)
            i += 1
        self.ui.tableWidget.setSortingEnabled(True)


class selectTemplate(QWidget):
    def __init__(self, ref):
        super(selectTemplate, self).__init__()

        self.ui = Ui_selectTemplate()
        self.ui.setupUi(self)
        self.ref = ref

        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.okayButton.clicked.connect(self.submit)

        # Scan template directory for list of templates.
        for file in os.listdir("templates"):
            if file.endswith(".csv"):
                file = file[:-4]
                self.ui.listWidget.addItem(QListWidgetItem(file, self.ui.listWidget))


    def submit(self):
        if not len(self.ui.listWidget.selectedItems()) == 0:
            self.ref.changeLibrary(self.ui.listWidget.selectedItems()[0].text())
            self.close()

class newEntry(QWidget):
    def __init__(self, ref, currentTemplate, rawTemplate, fields, field_list, tableColumns):
        super(newEntry, self).__init__()

        self.ui = Ui_newEntry()
        self.ui.setupUi(self)
        self.ref = ref
        self.fields = fields
        self.tableColumns = tableColumns
        self.selectedTemplate = currentTemplate
        self.rawTemplate = rawTemplate

        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.submitButton.clicked.connect(self.submit)

        self.formLayout = QFormLayout()

        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.formLayout)

        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setWidget(self.scrollWidget)

        for item in field_list:
            self.formLayout.addRow(QLabel(item), QLineEdit())



    def submit(self):
        types = {}
        submitDict = {}
        # Check all the fields to make sure they are of the correct type.
        for i in range(self.formLayout.rowCount()):
            field = self.formLayout.itemAt(i, 0).widget().text()
            value = self.formLayout.itemAt(i, 1).widget().text()
            type = self.fields[field]
            if type == "integer" and not checkInt(value):
                return
            submitDict[field] = value
            types[value] = type

        # Now, add to the database.
        conn = sqlite3.connect('libraries/' + self.rawTemplate + '.db')
        c = conn.cursor()
        command = "INSERT INTO " + self.selectedTemplate + " VALUES ("
        submitList = []
        for i in range(len(self.fields)):
            #command = command + submitDict[self.tableColumns[i]] + ","
            command += "?,"
            submitList.append(submitDict[self.tableColumns[i]])
        command = command[:-1] + ')'
        c.execute(command, submitList)

        conn.commit()
        conn.close()
        self.ref.refresh(submitDict)
        self.close()

if __name__ == '__main__':
    compileUIC()
    setupDirs()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
