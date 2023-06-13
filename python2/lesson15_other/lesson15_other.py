from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
# Это фреймы. Фреймы нужны если необходимо сгруппировать элементы
frame1 = Frame(window, padx=10, pady=10, background="red")
label1 = Label(frame1, text="Label 1")
label1.pack()
button1 = Button(frame1, text="Clck me")
button1.pack()
frame1.pack()
frame2 = Frame(window, padx=10, pady=10, background="blue")
label2 = Label(frame2, text="Label 2")
label2.pack()
button2 = Button(frame2, text="Clck me")
button2.pack()
frame2.pack()
# Это виджет ввода текста. Он похож на Entry, но в нем можно переносить строки и вводить многострочный текст
text = Text(window, width=10, height=4)
text.pack()
# Это список элементов для выпадающего окна
languages = ["Python", "C#", "Java", "JavaScript"]
# Combobox - выпадающее меню
# state="readonly" означает что мы не можем редактировать текст из списка
combobox = Combobox(window, values=languages, state="readonly")
combobox.pack()
mainloop()