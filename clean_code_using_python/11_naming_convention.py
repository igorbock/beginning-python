# Naming convention


# PEP 8 follows the suggested Python naming convention as we saw before :

# Type	Convention	Example
# Variable	snake_case all lower case	generated_result
# Function	snake_case all lower case	print_info()
# Constant	snake_case all upper case	PI = 3.14
# Class	CamelCase	MyClass
# module	snake_case all lower case	numpy

# You are given with some PEP 8 naming conventions violations can you spot & fix them?

class Soul:
	FREE_STRING = 'Soul freed'  # const string
	def __init__(self, name):
		self.name = name
	
	def free(self):
		print(self.FREE_STRING + ' - ' + self.name)

if __name__ == '__main__':
	instance = Soul('John Doe')
	instance.free()