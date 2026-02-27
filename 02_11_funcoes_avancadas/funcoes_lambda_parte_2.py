# Crie uma função lambda chamada categorize_number que recebe um número como argumento e retorna:

# "Positive" se o número for maior que 0
# "Zero" se o número for igual a 0
# "Negative" se o número for menor que 0
# Em seguida, use esta função lambda para categorizar um número recebido da entrada.

# Read a number from input
number = int(input())

# Define your lambda function here
categorize_number = lambda n: "Positive" if n > 0 else "Zero" if n == 0 else "Negative"

# Call your lambda function with the input number and print the result
print(categorize_number(number))