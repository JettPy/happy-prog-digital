from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QToolBar,
    QLabel
)
from PyQt6.QtGui import (
    QAction,
    QIcon
)
import sys

# В этом уроке рассмотрим, как работает меню в графических приложениях.
# В меню часто входят такие пункты как "Файл" "Открыть" "Создать" "Сохранить" и так далее.

# Для начала познакомимся с виджетом QToolBar.
# Он представляет собой виджет с различными кнопками и подменю


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.label = QLabel("Текст")
        self.layout.addWidget(self.label)
        # Создание виджета QToolBar, конструктор принимает строку, содержащая название панели:
        self.toolbar = QToolBar("Tool bar")
        # если в панели используются иконки, то их размер можно указать с помощью метода setIconSize и
        # специального объекта размера QSize:
        self.toolbar.setIconSize(QSize(50, 50))
        # Для создания кнопки меню используется специальный класс QAction: работает он подобно кнопке,
        # но с возможностью использования горячих клавиш. Принимает иконку QIcon и/или текст кнопки.
        ok_button = QAction(QIcon("icons8-ок-48.png"), "ok!", self)
        error_button = QAction(QIcon("icons8-удалить-48.png"), "wrong!", self)
        # Для добавления экшена в toolbar используется метод addAction:
        # self.toolbar.addAction(ok_button)
        # Если нужно добавить разделитель между элементами используется метод addSeparator:
        # self.toolbar.addSeparator()
        # self.toolbar.addAction(error_button)
        # Как и в кнопках, с помощью setCheckable можно задать режим переключения (True/False).
        # Если его не указывать, то состояние всегда будет False
        ok_button.setCheckable(True)
        # Сигнал который можно подключить к какому-нибудь слоту - triggered:
        ok_button.triggered.connect(self.ok_action_handler)
        error_button.triggered.connect(self.error_action_handler)

        # Для создания полноценного меню у QMainWindow есть метод menuBar:
        menu = self.menuBar()
        # Для создания подменю используется метод addMenu, он принимает название подменю:
        file_menu = menu.addMenu("File")
        # А для создания экшена используется метод addAction, он принимает QAction:
        file_menu.addAction(ok_button)
        edit_menu = menu.addMenu("Edit")
        edit_menu.addAction(error_button)
        menu.addAction(ok_button)

        # Пример создания подменю для вкладки File:
        new_action = QAction('Новый', self)
        # Для создания горячих клавиш используется метод setShortcut:
        new_action.setShortcut('Ctrl+N')
        file_menu.addAction(new_action)

        open_action = QAction('Открыть', self)
        open_action.setShortcut('Ctrl+O')
        file_menu.addAction(open_action)

        save_action = QAction('Сохранить', self)
        save_action.setShortcut('Ctrl+S')
        file_menu.addAction(save_action)

        exit_action = QAction('Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.widget = QWidget()
        self.addToolBar(self.toolbar)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    # Методы далее меняют текст self.label

    def ok_action_handler(self, a):
        self.label.setText("Окей! " + str(a))
        self.label.setStyleSheet("color: green")

    def error_action_handler(self, a):
        self.label.setText("Ошибка! " + str(a))
        self.label.setStyleSheet("color: red")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
