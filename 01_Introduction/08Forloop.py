numbers = [5, 10, 15, 20, 25]
su = 0
for num in numbers:
    print(num)
    su += num
print(su)

texts = ' All time -> GEAR ON '
for char in texts:
    print(char)

for i in range(1,5):  # 1, 2, 3, 4, 5
    print(i)
for i in range(1,5,2):  # 1,3, 5
    print(i)

test_list = [1, 4, 5, 6, 7]
print("List index-value are : ")
for i in range(len(test_list)):
    print(i, end=" ")
    print(test_list[i])
