# Neste desafio, você implementará uma hierarquia de classes.

# Você precisará editar estes arquivos:

# device.py: Implemente a classe base Device
# screen.py: Implemente a classe Screen que herda de Device
# computer.py: Implemente a classe Computer que herda de Device
# laptop.py: Implemente a classe Laptop com herança múltipla
# driver.py - Implemente casos de teste que verificarão se sua implementação funciona corretamente
# Cada arquivo contém comentários TODO detalhados que o guiarão passo a passo na implementação.

# TODO: Import all required classes
from device import Device
from screen import Screen
from computer import Computer
from laptop import Laptop

def explain_mro(class_name):
    # TODO: Print the MRO (Method Resolution Order) for the given class
    # TODO: Format: "MRO for [class name]:" (note: NO space after the colon)
    # TODO: Use class_name.__name__ to get the name of the class
    # TODO: Use class_name.__mro__ to get the MRO tuple
    # TODO: Print each class name in the MRO on separate lines
    print(f"MRO for {class_name.__name__}:")
    objects = class_name.__mro__
    for item in objects:
        print(item.__name__)

    # TODO: Create an instance of the class
    # TODO: Call power_on() on the instance and store the result
    # TODO: Print: "Power on result: [result]"
    # TODO: Print an empty line for better readability
    teste = class_name()
    print(f"Power on result: {teste.power_on()}")
    print("")

# Test your code
# TODO: Call explain_mro() with each class: Device, Screen, Computer, and Laptop
explain_mro(Device)
explain_mro(Screen)
explain_mro(Computer)
explain_mro(Laptop)
