class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def __init__(self):  # THis will override the parent class constructor.
        # invoke constructor of the superclass / parent class.
        super().__init__()
        print("Mammal Constructor")
        self.weight = 3

    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("Swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)
print(m.weight)

f = Fish()
f.eat()
f.swim()
print(m.age)
print(isinstance(f, Mammal))  # False
print(isinstance(f, Fish))  # True
print(isinstance(f, Animal))  # True
print(isinstance(f, object))  # True

issubclass(Mammal, Animal)  # True
issubclass(Mammal, object)  # True
