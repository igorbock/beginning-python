# Add to the existing password, two random uppercase letters.

# The ASCII values for uppercase letters are 65 to 90.

# Examples of possible outputs:

# abCD
# neHU
# okUH
# brEE
# ijYT

import random

num1 = random.randint(97, 122)
num2 = random.randint(97, 122)
num3 = random.randint(65, 90)
num4 = random.randint(65, 90)

print(f"{chr(num1)}{chr(num2)}{chr(num3)}{chr(num4)}")