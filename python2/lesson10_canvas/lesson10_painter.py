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

# В PyQt6, класс QPainter используется для рисования на виджетах и других элементах пользовательского интерфейса.

# QPainter в PyQt6 рисует на различных устройствах вывода. Основными целями для рисования с помощью QPainter являются:
# 1. QWidget: Вы можете использовать QPainter для рисования на виджетах. Это позволяет создавать пользовательские
# элементы интерфейса или рисовать графику непосредственно на окне приложения.
# 2. QImage: QPainter может также рисовать на изображениях, создавая изображения в памяти. Это полезно, например,
# для генерации и обработки изображений.
# 3. QPixmap: QPainter может рисовать на пиксмапах, которые также представляют собой изображения,
# но они оптимизированы для отображения на экране и обеспечивают быструю отрисовку.
# 4. QPrinter: Если вам нужно создавать документы для печати, QPainter может рисовать на принтере.
# Это позволяет создавать качественные печатные материалы.

# QPainter предоставляет множество методов для рисования различных элементов и настройки стиля рисования.
# Вот некоторые из наиболее часто используемых методов QPainter:
# 1. begin(device): Начинает рисование на указанном устройстве вывода (например, виджете, изображении или принтере).
# 2. end(): Завершает рисование и освобождает ресурсы.
# 3. drawRect(x, y, width, height): Рисует прямоугольник.
# 4. drawEllipse(x, y, width, height): Рисует эллипс.
# 5. drawText(x, y, text): Рисует текст.
# 6. setPen(pen): Устанавливает перо для рисования (цвет, толщина и стиль линии).
# 7. setBrush(brush): Устанавливает кисть для заливки фигур.
# 8. setFont(font): Устанавливает шрифт для текста.
# 9. setRenderHint(hint, on): Включает/выключает определенные подсказки рендеринга (сглаживание или антиалиасинг).
# 10. translate(dx, dy): Переносит текущую систему координат на указанный сдвиг.
# 11. rotate(degrees): Поворачивает текущую систему координат на указанный угол.
# 12. scale(sx, sy): Масштабирует текущую систему координат.
# 13. save(): Сохраняет текущее состояние рисования (цвета, перо, кисть и другие параметры).
# 14. restore(): Восстанавливает ранее сохраненное состояние рисования.

# С использованием QPainter в PyQt6 вы можете нарисовать различные геометрические фигуры.
# Вот некоторые из фигур, которые вы можете нарисовать:
# 1. Прямоугольники:
#    - drawRect(x, y, width, height): Рисует прямоугольник.
# 2. Эллипсы:
#    - drawEllipse(x, y, width, height): Рисует эллипс.
# 3. Линии:
#    - drawLine(x1, y1, x2, y2): Рисует линию от точки (x1, y1) до точки (x2, y2).
# 4. Многоугольники:
#    - drawPolygon(polygon): Рисует многоугольник, используя объект QPolygon.
# 5. Треугольники:
#    - drawPolygon(points): Рисует многоугольник, указав его вершины в виде списка точек.
# 6. Дуги и секторы:
#    - drawArc(x, y, width, height, startAngle, spanAngle): Рисует дугу или сектор.
# 7. Текст:
#    - drawText(x, y, text): Рисует текст на виджете.
# 8. Круги:
#    - drawEllipse(x, y, radius, radius): Рисует круг с заданным радиусом.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создадим QLabel в котором будем рисовать используя QPixmap
        self.label = QLabel()
        canvas = QPixmap(400, 300)
        # Зададим цвет фона с помощью fill и класса QColor
        canvas.fill(QColor(184, 227, 211))
        self.label.setPixmap(canvas)
        # Создадим объект QPainter в него "холст для рисования"
        self.painter = QPainter(canvas)

        # Классы QPen и QBrush используются для настройки стиля контура и стиля заливки соответсвенно
        # pen = QPen(QColor(255, 0, 0))  - Создание красного пера
        # pen.setWidth(2)  - Установка толщины линии
        # painter = QPainter(self)
        # painter.setPen(pen)
        # pen.setStyle(Qt.PenStyle.DashLine)  - Установка стиля линии (пунктирная линия)
        # pen.setCapStyle(Qt.PenCapStyle.RoundCap)  - Установка стиля окончания линии (круглое окончание)

        #  Вы можете изменять параметры QPen в любой момент перед выполнением операций рисования с QPainter.
        #  Например, вы можете изменить цвет линии или стиль линии перед рисованием разных элементов.
        # Начальный цвет линии (красный)
        # pen = QPen(QColor(255, 0, 0))
        # painter.setPen(pen)
        #
        # Рисование красной линии
        # painter.drawLine(10, 10, 100, 100)
        #
        # Получение текущего QPen
        # current_pen = painter.pen()
        #
        # Изменение цвета линии (синий)
        # current_pen.setColor(QColor(0, 0, 255))
        #
        # Установка обновленного QPen
        # painter.setPen(current_pen)
        #
        # Рисование синей линии
        # painter.drawLine(10, 50, 100, 150)

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
        # drawRects - позволяет рисовать несколько прямоугольников сразу
        self.painter.drawRects(
            QRect(0, 0, 100, 100),
            QRect(110, 0, 100, 100),
            QRect(0, 110, 100, 100),
            QRect(110, 110, 100, 100)
        )
        # Сразу после окончания рисования нужно выполнить команду end, для очистки памяти и
        # сохранить текущее значение canvas в label с помощью метода setPixmap
        self.painter.end()
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()