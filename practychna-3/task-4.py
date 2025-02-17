#Завдання 4: Створити абстрактний базовий клас (ABC) Shape з абстрактним методом area().
# Створити клас Circle, який успадковує Shape. Властивості - radius. Функції - area().
# Створити клас Rectangle, який успадковує Shape. Властивості - width та height. Функції - area()



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Клас Circle (коло)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Формула площі прямокутника


# Перевіряємо роботу
width_input = float(input("Введіть ширину прямокутника:"))
height_input = float(input("Введіть висоту прямокутника: "))
circle = Circle(float(input("Введіть радіус кола: ")))
rectangle = Rectangle(width_input, height_input)


print(f"Площа кола: {circle.area()}")  # Виведе 78.5
print(f"Площа прямокутника: {rectangle.area()}")  # Виведе 24
