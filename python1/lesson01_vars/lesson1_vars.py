# Переменные и функции

# Для вывода информации в python используется функция print().
# Вызов функции всегда заканчивается скобочками ().

print("Привет, мир!")

# Для хранения данных и работы с ними используются переменные.
# Переменная - это ячейка памяти которая хранит в себе информацию определенного типа.

x = "Привет, мир!"  # переменная x - хранит в себе строчку "Привет, мир!"
print(x)  # выводим переменную x

# У переемных есть тип.
# Тип переменной это описание того что хранится в переменной.
# Для того что бы узнать тип переменной можно воспользоваться функцией type()
# например переменная x содержит в себе текст, значит ее тип строка(str)

# основные типы в python:
print(type("Строка"))  # str, строка
print(type(12))  # int, целое число 0, 1, 2, ...
print(type(2.5))  # float, вещественное число
print(type(True))  # bool, логический тип ИСТИНА / ЛОЖЬ


# для ввода используется функция input()
x = input()  # вводим данные
print(x)  # выводим x

# input возвращает строку, поэтому для работы
# с другими переменными необходимо привести ее к нужному типу:
x = input()  # вводим 3
print(x + x)  # вывод будет 33 строки просто объединились
x = int(x)  # теперь x - число
print(x + x)  # вывод будет 6

# арифметические операции
y = 5  # присваивание (это не равенство из математики!)
x = 2  # читается справа налево "5 положить в y" и "2 положить в x"
r = y + x  # сложение r = 5 + 2
print(r)  # вывод: 7
r = y - x  # вычитание r = 5 - 2
print(r)  # вывод: 3
r = y * x  # умножение r = 5 * 2
print(r)  # вывод: 10
r = y / x  # деление r = 5 / 2
print(r)  # вывод: 2.5
r = y // x  # целочисленное деление r = mod(5,2)
print(r)  # вывод: 2
r = y % x  # остаток от деления r = ost(5,2)
print(r)  # вывод: 1
r = y ** x  # возведение в степень r = 5^2
print(r)  # вывод: 25

# если мы проводим операцию с переменной и хотим
# в нее же сохранить результат можно записать это так:

a = 2
a = a + 1  # читается как прибавить к переменной a 1 и сохранить переменную в a
print(a)  # вывод: 3

# эту запись можно укоротить:
a = 2
a += 1  # теперь a = 3

# такое сокращение работает со всеми операциями +=, -=, *=, /=, //=, %=, **=
a = 2
a += 2
print(a)

a = 2
a -= 2
print(a)

a = 2
a *= 2
print(a)

a = 2
a /= 2
print(a)

a = 2
a //= 2
print(a)

a = 2
a %= 2
print(a)

a = 2
a **= 2
print(a)

# для сравнения чисел моно используются следующие операции:
a = 3
b = 4
c = a > b  # a больше b
print(c)  # Вывод: False
c = a >= b  # a больше либо равно b
print(c)  # Вывод: False
c = a < b  # a меньше b
print(c)  # Вывод: True
c = a <= b  # a меньше либо равно b
print(c)  # Вывод: True
c = a == b  # a равно b
print(c)  # Вывод: False
c = a != b  # a не равно b
print(c)  # Вывод: True

# с логическими типами тоже есть логические операции

a = True
b = False

# a И b - если a и b ИСТИНА, вернет ИСТИНУ(True),
# в противном случае вернет ЛОЖЬ(False)
print(a and b)  # вывод: False
print(True and True)  # вывод: True
print(True and False)  # вывод: False
print(False and True)  # вывод: False
print(False and False)  # вывод: False

# a ИЛИ b - если a или b ИСТИНА, вернет ИСТИНУ(True),
# в противном случае вернет ЛОЖЬ(False)
print(a and b)  # вывод: True
print(True and True)  # вывод: True
print(True and False)  # вывод: True
print(False and True)  # вывод: True
print(False and False)  # вывод: False

# НЕ a - вернет ИСТИНУ(True), если a = ЛОЖЬ(False)
# или ЛОЖЬ(False), если a = ИСТИНА(True)
print(not a)  # вывод: False
print(not True)  # вывод: False
print(not False)  # вывод: True