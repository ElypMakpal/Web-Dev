from models import Animal, Dog, Cat

a = Animal("Animal", 5, "Gray")
d = Dog("Buddy", 3, "Brown")
c = Cat("Kitty", 2, "White")

animals = [a, d, c]

for x in animals:
    print(x)
    print(x.speak())

print(d.fetch())
print(c.sleep())