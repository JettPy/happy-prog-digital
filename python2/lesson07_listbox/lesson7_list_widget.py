from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QMainWindow,
    QGridLayout,
    QListWidget,
    QListWidgetItem
)
import sys

# В этом уроке познакомимся с виджетом списком (QListbox) и немного со стилями

# Виджет QListbox представляет окно со списком из текстовых строк, по ним можно перемещаться и взаимодействовать с
# каждым элементом (выбирать, добавлять и удалять)

# Напишем простое приложение меню в котором будет список блюд и их стоймость.
# Также добавим список выбранных блюд и текстовое поле с общей стоимостью

# Константа с данными
FOOD = {
    'Стейк': 300,
    'Паста': 400,
    'Суши': 250,
    'Пицца': 675,
    'Салат': 200,
    'Суп': 300,
    'Бургер': 450,
    'Рыба': 175,
    'Карри': 280,
    'Шашлык': 215
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Меню ресторана')
        self.layout = QGridLayout()
        # Заведем переменную для хранения стоимости заказа
        self.cost = 0
        # Создадим список meal_list с названиями блюд и их стоимостью
        self.meal_list = QListWidget()
        # И создадим список order_list с выбранными блюдами
        self.order_list = QListWidget()
        self.total_cost = QLabel('Выберите блюда для расчета стоимости')
        self.reset_button = QPushButton('Очистить')
        self.layout.addWidget(self.meal_list, 0, 0)
        self.layout.addWidget(self.order_list, 0, 1)

        # (Тут я оставил свою задумку до того как добавил кнопку, что бы показать как можно еще использовать гриды)
        # Здесь помимо row и column указаны параметры rowSpan и columnSpan.
        # Последние два отвечают за то, сколько ячеек в ряду и в колонке займет виджет
        # self.layout.addWidget(self.total_cost, 1, 0, 1, 2)

        self.layout.addWidget(self.total_cost, 1, 0)
        self.layout.addWidget(self.reset_button, 1, 1)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        # Добавим еду из константы FOOD:
        for food, cost in FOOD.items():
            # Для добавления используется метод addItem или addItems (если нужно добавить сразу несколько)
            self.meal_list.addItem(f'{food} / {cost}')
        # self.meal_list.addItems(['Вода / 50', 'Пельмени / 150'])
        # Мы можем отслеживать переключение курсора с помощью сигнала currentItemChanged:
        # Этот сигнал передает объект QListWidgetItem - элемент списка.
        # У элементов списка есть такой полезный метод как text() - он возвращает текст содержимого элемента
        # Так же как и в обычных списках у наших элементов есть их индекс в списке.
        # Получить его у активного элемента можно, например методом currentRow() у списка
        # Данная строка может вызывать баг при удалении единственного элемента списка
        self.meal_list.currentItemChanged.connect(lambda x: print(x.text(), self.meal_list.currentRow()))
        # Теперь реализуем добавление выбранного объекта списка в список заказа.
        # Сделаем это сигналом двойного клика по элементу itemDoubleClicked:
        self.meal_list.itemDoubleClicked.connect(self.choose_a_meal)
        # А теперь добавим возможность удаления блюда из списка уже выбранных:
        self.order_list.itemDoubleClicked.connect(self.delete_a_meal)
        # И добавим очистку всего списка по нажатия на кнопку:
        self.reset_button.clicked.connect(self.reset)

    # Данный слот принимает сигнал с выбранным блюдом и добавляет его в список выбранных блюд
    def choose_a_meal(self, meal: QListWidgetItem):
        self.order_list.addItem(meal.text())
        # Также после добавления блюда будем пересчитывать общую стоимость заказа:
        self.cost += int(meal.text().split(' / ')[-1])
        self.total_cost.setText(f'Общая стоимость заказа: {self.cost}')

    # Этот слот отвечает за удаление выбранного элемента из списка
    def delete_a_meal(self, meal: QListWidgetItem):
        # Для удаления используется метод takeItem. Он принимает индекс элемента который мы удаляем.
        # В объекте QListWidgetItem к сожалению не находится индекс элемента в списке,
        # но его можно получить используя метод row у самого списка,
        # он принимает объект QListWidgetItem и возвращает индекс в списке
        # takeItem так же как и pop в обычном списке при удалении возвращает удаляемый элемент
        deleting_meal = self.order_list.takeItem(self.order_list.row(meal))
        # Теперь после удаления надо удалить и стоимость из общей суммы:
        self.cost -= int(deleting_meal.text().split(' / ')[-1])
        # Проверим self.cost на 0. Если список оказался пустым (cost = 0), то возвращаем первоначальный текст,
        # иначе просто обновим цифру в тексте:
        if self.cost == 0:
            self.total_cost.setText('Выберите блюда для расчета стоимости')
        else:
            self.total_cost.setText(f'Общая стоимость заказа: {self.cost}')

    # Этот слот для очистки всего списка заказа
    def reset(self):
        # Для полной очистки списка используется метод clear():
        self.order_list.clear()
        self.cost = 0
        self.total_cost.setText('Выберите блюда для расчета стоимости')


# Теперь поговорим немного о стилях
# Qt подчиняется тем же правилам, что и обычные CSS свойства.
# Стили можно указывать отдельно для каждого виджета или сразу ко всему приложению методом setStyleSheet.
# Либо можно создавать стили в отдельном файле, например style.qss:
# app.setStyleSheet(Path('login.qss').read_text())
# В закомментированном примере используется класс Path для вычисления пути.
# Для использования этого объекта добавьте from pathlib import Path

# Либо стили можно задавать как текст (в формате строки как в примере)
app = QApplication(sys.argv)
style = """
QWidget {
  background-color: #fff;
}
QLabel {
  color: #464d55;
  font-weight: 600;
}
QListWidget {
  border-radius: 8px;
  border: 1px solid #e0e4e7;
  padding: 5px 15px;
}
QListWidget:focus {
  border: 1px solid #d0e3ff;
}
QListWidget::placeholder {
  color: #767e89;
}
QPushButton {
  background-color: #0d6efd;
  color: #fff;
  font-weight: 600;
  border-radius: 8px;
  border: 1px solid #0d6efd;
  padding: 5px 15px;
  margin-top: 10px;
  outline: 0px;
}
QPushButton:hover,
QPushButton:focus {
  background-color: #0b5ed7;
  border: 3px solid #9ac3fe;
}
"""

app.setStyleSheet(style)
window = MainWindow()
window.show()
app.exec()
