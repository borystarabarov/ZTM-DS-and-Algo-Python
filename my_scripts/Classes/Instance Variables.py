class Rectangle:
    def __init__(self, length=1, breadth=1) -> None:

        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length + self.breadth)
    
r1 = Rectangle()
print(r1.area())

r2 = Rectangle(5,10)
print(r2.area())


# Instance variables

class Test:
    def __init__(s):
        s.var1 = 1
    
    def func(s):
        s.var2 = 2

class Test2(Test):
    pass
    
    def __init__(s):
        super().__init__()
        s.var4 = 4


t1 = Test()
t1.func()
t1.var3 = [1,2,3,4,5]
print('t1      :', dir(t1))

t2 = Test2()
t2.func()
t2.var3 = [1,2,3,4,5]
print('t2      :', dir(t2))
