# Bus Company
class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []
        
class Driver:
    def __init__(self, name, age, license) -> None:
        self.name = name
        self.age = age
        self.license = license

class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

red_mia = Driver("Dipjol's", 32, 'asd52ef9r')