# base / parent class, common attribute + functionality 
# derived / child class, uncommon attribute + functionality 

class Device:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Device name: {self.brand}'


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'learning python and practicing'
    

class Phone(Device):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        print( f'Sending SMS to: {number} with: {text}')
    
    def __repr__(self) -> str:
        return f'Brand: {self.brand}, Price: {self.price}, Support Dual SIM: {self.dual_sim}'


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass


# inheritance
my_phone = Phone('SAMSUNG', 190000, 'Gray', 'Singapore', True)
my_phone.phone_call(7155, 'I Love You')
print(my_phone.brand)
print(my_phone)