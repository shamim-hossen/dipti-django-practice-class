#CLASS & OBJECT
# class MyClass:
#     x = 5

# p1 = MyClass()
# p1.x = 10

# p2 = MyClass()
# p2.x = 20

# p3 = MyClass()
# p3.x = 30

# print(p1.x, p2.x, p3.x)



'''Creating a simple class and object'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Creating an object of Car class
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()  # Output: Brand: Toyota, Model: Corolla, Year: 2020

'''Using class inheritance'''
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} says {self.sound}")

class Dog(Animal):
    def __init__(self, breed, name):
        super().__init__("Dog", "bark")
        self.breed = breed
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

# Creating an object of Dog class
dog1 = Dog("Labrador", "Buddy")
dog1.display_info()  # Output: Name: Buddy, Breed: Labrador
dog1.make_sound()    # Output: The Dog says bark



'''Using class variables and methods'''
class Circle:
    # Class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

    @classmethod
    def set_pi(cls, value):
        cls.pi = value

# Creating objects of Circle class
circle1 = Circle(5)
print(circle1.area())  # Output: 78.53975

circle2 = Circle(7)
print(circle2.area())  # Output: 153.93804

# Changing the value of pi using class method
Circle.set_pi(3.14)

# Area recalculated with the updated value of pi
print(circle1.area())  # Output: 78.5
print(circle2.area())  # Output: 153.86
