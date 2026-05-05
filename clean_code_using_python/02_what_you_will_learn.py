# What will you learn?


# In this course you will learn the concepts of Clean Code when coding with Python .

# Main topics are :

# Styles conventions
# Pythonic code
# PEP 8
# As always the key to success is practice so we will practice a lot.

# Let's start from a simple challenge!

# challenge icon
# Desafio

# Fácil
# You are given a code for function init which gets name and age.

# The function prints some greet and then calculates some kind of id and returns it.

# As we will learn this function uses some bad practices but for now your task is to seperate the concerns .

# Create two helper functions to take care of the greet and the id calculations separately.

# In the end it will look something like this,

# def init(name, age):
# 	greet(name, age)
# 	res = calc_id(name, age)
# 	return res
# ord function converts char to his ASCII representation (int)

def init(name, age):
    greet(name, age)
    res = calc_id(name, age)
    return res

def greet(name, age):
    print('Hello,', name)
    if age >= 18:
        print('Above 18')
    else:
        print('Below 18')

def calc_id(name, age):
    res = 0
    for c in name:
        res += ord(c) * age
    return res

name = input()
age = int(input())
print(init(name, age))