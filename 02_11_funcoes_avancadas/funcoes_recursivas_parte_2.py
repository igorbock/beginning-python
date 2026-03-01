# Escreva uma função recursiva chamada fibonacci que recebe um inteiro positivo n como argumento e 
# retorna o n-ésimo número de Fibonacci. A sequência de Fibonacci é definida como:

# fibonacci(1) = 0
# fibonacci(2) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) para n > 2.

def fibonacci(n):
    # Write code here
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))
print(fibonacci(12))
print(fibonacci(21))
print(fibonacci(4))
print(fibonacci(9))