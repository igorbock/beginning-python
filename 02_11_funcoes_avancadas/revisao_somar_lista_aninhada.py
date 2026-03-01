# Escreva uma função recursiva chamada sum_nested que recebe uma lista aninhada nested_list como argumento. 
# A função deve:
# Adicionar todos os inteiros na lista, incluindo inteiros em quaisquer sublistas.
# Retornar a soma total como um inteiro.

# Você pode verificar se um elemento é uma lista usando isinstance(element, list)
# Exemplo de Entrada:
# nested_list = [1, [2, 3], [4, [5, 6]], 7]

# Exemplo de Saída:
# 28

def sum_nested(nested_list):
    soma = 0
    for i in nested_list:
        if isinstance(i, list):
            n = sum_nested(i)
            soma += n
        else:
            soma += i
    return soma

print(sum_nested([1, [2, 3], [4, [5, 6]], 7]))
print(sum_nested([10, 20, 30, 40]))
print(sum_nested([[[[1]], 2], [3, [4, [5]]]]))
print(sum_nested([]))
print(sum_nested([1, [], [2, []], [3, [4, []]]]))
print(sum_nested([[1], [2, [3, [4]]]]))