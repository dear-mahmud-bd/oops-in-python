from Bank import Bank
from Person import User, Admin

class Main:
    def __init__(self):
        self.bank = Bank("Bank_Of_Anonna")
        print(f"\n-----------------Welcome to '{self.bank.name}'-----------------\n")
        self.logged_in_user = None

    def create_admin_account(self):
        print(f"\n           Register as a ADMIN")
        print(f"           -------------------")
        name = input("Enter admin name: ")
        email = input("Enter admin email: ")
        nid = input("Enter admin NID: ")
        admin = Admin(name, email, nid)
        self.bank.admins.append(admin)
        return admin
    
    def login_admin_account(self):
        nid = input("Enter NID: ")
        admin = next((a for a in self.bank.admins if a.nid == nid), None)
        if admin:
            self.logged_in_user = admin
            return True
        else:
            print("Admin not found.")
            return False

    def create_user_account(self):
        print(f"\n           Register as a USER")
        print(f"           ------------------")
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        nid = input("Enter user NID: ")
        user = User(name, email, nid)
        self.bank.create_account(user)
        return user
    
    def login_user_account(self):
        nid = input("Enter NID: ")
        user = next((u for u in self.bank.users if u.nid == nid), None)
        if user:
            self.logged_in_user = user
            return True
        else:
            print("User not found.")
            return False

    def admin_operations(self):
        while True:
            print(f"\n---------- {self.logged_in_user.name} ----------")
            print(f"\n---------- Select an option ----------\n")
            print(f"           1. View User Information")
            print(f"           2. View Admin Information")
            print(f"           3. View Total Bank Balance")
            print(f"           4. View Total Loan Amount")
            print(f"           5. Toggle Loan Feature")
            print(f"           6. See Loan Feature Status")
            print(f"           7. Logout\n")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.bank.user_info()
            elif choice == '2':
                self.bank.admin_info()
            elif choice == '3':
                self.bank.display_total_balance()
            elif choice == '4':
                self.bank.display_total_loan()
            elif choice == '5':
                status = input("Enter 'on' to enable or 'off' to disable loan feature: ").lower()
                if status == 'on':
                    self.bank.toggle_loan_feature(True)
                elif status == 'off':
                    self.bank.toggle_loan_feature(False)
                else:
                    print("Invalid choice. Please enter 'on' or 'off'.")
            elif choice == '6':
                status = "enabled" if self.bank.loan_feature else "disabled"
                print(f"\n-------------Loan feature is currently {status}-------------\n")
            elif choice == '7':
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def user_operations(self):
        while True:
            print(f"\n---------- {self.logged_in_user.name} ----------")
            print(f"\n---------- Select an option ----------\n")
            print(f"           1. Deposit Money")
            print(f"           2. Withdraw Money")
            print(f"           3. Request Loan")
            print(f"           4. My Total Bank Balance")
            print(f"           5. View Transaction History")
            print(f"           6. Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                self.logged_in_user.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                self.logged_in_user.withdraw(amount)
            elif choice == '3':
                if self.bank.loan_feature:
                    amount = float(input("Enter loan amount: "))
                    self.logged_in_user.request_loan(self.bank.total_bank_balance(), self.logged_in_user.balance, amount)
                else:
                    print("Loan feature is off.")
            elif choice == '4':
                self.logged_in_user.user_balance()
            elif choice == '5':
                self.logged_in_user.transaction_history()
            elif choice == '6':
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please select a valid option.")
                
    def display_menu(self):
        print(f"---------- HOME PAGE {self.bank.name} ----------")
        print(f"           1. Create Admin account")
        print(f"           2. Admin Login")
        print(f"           3. Create User account")
        print(f"           4. User Login")
        print(f"           5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")
            if choice == '1':
                admin = self.create_admin_account()
                print(f"           ADMIN account created named '{admin.name}'\n")
            elif choice == '2':
                if self.login_admin_account():
                    self.admin_operations()
            elif choice == '3':
                user = self.create_user_account()
                print(f"           USER account created named '{user.name}'\n")
            elif choice == '4':
                if self.login_user_account():
                    self.user_operations()
            elif choice == '5':
                print(f"\n------------------------ Thanks for all your activities, wish you all the best (^_^) ------------------------\n")
                break
            else:
                print(f"\n------------------------ Invalid choice. Please select a valid option. ------------------------\n")


if __name__ == "__main__":
    main = Main()
    main.run()