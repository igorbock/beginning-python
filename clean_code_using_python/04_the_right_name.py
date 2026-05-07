# When choosing names you should always choose descriptive names that will make your code much more readable.

# def foo(x):
#     return x * 2
# The following example is unclear and not so readable.

# The right way,

# def multiply_by_2(num):
#     return num * 2
# Now the code is clear even without reading it's body.

# If it's possible and not necessary you should avoid one letter names like a, x, i and etc...

# challenge icon
# Desafio

# Fácil
# When giving a right name to a function or class first you should understand what the purpose and what describes it best.

# You are given a code - fix the names in this code!

# First - understand what the purpose of each code chunk!

# There are of course many possible answers but we are aiming for specific ones..

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def update_info(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f'My name is {self.name} and I\'m {self.age} years old')

if __name__ == '__main__':
    person_name = 'Bob'
    person_age = 32
    person = Person(person_name, person_age)
    person.update_info(person_name, 33)
    person.print_info()