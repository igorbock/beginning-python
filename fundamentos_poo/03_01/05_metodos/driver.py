from bank_account import BankAccount

# Create an account and test your methods
my_account = BankAccount()
my_account.balance = 0  # Starting balance

# TODO: Make transactions
# (Your code here)
my_account.deposit(100)
my_account.withdraw(30)

# TODO: Print the final balance
# (Your code here)
print(f"Current balance: ${my_account.get_balance()}")