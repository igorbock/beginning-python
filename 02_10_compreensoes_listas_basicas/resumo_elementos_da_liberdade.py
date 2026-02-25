# Crie uma função chamada elements_of_freedom que processa uma lista de elementos de string de acordo com 
# regras específicas.

# Sua função deve:

# Filtrar elementos que têm menos de 5 caracteres
# Converter os elementos restantes para maiúsculas
# Remover quaisquer elementos duplicados
# Retornar uma lista dos elementos únicos em maiúsculas
# Use operações de lista para processar os dados de forma eficiente.

# Nota: Preserve a ordem original dos elementos na lista.

def elements_of_freedom(elements):
    # Your solution here
    if elements == []:
        return []
    # Step 1: Filter elements with length >= 5
    filtro = [x for x in elements if len(x) >= 5]
    # Step 2: Convert filtered elements to uppercase
    upper = [y.upper() for y in filtro]
    # Step 3: Create a list of unique elements
    unicos = []
    uniques = [unicos.append(z) for z in upper if z not in unicos]
    # Step 4: Return the final result
    return unicos

print(elements_of_freedom(["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"]))
print(elements_of_freedom(["freedom", "liberty", "justice", "hope", "dreams", "hope", "peace"]))