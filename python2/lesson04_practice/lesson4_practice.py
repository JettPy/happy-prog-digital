from abc import ABC, abstractmethod


# Это абстрактный класс транспорта, от него будут наследоваться все виды транспорта
class Vehicle (ABC):
    def __init__(self, speed: int):  # Это конструктор класса
        self._speed = speed

    @abstractmethod
    def move(self):  # Это абстрактный метод, он зависит от вида транспорта
        pass


# Класс человека
class Person:
    def __init__(self, name: str, age: int):
        """
        Это конструктор человека который принимает имя и возраст
        :param name:
        :param age:
        """
        self.__name = name
        self.__age = age

    def __str__(self):  # Переопределенный дандер метод для приведения объекта к строке
        return self.__name


# Это класс автобуса, он способен перевозить людей.
class Bus (Vehicle):
    def __init__(self, number: int, speed: int):  # конструктор, принимает номер и скорость автобуса
        super().__init__(speed)
        self.__number = number
        self.__passengers = []  # список пассажиров внутри автобуса

    def move(self):  # метод движения автобуса
        print(f"Автобус № {self.__number} отправляется дальше")

    def get_people(self, person: Person | list[Person]):  # метод посадки пассажира или пассажиров
        if isinstance(person, Person):  # если это пассажир, то садиться 1 человек
            print(f'Пассажир {person} зашел в автобус № {self.__number}')
            self.__passengers.append(person)
        else:  # иначе это список пассажиров, и каждый по очереди садится в автобус
            print(f'Пассажиры ', end='')
            for p in person:
                print(f'{p} ', end='')
            print(f'зашли в автобус № {self.__number}')
            self.__passengers.extend(person)


# запуск нашей программы
b = Bus(2, 60)
p1 = Person("Иванов", 24)
p2 = Person("Петров", 20)
p3 = Person("Сидоров", 14)
p4 = Person("Маркин", 22)
b.get_people(p1)
b.get_people([p2, p3, p4])
b.move()
