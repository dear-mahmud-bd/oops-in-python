class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.admins = []
        self.initial_amount = 0
        self.loan_amount = 0
        self.loan_feature = True

    def create_account(self, user):
        if any(existing_user.nid == user.nid for existing_user in self.users + self.admins):
            print("An account with the same NID already exists.")
            return
        self.users.append(user)
        print(f"\n----------Account for {user.name} created at '{self.name}'----------\n")

    def user_info(self):
        print(f"\n            User Information for '{self.name}':")
        print(f"            ------------------------------------")
        for user in self.users:
            print(f"         Name: {user.name}, Email: {user.email}, NID: {user.nid}")

    def admin_info(self):
        print(f"            Admin Information for '{self.name}':")
        print(f"            ------------------------------------")
        for admin in self.admins:
            print(f"         Name: {admin.name}, Email: {admin.email}, NID: {admin.nid}")

    def display_total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        total_loan = sum(user.loan for user in self.users)
        print(f"\n--------Total balance in '{self.name}': ${(total_balance-total_loan):.2f}--------\n")

    def total_bank_balance(self):
        total_balance = sum(user.balance for user in self.users)
        total_loan = sum(user.loan for user in self.users)
        return total_balance-total_loan

    def display_total_loan(self):
        total_loan = sum(user.loan for user in self.users)
        print(f"\n--------Total loan amount in {self.name}: ${total_loan:.2f}--------\n")

    def toggle_loan_feature(self, status):
        self.loan_feature = status
        status_str = "enabled" if status else "disabled"
        print(f"\n--------Loan feature in {self.name} is {status_str}--------\n")
