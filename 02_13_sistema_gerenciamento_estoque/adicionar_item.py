# Crie uma função chamada add_item que recebe três argumentos: item (string), price (float) e stock (int). 
# A função deve:

# Verifique se o item já existe no dicionário inventory.
# Se existir, imprima "Error: Item '<item>' already exists.".
# Se o item não existir, adicione-o ao inventory com o preço e o estoque fornecidos.
# Armazene o preço como um float e o estoque como um inteiro.
# Imprima "Item '<item>' added successfully.".
# Adicione (substitua) o seguinte bloco de código no final do seu código:

# add_item("Apple", 0.5, 100)
# add_item("Banana", 0.2, 50)
# add_item("Apple", 0.6, 30)  # Should print an error
# print(inventory)  

inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": price, "stock": stock}
        print(f"Item '{item}' added successfully.")

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)