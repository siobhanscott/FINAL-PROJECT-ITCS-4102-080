class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Withdrawal amount must be greater than zero and less than or equal to balance.")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

if __name__ == "__main__":
    owner_name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance (if any): $"))
    
    account = BankAccount(owner_name, initial_balance)
    
    while True:
        print("\n===== Bank Account Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            deposit_amount = float(input("Enter amount to deposit: $"))
            account.deposit(deposit_amount)
        elif choice == '2':
            withdraw_amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(withdraw_amount)
        elif choice == '3':
            print(account)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
