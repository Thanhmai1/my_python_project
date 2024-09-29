from Animals import Animal 


class Dog(Animal) :
    def __init__(self, name, sound):
        super().__init__(name, sound)
        """
        Dog(Dog,woof) ==> dog = Aniamal((Dog,woof)) dog.sp
        """        

dog = Dog("Dog", "Woof")
print(type(dog))
print(dog.speak())