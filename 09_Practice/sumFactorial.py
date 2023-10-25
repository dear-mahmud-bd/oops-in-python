from math import factorial

class Numbers:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

    def factorial(self):
        return factorial(self.b)

obj = Numbers(3, 4, 5)

result_sum = obj.sum()
print("a+b+c =", result_sum)

result_factorial = obj.factorial()
print("Factorial of b:", result_factorial)