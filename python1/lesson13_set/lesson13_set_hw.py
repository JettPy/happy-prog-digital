# Домашнее задание по множествам set:

# Задача 1:
# Напишите программу, которая будет выполнять последовательность запросов вида ADD num, PRESENT num и
# COUNT (без параметра). Программу обязательно следует писать с использованием шаблонного типа set.
# Выполнение каждого запроса вида ADD num должно добавлять элемент num во множество (если такой элемент уже есть,
# добавление ещё одной копии не изменяет множество), на экран при этом ничего не выводится.
# При выполнении каждого запроса вида PRESENT num должно выдаваться сообщение «YES» или «NO» (большими буквами, в
# отдельной строке), соответственно тому, есть ли такой элемент во множестве; значение множества при этом не изменяется.
# При выполнении каждого запроса вида COUNT должна выдаваться на экран в отдельной строке текущее количество
# различных элементов в множестве; значение множества при этом не изменяется.

# Пример:
# ввод:
# 7
# ADD 5
# ADD 7
# COUNT
# PRESENT 3
# PRESENT 5
# ADD 3
# COUNT

# вывод:
# 2
# NO
# YES
# 3

# Задача 2:
# Дан текст:
text = """Advertisements want to persuade us to buy particular products How do they do it? 
Let imagine You are watching TV. It is a hot evening: You feel thirsty. You see an advert for a refreshing drink.
You see people looking cool and relaxed. You notice the name of the refreshing drink because you think it could be 
useful for you to satisfy your thirst. Advertisers study how people learn so that they can teach them to respond to 
their advertising. They want us to be interested, to try something, and then to do it again. These are the elements 
of learning: interest, experience and repetition. If an advert can achieve this, it is successful. If an advert 
works well, the same technique can be used to advertise different things. So, for example, in winter if the weather 
is cold and you see a family having a warming cup of tea and feeling cosy, you may be interested and note the name of 
the tea. Here the same technique is being used as with the cool, refreshing drink. If advertisements are to he learned, 
there is a need for lots of repetition. But advertisers have to be careful because too much repetition can result in 
consumer tiredness and the message may fall on deal ears. Consumers learn to generalize from what they have learned. 
So advertisers sometimes copy a highly successful idea that has been well learned by consumers. For example, the highly 
successful Weston Tea Country advertising for different tea has led to DAEWOO Country for automobile dealers and 
Cadbury Country for chocolate bars."""

# Посчитайте количество уникальных слов в тексе. Не забудьте привести все буквы к нижнему регистру и удалите знаки
# препинания. Выведите результат в виде числа.
