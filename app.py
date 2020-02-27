import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from loginpage import Ui_MainWindow


class first(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(first, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = first()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
