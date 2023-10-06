def multiple():
    return 3, 4
print(multiple())

things = 'pen', 'pencil', 'water bottle', 'charger', 'phone', 'mirror', 'sunglass'
print(type(things))
print(things[0])
print(things[-2])
print(things[3:6])
if 'phone' in things:
    print('exists')
for item in things:
    print(item)

# tuples are immutable, which means their elements cannot be changed, added, or removed after the tuple is created.
# things[0]='wagon'
# print(things)
items = ('book', 'monitor', 'note')

# ignore
print(len(things))
tpl = ([2,3,4], [6,9,5])
# print(type(mega))
print(tpl[0])
tpl[0][1]=7
print(tpl)