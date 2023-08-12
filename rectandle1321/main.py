class Rectagnle():

    """ Класс с атрибутами длины и ширины """

    def __init__(self, length, width):

        """ Инициализируем атрибуты класса """

        self.length = length
        self.width = width


    def perimeter(self):

        """ Вычисляем периметр треугольника """

        return (self.length + self.width) * 2


    def area(self):

        """ Вычисляем площадь треугольника """

        return self.width * self.length


    def display(self):

        """ Метод, для отображения длины, ширины, периметра и площади """

        return f"""Длина прямоугольника {self.length}.
Ширина прямоугольника {self.width}.
Периметр прямоугольника {self.perimeter()}.
Площадь прямоугольника {self.area()}."""


r1 = Rectagnle(12, 6)
print(r1) # <__main__.Rectagnle object at 0x7f88cc513ad0>
p = r1.perimeter()
a = r1.area()
d = r1.display()
print(p) # (12 + 6) * 2 = 36
print(a) # 12 * 6 = 72
print(d) # Длина прямоугольника 12.
# Ширина прямоугольника 6.
# Периметр прямоугольника 36.
# Площадь прямоугольника 72.