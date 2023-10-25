class MyClass:
    cls_var = "Class Variable"

    def __init__(self, instnc_var):
        self.instance = instnc_var

    @classmethod
    def class_method(self):
        print("Class Method")
        print(f"Class Variable: {self.cls_var}")

    @staticmethod
    def static_method():
        print("Static Method")
    @staticmethod
    def utility_method(x, y):
        return x + y

    def instance_method(self):
        print("Instance Method")
        print(f"Instance Variable: {self.instance}")

# Creating an instance of the class
obj = MyClass("Instance Variable")

# Calling class methods and static methods
obj.class_method()
obj.static_method()

# Using a utility method (static method)
result = MyClass.utility_method(5, 7)
print("Result of Utility Method:", result)

# Calling an instance method
obj.instance_method()