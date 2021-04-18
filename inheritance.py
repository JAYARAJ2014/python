class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("Swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)

f = Fish()
f.eat()
f.swim()
print(m.age)
