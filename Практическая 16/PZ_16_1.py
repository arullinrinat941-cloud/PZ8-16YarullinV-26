 #Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
#площади, длины окружности и диаметра.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # диаметр
    def diameter(self):
        return self.radius * 2

    # длина окружности
    def length(self):
        return 2 * math.pi * self.radius

    # площадь круга
    def area(self):
        return math.pi * self.radius ** 2


# ввод от пользователя
r = float(input("Введите радиус круга: "))

circle = Circle(r)

print("Диаметр:", circle.diameter())
print("Длина окружности:", circle.length())
print("Площадь:", circle.area())