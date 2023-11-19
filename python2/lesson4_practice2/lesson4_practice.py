from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, is_predator: bool):
        self._name = name
        self.__is_predator = is_predator

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food=None):
        print("Начинается кормешка")


class Lion (Animal):
    def __init__(self, name: str):
        super().__init__(name, True)

    def make_sound(self):
        print(f"{self._name} рычит")

    def feed(self, food=None):
        super().feed()
        print(f"Лев {self._name} ест {food}")


class Cow (Animal):
    def __init__(self, name: str):
        super().__init__(name, False)

    def make_sound(self):
        print(f"{self._name} мычит")


class Spider (Animal):
    def __init__(self, name: str):
        super().__init__(name, True)

    def make_sound(self):
        print(f"{self._name} молчит и стучит лапками")

    def feed(self, food=None):
        super().feed()
        print(f'Паук {self._name} ест {food}')


class Mosquito (Animal):
    def __init__(self, name: str):
        super().__init__(name, True)

    def make_sound(self):
        print(f"{self._name} надоедливо жужжит")


class Zoo:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__animals = []

    def feed_animals(self):
        for animal in self.__animals:
            animal.feed()

    def add_animal(self, anima: Animal):
        self.__animals.append(anima)

    def __add__(self, anima: Animal):
        self.__animals.append(anima)
        return self

    def animals_make_sound(self):
        for animal in self.__animals:
            animal.make_sound()


lion = Lion("Лёва")
cow = Cow("Ирина Николаевна")
mosq = Mosquito("Баран")
spider = Spider("Гена")

zoo = Zoo()
zoo + lion
zoo.add_animal(cow)
zoo + mosq + spider
zoo.feed_animals()
zoo.animals_make_sound()
