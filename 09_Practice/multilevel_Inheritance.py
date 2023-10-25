class Animal:
    def __init__(self, name):
        self.name = name  
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Shepherd(Dog):
    def swim(self):
        print(f"{self.name} is swimming.")

shepherd = Shepherd("Militaru Ku**a")
shepherd.eat()  
shepherd.bark()  
shepherd.swim()  