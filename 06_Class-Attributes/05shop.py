class Shop:
    cart = [] # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer

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