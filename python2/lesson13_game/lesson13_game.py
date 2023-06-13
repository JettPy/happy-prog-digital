import enum
from tkinter import *

# Задаем размер нашего пикселя
PIX = 20


# Создаем класс на основе Enum. Enum - это класс перечисление. Он используется для хранения констант связанных с
# какой-либо сущностью. В нашем случае у нс есть сущность направление движения змейки (Direction) и он содержит 5
# состояний движения: вверх, вниз, влево, вправо и стоит на месте.
class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    STOP = 5


class Snake:
    # Это конструктор змейки, он принимает координаты расположения головы змейки и ссылку на canvas в котором она
    # рисуется. Внутри мы также определяет поле направления, в начале змейка стоит на месте.
    def __init__(self, x: int, y: int, canvas: Canvas):
        self.canvas = canvas
        self.head = canvas.create_rectangle((x - 1) * PIX, (y - 1) * PIX, x * PIX, y * PIX, fill='#4c7847')
        self.direction = Direction.STOP

    # Это метод движения змейки, в зависимости от текущего направления движения, она перемещает сегменты змейки
    def move(self):
        match self.direction:
            case Direction.UP:
                self.canvas.move(self.head, 0, -PIX)
            case Direction.DOWN:
                self.canvas.move(self.head, 0, PIX)
            case Direction.LEFT:
                self.canvas.move(self.head, -PIX, 0)
            case Direction.RIGHT:
                self.canvas.move(self.head, PIX, 0)
            case Direction.STOP:
                return

    # Это метод изменения направления змейки. Змейка меняет свое направление только в том случае если направление
    # меняется с горизонтального на вертикальное, или наоборот, а также когда змейка стоит на месте
    def change_direction(self, direction: Direction):
        if (self.direction == Direction.UP or self.direction == Direction.DOWN) \
                and (direction == Direction.LEFT or direction == Direction.RIGHT) \
                or (self.direction == Direction.LEFT or self.direction == Direction.RIGHT) \
                and (direction == Direction.UP or direction == Direction.DOWN) \
                or self.direction == Direction.STOP:
            self.direction = direction


# Это класс игры, в нем мы создаем наше окно и помещаем в нее змейку и описываем управление.
class Game:
    def __init__(self):
        self.window = Tk()
        self.width = 35 * PIX
        self.height = 35 * PIX
        self.canvas = Canvas(width=self.width, height=self.height, bg='#6da4fc')
        self.canvas.pack()
        # Помещаем змейку в центр
        self.snake = Snake((self.width // 2 + 1) // PIX, (self.height // 2 + 1) // PIX, self.canvas)
        # Устанавливаем фокус на canvas
        self.canvas.focus_set()
        # Добавляем слушатели событий нажатия кнопок управления и их слушатели
        self.canvas.bind('<a>', lambda _: self.snake.change_direction(Direction.LEFT))
        self.canvas.bind('<d>', lambda _: self.snake.change_direction(Direction.RIGHT))
        self.canvas.bind('<w>', lambda _: self.snake.change_direction(Direction.UP))
        self.canvas.bind('<s>', lambda _: self.snake.change_direction(Direction.DOWN))

    # Это метод цикла в змейке. Мы перемещаем змейку и через 0.1 секунды запускаем метод заново
    def loop(self):
        self.snake.move()
        print(self.snake.direction)
        self.window.after(100, self.loop)

    # Метод для запуска процесса игры, запускает отрисовку анимации перемещения змейки.
    def run(self):
        self.loop()
        mainloop()


# Создание и запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()
