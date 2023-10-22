class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        pass

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'learning Python and practicing OOPs'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    
    def run(self):
        return f'phone tipa tipi kore'
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'

class SmartWatch:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f'Apna time ayega'

    def change_lens(self):
        pass