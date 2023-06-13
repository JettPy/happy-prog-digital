import enum
import random
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
        self.tail = []

    # Это метод движения змейки, в зависимости от текущего направления движения, она перемещает сегменты змейки
    def move(self):
        # Если есть хвост, то перемещаем каждый сегмент с конца к следующему сегменту
        if len(self.tail) > 0:
            if len(self.tail) > 1:
                for i in range(len(self.tail), 0, -1):
                    self.canvas.coords(self.tail[i - 1], self.canvas.coords(self.tail[i - 2]))
            self.canvas.coords(self.tail[0], self.canvas.coords(self.head))
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

    # Метод возвращает координату столбца и строки в которой расположена голова змейки
    def get_coords(self):
        x = int(self.canvas.coords(self.head)[2]) // PIX
        y = int(self.canvas.coords(self.head)[3]) // PIX
        return x, y

    # Этот метод увеличивает длину змейки, то есть добавляет сегмент хвоста в конец
    def increase_length(self):
        # Если хвост есть, то берем координаты последнего сегмента хвоста
        if len(self.tail) > 0:
            x = int(self.canvas.coords(self.tail[-1])[2]) // PIX
            y = int(self.canvas.coords(self.tail[-1])[3]) // PIX
        # Если хвоста нет, то берем координаты головы
        else:
            x, y = self.get_coords()
        # Далее в зависимости от направления змейки добавляем новый сегмент
        match self.direction:
            case Direction.UP:
                self.tail.append(
                    self.canvas.create_rectangle((x - 1) * PIX, y * PIX, x * PIX, (y + 1) * PIX, fill='#99f78b')
                )
            case Direction.DOWN:
                self.tail.append(
                    self.canvas.create_rectangle((x - 1) * PIX, (y - 2) * PIX, x * PIX, (y - 1) * PIX, fill='#99f78b')
                )
            case Direction.LEFT:
                self.tail.append(
                    self.canvas.create_rectangle(x * PIX, (y - 1) * PIX, (x + 1) * PIX, y * PIX, fill='#99f78b')
                )
            case Direction.RIGHT:
                self.tail.append(
                    self.canvas.create_rectangle((x - 2) * PIX, (y - 1) * PIX, (x - 1) * PIX, y * PIX, fill='#99f78b')
                )
            case Direction.STOP:
                return


# Создадим класс для еды:
class Food:
    # Конструктор еды похож на конструктор головы змейки
    def __init__(self, x: int, y: int, canvas: Canvas):
        self.canvas = canvas
        self.food = canvas.create_rectangle((x - 1) * PIX, (y - 1) * PIX, x * PIX, y * PIX, fill='#f5594e')

    # Метод возвращает координату столбца и строки в которой расположена еда
    def get_coords(self):
        x = int(self.canvas.coords(self.food)[2]) // PIX
        y = int(self.canvas.coords(self.food)[3]) // PIX
        return x, y

    # Метод для пересоздания еды на поле. Сначала удаляем прошлую еду, а затем создаем новую
    def regenerate(self, x: int, y: int):
        self.canvas.delete(self.food)
        self.food = self.canvas.create_rectangle((x - 1) * PIX, (y - 1) * PIX, x * PIX, y * PIX, fill='#f5594e')


# Это класс игры, в нем мы создаем наше окно и помещаем в нее змейку и описываем управление.
class Game:
    def __init__(self):
        self.window = Tk()
        self.width = 35
        self.height = 35
        self.canvas = Canvas(width=self.width * PIX, height=self.height * PIX, bg='#6da4fc')
        self.canvas.pack()
        # Помещаем змейку в центр
        self.snake = Snake(self.width // 2 + 1, self.height // 2 + 1, self.canvas)
        # создаем еду в случайной ячейке поля
        food_x, food_y = random.randint(1, self.width), random.randint(1, self.height)
        self.food = Food(food_x, food_y, self.canvas)
        # Устанавливаем фокус на canvas
        self.canvas.focus_set()
        # Добавляем слушатели событий нажатия кнопок управления и их слушатели
        self.canvas.bind('<a>', lambda _: self.snake.change_direction(Direction.LEFT))
        self.canvas.bind('<d>', lambda _: self.snake.change_direction(Direction.RIGHT))
        self.canvas.bind('<w>', lambda _: self.snake.change_direction(Direction.UP))
        self.canvas.bind('<s>', lambda _: self.snake.change_direction(Direction.DOWN))

    # Это метод получения очка. В нем мы увеличиваем размер змейки и пересоздаем еду
    def get_score(self):
        self.snake.increase_length()
        food_x, food_y = random.randint(1, self.width), random.randint(1, self.height)
        self.food.regenerate(food_x, food_y)

    # Это метод цикла в змейке. Мы перемещаем змейку и через 0.1 секунды запускаем метод заново
    def loop(self):
        self.snake.move()
        # Если еда совпала с координатами головы, то прибавляем очко
        if self.food.get_coords() == self.snake.get_coords():
            self.get_score()
        self.window.after(100, self.loop)

    # Метод для запуска процесса игры, запускает отрисовку анимации перемещения змейки.
    def run(self):
        self.loop()
        mainloop()


# Создание и запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()
