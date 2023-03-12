# Проект калькулятор

from tkinter import *


# Для удобства работы обернем все окно в класс. Тогда мы сможем разделить логику программы на инициализацию,
# дизайн приложения, и вспомогательные методы, которые у нас раньше были функциями.
class Calculator:
    def __init__(self) -> None:  # Это конструктор, тут создаются все виджеты приложения
        self.window = Tk()
        self.entry = Entry(self.window, )
        self.history = Listbox(self.window)
        self.button1 = Button(self.window, text="1", width=3, height=3, command=lambda: self.put_sym("1"))
        self.button2 = Button(self.window, text="2", width=3, height=3, command=lambda: self.put_sym("2"))
        self.button3 = Button(self.window, text="3", width=3, height=3, command=lambda: self.put_sym("3"))
        self.button4 = Button(self.window, text="4", width=3, height=3, command=lambda: self.put_sym("4"))
        self.button5 = Button(self.window, text="5", width=3, height=3, command=lambda: self.put_sym("5"))
        self.button6 = Button(self.window, text="6", width=3, height=3, command=lambda: self.put_sym("6"))
        self.button7 = Button(self.window, text="7", width=3, height=3, command=lambda: self.put_sym("7"))
        self.button8 = Button(self.window, text="8", width=3, height=3, command=lambda: self.put_sym("8"))
        self.button9 = Button(self.window, text="9", width=3, height=3, command=lambda: self.put_sym("9"))
        self.button0 = Button(self.window, text="0", width=3, height=3, command=lambda: self.put_sym("0"))
        self.button_p = Button(self.window, text="+", width=3, height=3, command=lambda: self.put_sym("+"))
        self.button_m = Button(self.window, text="-", width=3, height=3, command=lambda: self.put_sym("-"))
        self.button_d = Button(self.window, text="/", width=3, height=3, command=lambda: self.put_sym("/"))
        self.button_u = Button(self.window, text="*", width=3, height=3, command=lambda: self.put_sym("*"))
        self.button_r = Button(self.window, text="=", width=3, height=3, command=self.get_answer)
        self.button_c = Button(self.window, text="c", width=3, height=3, command=self.clear_entry)
        self.button_rs = Button(self.window, text=")", width=3, height=3, command=lambda: self.put_sym(")"))
        self.button_ls = Button(self.window, text="(", width=3, height=3, command=lambda: self.put_sym("("))
        self.design()
        mainloop()

    def design(self):  # Это метод отвечающий за дизайн приложение, то как располагаются элементы в приложении
        self.history.grid(row=0, column=0, rowspan=5)
        self.entry.grid(row=0, column=1, columnspan=5)
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=1, column=2)
        self.button3.grid(row=1, column=3)
        self.button4.grid(row=2, column=1)
        self.button5.grid(row=2, column=2)
        self.button6.grid(row=2, column=3)
        self.button7.grid(row=3, column=1)
        self.button8.grid(row=3, column=2)
        self.button9.grid(row=3, column=3)
        self.button0.grid(row=4, column=1)
        self.button_c.grid(row=4, column=3)
        self.button_p.grid(row=1, column=4)
        self.button_m.grid(row=2, column=4)
        self.button_d.grid(row=4, column=4)
        self.button_u.grid(row=3, column=4)
        self.button_r.grid(row=4, column=2)
        self.button_rs.grid(row=1, column=5)
        self.button_ls.grid(row=2, column=5)

    def put_sym(self, sym):  # Это метод, который помещает символ нажатой кнопки в поле ввода
        self.entry.insert(END, sym)

    def get_answer(self):  # Метод отвечает за расчет переданного выражения и вывода результата в историю и в поле ввода
        express = self.entry.get()
        res = eval(express)
        self.history.insert(END, express + "=" + str(res))
        self.entry.delete(0, END)
        self.entry.insert(END, res)

    def clear_entry(self):  # Этот метод очищает поле ввода
        self.entry.delete(0, END)


if __name__ == "__main__":  # Это точка входа программы. Запуск начинается отсюда
    c = Calculator()
