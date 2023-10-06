name = 'Jomsed\'s Khan' # escape 
name2 = "Jomsed khan"
# multiline string
name3 = """
    Jomsed nam
    modhu khan
"""

print(name)
print(name3)
# string is a sequence of characters
for char in name2:
    print(char, end=" ")

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

# mutable means changeable 
# immutable means you can not change it
# name2[0] = 'R'
print(name2)
if 'khan' in name2:
    print('exists')

print(name2.upper())