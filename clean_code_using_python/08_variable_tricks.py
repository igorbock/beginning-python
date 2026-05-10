# Python offers various option for dealing with variables one of the strongest one is variable unpacking .

# When it comes to swapping between values, You can do it in this way,

# temp = a
# a = b
# b = temp
# Now the values of a and b have been swapped.

# In a pythonic way using variable unpacking you can do it easily,

# a, b = b, a
# Or to unpack tuples,

# x, y = (10, 20)  # x = 10, y = 20
# Using * we can deal with multiple values at ones!

# a, *b, c = [1, 2, 3, 4]  # a = 1, b = [2, 3], c = 4
# In case there is no enough variables to unpack to python will throw error!

# a, b = [1, 2, 3]  # Error
# a, *b = [1, 2, 3]  # a = 1, b = [2, 3]
# challenge icon
# Desafio

# Fácil
# You are given part of code which should take from the user array as input in arr and print the 
# head and tail of arr.

# You should initialise head and tail with the corresponding values, use variable unpacking only!

# Do not remove the given code!

# For example for input [1, 2, 3] - head = 1 and tail = [2, 3]


arr = eval(input())
# Do not change above

head, *tail = arr

# Do not change below
print(head, tail)