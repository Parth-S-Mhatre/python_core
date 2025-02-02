class BankAccount:
    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        print(f"Account created for {self.name} with Account No: {self.account_no}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def bank_fees(self):
        fees = self.balance * 0.05
        return fees

    def display(self):
        print("Account Details:")
        print(f"Account No: {self.account_no}")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Bank Fees (5%): ${self.bank_fees():.2f}")

    def __del__(self):
        print(f"Account for {self.name} with Account No: {self.account_no} is being closed.")

# Example usage
if __name__ == "__main__":
    # Create a bank account
    account = BankAccount("123456", "John Doe", 1000)

    # Deposit some money
    account.deposit(500)

    # Display account details
    account.display()

    # The destructor will be called when the object is deleted or goes out of scope
    del account  
    