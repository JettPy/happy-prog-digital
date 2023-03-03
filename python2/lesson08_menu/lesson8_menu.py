# Виджет меню Menu

# Часто в программах можно увидеть меню, которое находиться слева вверху окна.
# Что бы создать меню в tkinter используется класс Menu.

from tkinter import *


# Функции для заданий:
def add_label(text):  # функция добавления лейбла на экран
    label = Label(text=text)
    label.pack()
    widgets.append(label)  # запоминаем все лейблы в списке виджетов (для удаления)


def clear():  # функция удаления виджетов
    for widget in widgets:  # проходим по всем виджетам в списке и уничтожаем их с помощью метода destroy
        widget.destroy()


window = Tk()
# Создадим главное меню:
main_menu = Menu(window)
# Но меню не простой виджет, его нельзя разместить с помощью pack, grid и place.
# Для него есть специальный параметр menu в окне:
window.config(menu=main_menu)
# Заполним меню частыми командами. Для этого используется метод add_command:
main_menu.add_command(label='Edit')  # текст кнопки меню записывается в параметр label
# Для того что бы добавить команду в параметр command передаем имя функции которая будет выполнятся
main_menu.add_command(label='Help', command=lambda: print('Help нажата'))  # передаем анонимную функцию
# В меню можно вставлять и подменю. Добавим одно:
# Для подменю тоже нужно создавать меню:
file_menu = Menu(main_menu)  # но крепится оно к главному меню, а не к окну
# Добавим команд:
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
# Вложим наше подменю в главное меню. Для этого используется метод add_cascade:
main_menu.add_cascade(label='File', menu=file_menu)
# Но тут у нас появляется пунктирная линия, что бы ее убрать надо указать параметр teaoff со значением 0:
file_menu2 = Menu(main_menu, tearoff=0)
file_menu2.add_command(label='Open')
file_menu2.add_command(label='Save')
main_menu.add_cascade(label='File2', menu=file_menu2)


# Задание 1:
# Создать программу про города, страны и материки.
# При выборе пункта меню в окне появляется надпись соответствующего географического объекта
city_menu = Menu(main_menu, tearoff=0)
city_menu.add_command(label='Москва', command=lambda: add_label('Москва'))
city_menu.add_command(label='Одинцово', command=lambda: add_label('Одинцово'))
city_menu.add_command(label='Казань', command=lambda: add_label('Казань'))
main_menu.add_cascade(label='Города', menu=city_menu)

country_menu = Menu(main_menu, tearoff=0)
country_menu.add_command(label='Россия', command=lambda: add_label('Россия'))
country_menu.add_command(label='Китай', command=lambda: add_label('Китай'))
country_menu.add_command(label='Англия', command=lambda: add_label('Англия'))
main_menu.add_cascade(label='Страны', menu=country_menu)

mainland_menu = Menu(main_menu, tearoff=0)
mainland_menu.add_command(label='Евразия', command=lambda: add_label('Евразия'))
mainland_menu.add_command(label='Африка', command=lambda: add_label('Африка'))
mainland_menu.add_command(label='Австралия', command=lambda: add_label('Австралия'))
main_menu.add_cascade(label='Материки', menu=mainland_menu)


# Задание 2:
# Создайте дополнительное меню Очистить. При его выборе все надписи очищаются.
widgets = []
main_menu.add_command(label='Очистить', command=clear)

mainloop()