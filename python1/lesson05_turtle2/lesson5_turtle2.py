# Дополнительные команды turtle

# В этом уроке посмотрим что еще интересного можно сделать с черепашкой и ее окружением.
# В этот раз импортируем черепашку другим способом:

from turtle import *
# from ... import - подключает только определенные функции, которые указываются после import.
# А звездочка * говорит о том что мы импортируем все функции.
# Таким образом нам больше не нужно добавлять имя библиотеки turtle:

trtl = Turtle()
trtl.shape('turtle')
trtl.speed(0)

# Мы можем получить экран по которому бегает черепашка с помощью Screen():
screen = Screen()

# Зададим фон методом bgcolor('цвет'):
screen.bgcolor('light green')

# Добавим интерактива, настроим экран, что бы пользователь сам мог управлять черепашкой.
# Для начала укажем экрану, что он должен обрабатывать события методом listen():
screen.listen()

# События - это какие-то действия: нажатия клавиш и клики.
# Обработчики событий - функции которые запускаются по определенным событиям


# Объявим функции которые будут вызываться по нажатию клавиш:
def move_forward():  # Движение прямо
    trtl.fd(10)


def move_back():  # Движение назад
    trtl.bk(10)


def turn_left():  # Поворачиваем налево
    trtl.lt(10)


def turn_right():  # Поворачиваем направо
    trtl.rt(10)


# Далее добавим события нажатия клавиш методом onkeypress(<функция, которая что то делает>, какая клавиша нажата):
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_back, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
# Заметьте, что, при передаче функции мы не вызываем ее: move_forward(), а указываем только имя функции move_forward.
# А вызов этой функции произойдет самостоятельно, когда будет нажата соответсвующая клавиша.

# Есть еще метод onkey. Разница лишь в том, что onkeypress будет работать пока зажата клавиша, а onkey сработает
# только после того, как клавиша будет отжата.
screen.onkey(bye, 'Escape')  # bye - встроенная функция завершения работы черепашки, будем ее вызывать по нажатию Esc.


# А теперь давайте еще добавим, что бы черепашка перемещалась в точку клика мыши.
# Для этого применяется метод onclick(<функция, которая что то делает>, <какая кнопка нажата>)
# Кнопку необязательно указывать, тогда по умолчанию будет считаться нажатие левой кнопки мыши.
# Отличие этого метода в том, что вызываемая функция будет принимать аргументы x и y - координаты точки, где был клик.
# Передадим метод черепашки goto(<координата x>, <координата y>) - который перемещает черепашку в заданную точку:
screen.onclick(trtl.goto)


# Задача 1:
# Сделайте так, что бы по нажатию на клавиши 1 и 2 рисовались квадрат и круг соответственно
def draw_circle():
    trtl.color('blue', 'pink')
    trtl.begin_fill()
    trtl.circle(50, 360)
    trtl.end_fill()
    trtl.color('black')


def draw_square():
    trtl.color('red', 'yellow')
    trtl.begin_fill()
    for i in range(4):
        trtl.fd(100)
        trtl.lt(90)
    trtl.end_fill()
    trtl.color('black')


screen.onkey(draw_circle, '1')
screen.onkey(draw_square, '2')

mainloop()
