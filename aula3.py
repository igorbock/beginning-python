#Funções
def obter_numero(index) :
    try :
        return float(input(f"Digite o {index}º número: "))
    except :
        return obter_numero(index)

def obter_inteiros(index) :
    try :
        return int(input(f"Digite o {index}º número inteiro: "))
    except:
        return obter_inteiros(index)
    
def obter_inteiros_positivos(index) :
    try :
        numero = int(input(f"Digite o {index}º número inteiro positivo: "))
        if numero > 0 :
            return numero
        else :
            raise ValueError("Somente números positivos")
    except ValueError as erro:
        print(f"Erro => {erro}")
        return obter_inteiros_positivos(index)
    
#Exercicio 1
# for x in range(1, 6) :
#     print(f"{x}º - {x * 3}")

#Exercicio 2
# print("Com laço for...")
# for x in range(1, 101) :
#     print(x)

# x = 0
# print("Com laço while...")
# while x < 100 :
#     x += 1
#     print(x)

#Exercicio 3
# x = 10
# while x >= 0 :
#     print(x)
#     x -= 1

# print("FIM!")

#Exercicio 4
# inteiro = 0
# while inteiro <= 100000 :
#     print(inteiro)
#     inteiro += 1000

#Exercicio 5
# index = 1
# soma = float()
# while index < 11 :
#     soma += obter_numero(index)
#     index += 1

# print(f"A soma dos valores é: {soma}")

#Exercicio 6
# i = 1
# soma = int()
# while i < 11 :
#     soma += obter_inteiros(i)
#     i += 1

# print(f"A média dos 10 números inteiros é: {soma / 10}")

#Exercicio 7
# i = 1
# ignorados = int()
# soma = int()

# while i < 11 :
#     try :
#         numero = int(input(f"Digite o {i}º número inteiro positivo: "))
#         if numero > 0 :
#             soma += numero
#         else :
#             raise Exception("Somente números positivos")
#     except :
#         ignorados += 1
#     finally :
#         i += 1

# print(f"A média dos {10 - ignorados} números inteiros positivos é: {soma / (10 - ignorados)}")

#Exercicio 8
# maior = float()
# menor = float()
# atual = float()
# i = 1

# while i < 11 :
#     atual = obter_numero(i)
#     if atual > maior :
#         maior = atual
#     if atual < menor :
#         menor = atual
#     i += 1

# print(f"O maior número é '{maior}' e o menor número é '{menor}'")
