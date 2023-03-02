# Виджет поле ввода Entry

from tkinter import *

# Часто в программах можно встретить текстовые поля для ввода информации.
# Например, формы для заполнения имени, пароля, почты.
# В tkinter этот функционал реализует класс Entry.

# Рассмотрим как работает программа на примере калькулятора.

# Далее создадим функции, которые нам пригодятся попозже:


# Функция получения чисел из полей ввода
def get_nums():
    try:
        # У класса Entry есть метод get:
        # <объект Entry>.get()
        # этот метод работает аналогично функции input. Он тоже читает ввод и возвращает результат строкового типа
        a = int(first_entry.get())  # преобразуем полученный текст к типу целого числа int
        b = int(second_entry.get())
        return a, b, False  # в случае успеха возвращаем из функции эти два числа и значение ошибки, равное false
    except ValueError:  # если же были введены не целые числа или поля пустые, то обработаем эту ошибку
        result_label.config(text='введите 2 целых числа!')  # в поле результата выведем сообщение об ошибке
        return 0, 0, True  # в случае некорректного ввода возвращаем нули и значение ошибки, равное true


# Функция сложения введенных чисел
def get_sum_of_nums():
    a, b, error = get_nums()  # получаем результат из функции выше
    if not error:  # если ошибки нет
        result_label.config(text=a + b)  # выводим сумму в поле результата, иначе ничего не делаем


# Функция разности введенных чисел
def get_diff_of_nums():
    a, b, error = get_nums()  # получаем результат из функции get_nums
    if not error:  # если ошибки нет
        result_label.config(text=a - b)  # выводим разность в поле результата, иначе ничего не делаем


# Функция произведения введенных чисел
def get_prod_of_nums():
    a, b, error = get_nums()  # получаем результат из функции get_nums
    if not error:  # если ошибки нет
        result_label.config(text=a * b)  # выводим произведение в поле результата, иначе ничего не делаем


# Функция частного введенных чисел
def get_quot_of_nums():
    a, b, error = get_nums()  # получаем результат из функции get_nums
    if not error:  # если ошибки нет
        if b == 0:  # если делитель равен нулю
            result_label.config(text='на 0 делить нельзя!')  # то выводим в поле результата, что на 0 делить нельзя
        else:  # если же делитель не равен нулю
            result_label.config(text=a / b)  # выводим частное в поле результата, иначе ничего не делаем


# Функция очистки полей ввода
def clear_entries():
    # В классе Entry есть метод delete:
    # <объект Entry>.delete(<откуда>, <докуда>)
    # этот метод удаляет символы в указанном диапазоне, последний элемент не включается
    # Также в tkinter есть специальная константа, означающая конец - END
    first_entry.delete(0, END)  # удаляем все символы из полей ввода с начала и до конца
    second_entry.delete(0, END)


# Функция вставки примера в поля ввода
def paste_example():
    # Используя метод insert класса Entry можно вставлять строки в указанную позицию поля ввода:
    # <объект Entry>.insert(<куда>, <что вставляем>)
    # опять же воспользуемся константой END для вставки чисел:
    first_entry.insert(END, '5')  # вставляем число 5 в конец первого поля ввода
    second_entry.insert(END, '2')  # вставляем число 2 в конец второго поля ввода


# Основная программа:

window = Tk()
window.title('калькулятор')
first_label = Label(window, text="первое число", width=14)
first_label.grid(row=0, column=0)
second_label = Label(window, text="второе число", width=14)
second_label.grid(row=1, column=0)
# Создадим объект класса Entry для ввода первого числа, структура конструктора выглядит так:
first_entry = Entry(window, width=6)  # В конструкторе можно настроить по размер, цвет и т. д., смотрите документацию
first_entry.grid(row=0, column=1)
second_entry = Entry(window, width=6)  # Создаем еще одно поле ввода для второго числа
second_entry.grid(row=1, column=1)
button_add = Button(window, text=' + ', command=get_sum_of_nums, width=10)  # создадим кнопку для сложения чисел
button_add.grid(row=2, column=0)
button_sub = Button(window, text=' - ', command=get_diff_of_nums, width=10)  # создадим кнопку для вычитания чисел
button_sub.grid(row=2, column=1)
button_mult = Button(window, text=' * ', command=get_prod_of_nums, width=10)  # создадим кнопку для умножения чисел
button_mult.grid(row=3, column=0)
button_div = Button(window, text=' / ', command=get_quot_of_nums, width=10)  # создадим кнопку для деления чисел
button_div.grid(row=3, column=1)

# Далее создадим вспомогательные функции для очистки полей и вставки значений для примера работы
button_clear = Button(window, text=' очистить ', command=clear_entries, width=10)  # создадим кнопку для очистки полей
button_clear.grid(row=4, column=0)
button_example = Button(window, text=' пример ', command=paste_example, width=10)  # создадим кнопку для вставки примера
button_example.grid(row=4, column=1)

# И наконец создадим лейбл для вывода результата работы программы (светло-зеленого цвета)
result_label = Label(window, text='Результат', width=24, bg='#9AD9A0')
result_label.grid(row=5, column=0, columnspan=2)
mainloop()
