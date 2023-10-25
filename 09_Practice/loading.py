class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def __lt__(self, other):
        return self.age < other.age
    
Sakib = Cricketer('Sakib', 38, 68, 91)
Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
Riyad = Cricketer('Riyad', 39, 72, 92)

cricketers = [Sakib, Mushfiq, Mustafiz, Riyad]
youngest_cricketer = cricketers[0]

for cricketer in cricketers:
    if cricketer < youngest_cricketer:
        youngest_cricketer = cricketer

print(f"The youngest cricketer is '{youngest_cricketer.name}'")