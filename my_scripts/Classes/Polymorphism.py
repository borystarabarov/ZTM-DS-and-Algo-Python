def driver(c): # function that calls method drive of a class
    c.drive()


class Mercedes:
    def __init__(self):
        pass

    def drive(self):
        print('Mercedes is driving')

class Lexus:
    def __init__(self):
        pass

    def drive(self):
        print('Lexus is driving')


m1 = Mercedes()
l1 = Lexus()

driver(m1)
driver(l1)

# calling of the same function is causing different actions depending on the class realization


# Method Overloading

class Math:

    def sum(self,a,b):
        return a + b
    
a = Math()
print(a.sum(5, 4))
print(a.sum(5.98, 0.00000000112))
print(a.sum('Hello ', 'World!!!'))

# Or

class Math():

    def sum(self, a, b, c=None ):
        
        s = a + b
        if c == None:
            return s
        else:
            return s + c
        
n = Math()

print(n.sum(1,2))
print(n.sum(1,2,100))


# Method Overriding

class Animal:

    def speak(self):
        return 'Animal can speak' 

class Dog(Animal):

        def speak(self):
            return super().speak() + ' and Bark' 

class Cat(Animal):

        def speak(self):
            return 'Meow'
        
a = Animal()
d = Dog()
c = Cat()

print(a.speak()) # Animal can speak
print(d.speak()) # Animal can speak and Bark
print(c.speak()) # Meow