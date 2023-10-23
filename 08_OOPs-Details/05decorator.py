from math import factorial
import time
def timer(func):
    def inner(*args, **kwargs):
        print('---Time Started')
        start = time.time()
        # print(func)
        func(*args, **kwargs)
        print('---Time Ended')
        end = time.time()
        print(f'Total time taken: {end-start} second')
    return inner

# timer()()

# decorator (autometic function call...)
@timer
def get_factorial(n):
    print('   Factorial starting')
    result = factorial(n)
    print(f'   Factorial of {n} is: {result}')

get_factorial(454)

# adulterated way to decorate
# timer(get_factorial)()