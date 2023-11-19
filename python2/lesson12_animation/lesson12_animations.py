from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PyQt6.QtCore import (
    QPropertyAnimation,
    QRect,
    QEasingCurve,
    QPauseAnimation,
    Qt,
    QSequentialAnimationGroup
)
import sys

# Для создания анимаций в PyQt6, можно использовать модуль QPropertyAnimation для анимации свойств объектов.
# Вот простой пример:


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Текст")
        self.button = QPushButton("Кнопка")
        self.layout.addWidget(self.button)
        # self.button.clicked.connect(self.my_animation)
        self.layout.addWidget(self.label)
        self.animation = QPropertyAnimation(self.label, b"geometry")  # Какое свойство меняем
        self.animation.setDuration(2000)  # Длительность анимации в миллисекундах
        self.animation.setEasingCurve(QEasingCurve.Type.InBounce)  # Тип кривой анимации
        self.animation.setStartValue(QRect(0, 0, 200, 30))  # Начальное значение анимации
        self.animation.setEndValue(QRect(0, 0, 0, 0))  # Конечное значение анимации
        self.animation.setLoopCount(5)  # Количество повторений анимации
        self.animation.start()  # Старт анимации
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def my_animation(self):
        if self.label.isHidden():
            self.label.setHidden(False)  # Прячем элемент
            self.animation.setStartValue(QRect(0, 0, 0, 0))
            self.animation.setEndValue(QRect(0, 0, 1000, 300))
        else:
            self.animation.setStartValue(QRect(0, 0, 1000, 300))
            self.animation.setEndValue(QRect(0, 0, 0, 0))
            self.label.setHidden(True)
        self.animation.start()

# В PyQt6 существует несколько способов создания анимаций, помимо QPropertyAnimation.
# Вот несколько других видов анимаций:
# 1. QSequentialAnimationGroup: Позволяет группировать несколько анимаций и выполнять их последовательно.
# 2. QParallelAnimationGroup: Позволяет выполнять несколько анимаций параллельно.
# 3. QAbstractAnimation: Абстрактный класс, который вы можете использовать для создания собственных анимаций.
# Вы можете создать подкласс и определить свою логику анимации, реализовав метод updateCurrentTime().


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример последовательной анимации PyQt6")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Привет, анимация!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(50, 50, 200, 30)

        self.start_animation()

    def start_animation(self):
        animation1 = QPropertyAnimation(self.label, b"geometry")
        animation1.setDuration(1000)
        animation1.setStartValue(self.label.geometry())
        animation1.setEndValue(self.label.geometry().translated(100, 0))

        animation2 = QPropertyAnimation(self.label, b"geometry")
        animation2.setDuration(1000)
        animation2.setStartValue(self.label.geometry())
        animation2.setEndValue(self.label.geometry().translated(0, 100))

        sequential_group = QSequentialAnimationGroup(self)
        sequential_group.addAnimation(animation1)
        sequential_group.addAnimation(animation2)
        sequential_group.start()

# Кроме QPropertyAnimation, QSequentialAnimationGroup и QParallelAnimationGroup, PyQt6 предоставляет и другие классы
# для работы с анимациями. Вот несколько из них:
# 1. QAnimationGroup: Базовый класс для группирования анимаций.
# Оба QSequentialAnimationGroup и QParallelAnimationGroup являются подклассами QAnimationGroup.
# 2. QAbstractAnimation: Абстрактный базовый класс для всех анимаций. Если вам нужно создать собственный тип анимации,
# вы можете унаследоваться от этого класса.
# 3. QPauseAnimation: Анимация паузы, которая позволяет добавить задержку между другими анимациями.
# 4. QEasingCurve: Класс для определения кривых времени, регулирующих изменение значения свойства во времени.
# Он определяет, как изменяется скорость анимации.
#
# Пример с QPauseAnimation и QEasingCurve:


class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример анимации с паузой PyQt6")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Привет, анимация!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(50, 50, 200, 30)

        self.start_animation()

    def start_animation(self):
        animation1 = QPropertyAnimation(self.label, b"geometry")
        animation1.setDuration(1000)
        animation1.setStartValue(self.label.geometry())
        animation1.setEndValue(self.label.geometry().translated(100, 0))
        animation1.setEasingCurve(QEasingCurve.Type.OutQuad)

        pause = QPauseAnimation(500)  # Пауза в миллисекундах

        animation2 = QPropertyAnimation(self.label, b"geometry")
        animation2.setDuration(1000)
        animation2.setStartValue(self.label.geometry())
        animation2.setEndValue(self.label.geometry().translated(0, 100))
        animation2.setEasingCurve(QEasingCurve.Type.InQuad)

        sequential_group = QSequentialAnimationGroup(self)
        sequential_group.addAnimation(animation1)
        sequential_group.addAnimation(pause)
        sequential_group.addAnimation(animation2)
        sequential_group.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet("QLabel { background-color: red }")
    window = MainWindow1()
    window.show()
    app.exec()
