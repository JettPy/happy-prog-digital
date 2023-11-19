import sys
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen, QPaintEvent, QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow

# Qt.GlobalColor.white - белый цвет

# скругление по x и y прямоугольников в QPaint
# painter.drawRoundedRect(<координата x>, <координата y>, <ширина>, <высота>, <скругление по x>, <скругление по y>)
# painter.drawRoundedRect(40, 40, 100, 100, 10, 10)

# работа с эллипсами в QPaint
# painter.drawEllipse(<координата x>, <координата y>, <ширина>, <высота>)
# painter.drawEllipse(10, 10, 100, 100)

# работа с текстом в QPaint

# font = QFont() - объект для шрифта
# font.setBold(True) - установка жирного шрифта
# font.setPointSize(40) - установка размера шрифта
# painter.setPen(QColor(0, 255, 0)) - установка цвета фона
# painter.setFont(font) - установка шрифта


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Drawing App')
        self.show()
        self.startPoint = None
        self.endPoint = None

    # paintEvent - обработчик события отрисовки, event (QPaintEvent) - произошедшее событие отрисовки

    # Это событие запускается при перерисовке виджета, например во время вызова self.update()
    def paintEvent(self, event: QPaintEvent):
        if self.startPoint is not None and self.endPoint is not None:
            painter = QPainter(self)
            brush = QBrush(QColor(255, 0, 0, 127))
            pen = QPen(QColor(255, 0, 0, 255))
            pen.setWidth(2)
            painter.setBrush(brush)
            painter.setPen(pen)
            # QRect - прямоугольник из PyQt
            rect = QRect(self.startPoint, self.endPoint)
            painter.drawRect(rect)

    # mousePressEvent - обработчик события нажатия кнопки мыши, event (QMouseEvent) - произошедшее событие мыши
    # Этот обработчик запускается в момент нажатия клавиши мыши
    def mousePressEvent(self, event: QMouseEvent):
        print("mousePressEvent")
        # event.button() - получение информации о нажатой кнопке.
        # Qt.MouseButton.LeftButton - константа отвечающая за левую кнопку мыши
        if event.button() == Qt.MouseButton.LeftButton:
            # event.pos() - получение координат точки в которой произошло событие
            # event.pos().x() - получение координаты x
            # event.pos().y() - получение координаты y
            self.startPoint = event.pos()
            self.endPoint = event.pos()
            # событие обновления виджета. Обновляет его отрисовку на экране.
            self.update()

    # mouseMoveEvent - обработчик события перемещения мыши, event (QMouseEvent) - произошедшее событие мыши
    # Этот обработчик запускается в момент перемещения мыши
    def mouseMoveEvent(self, event):
        print("mouseMoveEvent")
        # event.buttons() возвращает битовую маску, представляющую состояние всех кнопок мыши во время события.
        # Выражение event.buttons() & Qt.MouseButton.LeftButton выполняет побитовую операцию И между битовой маской
        # кнопок мыши и маской для левой кнопки мыши.
        # Если результат этой операции не равен нулю, то левая кнопка мыши была нажата во время события.
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.endPoint = event.pos()
            self.update()

    # mouseReleaseEvent - обработчик события отжатия мыши, event (QMouseEvent) - произошедшее событие мыши
    # Этот обработчик запускается в момент отжатия клавиши мыши
    def mouseReleaseEvent(self, event: QMouseEvent):
        print("mouseReleaseEvent")
        if event.button() == Qt.MouseButton.LeftButton:
            self.endPoint = event.pos()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
