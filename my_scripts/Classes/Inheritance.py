# Parent Class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Child class
class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        self.height = height
        super().__init__(length, breadth)

    def volume(self):
        return self.length * self.breadth * self.height


# Testing the classes
r1 = Rectangle(3, 5)
print(r1.area())  # Output: 15

c1 = Cuboid(3, 5, 4)
print(c1.area())  # Output: 15 (Inherited from Rectangle)
print(c1.volume())  # Output: 60