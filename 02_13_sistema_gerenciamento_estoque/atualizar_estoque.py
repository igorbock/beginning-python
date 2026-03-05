# Crie uma função chamada update_stock que recebe dois argumentos: item (string) e quantity (int). A função deve:

# Verifique se o item existe no dicionário inventory.
# Se não existir, imprima "Error: Item '<item>' not found.".
# Se o item existir, calcule o novo estoque somando o quantity ao estoque atual.
# Se o novo estoque for negativo, imprima "Error: Insufficient stock for '<item>'." e não atualize.
# Caso contrário, atualize o estoque no inventory.
# Imprima "Stock for '<item>' updated successfully.".
# Adicione (substitua) o seguinte bloco de código no final do seu código:

# add_item("Apple", 0.5, 100)
# add_item("Banana", 0.2, 50)
# add_item("Apple", 0.6, 30)  # Should print an error
# update_stock("Apple", -20)
# update_stock("Banana", 30)
# update_stock("Orange", 10)  # Should print an error
# update_stock("Apple", -90)
# print(inventory)  

inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": price, "stock": stock}
        print(f"Item '{item}' added successfully.")

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        if abs(quantity) > inventory[item]["stock"]:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] += quantity
            print(f"Stock for '{item}' updated successfully.")

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
update_stock("Apple", -20)
update_stock("Banana", 30)
update_stock("Orange", 10)  # Should print an error
update_stock("Apple", -90)
print(inventory)  