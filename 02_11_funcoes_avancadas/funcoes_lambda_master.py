# Crie uma função lambda chamada average que recebe quatro argumentos, a, b, c e d, e retorna a média deles. 
# Após definir a função lambda, chame-a com os valores 10, 15, 20 e 25, e imprima o resultado.

# Create a lambda function that calculates the average of four numbers
average = lambda a, b, c, d: (a + b + c + d) / 4

# Call the lambda function with the values 10, 15, 20, and 25
result = average(10, 15, 20, 25)

# Print the result
print(result)