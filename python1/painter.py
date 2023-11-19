from PyQt6.QtCore import Qt, QRect
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
)
from PyQt6.QtGui import QPainter, QPixmap, QColor, QPen, QBrush
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(QColor(184, 227, 211))
        self.label.setPixmap(canvas)

        self.painter = QPainter(canvas)
        self.pen = QPen()
        self.brush = QBrush(QColor(245, 148, 44))
        # self.brush.setColor(QColor(245, 148, 44))
        self.pen.setWidth(3)
        self.pen.setColor(QColor("red"))
        self.painter.setPen(self.pen)
        # self.painter.setBrush(QColor(245, 148, 44))
        self.painter.setBrush(self.brush)
        # self.painter.drawLine(10, 10, 300, 200)
        # self.painter.drawPoint(200, 150)
        # self.painter.drawRect(10, 10, 200, 150)
        self.painter.drawRects(
            QRect(0, 0, 100, 100),
            QRect(110, 0, 100, 100),
            QRect(0, 110, 100, 100),
            QRect(110, 110, 100, 100)
        )

        self.painter.end()
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()