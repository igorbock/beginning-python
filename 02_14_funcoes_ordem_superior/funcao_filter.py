# Crie uma função chamada get_long_strings que recebe uma lista de strings strings como argumento. 
# A função deve usar a função filter() junto com uma função lambda para selecionar strings que tenham um comprimento 
# maior que 5. A função deve retornar uma lista contendo as strings selecionadas.

def get_long_strings(strings):
    # Use filter() with a lambda function to select strings with length greater than 5
    long_strings = filter(lambda x: len(x) > 5, strings)
    
    # Return the list of selected strings
    return list(long_strings)

print(get_long_strings(['apple', 'banana', 'cherry', 'dragonfruit']))
print(get_long_strings(['cat', 'dog', 'fish', 'bird']))
print(get_long_strings(['elephant', 'giraffe', 'penguin']))
print(get_long_strings(['hi!', 'hello!', 'hey there!', 'hi world', 'greetings!']))