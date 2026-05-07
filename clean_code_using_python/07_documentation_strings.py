# Document String or Docstring it mostly occurs as the first statement in a module, function, class, or method definition.

# Declare docstring by wrapping string with """ or ''' for example,

# def complex(real=0.0, imag=0.0):
#     """
#     Form a complex number.
    
#         Parameters:
#             real (float) -- the real part (default 0.0)
#             imag (float) -- the imaginary part (default 0.0)
#     """
#     if imag == 0.0 and real == 0.0:
#         return complex_zero
#     ...
# take a look at how it documents the complex(real, imag) function. 

# Notice the indentation of the doc body and the """

# After using docstring like this you can use __doc__ property to get the documentation,

# complex.__doc__
# Will output the following,

# Form a complex number.
    
#     Parameters:
#         real (float) -- the real part (default 0.0)
#         imag (float) -- the imaginary part (default 0.0)
# challenge icon
# Desafio

# Fácil
# Your are given function with block comment instead of docstring.

# Your task is to replace it with valid docstring, check the test case to achieve right formatting to the docstring!

def sum_binary(a, b):
    """
    Calculate sum of two integers in binary formatted string

        Parameters:
            a (int) -- Integer number
            b (int) -- Another integer number

        Returns:
            binary_sum (str) -- The sum of a and b in binary format
    """
    sum = a + b
    binary_sum = bin(sum)
    return str(binary_sum)[1:] # Final formmating

print(sum_binary.__doc__)