class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Brand: {self.name}, Price: {self.price}'
    
    def move(self):
        pass


class Truck(Vehicle):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
class PickUpTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)


class Bus(Vehicle):
    def __init__(self, name, price, seat):
        super().__init__(name, price)
        self.seat = seat

    def __repr__(self) -> str:
        vehi = super().__repr__()
        return vehi+f", Seat: {self.seat}"


class AC_Bus(Bus):
    all_ac_buses = []

    def __init__(self, name, price, seat, temperature):
        super().__init__(name, price, seat)
        self.temperature = temperature
        AC_Bus.all_ac_buses.append(self)

    def __repr__(self):
        bus = super().__repr__()
        return bus+f", Temperature :{self.temperature}°C."

# Create AC_Bus objects
green_line = AC_Bus('GREENLINE', 7500000, 42, 25)
# print(green_line)
blue_line = AC_Bus('BLUELINE', 8000000, 45, 20)
# print(blue_line)

# Print all AC_Bus objects
for ac_bus in AC_Bus.all_ac_buses:
    print(ac_bus)