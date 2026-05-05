# Congrats! Your script generated a random strong password!

# To make it fun, let's shuffle the characters in the password to make it even more random.

import random

num1 = random.randint(97, 122)
num2 = random.randint(97, 122)
num3 = random.randint(65, 90)
num4 = random.randint(65, 90)
num5 = random.randint(48, 57)
num6 = random.randint(48, 57)
num7 = random.randint(33, 47)
num8 = random.randint(33, 47)

password = [chr(num1), chr(num2), chr(num3), chr(num4), chr(num5), chr(num6), chr(num7), chr(num8)]
random.shuffle(password)
print("".join(password))