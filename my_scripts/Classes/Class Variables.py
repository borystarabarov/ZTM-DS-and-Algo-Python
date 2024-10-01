class Rectangle:
    
    class_variable = 0
    class_count = 0

    def __init__(self, length=1, breadth=1) -> None:

        self.length = length
        self.breadth = breadth
        Rectangle.class_count += 1

    def area(self):
        return self.length * self.breadth
# Instance Method is dependent on instance variables    
    def perimeter(self):
        return 2*(self.length + self.breadth)
# Class Method dependent on class variables only    
    @classmethod # decorator is not mandatory
    def countRectangleClassMethod(cls):
        print(cls.class_count)
    
r1 = Rectangle()
print(r1.class_count)

r2 = Rectangle()
print(r2.class_count)
r2.countRectangleClassMethod()
r1.countRectangleClassMethod() 
Rectangle.countRectangleClassMethod() # All three lines are refferencing to the same variable

