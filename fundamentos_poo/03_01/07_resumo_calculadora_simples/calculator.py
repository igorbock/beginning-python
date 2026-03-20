# Sua classe Calculator em calculator.py deve:

# Ter um construtor que inicializa um atributo result para 0
# Incluir métodos para add, subtract, multiply e divide que cada um:
# Receba um número como argumento
# Realize a operação entre o result atual e o número
# Atualize o atributo result
# Retorne o novo resultado
# Incluir um método clear que redefine o result para 0
# Incluir um método get_result que retorna o resultado atual
# Para o método divide, você deve lidar com divisão por zero da seguinte forma:
# Verifique se o número fornecido é igual a 0
# Se for zero, imprima exatamente: "Error: Division by zero"
# Deixe o atributo result inalterado neste caso
# Retorne o valor result inalterado
# O arquivo driver.py importará sua classe Calculator e a testará com código semelhante a este:

# from calculator import Calculator

# calc = Calculator()
# calc.add(5)       # result becomes 5
# calc.multiply(3)  # result becomes 15
# calc.subtract(2)  # result becomes 13
# calc.divide(0)    # prints "Error: Division by zero", result remains 13
# calc.divide(2)    # result becomes 6.5
# calc.clear()      # result becomes 0
# Siga os comentários TODO no arquivo calculator.py para implementar toda a funcionalidade necessária.

class Calculator:
    def __init__(self):
        # TODO: Initialize the result attribute to 0
        self.result = 0
        
    def add(self, number):
        # TODO: Add the number to result and return the new result
        self.result += number
        return self.result
    
    def subtract(self, number):
        # TODO: Subtract the number from result and return the new result
        self.result -= number
        return self.result
    
    def multiply(self, number):
        # TODO: Multiply result by the number and return the new result
        self.result *= number
        return self.result 
    
    def divide(self, number):
        # TODO:
        # Check if number is 0
        # If it is, print error message and return unchanged result
        # Otherwise, divide result by the number and return the new result
        if number == 0:
            print("Error: Division by zero")
            return self.result
        else:
            self.result /= number
            return self.result
    
    def clear(self):
        # TODO: Reset result to 0 and return it
        self.result = 0
        return self.result
    
    def get_result(self):
        # TODO: Return the current value of result
        return self.result