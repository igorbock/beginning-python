# PEP 8 rules related to blank lines:

# Surround top-level function and class definitions with two blank lines
# import some_module


# class ClassA:
#     pass


# class ClassB:
#     pass
# or

# def top_function1():
#     pass


# def top_function2():
#     pass
# Method definitions inside a class are surrounded by a single blank line.
# class MyClass:
#     def __init__(self):
#         pass

#     def func1(self):
#         pass

#     def func2(self):
#         pass
# Extra blank lines may be used (sparingly) to separate groups of related functions.
# Use blank lines in functions, sparingly, to indicate logical sections.

# You are given a code edit the blank lines to apply PEP 8 rules

# Make sure to add clean new lines - without trailing spaces/tabs.
# Do not change the code you are given apart from blank lines

import math

class Operator:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		
	def eval(self):
		pass
	

class Plus(Operator):
	def __init__(self, num1, num2):
		super().__init__(num1, num2)
		
	def eval(self):
		return self.num1 + self.num2
	
	
if __name__ == "__main__":
	num1 = int(input())
	num2 = int(input())
	op = Plus(num1, num2)
	print(op.eval())