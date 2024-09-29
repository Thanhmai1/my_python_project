from Animals import Animal

class Person(Animal):
    def __init__(self, name, sound, age):
        super().__init__(name, sound)
        self._age = age
    def print_age(self):
        print(f"Age: {self._age}")
        
person = Person("Iner", "Hello", 11)
print(person.speak())
person.print_age()