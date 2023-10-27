class Restaurant:
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name
        self.orders = []
        self.chefs = []
        self.servers = []
        self.managers = []
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chefs.append(employee)
        elif employee_type == 'server':
            self.servers.append(employee)
        elif employee_type == 'manager':
            self.managers.append(employee)

    def add_order(self, order):
        self.orders.append(order)

    def receive_payment(self, order, amount, customer):
        # print(amount, order.bill)
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('-----------Not Enough money. Pay more (°_°) -----------')
        
    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')

    def pay_salary(self, employee):
        if employee.salary <= self.balance:
            print(f"Paying salary for '{employee.name}' salary: {employee.salary} TK")
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()
        else:
            print(f"Not enought money to pay 'salary: {employee.salary} TK'")

    def show_employees(self):
        print(f'-----------SHOWING EMPLOYEES--------')
        for manager in self.managers:
            print(f'Manager: {manager.name} with salary: {manager.salary}')
        for chef in self.chefs:
            print(f'Chef: {chef.name} with salary: {chef.salary}')
        for server in self.servers:
            print(f'Server: {server.name} with salary: {server.salary}')
        