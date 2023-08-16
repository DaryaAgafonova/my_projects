"""
Задача 3. Mixins
От класса Vehicle будет наследоваться два новых класса, подлежащих дальйшей реализации, — Car и Airplane:
Подключите функционал радио к машине таким образом, чтобы не добавлять его к самолету.

Используйте класс-миксин, который самостоятельно создайте. Реализация миксина может быть минимальной — так,
чтобы ожидаемое поведение соблюдалось. Пропишите инициализатор в классе Car
"""

class Vehicle:

    def __init__(self, position):  # position: кортеж (10, 20)

        self.position = position


    def travel(self, destination):

        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)


    @staticmethod
    def calculate_route(source, to):

        return 0  # to be realized


    def move_along(self, route):

        print("moving")


class Radio():

    def turn_on_radio(self, title):

        return f"Playing {title}"


class Car(Vehicle, Radio):
    pass


class Airplane(Vehicle):
    pass


car = Car((10, 20))
print(car.turn_on_radio('Moscow FM'))
# Playing Moscow FM