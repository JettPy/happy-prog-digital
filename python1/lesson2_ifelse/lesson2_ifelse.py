# Ветвление if-else

# Иногда необходимо выполнить какое-то действие в зависимости от условия.
# Например: повернуть налево, если впереди тупик или проверить число на четность,
# если оно четное то вывести "четное", иначе вывести "нечетное".

# Это все ветвление (как ветки на дереве)

# В python для этого используется специальная команда if(если):
#   if <условие>:
#       <набор команд>

a = 5
if a > 3:
    print("a > 3")  # a > 5 ? да, значит выведет "a > 3"
print("a =", a)  # эта строчка будет выводиться всегда

# Условие - это логическая операция, которая возвращает либо true "истина", либо false "ложь".

# Для того что бы отделить блоки команд в python используется отступ слева:

# блок кода 1
if a > 3:  # if 1
    # блок кода 2
    print("a > 3")
    if a > 4:  # if 2
        # блок кода 3
        print("a > 4")
    if a == 5:  # if 3
        # блок кода 4
        print("a = 5")
# снова блок кода 1
print("a = ", a)

# Если if 1 будет ложным, то весь код в блоке 2 не будет выполнен

# Если необходимо выполнить код в случае ложи в if существует команда else (иначе):
b = 3
if b > 4:  # false
    print("b > 4")  # этот код не будет выполнен
else:
    print("b <= 4")

# что бы осуществлять ветвление больше чем на 2 варианта,
# можно вставлять промежуточную команду elif (сокращение от if else):
#   if <условие 1>:
#       <набор команд 1>
#   elif <условие 2>:
#       <набор команд 2>

c = 5
if c > 10:  # false
    print('c > 10')  # этот код не будет выполнен
elif c > 2:  # true
    print('c > 2, но c <= 10')  # Вывод: c > 2, но c <= 10
else:  # сюда программа уже не зайдет
    print('c <= 2')

# условия elif и else не обязательны для if,
# но if обязателен для elif и else

# В python версии 3.10 (вышла осенью 2021 года) добавили конструкцию известную как switch-case.
# Но в python она называется match-case.
# Эта конструкция используется, в случаях когда возникает большое перечисление условий elif:
# match <выражение>:
#   case <результат 1>:
#     <набор команд 1>
#   case <результат 2>:
#     <набор команд 2>
#   ...
#   case _: результат по умолчанию
#     <набор команд по умолчанию>

d = 1
e = 2
match d + e:
    case 2:
        print("e + d =", 2)
    case 3:
        print("e + d =", 3)
    case 4:
        print("e + d =", 4)
    case _:
        print("я не знаю")

# эта запись аналогична такой в if-else:
if d + e == 2:
    print("e + d =", 2)
elif d + e == 3:
    print("e + d =", 3)
elif d + e == 4:
    print("e + d =", 4)
else:
    print("я не знаю")

# Задание 1:
# Написать программу мини-ежедневник, в зависимости от дня недели она должна выводить,
# чем автор будет заниматься в этот день
day = 'Пятница'
if day == 'Воскресенье':
    print('Я отдыхаю дома')
elif day == 'Суббота':
    print('Я учу питон')
else:
    print('Я учусь в школе')

# Задание 2:
# Пользователь вводит число с клавиатуры, и программа должна вывести, четное оно или нечетное
num = int(input())
if num % 2 == 0:
    print('even')
else:
    print('odd')
