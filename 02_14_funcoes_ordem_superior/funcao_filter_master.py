# Crie uma função chamada get_prime_numbers que recebe uma lista de inteiros numbers como argumento. 
# A função deve usar a função filter() para selecionar números primos da lista. 
# Um número primo é um número maior que 1 que não possui divisores positivos outros além de 1 e ele mesmo. 
# A função deve retornar uma lista contendo os números primos selecionados.

def get_prime_numbers(numbers):
    # Define a helper function to check if a number is prime
    # A number n is prime if n >= 2 and it has no divisors between 2 and int(n**0.5) + 1
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Use filter() with the helper function to select prime numbers
    prime_numbers = filter(is_prime, numbers)
    
    # Return the list of selected prime numbers
    return list(prime_numbers)

print(get_prime_numbers([2,3,4,5,10,11,13,17,18,19]))
print(get_prime_numbers([23,29,31,32,33,37,39,41,42,43]))
print(get_prime_numbers([47,48,49,50,51,53,59,60,61,67]))
print(get_prime_numbers([71,72,73,74,75,76,77,79,83,89]))
print(get_prime_numbers([97,98,99,100,101,103,107,109,113,127]))