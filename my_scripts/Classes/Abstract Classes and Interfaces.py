from abc import ABC, abstractmethod

class Animal(ABC):

    def speak(self):
        pass

    def eat(self):
        print('Eating!')


class Dog(Animal):

        def speak(self):
             print('Dog barks!')


# animal = Animal()  # This would raise an error
d = Dog()
d.eat()
d.speak()


