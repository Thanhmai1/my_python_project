from Animals import Animal

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
cat = Cat("Marry", "Meow Meow")
print(cat.speak())
print(type())