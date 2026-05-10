# When accessing element in dictionary there is always the risk that the key does not exists.

# The Pythonic way to check if key exist in dictionary is the in keyword,

# if 'name' in person_dict:
#     print(person_dict['name'])
# if default value can be supplied it's good idea to use get(),

# print(person_dict.get('name', 'Anonymous'))
# The following will print 'Anonymous' if 'name' not exits in person_dict, otherwise the value of 'name'.

# challenge icon
# Desafio

# Fácil
# Create a function area(sizes).

# sizes is a dictionary with 2 keys - width and height if the keys not exists the default value should be 1.

# The expected output should be the area size - width * height.

def area(sizes):
    if not sizes:
        return 1

    width = sizes.get('width', 1)
    height = sizes.get('height', 1)
    return width * height

# Example usage:
input_dict = eval(input())
result = area(input_dict)
print(result)