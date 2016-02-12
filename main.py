from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
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

    def createNewTemplate(self):
        self.hide()
        self.w = newTemplate()
        self.w.show()


class newTemplate(QWidget):
    def __init__(self):
        super(newTemplate, self).__init__()

        self.ui = Ui_newTemplate()
        self.ui.setupUi(self)



if __name__ == '__main__':
    compileUIC()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
