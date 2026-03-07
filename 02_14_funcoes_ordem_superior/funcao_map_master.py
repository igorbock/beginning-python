# Crie uma função chamada calculate_lengths que recebe uma lista de palavras words como argumento. 
# A função deve usar a função map() junto com uma função lambda para calcular o comprimento de cada palavra na lista. 
# A função deve retornar uma lista contendo os comprimentos das palavras.

def calculate_lengths(words):
    # Use map() with a lambda function to calculate the length of each word
    word_lengths = map(lambda x: len(x), words)
    
    # Return the list of word lengths
    return list(word_lengths)

print(calculate_lengths(["apple","banana","cherry","date","fig"]))
print(calculate_lengths(["elephant","lion","tiger","bear","zebra"]))
print(calculate_lengths(["hello","world","python","map","function"]))
print(calculate_lengths(["quick","brown","fox","jumps","over"]))
print(calculate_lengths(["summertime","winter","spring","fall","seasons"]))