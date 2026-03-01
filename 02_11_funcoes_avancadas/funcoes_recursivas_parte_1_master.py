# Escreva uma função recursiva chamada print_sequence que recebe um inteiro positivo n como argumento e 
# imprime uma sequência de contagem regressiva. 
# Para cada número de n até 1, ela deve imprimir 'T-minus {number}'. 
# Quando chegar a 0, ela deve imprimir 'Blast off!'. Por exemplo, se n for 3, a saída deve ser:
# T-minus 3
# T-minus 2
# T-minus 1
# Blast off!

def print_sequence(n):
    # Write code here
    if (n == 0):
        print("Blast off!")
        return
    print(f"T-minus {n}")
    return print_sequence(n - 1)

print(print_sequence(5))
print(print_sequence(3))
print(print_sequence(1))
print(print_sequence(10))
print(print_sequence(7))