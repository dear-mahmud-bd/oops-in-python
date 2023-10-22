# abstract base class = abc
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod # enforce all child class to have a eat method
    def eat(self):
        print('I\'m eating food')
    
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('Hey na nana, I\'m eating banana')
    def move(self):
        print('Hanging on the branches')

layka = Monkey('lucky')
layka.eat()



# class Book: 
#     def __init__(self, name) -> None:
#         self.name = name
#     def read(self):
#         raise NotImplementedError

# class Physics(Book):
#     def __init__(self, name, lab) -> None:
#         self.lab = lab
#         super().__init__(name) 
#     def read(self):
#         print('reading physics vector chapter')

# topon = Physics('topon', True)
# print(issubclass(Physics, Book))
# print(isinstance(topon, Physics))
# print(isinstance(topon, Book))
# topon.read()