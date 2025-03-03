import sys
from PyQt6 import QtWidgets
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    main_window.setupUi(w)
    w.show()
    sys.exit(app.exec())