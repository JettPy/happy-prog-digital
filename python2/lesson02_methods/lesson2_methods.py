# Методы классов

# Вы уже знакомы с классами, объектами и их полями.
# Рассмотрим функции внутри классов, то есть методы.
# Мы уже знакомы с методом называемый конструктором: __init__.
# Названия, которые имеют два нижних подчеркивания вначале и в конце называются дандер методы или "магические методы".
# Это специальные методы которые неявно вызываются самим интерпретатором python.
# Например:
# __init__ - вызывается когда мы создаем класс: tr = Turtle()
# __str__ - вызывается когда мы пытаемся вывести объект в консоль и наш объект приводиться к строке
# __add__ - вызывается когда мы складываем два класса с помощью знака "+": a = classA; b = classB; c = a + b
# и так далее. Этих методов много


# Так же можно создавать и обычные функции (методы) внутри наших классов.
# Рассмотрим пример на классе Person:
class Person:
    def __init__(self, name):  # дандер метод конструктора класса, принимает имя name, тип: строка
        self.age = None
        self.name = name

    def __str__(self):  # дандер метод перевода объекта к строке, что бы вывести его с помощью print()
        return f'Person: {self.name}'

    def walk(self):  # обычный метод, который печатает, что человек идет
        print(f'{self.name} идёт')

    def get_name(self):  # обычный метод, который возвращает имя человека (такие методы называются геттеры)
        return self.name

    def set_age(self, age):  # обычный метод, который устанавливает возраст человека (такие методы называются сеттеры)
        self.age = age


p = Person('Sergey')
p.set_age(22)
print(p)  # выведет "Person: Sergey"
p.walk()  # выведет "Sergey идёт"


# Рассмотрим другие методы на основе класса дроби.
# Далее увидим как работает дандер метод __add__ и реализуем статический метод.
# Статические методы - это такие методы которые принадлежат самому классу, но не конкретному объекту
# У таких методов нет аргумента self, так как они не зависят от объекта.
# Статические методы вызываются не через объект класса как: <объект>.<метод>, а через сам класс: <класс>.<метод>
class Fraction:
    def __init__(self, a, b):  # конструктор, принимает числитель (numerator) и знаменатель (denominator)
        self.num = a
        self.den = b

    # @<название> - это функции декораторы. Декораторы оборачивают функцию, как бы перехватывая управление функцией,
    # для того что бы предварительно выполнить какую то дополнительную логику указанную языком python или разработчиком
    @staticmethod
    def gcd(a, b):  # это статический метод, он не зависит от объекта, и не имеет указателя self
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    def __add__(self, other):  # дандер метод, который вызнается когда мы хотим сложить две дроби через знак "+"
        common_den = self.den * other.den
        common_num = self.num * other.den + self.den * other.num
        gcd = Fraction.gcd(common_den, common_num)  # вызываем статический метод у самого класса Fraction
        return Fraction(common_num // gcd, common_den // gcd)

    def __str__(self):  # дандер метод для того что бы дробь выводилась в привычном для нас виде.
        return f'{self.num}/{self.den}'


# Создадим два объекта класса дроби соответсвующее дробям 5/6 и 1/6.
f1 = Fraction(5, 6)
f2 = Fraction(1, 6)
print(f1 + f2)  # Сложение дробей и вывод результата в консоль. Тут неявно вызываются дандер методы __add__ и __str__