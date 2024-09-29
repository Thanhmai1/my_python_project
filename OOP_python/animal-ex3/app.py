from animal import Cat, Dog, Person
from database import save_to_db
def create_animal():
    animals = []
    while True:
        animal_type = input("Enter animal type (cat, dog, person or 'exit' to exit):").lower()
        if animal_type == 'exit':
            break
        name = input("Enter the name: ")
        if animal_type == "cat":
            animal = Cat(name)
        elif animal_type == "dog":
            animal = Dog(name)
        elif animal_type == "person":
            animal = Person(name)
        else:
            print("Invalid animal type. Please try again.")
            continue
        animals.append(animal)
        print(f"Added {animal_type.capitalize()} named {name}")
    return animals


def display_animals(animals):
    for animal in animals:
        print(animal.speak())
if __name__ == "__main__":
    animals_list = create_animal()
    save_to_db(animals_list)
    display_animals(animals_list)
