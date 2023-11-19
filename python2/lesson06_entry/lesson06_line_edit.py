from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    W,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout
)
import sys


# Про макеты

# Любой виджет без указания родителя в конструкторе является отдельным окном
# Например такой пример выдаст два окна:
# window = QWidget()
# btn = QPushButton("Кнопка")
# А с привязкой родителей, кнопка окажется внутри виджета:
# window = QWidget()
# btn = QPushButton("Кнопка", window)

# Но при такой привязке все внутренние виджеты будут крепиться к левому верхнему углу.
# Для того что бы их сместить используется метод move:
# window = QWidget()
# btn1 = QPushButton("Кнопка 1", window)
# btn2 = QPushButton("Кнопка 2", window)
# btn2.move(100, 50) # перемещает кнопку на 100 пикселей влево (ось x) и на 50 пикселей вниз (ось y)

# Этот подход плох тем, что мы задаем фиксированное положение элементов.
# Поэтому при увеличении размера окна виджеты не будут растягиваться.
# И тут нам на помощь приходят макеты

# Есть три основных вида макета:

# 1) QVBoxLayout - вертикальный макет, позволяет размещать элементы в вертикальный столбик.
# При растягивании окна виджеты также будут пропорционально растягиваться.
# Чтобы добавить виджет в макет используется метод макета addWidget:
# btn1 = QPushButton("Кнопка 1") # Создаем 3 кнопки
# btn2 = QPushButton("Кнопка 2")
# btn3 = QPushButton("Кнопка 3")
# layout = QVBoxLayout() # Создаем вертикальный макет
# layout.addWidget(btn1) # Добавляем кнопки в макет
# layout.addWidget(btn2)
# layout.addWidget(btn3)
# widget = QWidget() # Создаем виджет в который разместим макет
# widget.setLayout(layout) # Устанавливаем макет в виджет методом setLayout

# 2) QHBoxLayout - горизонтальный макет, позволяет размещать элементы в горизонтальный столбик.
# При растягивании окна виджеты также будут пропорционально растягиваться.
# Чтобы добавить виджет в макет используется метод макета addWidget:
# btn1 = QPushButton("Кнопка 1") # Создаем 3 кнопки
# btn2 = QPushButton("Кнопка 2")
# btn3 = QPushButton("Кнопка 3")
# layout = QHBoxLayout() # Создаем вертикальный макет
# layout.addWidget(btn1) # Добавляем кнопки в макет
# layout.addWidget(btn2)
# layout.addWidget(btn3)
# widget = QWidget() # Создаем виджет в который разместим макет
# widget.setLayout(layout) # Устанавливаем макет в виджет методом setLayout

# Так же можно использовать сочетания этих двух макетов,
# например, вертикальный макет, где каждый элемент это горизонтальный макет.
# Для того что бы в один макет поместить другой макет используется метод addLayout:

# class MainWindow(QMainWindow): # Это класс главного окна
#     def __init__(self):
#         super().__init__()
#         self.btn1 = QPushButton("Кнопка 1") # Создадим 6 кнопок
#         self.btn2 = QPushButton("Кнопка 2")
#         self.btn3 = QPushButton("Кнопка 3")
#         self.btn4 = QPushButton("Кнопка 4")
#         self.btn5 = QPushButton("Кнопка 5")
#         self.btn6 = QPushButton("Кнопка 6")
#         self.layout = QVBoxLayout() # Создадим главный макет, пусть он будет вертикальный
#         self.layout1 = QHBoxLayout() # Создадим два горизонтальных макета
#         self.layout2 = QHBoxLayout()
#         self.layout1.addWidget(self.btn1) # Заполним первый макет
#         self.layout1.addWidget(self.btn2)
#         self.layout1.addWidget(self.btn3)
#         self.layout2.addWidget(self.btn4) # Заполним второй макет
#         self.layout2.addWidget(self.btn5)
#         self.layout2.addWidget(self.btn6)
#         self.layout.addLayout(self.layout1) # Добавим горизонтальные макеты в вертикальный
#         self.layout.addLayout(self.layout2)
#         self.widget = QWidget()
#         self.widget.setLayout(self.layout)
#         self.setCentralWidget(self.widget)

# 3) QGridLayout - сеточный макет, позволяет размещать элементы по сетке разметки (как ячейки в Excel)
# При растягивании окна виджеты также будут пропорционально растягиваться.
# Чтобы добавить виджет в макет используется метод макета addWidget.
# Помимо самого виджета нужно указать индекс строки и колонки в макете.
# Стоит отметить, что ширина колонок и строк по умолчанию высчитывается из самого большого элемента,
# поэтому если мы пропустим одну колонку или строку, то ее ширина будет 0, и как будто этого столбца или строки и нет.
#  Пример:
# btn1 = QPushButton("Кнопка 1")
# btn2 = QPushButton("Кнопка 2")
# btn3 = QPushButton("Кнопка 3")
# btn4 = QPushButton("Кнопка 4")
# layout = QGridLayout()
# layout.addWidget(btn1, 0, 0)
# layout.addWidget(btn2, 0, 2)
# layout.addWidget(btn3, 1, 0)
# layout.addWidget(btn4, 1, 1)
# widget = QWidget()
# widget.setLayout(layout)

# Слоты и сигналы

# Сигналами называются объекты с данными, которые генерируется во время событий
# произошедшие в приложении (клик, скролл, загрузка данных и т.п.)

# Слотами называются функции обработчики, которые запускаются для обработки сигналов.
# Каждому сигналу можно добавить несколько слотов
# Например:
# btn1 = QPushButton("Кнопка 1")
# Соединяем событие clicked c анонимной функцией обработчиком, которая выводит номер кнопки
# btn1.clicked.connect(lambda: print(1))

# Поле для ввода текста QLineEdit

# Для создания виджета с полем ввода используется класс QLineEdit:
# Пример:
# line_edit = QLineEdit()

# У этого объекта есть такие полезные поля и методы как:
# Сигналы textChanged и textEdited - оба вызываются когда меняется текст:
# textChanged - вызывается когда текст меняется пользователем или действием программы
# textEdited - вызывается когда поле редактирует пользователь
# Аргументы событий - текущий текст.

# метод clear() - очищает поле ввода
# метод text() - возвращает текущий текст в виджете


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создадим 6 кнопок и свяжем их с обработчиком событий signal_handler.
        # Добавим между ними "прослойку" в виде анонимной функции, что бы передавать дополнительные аргументы (кнопку)
        self.btn1 = QPushButton("Кнопка 1")
        self.btn1.clicked.connect(lambda: self.signal_handler(self.btn1))
        self.btn2 = QPushButton("Кнопка 2")
        self.btn2.clicked.connect(lambda: self.signal_handler(self.btn2))
        self.btn3 = QPushButton("Кнопка 3")
        self.btn3.clicked.connect(lambda: self.signal_handler(self.btn3))
        self.btn4 = QPushButton("Кнопка 4")
        self.btn4.clicked.connect(lambda: self.signal_handler(self.btn4))
        self.btn5 = QPushButton("Кнопка 5")
        self.btn5.clicked.connect(lambda: self.signal_handler(self.btn5))
        self.btn6 = QPushButton("Кнопка 6")
        self.btn6.clicked.connect(lambda: self.signal_handler(self.btn6))
        # Создадим макет в виде сетки и разместим туда кнопки
        self.layout = QGridLayout()
        self.layout.addWidget(self.btn1, 0, 0)
        self.layout.addWidget(self.btn2, 0, 2)
        self.layout.addWidget(self.btn3, 1, 0)
        self.layout.addWidget(self.btn4, 1, 1)
        self.layout.addWidget(self.btn5, 2, 2)
        self.layout.addWidget(self.btn6, 2, 3)
        # Создадим поле ввода и поместим в макет
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit, 1, 3)
        # Создадим поле с текстом и поместим в макет
        self.label1 = QLabel()
        self.layout.addWidget(self.label1, 0, 3)
        # Свяжим сигналы изменения текста и нажатие кнопок 5 и 6 с разными слотами:
        self.line_edit.textChanged.connect(lambda x: self.label1.setText(x))  # Изменение текста label1
        self.line_edit.textEdited.connect(lambda x: print(f"Edit: {x}"))  # Отладочный вывод textEdited
        self.line_edit.textChanged.connect(lambda x: print(f"Change: {x}"))  # Отладочный вывод textChanged
        self.btn6.clicked.connect(lambda: self.line_edit.clear())  # По нажатию кнопки очищаем поле ввода
        self.btn5.clicked.connect(lambda: print(self.line_edit.text()))  # По нажатию кнопки выводим введеный текст в консоль
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def signal_handler(self, button):
        print("Нажата ", button.text())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

# ===================================================================
# Дополнительная теория
# ===================================================================

# Лямбда функции, они же анонимные функции

# Анонимная функция - это функция без имени с ограниченным функционалом тела.
# Записывается так: lambda <аргументы функции>: <возвращаемое значение>

# Например, такую функцию можно переписать как анонимную функцию:

# def sum(a, b):
#     return a + b

# sum = lambda a, b: a + b

# Функции с неизвестным количеством аргументов:
# Что бы создать функцию с неизвестным числом аргументов используется такой синтаксис:
# def func(*args, **kwargs):
#     # звездочка (*) - оператор распаковки, все значения из последовательности собираются в одну переменную
#     for arg in args:  # args - аргументы функции по типу: f(1, 2) [картеж]
#         print(arg)
#     for k, v in kwargs.items(): # kwargs - именованные аргументы по типу: f(a=1, b=2) [словарь]
#         print(f"{k} = {v}")
#
#
# func("Hello", 3, key=True, sep=123)
