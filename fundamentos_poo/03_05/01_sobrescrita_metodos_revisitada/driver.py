# Neste desafio, você implementará um sistema de herança de veículos.

# Você precisará editar estes arquivos:

# vehicle.py: Implemente a classe base Vehicle com atributos make/model e métodos
# car.py: Crie a classe Car que herda de Vehicle
# motorcycle.py: Crie a classe Motorcycle que herda de Vehicle
# truck.py: Crie a classe Truck que herda de Vehicle
# Cada arquivo contém comentários TODO detalhados para guiar sua implementação passo a passo. 
# Preste atenção às instruções de importação necessárias entre os arquivos e siga as relações de herança. 
# O arquivo driver.py contém casos de teste que verificarão se sua implementação funciona corretamente 
# para todos os tipos de veículos.

from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def vehicle_info(vehicle):
    return f"{vehicle.make} {vehicle.model}: {vehicle.start()}, Efficiency: {vehicle.fuel_efficiency()} mpg"


# Test with different vehicles - DO NOT MODIFY THIS TEST CODE
vehicles = [
    Car("Toyota", "Camry"),
    Motorcycle("Harley", "Davidson"),
    Truck("Ford", "F-150"),
    Vehicle("Generic", "Vehicle")
]

for v in vehicles:
    print(vehicle_info(v))