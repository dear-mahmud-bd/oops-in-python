class MathOperations:
    def add(self, a, b):
        return self._calculate(a,b, lambda x,y : x+y)

    def subtract(self, a, b):
        return self._calculate(a,b, lambda x,y : x-y)

    def _calculate(self, a, b, operation):
        return operation(a, b)

calculator = MathOperations()
result1 = calculator.add(5, 3)
print(result1)
result2 = calculator.subtract(10, 4)
print(result2)