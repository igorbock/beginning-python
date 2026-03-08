# Crie uma função chamada process_numbers que recebe uma lista de números e os processa de acordo com regras específicas.

# Requisitos:

# Primeiro, filtre todos os números negativos e zero
# Em seguida, para os números positivos restantes:
# Dobre os números pares
# Triplique os números ímpares
# Use map() e filter() para resolver o problema.

def process_numbers(numbers):
    # Write your code below
    positivos = filter(lambda x: x > 0, numbers)
    
    processed_numbers = map(lambda x: x * 2 if x % 2 == 0 else x * 3, positivos)
    return list(processed_numbers)

print(process_numbers([-4, 0, 5, 2, 8, -3, 7]))
print(process_numbers([1, 2, 3, 4]))
print(process_numbers([100, 99, -100]))