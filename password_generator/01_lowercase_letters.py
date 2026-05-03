# Generate two random lowercase letters, concatenate them together, and print the result on the screen!

# How do I generate a random character?
# Each character have a numeric representation called ASCII value, for lower case letters it's 
# the numbers from 97 to 122.

# To cast from a number to character use chr() function:

# print(chr(97))  # Prints 'a'
# Examples of possible outputs:

# ab
# ne
# ok
# br
# ij
# mm

import random

num1 = random.randint(97, 122)
num2 = random.randint(97, 122)

print(f"{chr(num1)}{chr(num2)}")