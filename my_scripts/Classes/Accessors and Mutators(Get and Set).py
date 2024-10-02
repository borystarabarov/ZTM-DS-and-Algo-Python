class Rectangle:
    def __init__(self, len, bre):
        self.len = len
        self.bre = bre

    def area(self):
        return self.len * self.bre


r1 = Rectangle(3,5)

print(r1.len)
print(r1.bre)
print(r1.area())

print('-------------------')
r1.len = 5


print(r1.len)
print(r1.bre)
print(r1.area())
        
