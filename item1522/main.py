"""
Задача 2. Функции issubclass() и isinstance()
Реализуйте метод __check, который проверяет допустимость данных при инициализации товара.
"""

class Item():

    """ Класс Item с полями:
    название товара,
    цена товара,
    количество товара."""

    def __init__(self, name, price, quantity=0):

        """ Инициализируем атрибутов класса  """

        self.name = name
        self.price = price
        self.quantity = quantity

        self.__check(name, price, quantity)


   # @property
   # def check(self):

    #    """ """

     #   return self._check

    @staticmethod
    def __check(name: str, price: int | float, quantity: int) -> None:


        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой.")

        if not isinstance(price, int | float):
            raise TypeError("Цена товара должна быть числом.")

        if not isinstance(quantity, int):
            raise TypeError("Количество товара должно быть целым числом.")



print(Item("phone", 1800, 5))
# <__main__.Item object at 0x7f38a7110b90>

print(Item(18000, 'phone', 5))
# TypeError: Название товара должно быть строкой.


print(Item('phone', '18000', 5))
# TypeError: Цена товара должна быть числом.


print(Item('phone', 18000, 5.5))
# TypeError: Количество товара должно быть целым числом.