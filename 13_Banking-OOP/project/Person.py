class Person:
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid


class Admin(Person):
    def __init__(self, name, email, nid):
        super().__init__(name, email, nid)


class User(Person):
    def __init__(self, name, email, nid, initial_balance=0):
        super().__init__(name, email, nid)
        self.balance = initial_balance
        self.loan = 0
        self.transactions = []

    def user_balance(self):
        print(f"\n------------User: {self.name}, Bank-Balance: ${self.balance:.2f}, Bank-Loan: ${self.loan:.2f} ------------")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount:.2f}")
            print(f"\n---------Deposited ${amount:.2f} into your account.---------")
        else:
            print("\n         Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount:.2f}")
            print(f"\n---------Withdrew ${amount:.2f} from your account.---------")
        else:
            print("\n---------Insufficient balance or invalid withdrawal amount.---------")

    def request_loan(self, bank_balance, user_balance, loan_amount):
        if loan_amount<=(user_balance*2) and loan_amount<=bank_balance:
            self.loan += loan_amount
            self.balance += loan_amount
            self.transactions.append(f"Borrowed ${loan_amount:.2f}")
            print(f"Loan approved. Borrowed ${loan_amount:.2f}")
        else:
            if loan_amount > (user_balance*2):
                print("\n---------You can't borrow more than twice your balance.---------")
            else:
                print("\n---------Loan request denied.---------")

    def transaction_history(self):
        print(f"\n--------------Transaction history for '{self.name}':--------------")
        for transaction in self.transactions:
            print(f"              {transaction}")
