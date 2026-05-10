# Crie uma função chamada revolutionary_appliance_search que recebe appliances e target_appliance como parâmetros.

# Esta função procura por um eletrodoméstico alvo dentro de um array de eletrodomésticos e retorna seu 
# índice no array invertido se encontrado, ou -1 se não encontrado.

# Passos:

# Procure por target_appliance em appliances.
# Se encontrado:
# Obtenha o índice de target_appliance.
# Inverta o array até o índice encontrado (inclusive).
# Retorne uma tupla com o array modificado e o índice no array invertido.
# Se não encontrado:
# Retorne uma tupla com o array original e -1.
# Parâmetros:

# appliances (list of str): Um array de nomes de eletrodomésticos.
# target_appliance (str): O eletrodoméstico a ser procurado.
# A função retorna uma tupla com o array possivelmente modificado e o índice de target_appliance 
# no array invertido, ou -1 se não encontrado.

def revolutionary_appliance_search(appliances, target_appliance):
    if target_appliance in appliances:
        index = appliances.index(target_appliance)
        appliances[:index + 1] = appliances[:index + 1][::-1]
        return appliances, index
    else:
        return appliances, -1
    
# Exemplos de uso:
appliances = ["oven", "refrigerator", "microwave", "toaster"]
print(revolutionary_appliance_search(appliances, "microwave")) 

appliances = ["dishwasher", "stove", "oven", "freezer", "microwave"]
print(revolutionary_appliance_search(appliances, "freezer")) 