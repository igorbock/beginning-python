# Escreva uma função sum_positive_evens que recebe uma lista de números como entrada. 
# Use uma compreensão de lista para filtrar números pares positivos, depois use sum() 
# para calcular o total deles. Retorne o resultado.

def sum_positive_evens(numbers):
    # Write code here
    soma = sum([x for x in numbers if x > 0 and x % 2 == 0])
    return soma

print(sum_positive_evens([-10, -5, 0, 2, 4, 7, 10, 12]))
print(sum_positive_evens([1, 3, 5, 7]))