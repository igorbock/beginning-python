# PEP 8 states some rules realted to "Code Lay-out":

# Indent using 4 space or tab
# lines should not be longer then 79 characters
# # line with 137 characters
# def some_very_long_function_name(very_important_argument1, very_important_argument2, very_important_argument3, very_important_argument4):
#     pass 
# # Fix suggestion
# def some_very_long_function_name(
#     very_important_argument1,
#     very_important_argument2,
#     very_important_argument3,
#     very_important_argument4):
#     pass
# # Much better!
# Tab after new line as in the above example is good practice

# avoid multiple statements on the same line
# do_calc1(); do_calc2(); x = 3;  # bad
# # good
# do_calc1()
# do_calc2()
# x = 3
# imports should be on separate lines
# import sys, numpy  # bad
# # good
# import sys
# import numpy

# You are given code fix the PEP 8 guidelines violations!

import my_module
import other_module

some_very_important_argument = 0
another_very_important_argument = 3
very_big_and_important_argument = "Hello?"

my_module.calc_something_big_and_important(
    some_very_important_argument, 
    another_very_important_argument, 
    very_big_and_important_argument)

