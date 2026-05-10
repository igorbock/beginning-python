# Escreva uma função create_item_tag que recebe item_name, price e retorna uma string
#  de etiqueta de preço formatada.

# A função converte o preço para o formato binário e coloca o nome do item em maiúsculas 
# para criar uma etiqueta padronizada para o sistema de inventário de venda de garagem.

# Parâmetros:

# item_name (str): Nome do item sendo vendido
# price (int): Preço em dólares (formato decimal)
# Retorna: String de etiqueta formatada. Formato: "ITEM_NAME: 0bBINARY_PRICE"

def create_item_tag(item_name, price):
    # Write code here 
    binary_price = bin(price)
    item_name_upper = item_name.upper()
    return f"{item_name_upper}: {binary_price}"

# Exemplos de uso:
print(create_item_tag("ball", 0))  # Output: "BALL: 0b0"
print(create_item_tag("pen", 1))
print(create_item_tag("oil_filter", 3))
print(create_item_tag("mug", 5))
print(create_item_tag("spark_plug", 7))
print(create_item_tag("screwdriver", 8))
print(create_item_tag("desk lamp", 12))
print(create_item_tag("ignition_coil", 25))
print(create_item_tag("tire", 100))