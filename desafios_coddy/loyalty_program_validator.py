# Create a program that validates customer information for your sandwich shop's loyalty program. 
# Read a username, an account balance, and the customer's position in the queue.

# Check if the username is valid (3-15 characters, letters/numbers/underscores only, can't start with a number), 
# verify the balance is a valid decimal number, and calculate the estimated wait time (5 minutes per customer 
# ahead in queue). Print "Valid" or "Invalid" for each check, followed by the wait time in minutes.

# Read the customer information
username = input()  # Read the username
balance = input()  # Read the account balance as string
queue_position = int(input())  # Read the queue position as integer

username_valid = False  # Replace with your validation logic

# Validate the username
username_valid = False

# Check if length is between 3-15 characters
tamanho = len(username)
if 3 <= tamanho <= 15 and username.replace('_', '').isalnum() and not username[0].isdigit():
    username_valid = True

# TODO: Validate the balance
# Check if the balance string represents a valid decimal number

balance_valid = False  # Replace with your validation logic

try:
    numero = float(balance)
    balance_valid = True
except ValueError:
    balance_valid = False

# TODO: Calculate estimated wait time
# Each customer ahead takes 5 minutes

wait_time = 0  # Replace with your calculation

wait_time = queue_position * 5

# Print the results
if username_valid:
    print("Valid")
else:
    print("Invalid")

if balance_valid:
    print("Valid")
else:
    print("Invalid")

print(wait_time)