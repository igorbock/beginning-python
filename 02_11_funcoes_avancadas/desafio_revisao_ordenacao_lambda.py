# Crie uma função chamada sort_tuples que recebe uma lista de tuplas data como argumento. 
# Cada tupla em data contém dois elementos: uma string e um número. 
# A função deve usar a função sorted() junto com uma função lambda para ordenar a lista de tuplas 
# com base no segundo elemento (o número) em ordem crescente. A função deve retornar a lista de tuplas ordenada.

def sort_tuples(data):
    # Use sorted() with a lambda function to sort the list of tuples
    sorted_data = sorted(data, key=lambda x: x[1])
    
    # Return the sorted list
    return sorted_data

print(sort_tuples([("Alice", 25), ("Bob", 30), ("Charlie", 20)]))