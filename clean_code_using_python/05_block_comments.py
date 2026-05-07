# “If the implementation is hard to explain, it’s a bad idea.”

# - The Zen of Python

# Comments are important so that anyone who will read your code can understand it.

# Comments in Python seperate into 3 kinds:

# Block Comments
# Inline Comments
# Documentation Strings
# Let's start from the Block Comments -

# Starts from the same indent block as the code they describe.
# Start each line with a # followed by a single space.
# For example,

# while i < 10:
#     # Loop over i until i < 10
#     # print i with new line and increment it by 1
#     print(i, '\n')
#     i += 1
# challenge icon
# Desafio

# Fácil
# You are given greet function write block comment to describe what this function do - in your words.

# Follow the rules!

def greet(name):
    # This function takes a name as an argument and prints a greeting message to the console.
	print('Hello', name)