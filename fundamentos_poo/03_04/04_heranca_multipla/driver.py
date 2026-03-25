# Neste desafio, você implementará um sistema de classes em múltiplos arquivos demonstrando herança múltipla 
# com smartphones. Cada classe está organizada em seu próprio arquivo para melhor organização do código.

# Você precisará editar estes arquivos:

# device.py - Implemente a classe base Device
# internet.py - Implemente a classe base Internet
# smartphone.py - Implemente a classe Smartphone que herda de ambas as classes base
# driver.py - Implemente casos de teste que verificarão se sua implementação funciona corretamente
# Cada arquivo contém comentários TODO detalhados que o guiarão passo a passo na implementação.

# TODO: Import the Smartphone class from smartphone.py
from smartphone import Smartphone

# Create a smartphone and test its methods
# TODO: Create a Smartphone object with brand "Apple" and model "iPhone 13"
my_phone = Smartphone("Apple", "iPhone 13")

# TODO: Call and print the power_on() method of the smartphone
print(my_phone.power_on())

# TODO: Call and print the connect() method of the smartphone
print(my_phone.connect())

# TODO: Call and print the make_call() method of the smartphone with parameter "123-456-7890"
print(my_phone.make_call("123-456-7890"))