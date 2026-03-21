from bank_account import BankAccount

# Test case handler
test_case = input()

if test_case == "account_creation":
    # Test account creation
    account = BankAccount("Alice", 1000)
    print(f"Owner: {account.owner_name}")
    print(f"Initial balance: ${account.balance}")
    print(f"Interest rate: {BankAccount.interest_rate * 100}%")

elif test_case == "deposit_method":
    # Test deposit functionality
    account = BankAccount("Bob", 500)
    print(f"Initial balance: ${account.balance}")
    
    # Valid deposit
    result = account.deposit(300)
    print(f"Deposit result: {result}")
    print(f"New balance: ${account.balance}")
    
    # Invalid deposit
    result = account.deposit(-50)
    print(f"Negative deposit result: {result}")
    print(f"Balance after invalid deposit: ${account.balance}")

elif test_case == "withdraw_method":
    # Test withdraw functionality
    account = BankAccount("Charlie", 1000)
    
    # Valid withdrawal
    result = account.withdraw(400)
    print(f"Withdrawal result: {result}")
    print(f"Balance after withdrawal: ${account.balance}")
    
    # Invalid withdrawal (negative)
    result = account.withdraw(-50)
    print(f"Negative withdrawal result: {result}")
    
    # Invalid withdrawal (exceeds balance)
    result = account.withdraw(1000)
    print(f"Excessive withdrawal result: {result}")
    print(f"Final balance: ${account.balance}")

elif test_case == "property_access":
    # Test property access and protection
    account = BankAccount("Dave", 800)
    
    print(f"Owner via property: {account.owner_name}")
    print(f"Balance via property: ${account.balance}")
    
    # Try to set balance (should use the setter)
    account.balance = 1200
    print(f"Balance after valid setter: ${account.balance}")
    
    # Try invalid balance
    account.balance = -500
    print(f"Balance after invalid setter: ${account.balance}")
    
    # Try to access private attributes directly (should fail)
    try:
        print(account.__owner_name)
    except AttributeError:
        print("Cannot access private owner_name directly")

elif test_case == "apply_interest":
    # Test interest application
    account = BankAccount("Eve", 2000)
    
    # Check original balance
    print(f"Initial balance: ${account.balance}")
    
    # Apply interest
    interest_earned = account.apply_interest()
    expected_interest = 2000 * 0.02
    
    print(f"Interest earned: ${interest_earned}")
    print(f"New balance after interest: ${account.balance}")
    print(f"Interest calculation correct: {interest_earned == expected_interest}")

elif test_case == "display_info":
    # Test display_info method format
    account = BankAccount("Frank", 1500)
    
    # Modify interest rate to test class variable
    original_rate = BankAccount.interest_rate
    BankAccount.interest_rate = 0.03
    
    print("Display info output:")
    account.display_info()
    
    # Restore original rate
    BankAccount.interest_rate = original_rate

elif test_case == "original_test_case":
    # Run the original test code from the challenge
    account = BankAccount("Coddy", 1000)

    # Perform operations
    account.deposit(500)
    account.withdraw(200)
    account.apply_interest()

    # Display account information
    account.display_info()

    # Test setter validation
    account.balance = 5000
    print(f"Balance after setter: ${account.balance}")

    # Test withdrawal validation
    account.withdraw(10000)
    print(f"Final balance: ${account.balance}")