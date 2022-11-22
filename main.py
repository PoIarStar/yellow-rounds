import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic, QtCore
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.draw_button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_rounds(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_rounds(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(3, 11)):
            r = randint(10, 100)
            qp.drawEllipse(QtCore.QPoint(randint(0, 500), randint(0, 400)), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
