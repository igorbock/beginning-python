# Crie um programa que simule um carrinho de compras com tratamento de erros. Sua tarefa é:

# Criar uma função chamada handle_shopping_cart que processa pedidos de clientes
# A função deve aceitar uma lista de strings de pedidos no formato "item:quantity"
# Processar cada pedido da seguinte forma:
# Dividir a string de entrada para obter o item e a quantidade
# Converter a quantidade para um inteiro
# Adicionar o item a um dicionário de carrinho de compras com a quantidade como valor
# Se um item já existir no carrinho, atualizar sua quantidade
# Tratar estes erros específicos:
# Se o formato de entrada estiver incorreto (falta de dois-pontos), imprimir "Invalid format: {order}"
# Se a quantidade não for um número válido, imprimir "Invalid quantity: {order}"
# Se a quantidade for negativa, imprimir "Negative quantity not allowed: {order}"
# Retornar o dicionário completo do carrinho de compras

def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
            # Split the order and add to cart
            if ":" not in order:
                raise Exception(f"Invalid format: {order}")
            shop = str.split(order, ":")
            # Handle potential errors
            item = shop[0]
            quant = int(shop[1])
            if quant < 0:
                raise Exception(f"Negative quantity not allowed: {order}")
            if item in cart:
                cart[item] += quant
            else:
                cart[item] = quant
        except ValueError:
            # Handle value errors
            print(f"Invalid quantity: {order}")
        except Exception as e:
            # Handle unexpected errors
            print(e)
    # Return the completed cart
    return cart

print(handle_shopping_cart(["apple:3","banana:2","milk:5"]))
print(handle_shopping_cart(["bread:2","banana:five","eggs:10"]))
print(handle_shopping_cart(["chocolate:-5","yogurt:3","milk:2"]))
print(handle_shopping_cart(["cereal:1","cereal:3","orange:5","butter:2"]))