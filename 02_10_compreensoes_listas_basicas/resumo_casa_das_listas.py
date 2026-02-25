# Crie uma função chamada house_of_lists que recebe uma lista de listas list_of_lists como argumento. 
# Cada lista interna contém números. A função deve usar compreensões de listas para realizar as seguintes operações:

# Filtrar as listas internas que têm uma soma maior que 50.
# Das listas internas restantes, extrair números que sejam menores que 5.
# Combinar todos os números extraídos em uma única lista.
# Retornar a lista combinada de números.

def house_of_lists(list_of_lists):
    # Write code here
    if list_of_lists == []:
        return []
    lista_atual = []
    retorno = []
    for item in list_of_lists:
        soma_lista = sum(item)
        if soma_lista < 50:
            lista_atual = [x for x in item if x < 5]
            for i in lista_atual:
                retorno.append(i)
    return retorno

print(house_of_lists([[10, 20, 30], [1, 2, 3], [5, 50, 5], [0, 3, 6, 9]]))
print(house_of_lists([[4, 4, 4], [100], [2, 3, 4], [10, 10, 10, 10]]))