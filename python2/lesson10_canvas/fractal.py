import math
import sys
import random
from PyQt6.QtCore import Qt, QTimer, QPointF
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow

PIXMAP_WIDTH = 800
PIXMAP_HEIGHT = 800
HEIGHT = 0.8 * PIXMAP_HEIGHT
MARGIN = 0.1 * PIXMAP_HEIGHT

HALF_SIDE = HEIGHT / math.sqrt(3)
TOP = {"x": PIXMAP_WIDTH / 2, "y": MARGIN}
LEFT = {"x": TOP["x"] - HALF_SIDE, "y": MARGIN + HEIGHT}
RIGHT = {"x": TOP["x"] + HALF_SIDE, "y": MARGIN + HEIGHT}
# TOP = {"x": MARGIN, "y": MARGIN}
# LEFT = {"x": MARGIN, "y": PIXMAP_HEIGHT - MARGIN}
# RIGHT = {"x": PIXMAP_WIDTH - MARGIN, "y": PIXMAP_HEIGHT - MARGIN}


class PointDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.curr_x = 0
        self.curr_y = 0
        self.setGeometry(10, 10, PIXMAP_WIDTH, PIXMAP_HEIGHT)
        self.setWindowTitle('Рисование точек')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawPoint)
        self.timer.start(1)
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.GlobalColor.white)

    def drawPoint(self):
        match random.randint(1, 3):
            case 1:
                new_x = (self.curr_x + TOP["x"]) / 2
                new_y = (self.curr_y + TOP["y"]) / 2
            case 2:
                new_x = (self.curr_x + LEFT["x"]) / 2
                new_y = (self.curr_y + LEFT["y"]) / 2
            case 3:
                new_x = (self.curr_x + RIGHT["x"]) / 2
                new_y = (self.curr_y + RIGHT["y"]) / 2
        # match random.randint(1, 4):
        #     case 1:
        #         new_x = (self.curr_x + A["x"]) / 2
        #         new_y = (self.curr_y + A["y"]) / 2
        #     case 2:
        #         new_x = (self.curr_x + B["x"]) / 2
        #         new_y = (self.curr_y + B["y"]) / 2
        #     case 3:
        #         new_x = (self.curr_x + C["x"]) / 2
        #         new_y = (self.curr_y + C["y"]) / 2
        #     case 4:
        #         new_x = (self.curr_x + D["x"]) / 2
        #         new_y = (self.curr_y + D["y"]) / 2
            case _:
                new_x = self.curr_x
                new_y = self.curr_y
        self.curr_x = new_x
        self.curr_y = new_y

        painter = QPainter(self.pixmap)
        pen = QPen()
        pen.setColor(QColor("black"))
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawPoint(QPointF(self.curr_x, self.curr_y))
        painter.end()

        self.update()  # Вызывает перерисовку виджета

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)


def main():
    app = QApplication(sys.argv)
    window = PointDrawer()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
