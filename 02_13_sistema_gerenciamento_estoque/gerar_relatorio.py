# O sistema de inventário já tem estes componentes implementados:

# Um dicionário global inventory onde:
# Chaves são nomes de itens (strings)
# Valores são dicionários contendo:
# "price": O preço do item (float)
# "stock": Quantidade atual em estoque (integer)
# Uma função add_item(item, price, stock) que adiciona novos itens ao inventário
# Uma função update_stock(item, quantity) que atualiza o nível de estoque
# Uma função check_availability(item) que retorna o nível atual de estoque
# Sua tarefa é implementar a função sales_report(sales) que:

# Recebe um dicionário sales onde:
# Chaves são nomes de itens
# Valores são quantidades vendidas
# Para cada item no dicionário de vendas:
# Verifica se o item existe no inventário
# Verifica se há estoque suficiente
# Atualiza o inventário reduzindo os níveis de estoque
# Calcula a receita com base no preço e na quantidade vendida
# Retorna uma string formatada com a receita total
# Lide com estes erros específicos:

# Se um item não existir no inventário, imprima: "Error: Item '{item}' not found."
# Se houver estoque insuficiente, imprima: "Error: Insufficient stock for '{item}'."
# A saída deve ser uma string formatada como: “Total revenue: ${total:.2f}”

 

# Adicione (substitua) o seguinte bloco de código no final do seu código:

# add_item("Apple", 0.5, 50)
# add_item("Banana", 0.2, 60)
# sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
# print(sales_report(sales))  # Should output: 19.0
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

def check_availability(item):
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return "Item not found"

def sales_report(sales):
    total = 0
    for i, q in sales.items():
        if i not in inventory:
            print(f"Error: Item '{i}' not found.")
        elif inventory[i]["stock"] < q:
            print(f"Error: Insufficient stock for '{i}'.")
        else:
            inventory[i]["stock"] -= q
            total += q * inventory[i]["price"]
    return f"Total revenue: ${total:.2f}"

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)