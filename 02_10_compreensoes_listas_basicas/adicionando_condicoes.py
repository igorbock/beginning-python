# Crie uma função chamada filter_and_square que recebe uma lista de números numbers como argumento. 
# A função deve usar uma compreensão de lista para criar uma nova lista que inclui os quadrados 
# apenas dos números positivos da lista original. A função deve retornar a nova lista.

def filter_and_square(numbers):
    # Write code here
    nova_lista = [x**2 for x in numbers if x > 0]
    return nova_lista

print(filter_and_square([-3, -2, 0, 1, 2, 3]))
print(filter_and_square([1, 2, 3, 4, 5]))