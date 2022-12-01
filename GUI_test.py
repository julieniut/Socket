import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit


class MyWindow(QWidget):

    def __init__(self, win):
        super().__init__()
        self.win = win

    def build(self):
        self.win.setWindowTitle("QLineEdit Exemple")
        self.win.setGeometry(100, 100, 500, 300)

        # create a QLineEdit
        self.qLine = QLineEdit(self.win)
        self.qLine.setGeometry(50, 50, 250, 35)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QWidget()

    mywin = MyWindow(root)
    mywin.build()

    root.show()
    sys.exit(app.exec_())