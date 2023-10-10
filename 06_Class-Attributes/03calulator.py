class Calculator:
    brand = 'Casio fx-991 ES Plus'
    def add(self, n1, n2):
        return n1+n2
    def sub(self, n1, n2):
        return n1-n2
    def mul(self, n1, n2):
        return n1*n2
    def div(self, n1, n2):
        return n1/n2
calculate = Calculator() 
print(calculate.add(4,6))
print(calculate.sub(39,32))
print(calculate.mul(12,88))
print(calculate.div(1288,82))