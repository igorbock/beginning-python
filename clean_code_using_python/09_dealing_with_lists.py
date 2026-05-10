# Lists are a big part of Python, so various list techniques make your code more Pythonic.

# You can initiate or create a list in a simple way using the * operator.

# arr = [1] * 3  # arr = [1, 1, 1]
# Using for loop you can filter or map and create list in a more pythonic way,

# numbers = [1, 2, -3, -2, 5]

# # filter numbers list to hold only positive numbers
# # filtered_list = [1, 2, 5]
# filtered_list = [num for num in numbers if num > 0]

# # map numbers to array of their power of 2
# # mapped_list = [1, 4, 9, 4, 25]
# mapped_list = [num * num for num in numbers]
# You can map and filter in same time!

# positive_and_power = [num * num for num in numbers if num > 0]
# When using () instead of [] python will create generator instead of list

# filtered_gen = (num for num in numbers if num > 0)
# print(next(filtered_gen))  # 1
# print(next(filtered_gen))  # 2
# print(next(filtered_gen))  # 5

import ast

def firsts(names):
	return [name.split()[0] for name in names if name.startswith("A")]

input_list = ast.literal_eval(input())
result = firsts(input_list)
print(result)