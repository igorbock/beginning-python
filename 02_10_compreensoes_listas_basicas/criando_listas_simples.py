# Crie uma função chamada get_word_lengths que recebe uma lista de palavras como 
# argumento e retorna uma lista dos comprimentos de cada palavra usando uma compreensão de lista.

def get_word_lengths(words):
    # Write code here
    list_return = []
    for item in words:
        num_chars = [c for c in item]
        list_return.append(len(num_chars))
    return list_return

print(get_word_lengths(["python", "list", "comprehension", "challenge"]))
print(get_word_lengths(["apple", "banana", "cherry", "date"]))