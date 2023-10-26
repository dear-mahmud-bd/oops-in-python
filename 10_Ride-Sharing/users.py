from abc import ABC, abstractmethod
from datetime import datetime


class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def  add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return(f"Company name: '{self.company_name}' with {len(self.riders)} riders  and {len(self.drivers)} drivers")



class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.__nid = nid
        # TODO: set user id dynamically
        self.__id = 0
        self.wallet = 0

    @abstractmethod
    def displayProfile(self) -> None:
        raise NotImplementedError



class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def displayProfile(self) -> None:
        print(f"Rider,\n Name: {self.name}, Email: {self.email}")

    def load_cash(self, amount):
        if amount>0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location
           
    def req_ride(self, destination, rideSharing):
        if not self.current_ride:
            # TODO: set current ride via ride match...
            ride_req = Ride_Req(self, destination)
            ride_macher = Ride_Matching(rideSharing.drivers)
            # TODO: set ride properly...
            self.current_ride = ride_macher.find_driver(ride_req)
            
    def show_current_ride(self):
        print(f"Current ride: {self.current_ride}")



class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def displayProfile(self) -> None:
        print(f"Driver,\n Name: {self.name}, Email: {self.email}")
    
    def accept_ride(self, ride) -> None:
        ride.set_driver(self)



class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f"Ride details... Started: {self.start_location} to End: {self.end_location}"



class Ride_Req:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location



class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers
    
    def find_driver(self, ride_req):
        if len(self.available_drivers) > 0:
            # print('finding driver')
            # TODO: find  the closest driver of the rider...
            driver = self.available_drivers[0]
            ride = Ride(ride_req.rider.current_location, ride_req.end_location)
            driver.accept_ride(ride)
            return ride



class Vehicle(ABC):
    speed = {
        'car' : 50,
        'bike' : 60,
        'cng' : 40
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        raise NotImplementedError
    


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'
        print(f"Start Car driving")
    


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'
        print(f"Start Bike driving")




cholo_jai = Ride_Sharing("Cholo Jai")

topu = Rider('Ami TOPU', 'ami@topu.net', 1288, 'niribili', 4600)
cholo_jai.add_rider(topu)

driver_mama = Driver('Driver Mama', 'driver@mama.gari', 3932, 'nobinagar')
cholo_jai.add_driver(driver_mama)

print(cholo_jai)
topu.req_ride('manikganj', cholo_jai)
topu.show_current_ride()