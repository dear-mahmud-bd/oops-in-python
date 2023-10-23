# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod

class Shopping:
    cart = [] # class/static attribute
    origin = 'china'
    
    def __init__(self, name, location) -> None:
        self.name = name  # instance attribute
        self.location = location
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying: {item}, for price: {price} and remaining: {remaining}')

    @staticmethod # doesn't use instance attribute
    def multiply(a, b):
        result = a*b    
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        print(self.origin)
        print('hudai dekhi, kintu kinmu na, just AC er hawa khaite aschi, Aita ki', item)



dokan = Shopping('DeshiDokan', 'thikana')
dokan.purchase('lungi', 500, 1000)
dokan.hudai_dekhi('lungi-1')

""" Doesn't use @classmethod """
# Shopping.purchase(2, 3, 3)
Shopping.hudai_dekhi('Lungi-2')

# static method
Shopping.multiply(4,6) 
dokan.multiply(6,9)