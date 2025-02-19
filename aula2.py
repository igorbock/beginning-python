#Funções
def calcular_raiz_quadrada(numero):
    if numero < 0 :
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    
    aproximacao = numero / 2
    diferenca = float('inf')
    precisao = 0.00001

    while diferenca > precisao :
        novaAproximacao = (aproximacao + numero / aproximacao) / 2.0
        diferenca = abs(novaAproximacao - aproximacao)
        aproximacao = novaAproximacao

    return aproximacao

def calcular_quadrado(numero):
    return numero * numero

#Exercicio 1
# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))

# if numero1 > numero2 :
#     print(f"O número '{numero1}' é maior que '{numero2}'")
# else :
#     print(f"O número '{numero2}' é maior que '{numero1}'")

#Exercicio 2
# numero = float(input("Digite qualquer número: "))

# if numero >= 0 :
#     raiz_quadrada = calcular_raiz_quadrada(numero)
#     print(f"A raiz quadrada do número '{numero} é: {raiz_quadrada}'")
# else :
#     print(f"O número '{numero}' é inválido")


#Exercicio 3
# numero_decimal = float(input("Digite um número decimal: "))

# if numero_decimal > 0 :
#     raiz_quadrada = calcular_raiz_quadrada(numero_decimal)
#     print(f"A raiz quadrada de '{numero_decimal}' é: {raiz_quadrada}")
# else :
#     quadrado = calcular_quadrado(numero_decimal)
#     print(f"O número '{numero_decimal}' ao quadrado é: '{quadrado}'")

#Exercicio 4
# numero = float(input("Digite qualquer número: "))

# if numero >= 0 :
#     raiz_quadrada = calcular_raiz_quadrada(numero)
#     quadrado = calcular_quadrado(numero)
#     print(f"A raiz quadrada do número '{numero} é: {raiz_quadrada}' \nO número '{numero}' ao quadrado é: '{quadrado}'")
# else :
#     print(f"O número '{numero}' é inválido")

#Exercicio 5
numero = int(input(f"Digite um número inteiro: "))

if numero % 2 == 0 :
    print(f"O número '{numero}' é par")
else :
    print(f"O número '{numero}' é impar")
