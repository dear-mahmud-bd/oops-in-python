numbers = [12, 45, 98, 68]
numbers.append(39)
print(numbers)
numbers.insert(0, 4)
numbers.insert(2, 82)
print(numbers)
if 98 in numbers: 
    numbers.remove(98)
if 8 in numbers:
    numbers.remove(8)
print(numbers)
last = numbers.pop()
print(last, numbers)
index = numbers.index(45)
print(index)
if 5 in numbers:
    index = numbers.index(5)
    print(index)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)