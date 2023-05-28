money = input('My pocket money: ')
print('Here is your money ->',money)

hiraMoney = input('Hira dise: ')
sajMoney = input('Sajubul dise: ')
# By default the input from user will be string type
total = hiraMoney+sajMoney
print('Sob milaya Paysi->',total,'BDT')

hiraMoneyInt = int(hiraMoney)
sajMoneyInt = int(sajMoney)
totalInt = hiraMoneyInt+sajMoneyInt
print('Sob milaya Int Paysi->',totalInt,'BDT')

# Type casting---
num = 10
print("Type of variable before conversion : ", type(num))
converted_num = str(num)
print("Type After conversion : ",type(converted_num))