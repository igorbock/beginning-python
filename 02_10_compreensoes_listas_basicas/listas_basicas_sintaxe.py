# Crie uma função chamada double_numbers que recebe uma lista de números numbers como argumento. 
# A função deve usar uma compreensão de lista para criar uma nova lista onde cada número na lista original é dobrado. 
# A função deve retornar a nova lista.

def double_numbers(numbers):
    # Write code here
    return [n * 2 for n in numbers]

print(double_numbers([1, 2, 3, 4, 5]))
print(double_numbers([-10, 0, 10, 20, -30]))