
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return "Sound"

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.color


class Dog(Animal):
    def fetch(self):  
        return "Dog is running"

    def speak(self):
        return "Woof"


class Cat(Animal):
    def sleep(self):
        return "Cat is sleeping"

    def speak(self):
        return "Meow"