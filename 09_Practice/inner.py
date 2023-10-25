class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def _deduct(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def withdraw(self, amount):
        self._deduct(amount)

acc = BankAccount(1000)
acc.withdraw(5000)