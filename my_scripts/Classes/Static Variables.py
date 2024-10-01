class Rectangle:
    def __init__(self, length=1, breadth=1) -> None:
# Instance variables 
        self.length = length
        self.breadth = breadth
# Instance Method is dependent on instance variables 
    def area(self):
        return self.length * self.breadth
# Instance Method is dependent on instance variables     
    def perimeter(self):
        return 2*(self.length + self.breadth)
# Static method as it's not dependent on class or instance variables    
    @staticmethod
    def issquare(len, bre):
        return len == bre
    

r1 = Rectangle(3,5)
r2 = Rectangle(5,5)

print(r1.issquare(5, 5))
print(r2.issquare(5, 5))
print(Rectangle.issquare(5, 5)) # All three lines are refferencing to the same method

print(r1.issquare(r1.length, r1.breadth))
print(r1.issquare(r2.length, r2.breadth))
print(Rectangle.issquare(r1.length, r2.breadth)) 