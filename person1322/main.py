"""
Задача 1

Создайте класс Person, содержащий два атрибута: имя и возраст.

Создайте метод класса fromBirthYear с альтернативным способом создания экземпляра класса
Person — когда указан год рождения.

person = Person('Иван', 19)
person.display()

person1 = Person.fromBirthYear('Николай',  2000)
person1.display()

# вывод
Иван. Возраст: 19
Николай. Возраст: 23

Задача 2

Атрибуты из задачи 1 сделать приватными.
Написать к ним сеттеры, чтобы имя было строкой и содержало только буквы,
а возраст был больше нуля и меньше 120.
"""


from datetime import datetime
class Person():

    """ Класс с адтрибутами имя и возвраст """

    def __init__(self, name, age):

        """ Инициализируем атрибуты класса """

        self.__name = name
        self.__age = age


    @property
    def name(self):

        """ Сделан приваным """

        return self.__name


    @property
    def age(self):

        """ Сделан приватным """

        return self.__age


    @name.setter
    def name(self, name):

        """ Имя состоит только из букв и является строкой """

        if isinstance(name, str):
            self.__name = name
        else:
            print("Ошибка")


    @age.setter
    def age(self, age):

        """ Так как он приватный, делаем сеттер, если возраст от 0 и до 120 """

        if 0 < age < 120:
            self.__age = age
        else:
            print("Ошибка")

    def display(self):

        """ Метод, для отображения имени и возраста """

        return f"{self.name}. Возвраст {self.age}."


    @classmethod
    def fromBirthYear(cls, name, year):

        """ Метод, который высчитывает возраст, зная год рождения """

        age = datetime.today().year - year

        return cls(name, age)


p1 = Person("Дарья", 23)
print(p1) # <__main__.Person object at 0x7f9cf68f3a50>

d = p1.display()
print(d) # Дарья. Возвраст 23.

y = Person.fromBirthYear("Дарья", 2004)
print(y) # <__main__.Person object at 0x7f9cf68f3d90>
print(y.display()) # Дарья. Возвраст 19.

p1.name = "Lily"
p1.age = 121
print(p1.display()) # Ошибка
                    # Lily. Возвраст 23.

p1.name = 123
print(p1.display()) # Ошибка
                    # Lily. Возвраст 23.