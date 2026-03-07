# Crie uma função chamada convert_to_uppercase que recebe uma lista de strings strings como argumento.
# A função deve usar a função map() junto com uma função lambda para converter cada string na lista para maiúscula. 
# A função deve retornar uma lista contendo as strings em maiúscula.

def convert_to_uppercase(strings):
    # Use map() with a lambda function to convert strings to uppercase
    uppercase_strings = map(lambda x: x.upper(), strings)
    
    # Return the list of uppercase strings
    return list(uppercase_strings)

print(convert_to_uppercase(['hello', 'world', 'python']))
print(convert_to_uppercase(['Hello', 'World', 'PyThOn']))
print(convert_to_uppercase([]))
print(convert_to_uppercase(['hello world!', '@python', 'coding 123']))
print(convert_to_uppercase(['', 'test', '']))