# Escreva um programa que solicita ao usuário que insira um número. Use um bloco try-except 
# para lidar com casos em que a entrada não é um inteiro válido.

# Se o usuário inserir um inteiro válido, imprima "You entered: <number>".
# Se o usuário inserir um valor inválido (por exemplo, uma string ou caractere especial), capture a exceção e 
# imprima "Invalid input! Please enter a valid number.".

try:
    number = int(input())
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")