# Проект "Крестики-нолики"


# Задаем игровое поле, 0 - поле пустое, 1 - сходил первый игрок, 2 - сходил второй игрок
field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Номер текущего игрока
player = 1


# Функция вывода игрового поля в консоль
def print_field():
    print('+---+---+---+')
    for row in field:
        print('|', end='')
        for element in row:
            if element == 0:
                print('   |', end='')
            elif element == 1:
                print(' X |', end='')
            else:
                print(' O |', end='')
        print('\n+---+---+---+')


# Функция совершения хода в клеточку с переданным номером строки и столбца
def make_move(row: int, column: int):
    global player
    field[row - 1][column - 1] = player  # Указываем какой игрок сходил
    player = 3 - player  # Меняем номер игрока (Если ходил первый игрок: 3 - 1 = 2, если второй: 3 - 2 = 1)


# Функция проверки победителя, доработать дома самим.
# Она должна возвращать 0, если победителя нет, 1 если победил первый игрок, 2 если победил 2 игрок.
# Подсказка: обратите внимание на то, что содержится в переменной field.
def check_is_win():
    return 0


# Основная часть программы
count = 0  # Счетчик ходов
while True:
    print_field()  # Выводим поле на экран
    winner = check_is_win()  # Проверяем победителя
    if winner == 1 or winner == 2:  # Если есть победитель выводим его номер и выходим из цикла
        print(f'Победил игрок {winner}')
        break
    if count == 9:  # Если совершено 9 ходов, т.е. все клеточки заполнены, а победителя нет, значит ничья
        print(f'Ничья')
        break
    print(f'Ход игрока: {player}')
    while True:
        # Бесконечный цикл пока не будут введены правильные номера строки и столбца и если выбранная клеточка не пустая
        row, column = [int(x) for x in input("Введите № строки и № столбца (от 1 до 3): ").split()]
        if 1 <= row <= 3 and 1 <= column <= 3 and field[row - 1][column - 1] == 0:
            break
        else:
            print("Ход запрещен!")
    make_move(row, column)  # Совершаем ход и меняем игроков
    count += 1  # Увеличиваем счетчик ходов
