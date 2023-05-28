def sum(num1, num2, num3=0, num4=0):
    result = num1+num2+num3+num4
    return result
total = sum(99, 11, 11)
print('Total', total)


# *args
def all_sum(num1,num2,*numbers):
    print(numbers)
    for num in numbers:
        print(num)

mot = all_sum(12,23,36,54,55,17,18)
print('MOT-> ',mot)