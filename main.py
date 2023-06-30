#Hello Everyone
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.bank_accounts = []

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

    def add_bank_account(self, account):
        self.bank_accounts.append(account)
        print("New bank account created successfully. 😀")

    def switch_account(self, account_number):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                return account
        print("Invalid Account Number")
        return None



class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []
        self.interest_rate = 0.05 

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        self.transaction_history.append(
            {"type": "Deposit", "amount": self.amount, "timestamp": self.get_current_timestamp()}
        )
        print("Your account balance has been updated successfully : ₹", self.balance)

    def withdrawal(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds to withdraw | Balance Available: ₹", self.balance)
        else:
            self.balance -= self.amount
            self.transaction_history.append(
                {"type": "Withdrawal", "amount": self.amount, "timestamp": self.get_current_timestamp()}
            )
            print("Your account balance has been updated successfully : ₹", self.balance)

    def transfer_funds(self, recipient_account, amount):
        if amount > self.balance:
            print("Insufficient funds to transfer | Balance Available: ₹", self.balance)
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(
                {"type": "Transfer (To: {})".format(recipient_account.account_number), "amount": amount, "timestamp": self.get_current_timestamp()}
            )
            recipient_account.transaction_history.append(
                {"type": "Transfer (From: {})".format(self.account_number), "amount": amount, "timestamp": self.get_current_timestamp()}
            )
            print("Transfer successful.")
            print("Your account balance: ₹", self.balance)
            print("Recipient account balance: ₹", recipient_account.balance)

    def view_balance(self):
        print("Account number:", self.account_number)
        print("Account balance: ₹", self.balance)

    def view_transaction_history(self):
        print("Transaction History:")
        if len(self.transaction_history) == 0:
            print("No transactions found.")
        else:
            for transaction in self.transaction_history:
                print(
                    f"Type: {transaction['type']}, Amount: ₹{transaction['amount']}, Timestamp: {transaction['timestamp']}"
                )

    def get_current_timestamp(self):
        import datetime
        return datetime.datetime.now()

    def calculate_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        self.transaction_history.append(
            {"type": "Interest", "amount": interest_earned, "timestamp": self.get_current_timestamp()}
        )
        print("Interest has been calculated and added to the account balance at 5% interest rate : ₹", interest_earned)


# Get user input
print("Welcome to e-Banking service")
print("")
name = input("Please enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
print("")

# Create an instance of the User class with user input
user = User(name, age, gender)

# Perform user account operations
while True:
    print("1. Create Bank Account")
    print("2. Switch Bank Account")
    print("3. Access e-banking services")
    print("4. Check interest on current balance")
    print("5. Transfer Funds")
    print("6. Exit")
    print("")

    choice = input("Enter your choice (1-6): ")
    print("")

    if choice == '1':
        account_number = input("Enter the account number: ")
        bank_account = BankAccount(account_number)
        user.add_bank_account(bank_account)
    elif choice == '2':
        account_number = input("Enter the account number to switch: ")
        current_account = user.switch_account(account_number)
        if current_account:
            print("Switched to account number:", current_account.account_number)
    elif choice == '3':
        if len(user.bank_accounts) > 0:
            print("Select an account to access e-banking services:")
            for index, account in enumerate(user.bank_accounts):
                print(f"{index + 1}. Account number: {account.account_number}")
            account_index = int(input("Select your account using the account index: ")) - 1
            current_account = user.bank_accounts[account_index]
            while True:
                print("1. Deposit Funds")
                print("2. Withdraw Funds")
                print("3. View account Balance")
                print("4. View Transaction History")
                print("5. Go Back")
                print("")

                account_choice = input("Enter your choice (1-5): ")

                if account_choice == '1':
                    amount = float(input("Enter the deposit amount: "))
                    current_account.deposit(amount)
                elif account_choice == '2':
                    amount = float(input("Enter the withdrawal amount: "))
                    current_account.withdrawal(amount)
                elif account_choice == '3':
                    current_account.view_balance()
                elif account_choice == '4':
                    current_account.view_transaction_history()
                elif account_choice == '5':
                    print("Going back to account selection.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("No bank accounts found. Please create a bank account first.")
    elif choice == '4':
        if len(user.bank_accounts) > 0:
            print("Select an account to calculate interest:")
            for index, account in enumerate(user.bank_accounts):
                print(f"{index + 1}. Account number: {account.account_number}")
            account_index = int(input("Select your account using the account index: ")) - 1
            current_account = user.bank_accounts[account_index]
            current_account.calculate_interest()
        else:
            print("No bank accounts found. Please create a bank account first.")
    elif choice == '5':
        if len(user.bank_accounts) >= 2:
            print("Select the sender account:")
            for index, account in enumerate(user.bank_accounts):
                print(f"{index + 1}. Account number: {account.account_number}")
            source_index = int(input("Enter the source account index: ")) - 1

            print("Select the recipient account:")
            for index, account in enumerate(user.bank_accounts):
                if index != source_index:
                    print(f"{index + 1}. Account number: {account.account_number}")
            recipient_index = int(input("Enter the recipient account index: ")) - 1

            source_account = user.bank_accounts[source_index]
            recipient_account = user.bank_accounts[recipient_index]

            amount = float(input("Enter the transfer amount: "))
            source_account.transfer_funds(recipient_account, amount)
        else:
            print("Insufficient number of bank accounts. Please create at least 2 bank accounts to avail the service.")
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
print("Thanks for using our services, Please Visit Again!! 💐")

    
        

