class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass



class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Wof"
class Person(Animal):
    def speak(self):
        return f"{self.name} says hello"
