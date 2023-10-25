class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    def __gt__(self, other):
        return self.age > other.age

shakib = Cricketer('Sakib', 37, 178, 91)
musfiq = Cricketer('Rahim', 36, 160, 88)
musta = Cricketer('Musta', 26, 175, 94)
tamim = Cricketer('Tamim', 35, 170, 91)
taijul = Cricketer('Taijul', 34, 173, 95)

oldest_cricketer = max([shakib, musfiq, musta, tamim, taijul])

# print(oldest_cricketer.name)





class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this")
class Dog(Animal):
    def sound(self):
        print("Woof!")
class Cat(Animal):
    def sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
make_animal_sound(dog) 
make_animal_sound(cat)

class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def eat(self):
        print("Dog is eating kibble.")

class Cat(Animal):
    def eat(self):
        print("Cat is eating fish.")

dog = Dog()
dog.eat()  
cat = Cat()
cat.eat()  