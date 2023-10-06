# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate
numbers = [56 , 88, 78, 39 , 12 , 64, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(12)
numbers_set.add(12)
numbers_set.add(12)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)
# numbers_set[1] = 5
for item in numbers_set:
    print(item,end=" ")
print()
if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B) # A intersection B
print( A | B) # A union B