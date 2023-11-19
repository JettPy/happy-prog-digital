# Для установки pyQt6 используется команда pip install PyQt6

# Основные модули которые входит в библиотеку PyQt:
# QtWidgets - виджеты (то что может быть отдельным окном)
# QtCore - основные элементы для разработки GUI приложений
# QtGui - Элементы графики

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QVBoxLayout
# Также добавим встроенную библиотеку sys для получения аргументов командной строки
import sys


# Создадим свой класс главного окна и отнаследуем его от QMainWindow:
class MainWindow(QMainWindow):
    # В конструкторе обязательно не забываем проинициализировать родителя
    def __init__(self):
        super().__init__()
        # С помощью setWindowTitle укажем название нашего окна:
        self.setWindowTitle("Мое приложение")
        # Для отображения нескольких виджетов используем вертикальный макет QVBoxLayout:
        self.layout = QVBoxLayout()
        # Создадим кнопку с текстом "Push me!"
        self.button = QPushButton("Push me!")
        # Создадим текстовое поле с текстом "Это текст"
        self.label = QLabel("Это текст")
        # Свяжем событие клика по пнопке с событием изменения текста
        self.button.clicked.connect(self.change_text)
        # Добавим счетчик нажатий на кнопку
        self.count = 0
        # Добавим текст и кнопку в макет layout
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        # Далее создадим базовый виджет что бы разместить в нем наш макет
        self.widget = QWidget()
        # Устанавливаем в него макет
        self.widget.setLayout(self.layout)
        # И установим в цент нашего виджета MainWindow только что полученный виджет
        self.setCentralWidget(self.widget)

    # Эта функция для изменения текста в переменной self.label
    def change_text(self):
        # Увеличим счетчик кликов
        self.count += 1
        # И обновим текст в self.label
        self.label.setText(f"Вы нажали {self.count} раз")


# Класс QApplication - главный класс для запуска нашего приложения, но этот класс не создает окон.
# Он принимает параметры командной строки которые мы передаем при запуске программы через консоль
# python main.py commandline arguments - здесь аргументы будут:
# ['main.py', 'commandline', 'arguments'] - разбиты по словам, причем имя файла тоже является первым аргументом
# Если не хотите передавать аргументы, то можно указать просто пустой список []
app = QApplication(sys.argv)

# Создадим наш виджет
# Таким образом также можно создавать любые другие виджеты
window = MainWindow()
# button = QPushButton("Push me!") - создание виджета кнопки
# label = QLabel("Это текст") - создание виджета текста

# Для того чтобы отобразить наш виджет или любые другие виджеты, используется метод show:
window.show()
# button.show()
# label.show()

# И самым последнем делом идет метод создания цикла событий.
# Код написанный ниже этой строчки либо не будет исполняться, либо будет выполнен после завершения программы.
app.exec()
