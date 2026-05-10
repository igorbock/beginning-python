# PEP 8 whitespace guidelines are the following :

# avoid extra space within braces or brackets
# items = [ 1 , 'abc'  ]  # bad
# items = [1, 'abc']      # good

# def func( parm ):  # bad
#     ...
# def func(parm):    # good
#     ...
# avoid trailing whitespace anywhere
# surrounded operators with one space in each side
# n =3+5     # bad
# n = 3 + 5  # good
# don't use spaces around the = sign when used to indicate a keyword argument
# def calc(num = 0.0):  # bad
#     ...
# def calc(num=0.0):    # good
#     ...
# challenge icon

# Fix the given code to apply all PEP 8 whitespace guidelines

def secret(n, k=0):
	z = n + k

	a = [1, 2, 3, 4]
	for i in a:
		z += i
	return z