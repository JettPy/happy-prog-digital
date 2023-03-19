# Виджет холст Canvas

# В этом уроке познакомимся с виджетом Canvas. Он позволяет создавать рисунки, анимации и так далее.
# В этом уроке научимся создавать объекты на холсте.

from tkinter import *

window = Tk()

# Для того что бы создать виджет холст используется следующий конструктор:
canvas = Canvas(window, width=900, height=700, bg="pink")
# Параметры width и height обязательны. Это параметры ширины и высоты холста.
canvas.pack()  # размещаем элемент в окне

# Далее рассмотрим несколько методов для рисования.
# 1) create_line - создает линию, получает координаты x1, y1 первой точки и x2, y2 второй точки.
# Все остальные параметры, такие как width и fill не обязательные.
canvas.create_line(10, 10, 200, 200, width=5, fill="green")

# 2) create_rectangle - создает прямоугольник. Получает координаты x, y левого верхнего угла и x, y правого
# нижнего угла. Outline - Необязательный параметр задающий цвет границы.
canvas.create_rectangle(220, 30, 400, 400, width=5, fill='green', outline="cyan")

# 3) create_oval - создает эллипс внутри границ прямоугольника, задающегося через координаты x, y левого верхнего
# угла и x, y правого нижнего угла.
canvas.create_oval(500, 10, 600, 200, width=5, fill='orange')

# 4) create_polygon - создает полигон, т.е. фигуру, соединенную по переданным точкам. Если задать smooth=True, то тогда
# углы фигуры будут сглажены.
canvas.create_polygon(100, 400, 250, 510, 200, 400, 50, 440, fill='red')
canvas.create_polygon(600, 400, 750, 510, 700, 400, 550, 460, fill='purple', smooth=True)

# 5) create_arc - создает окружность или сектор окружности, в заданных координатах x, y левого верхнего угла и x, y
# правого нижнего угла.
# start - указывает начало окружности, считается что 0 - это правый угол, положительное направление против
# часовой стрелки.
# extent - указывает длину дуги в градусах.
# style - указывает стиль сектора: PIESLICE - по умолчанию, линии проходят через центр, ARC - просто дуга окружности и
# CHORD - соединяет концы дуг прямой линией.
canvas.create_arc(500, 500, 700, 700, start=45, extent=270, style=CHORD)
canvas.create_arc(300, 500, 500, 700, start=45, extent=270, style=ARC)
canvas.create_arc(100, 500, 300, 700, start=45, extent=180, style=PIESLICE)

# 6) create_text - помещает переданный текст в text по координатам на холст. font - обозначает шрифт
canvas.create_text(700, 400, text='canvas is beautiful', font="Verdana 24")

# Задание 1: нарисовать снеговика из 3 уровней. Добавить ему ведро на голову, морковку, глаза и руки.
window.mainloop()
