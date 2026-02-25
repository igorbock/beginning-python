# Crie uma função chamada get_product_info que não recebe argumentos. 
# A função deve retornar uma tupla contendo as seguintes informações sobre um produto:

# Nome: "Laptop"
# Preço: 999.99
# Avaliação: 4.5
# Após definir a função, chame-a e desempacote os valores retornados em três variáveis: 
# product_name, product_price e product_rating. Em seguida, imprima os valores dessas variáveis.

def get_product_info():
    name = "Laptop"
    price = 999.99
    rating = 4.5
    return name, price, rating

product_name, product_price, product_rating = get_product_info()
print(product_name)
print(product_price)
print(product_rating)