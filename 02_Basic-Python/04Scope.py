# global 
balance = 5000
def buy_things(item, price):
    global balance
    # access global variable without using global keyword
    print("Global Value:", balance)
    # using global keyword, modify the global value
    balance  -= price
    print(f"Balance after buying {item}", balance)

buy_things("Sunglass", 1200)
print("After buy the global variable value:",balance)