# function is a first class object
def double_decker():
    print('starting the double decker function')
    def inner_fun():
        print('inside the inner function')
        return 82000
    return inner_fun

# print(double_decker())
# print(double_decker()())

def do_something(work):
    print('work started')
    # print(work)
    work() # cause passed function 
    print('work ended')

# do_something(2)
# do_something('ami busy')

def coding():
    print('coding in Python')
do_something(coding)

def learning():
    print('Learning and dreaming in Python')
do_something(learning)