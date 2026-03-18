# Complete a classe Car em car.py adicionando um método chamado display_info que usa o parâmetro self 
# para imprimir o ano, marca e modelo do carro no formato:

# "This car is a [year] [make] [model]".

# car.py: Contém a definição da classe Car onde você adicionará o método display_info
# driver.py: Arquivo de execução principal que importa e usa a classe Car
# O arquivo driver.py importará sua classe Car e criará instâncias para testar sua implementação. 
# Certifique-se de que seu método funcione corretamente quando chamado do arquivo driver.

class Car:
    # TODO: Add the display_info method here
    def display_info(self):
        print(f"This car is a {self.year} {self.make} {self.model}")