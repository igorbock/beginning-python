# Crie uma função chamada check_availability que recebe um argumento: item (string). A função deve:

# Verifique se o item existe no dicionário inventory.
# Se não existir, retorne "Item not found".
# Se o item existir, retorne o estoque atual do item.
# Adicione (substitua) o seguinte bloco de código no final do seu código:

# add_item("Apple", 0.5, 100)
# add_item("Banana", 0.2, 50)
# update_stock("Apple", -20)
# update_stock("Banana", 30)
# print(check_availability("Apple"))  # Should return 80
# print(check_availability("Banana"))  # Should return 80
# print(check_availability("Orange"))  # Should return "Item not found"

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

def check_availability(item):
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return "Item not found"

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"