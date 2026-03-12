# main.py
from models import Animal, Dog, Cat

def main():
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    dog2 = Dog("Max", 5, "Bulldog")
    cat1 = Cat("Whiskers", 2, "Black")
    cat2 = Cat("Luna", 4, "White")

    animals = [dog1, dog2, cat1, cat2]

    for animal in animals:
        print(animal)
        print(animal.speak())
        if isinstance(animal, Dog):
            print(animal.fetch("ball"))
        elif isinstance(animal, Cat):
            print(animal.scratch())
        print("-" * 30)

if __name__ == "__main__":
    main()