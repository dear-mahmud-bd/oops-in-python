class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mehzben = Shop('mehjaben')
mehzben.add_to_cart('phone')
mehzben.add_to_cart('shoes')
print(mehzben.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)

arekjon = Shop('akjon')
arekjon.add_to_cart('potato')
print(arekjon.cart)