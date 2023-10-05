def full_name(first, last):
    name = f'Full name is: {first} {last}'
    return name
# take paremeter in order
nam = full_name('Kuddus','Boyati')
print(nam)
name = full_name(last='Boyati', first='Kuddus')
print(name)

# another way---
def famous_name(first, last, title, additional):
    name = f'{title} {first} {last}'
    return name
fName = famous_name(first='Kuddus', last='Chomo', title='Boyati', additional='Fock-Music')
print(fName)

# another way--(**kargs => key arguments)
def fam_name(first, last, **additional):
    name = f'{first} {last}'
    print(additional)
    print(additional['title'])
    for key, value in additional.items():
        print(key, value)
    return name
fNam = fam_name(first='Kuddus', last='Chomo', title='Boyati', additional='Fock-Music')
print(fNam)

# The way to declear function...
# def function_name(num1, num2, *args, **kargs):

# return multiple things from an array
def lotOfThings(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    # return [sum, mult, remain]
    return sum, mult, remain
everything = lotOfThings(55, 21)
print(everything)