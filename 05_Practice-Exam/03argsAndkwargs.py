# args
def add_nums(*args):
    result = 0
    for num in args:
        result += num
    return result
sum1 = add_nums(1, 2, 3, 4)
sum2 = add_nums(10, 20, 30, 40, 50)
print(sum1)
print(sum2)

# kwargs
def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_person_info(name="John", age=30, city="New York")


"""
import pyautogui
from time import sleep
n = int(input("Enter the number of experiments: "))
sleep(3)
for i in range(1, n + 1):
    experiment_name = f"Experiment No - {i}"
    pyautogui.typewrite(experiment_name, interval=.10)
    pyautogui.press("enter")

"""