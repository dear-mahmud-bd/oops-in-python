# read only --> Values can be seen, accessed, but not changed
# getter -----> get a value of a property through a method. Most of the time, get the value of a private attribute.
# setter -----> set a value of a property through a method. Most of the time, set the value of a private property.


class User:
    def __init__(self, name, age, teka) -> None:
        self._name = name
        self._age = age
        self.__teka = teka    
    # "getter without any setter" is read only attribute
    @property
    def age(self):
        return self._age
    # getter 
    @property
    def salary(self):
        return self.__teka
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            print ('salary can not be negative')
        else:
            self.__teka += value


samsu = User('Kopa', 25, 139000)

# print(samsu.__teka) # its private variable...
# print(samsu.age()) # doesn't run cause it's act an attribute
print(samsu.age)
print(samsu.salary)
samsu.salary = 23000
print(samsu.salary)