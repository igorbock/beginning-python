# Add to the existing password, two random digits.

# The ASCII values for digits are 48 to 57.

# Examples of possible outputs:

# abCD13
# neHU44
# okUH54
# brEE58
# ijYT92

import random

num1 = random.randint(97, 122)
num2 = random.randint(97, 122)
num3 = random.randint(65, 90)
num4 = random.randint(65, 90)
num5 = random.randint(48, 57)
num6 = random.randint(48, 57)

print(f"{chr(num1)}{chr(num2)}{chr(num3)}{chr(num4)}{chr(num5)}{chr(num6)}")