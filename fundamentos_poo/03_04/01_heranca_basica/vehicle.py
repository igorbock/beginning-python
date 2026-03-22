# vehicle.py: Contém a classe pai Vehicle
# car.py: Contém a classe Car que herda de Vehicle
# driver.py: Arquivo principal para testar sua implementação
# Cada arquivo contém comentários TODO detalhados para guiá-lo na implementação. Você precisará:

# Completar a classe Vehicle com os atributos make e model
# Implementar herança de classe adequada na classe Car
# Configurar as declarações de importação corretas entre os arquivos
# Criar e testar objetos no arquivo driver
# Siga os comentários TODO cuidadosamente, pois eles fornecem orientação passo a passo para a solução.

class Vehicle:
    def __init__(self, make, model):
        # TODO: Initialize the Vehicle class with make and model parameters
        # TODO: Store make and model as instance attributes (self.make, self.model)
        self.make = make
        self.model = model
    
    def display_info(self):
        # TODO: Implement a display_info method that prints vehicle information
        # TODO: Print in format: "Vehicle: [make] [model]"
        # TODO: Use f-string formatting: f"Vehicle: {self.make} {self.model}"
        print(f"Vehicle: {self.make} {self.model}")