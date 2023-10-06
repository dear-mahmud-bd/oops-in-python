# .csv comma separated value
# .txt text file

# with open('00message.txt', 'w') as file:
#     file.write('I Love You, Python ')

# with open('00message.txt', 'a') as file:
#     file.write('I Love You, Python ')

with open('00message.txt', 'r') as file:
    text = file.read()
    print(text)