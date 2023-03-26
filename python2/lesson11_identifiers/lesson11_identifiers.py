# Идентификаторы

# В этом уроке продолжим работать с Canvas и в этот раз рассмотрим идентификаторы.
# По сути идентификатор - это такая же переменная, которая хранит в себе фигуру, нарисованную на Canvas.

from tkinter import *


# Создадим класс приложения, в конструкторе создадим все виджеты. В метод design вынесем всю логику расположения
# элементов в окне. Остальные методы будут вызываться при клике по кнопкам.
class App:
    def __init__(self):
        self.window = Tk()
        # Создаем виджет Canvas размером 1000 x 500 c голубоватым фоном
        self.canvas = Canvas(self.window, width=1000, height=500, background='#92b6f0')
        # Создадим фигуру прямоугольник на холсте, и запишем ее в переменную rectangle. Это и есть идентификатор.
        self.rectangle = self.canvas.create_rectangle(20, 20, 300, 300, fill='orange', outline='red', width=3)
        # Если попробуем вывести значение и тип идентификатора, то он выдаст 1 и <class 'int'>,
        # потому что идентификатор - это номер элемента на холсте.
        print(self.rectangle)
        print(type(self.rectangle))

        # Создание полей ввода для координат x1, y1, x2, y2, и поле для ввода цвета
        self.entry_x1 = Entry(self.window)
        self.entry_y1 = Entry(self.window)
        self.entry_x2 = Entry(self.window)
        self.entry_y2 = Entry(self.window)
        self.entry_color = Entry(self.window)
        # Рассмотри три метода работы с идентификаторами:
        # 1) Метод move - перемещение фигуры.
        self.button_move = Button(self.window, text='Move', command=self.move)
        # 2) Метод coords - Перемещает фигуру в заданную позицию.
        self.button_coors = Button(self.window, text='Coords', command=self.coords)
        # 3) Метод itemconfig - позволяет изменить некоторые параметры фигуры.
        self.button_config = Button(self.window, text='Config', command=self.itemconfig)
        # Вызовем метод design для отображения элементов
        self.design()
        mainloop()

    def design(self):
        self.entry_x1.grid(column=0, row=0)
        self.entry_y1.grid(column=1, row=0)
        self.entry_x2.grid(column=0, row=1)
        self.entry_y2.grid(column=1, row=1)
        self.button_move.grid(column=2, row=0)
        self.button_coors.grid(column=2, row=1)
        self.entry_color.grid(column=3, row=0)
        self.button_config.grid(column=3, row=1)
        self.canvas.grid(column=0, row=2, columnspan=4)

    # Метод move - перемещает все точки фигуры на холсте на заданные значения x, и y.
    def move(self):
        self.canvas.move(self.rectangle, 200, 200)

    # Метод coords - Перемещает фигуру в заданную позицию по координатам левого верхнего угла и правого нижнего угла.
    # Обратите внимание, что этот метод может изменить размеры фигуры.
    def coords(self):
        self.canvas.coords(self.rectangle, 20, 20, 300, 300)

    # Метод itemconfig - позволяет изменить некоторые параметры фигуры, как например цвет.
    def itemconfig(self):
        self.canvas.itemconfig(self.rectangle, fill='green', outline='white')


if __name__ == '__main__':
    App()
