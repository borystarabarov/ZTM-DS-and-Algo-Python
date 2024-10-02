# Accessing class attributes directly is a bad practice
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


# Doing same with getters and setters
class Rectangle:
    def __init__(self, len, bre):
        self.__len = len         # __len is a private attribute
        self.__bre = bre

    def area(self):
        return self.__len * self.__bre
    
    def setlen(self, len):
        self.__len = len
        print(self.__len)

    def getlen(self):
        return self.__len


r1 = Rectangle(3,5)

print(r1.area())
r1.setlen(5)                 # through a setter I'm changing a private attribute
print(r1.getlen())           # through a getter I'm calling a private attribute
print(r1.area())



# Doing same with getters, setters and decorators
class Rectangle:
    def __init__(self, len, bre):
        self.__len = len         # __len is a private attribute
        self.__bre = bre

    def area(self):
        return self.__len * self.__bre

    @property
    def len(self):
        return self.__len
    
    @len.setter
    def len(self, len):
        if isinstance(len, int) and len > 0:
            self.__len = len
        else:
            raise ValueError('Incorrect value: ',len)
        print(self.__len)


r1 = Rectangle(3,5)

print(r1.len)    
r1.len = -5
r1.len = 0
r1.len = 5           
print(r1.len)           
print(r1.area())
