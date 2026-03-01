# Escreva uma função recursiva chamada count_down que recebe um inteiro positivo n como argumento e 
# imprime cada número de n até 0.

def count_down(n):
    # Write code here
    print(n)
    if n == 0:
        return 0
    return count_down(n - 1)

print(count_down(3))
print(count_down(5))
print(count_down(0))