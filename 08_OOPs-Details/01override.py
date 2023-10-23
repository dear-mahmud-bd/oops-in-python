class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Pustikor Khabar')

    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # override...
    def eat(self):
        print('Susomo Khabar')
    def exercise(self):
        print('GYM e poisa diya hudai gham jhorai')
    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    # len overload
    def __len__(self):
        return self.height
    # > operator overload
    def __gt__(self, other):
        return self.age > other.age


saikka_pal = Cricketer('sakib', 38, 168, 58, 'BD')
fizz = Cricketer('mustafiz', 24, 175, 69, 'BD')

saikka_pal.eat()
saikka_pal.exercise()
print(82 + 39)
print( 'Abba nehi manega, ' + 'Rakib' )
print([12, 98] + [5,6,7,1,2])
print(saikka_pal + fizz)
print(saikka_pal * fizz)
print(len(saikka_pal), 'cm')
print(saikka_pal > fizz)