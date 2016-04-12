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
from addEncounter import Ui_addEncounter
from activeEncounter import Ui_activeEncounter
from LibraryDef import *
from PyQt5 import uic
import os
import sys
import sqlite3
import re

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

def populateTable(table, selectedTemplate, editable):
    field_list = []
    fields = {}
    table_columns = []

    # From the template file determine what fields will be on the table.
    with open('templates/' + selectedTemplate + '.csv', 'r') as file:
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

    # Set the initial row and column count.
    table.setColumnCount(len(fields))
    table.setRowCount(1)

    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    # Set the headers for the table to the fields of the template.
    i = 0
    for item in field_list:
        table.setHorizontalHeaderItem(i, QTableWidgetItem(item))
        i += 1

    # Connect to the database to read the library.
    conn = sqlite3.connect('libraries/' + selectedTemplate + '.db')
    table_name = cleanse(selectedTemplate)
    c = conn.cursor()

    # If the table does not exist then create it.
    c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name=?''', (cleanse(selectedTemplate),))
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

    # Fill a list with the names of the table columns.
    c.execute('''PRAGMA TABLE_INFO(''' + table_name + ''')''')
    for item in c:
        table_columns.append(item[1])

    # For each row of the table add it it to the table widget.
    row_count = 0
    for row in c.execute('''SELECT * FROM ''' + table_name):
        i = 0
        table.setRowCount(row_count + 1)
        for item in row:
            if fields[table_columns[i]] == "integer":
                newItem = NumericTableWidgetItem()
                newItem.setData(Qt.EditRole, QVariant(item))
            else:
                newItem = QTableWidgetItem()
                newItem.setData(Qt.EditRole, QVariant(item))
            if not editable:
                newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row_count, getColumn(field_list, table_columns[i]), newItem)
            i += 1
        row_count += 1

    conn.commit()
    conn.close()

    return LibraryDef(fields, field_list, table_columns)


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
        if filename[0]:
            self.openGroup(filename[0])

    def openGroup(self, filename):
        self.w = activeGroup(self, filename)
        self.w.show()


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
            file.write("library:" + self.ui.librarySelector.currentText() + '\n\n')

        self.ref.openGroup(filename)
        self.close()

    def cancel(self):
        self.close()
        self.ref.show()


def getLibraryInfo(libraryName):
    field_list = []
    fields = {}
    table_columns = []

    # From the template file determine what fields will be on the table.
    with open('templates/' + libraryName + '.csv', 'r') as file:
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


    # Connect to the database to read the library.
    conn = sqlite3.connect('libraries/' + libraryName + '.db')
    table_name = cleanse(libraryName)
    c = conn.cursor()

    # If the table does not exist then create it.
    c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name=?''', (cleanse(libraryName),))
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

    # Fill a list with the names of the table columns.
    c.execute('''PRAGMA TABLE_INFO(''' + table_name + ''')''')
    for item in c:
        table_columns.append(item[1])

    # Fill a list with the names of the table columns.
    c.execute('''PRAGMA TABLE_INFO(''' + table_name + ''')''')
    for item in c:
        table_columns.append(item[1])

    conn.commit()
    conn.close()

    return LibraryDef(fields, field_list, table_columns)


class activeGroup(QWidget):
    def __init__(self, ref, filename):
        super(activeGroup, self).__init__()

        self.ui = Ui_activeGroup()
        self.ui.setupUi(self)
        self.ref = ref
        self.filename = filename
        self.w = None
        self.encounter_list = []

        self.ui.exitButton.clicked.connect(self.cancel)
        self.ui.addEncounterButton.clicked.connect(self.addEncounterWindow)
        self.ui.openEncounterButton.clicked.connect(self.activeEncounterWindow)
        self.ui.editLibraryButton.clicked.connect(self.editLibraryWindow)

        self.groupName = filename.split('/')[-1]
        # Trim off file extension
        self.groupName = self.groupName[:-6]
        # Set the group label
        self.ui.groupLabel.setText(self.groupName)
        self.setWindowTitle(self.groupName)
        self.libraryName = ""
        # Parse Library name and encounters from file.
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("library:"):
                    self.libraryName = line.split(":")[1]
                    self.libraryName = self.libraryName.rstrip('\n')
                    self.ui.libraryLabel.setText(self.libraryName)
                if line.startswith("encounter:"):
                    line = line.split(':')
                    line.pop(0)
                    line = "".join(line)
                    line = line.rstrip('\n')
                    self.ui.encounterList.addItem(QListWidgetItem(line))

        self.library_info = getLibraryInfo(self.libraryName)


    def activeEncounterWindow(self):
        if not self.ui.encounterList.currentItem() is None:
            self.w = activeEncounter(self, self.ui.encounterList.currentItem().text())
            self.w.show()

    def addEncounterWindow(self):
        self.w = addEncounter(self)
        self.w.show()

    def editLibraryWindow(self):
        self.w = editLibrary(self)
        self.w.show()

    def cancel(self):
        self.close()
        self.ref.show()


class activeEncounter(QWidget):
    def __init__(self, parent, encounter_name):
        super(activeEncounter, self).__init__()

        self.ui = Ui_activeEncounter()
        self.ui.setupUi(self)
        self.parent = parent
        self.encounter_name = encounter_name

        self.ui.exitButton.clicked.connect(self.cancel)

        self.ui.encounterLabel.setText(self.encounter_name)
        self.ui.encounterTable.setColumnCount(len(self.parent.library_info.field_list))
        i = 0
        for item in self.parent.library_info.field_list:
            self.ui.encounterTable.setHorizontalHeaderItem(i, QTableWidgetItem(item))
            i += 1
        self.ui.encounterTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillEncounter()


    def fillEncounter(self):
        conn = sqlite3.connect('libraries/' + self.parent.libraryName + '.db')
        table_name = cleanse(self.parent.libraryName)
        c = conn.cursor()

        encounter_list = []
        with open(self.parent.filename, 'r') as file:
            found_encounter = False
            for line in file:
                # Skip lines until we find the given encounter.
                if line.startswith('encounter:' + self.encounter_name):
                    found_encounter = True
                    continue
                if found_encounter:
                    if line == '\n':
                        break
                    line = (line[1:]).split(',')
                    quantity = int(line[0])
                    line.pop(0)
                    name = ("".join(line)).rstrip('\n')
                    command = '''SELECT * FROM ''' + table_name + ''' WHERE ''' +\
                              self.parent.library_info.field_list[0] + '''=?'''
                    print(command)
                    print(name)
                    c.execute(command, (name,))
                    result = c.fetchone()
                    if result is not None:
                        for j in range(quantity):
                            i = 0
                            self.ui.encounterTable.insertRow(self.ui.encounterTable.rowCount())
                            for item in result:
                                self.ui.encounterTable.setItem(self.ui.encounterTable.rowCount()-1,
                                       self.parent.library_info.field_list.index(self.parent.library_info.table_columns[i]),
                                                               QTableWidgetItem(str(item)))
                                i += 1




    def cancel(self):
        self.close()


class addEncounter(QWidget):
    def __init__(self, parent):
        super(addEncounter, self).__init__()

        self.ui = Ui_addEncounter()
        self.ui.setupUi(self)
        self.parent = parent

        # Contains all of the active filters as well as the rows they apply to.
        self.filter_dict = {}

        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.addFilterButton.clicked.connect(self.addFilter)
        self.ui.removeFilterButton.clicked.connect(self.removeFilter)
        self.ui.addButton.clicked.connect(self.addToEncounter)
        self.ui.acceptButton.clicked.connect(self.acceptEncounter)

        # Populate the Library table.
        self.current_library = populateTable(self.ui.libraryTable, self.parent.libraryName, False)

        self.ui.currentEncounterTable.setSortingEnabled(False)
        self.ui.currentEncounterTable.setColumnCount(len(self.current_library.field_list) + 1)
        i = 1
        for item in self.current_library.field_list:
            self.ui.currentEncounterTable.setHorizontalHeaderItem(i, QTableWidgetItem(item))
            i += 1
        self.ui.currentEncounterTable.setHorizontalHeaderItem(0, QTableWidgetItem("Qty"))

        # Load the field selector.
        for i in range(self.ui.libraryTable.columnCount()):
            self.ui.filterFieldBox.addItem(self.ui.libraryTable.horizontalHeaderItem(i).text())



    def cancel(self):
        self.close()

    def addFilter(self):
        '''
        If the field type is text then the user can only search for a specific string.
        If the field type is int then the user can specify a range or a max or min value.
        '''
        new_filter = self.ui.filterEdit.text()
        field_to_filter = self.ui.filterFieldBox.currentText()

        self.filter_dict[new_filter] = []

        # Determine the field type.
        filter_type = self.current_library.field_types[field_to_filter]
        column_of_interest = self.current_library.field_list.index(field_to_filter)
        # Filter current selection based on the entered string.
        self.ui.filterList.addItem(field_to_filter + ": " + new_filter)
        if filter_type == "text":
            for i in range(self.ui.libraryTable.rowCount()):
                if not self.ui.libraryTable.isRowHidden(i):
                    # Make the cell lowercase.
                    current_field = self.ui.libraryTable.item(i, column_of_interest).text().lower()
                    if new_filter.lower() not in current_field:
                        self.filter_dict[new_filter].append(i)
                        self.ui.libraryTable.setRowHidden(i, True)

        else:
            if re.match('\d*-?\d*', new_filter) is not None:
                search_list = new_filter.split('-')
                if len(search_list) > 1:
                    if search_list[0] == '':
                        mini = 0
                    else:
                        mini = int(search_list[0])
                    if search_list[1] == '':
                        maxi = sys.maxsize
                    else:
                        maxi = int(search_list[1])
                    for i in range(self.ui.libraryTable.rowCount()):
                        if not self.ui.libraryTable.isRowHidden(i):
                            # Make the cell an int.
                            current_field = int(self.ui.libraryTable.item(i, column_of_interest).text())
                            if not mini <= current_field <= maxi:
                                self.filter_dict[new_filter].append(i)
                                self.ui.libraryTable.setRowHidden(i, True)
                else:
                    for i in range(self.ui.libraryTable.rowCount()):
                        if not self.ui.libraryTable.isRowHidden(i):
                            # Make the cell an int.
                            current_field = int(self.ui.libraryTable.item(i, column_of_interest).text())
                            if not current_field == int(new_filter):
                                self.filter_dict[new_filter].append(i)
                                self.ui.libraryTable.setRowHidden(i, True)

    def removeFilter(self):
        if self.ui.filterList.currentItem() is None:
            return
        filter_to_remove = self.ui.filterList.currentItem().text()
        filter_to_remove = filter_to_remove.split(':')[-1]
        filter_to_remove = filter_to_remove[1:]

        self.ui.filterList.takeItem(self.ui.filterList.currentRow())

        rows_filtered = self.filter_dict[filter_to_remove]
        for item in rows_filtered:
            for key in self.filter_dict:
                if key == filter_to_remove:
                    continue
                if item in self.filter_dict[key]:
                    rows_filtered.remove(item)
                    break

        self.filter_dict.pop(filter_to_remove, None)

        for row in rows_filtered:
            self.ui.libraryTable.setRowHidden(row, False)

    def addToEncounter(self):
        self.ui.currentEncounterTable.insertRow(self.ui.currentEncounterTable.rowCount())

        current_row = self.ui.currentEncounterTable.rowCount()-1
        selected_row = self.ui.libraryTable.selectedIndexes()[0].row()
        for i in range(self.ui.libraryTable.columnCount()):
            newItem = QTableWidgetItem(self.ui.libraryTable.item(selected_row, i).text())
            newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.ui.currentEncounterTable.setItem(current_row, i+1, newItem)
        newItem = QTableWidgetItem(str(self.ui.qtyCount.value()))
        newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.ui.currentEncounterTable.setItem(current_row, 0, newItem)

    def acceptEncounter(self):
        if self.ui.encounterNameEdit.text() == "" or self.ui.encounterNameEdit.text() in self.parent.encounter_list:
            return
        # Write the encounter to the group file.
        with open(self.parent.filename, 'a') as file:
            # Write the header.
            file.write("encounter:" + self.ui.encounterNameEdit.text() + '\n')
            for row in range(self.ui.currentEncounterTable.rowCount()):
                file.write('~' + self.ui.currentEncounterTable.item(row, 0).text())
                file.write(',')
                file.write(self.ui.currentEncounterTable.item(row, 1).text() + '\n')
            file.write('\n')

        # Clear the current encounter table.
        self.parent.encounter_list.append(self.ui.encounterNameEdit.text())
        self.parent.ui.encounterList.addItem(QListWidgetItem(self.ui.encounterNameEdit.text()))
        self.close()





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

        # From the template file determine what fields will be on the table.
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

        # Set the initial row and column count.
        self.ui.tableWidget.setColumnCount(len(self.fields))
        self.ui.tableWidget.setRowCount(1)

        # Set the headers for the table to the fields of the template.
        i = 0
        for item in self.field_list:
            self.ui.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(item))
            i += 1

        # Connect to the database to read the library.
        conn = sqlite3.connect('libraries/' + self.selectedTemplate + '.db')
        table_name = cleanse(self.selectedTemplate)
        c = conn.cursor()

        # If the table does not exist then create it.
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

        # Fill a list with the names of the table columns.
        c.execute('''PRAGMA TABLE_INFO(''' + table_name + ''')''')
        for item in c:
            self.table_columns.append(item[1])

        # For each row of the table add it it to the table widget.
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
