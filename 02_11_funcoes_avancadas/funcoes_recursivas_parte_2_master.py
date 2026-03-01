# Escreva uma função recursiva chamada sum_digits que recebe um inteiro positivo n como argumento
#  e retorna a soma de seus dígitos. A função deve funcionar da seguinte forma:

# Se n for um dígito único (menor que 10), retorne esse dígito.
# Caso contrário, retorne a soma do último dígito de n e o resultado de sum_digits
# chamada com n dividido por 10 (divisão inteira).

# Exemplo de Entrada:
# n = 1234

# Exemplo de Saída:
# 10
# Explicação: 1 + 2 + 3 + 4 = 10

def sum_digits(n):
    # Write code here
    if n < 10:
        return n
    soma = 0
    for num in str(n):
        soma += int(num)
    return soma

print(sum_digits(1))
print(sum_digits(555))
print(sum_digits(1001))
print(sum_digits(98765))
print(sum_digits(234567))
print(sum_digits(42))
print(sum_digits(789))
print(sum_digits(2023))
print(sum_digits(3071))
print(sum_digits(840))