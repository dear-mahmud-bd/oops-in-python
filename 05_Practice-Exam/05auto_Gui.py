import pyautogui
from time import sleep
n = int(input("Enter the number of rows: "))
sleep(5)
for i in range(1, n+1):
    pyautogui.typewrite("#" * i, interval=0.25)
    pyautogui.press("enter")
