# Implemente o Padrão Observer criando um sistema de monitoramento meteorológico. 
# Você precisa criar duas classes nas áreas designadas do código.

# Passo 1: Criar a classe WeatherStation

# Escreva sua classe WeatherStation onde o comentário indica. Esta classe deve:

# Herdar da classe Subject (use class WeatherStation(Subject):)
# Inicializar com:
# Chamar o construtor pai usando super().__init__()
# Definir a temperatura inicial como 0 usando um atributo privado self._temperature
# Implementar set_temperature(self, temperature):
# Atualizar o atributo de temperatura privado
# Chamar self.notify(self._temperature) para notificar todos os observadores
# Implementar get_temperature(self):
# Retornar o valor da temperatura atual
# Passo 2: Criar a classe WeatherDisplay

# Escreva sua classe WeatherDisplay onde o comentário indica. Esta classe deve:

# Herdar da classe Observer (use class WeatherDisplay(Observer):)
# Inicializar com:
# Aceitar um parâmetro name
# Armazenar o nome como self.name
# Implementar update(self, temperature):
# Imprimir a mensagem de atualização de temperatura no formato exato mostrado abaixo
# Formato da Mensagem:

# Quando um display recebe uma atualização de temperatura, ele deve imprimir exatamente:

# Display [name]: Current temperature is [temperature]C
# Exemplo de Uso:

# # Create weather station and displays
# station = WeatherStation()
# phone_display = WeatherDisplay("Phone")
# tablet_display = WeatherDisplay("Tablet")

# # Attach displays to station
# station.attach(phone_display)
# station.attach(tablet_display)

# # Update temperature - both displays will be notified
# station.set_temperature(25.5)

# # Output:
# # Display Phone: Current temperature is 25.5C
# # Display Tablet: Current temperature is 25.5C
# Notas Importantes:

# Os métodos attach() e detach() já estão implementados na classe base Subject - você não precisa implementá-los 
# ou chamá-los em sua classe WeatherStation
# No exemplo de uso acima, station.attach(phone_display) é chamado pelo usuário da sua classe, não dentro 
# da sua implementação de WeatherStation
# Sua WeatherStation só precisa chamar self.notify() quando a temperatura mudar - a classe base Subject cuida do resto
# Foque em implementar os três métodos exigidos em WeatherStation e os dois métodos exigidos em 
# WeatherDisplay conforme especificado acima

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
        
    def detach(self, observer):
        self._observers.remove(observer)
        
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
            
class Observer:
    def update(self, data):
        pass

# Write your WeatherStation class here
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify(self._temperature)

    def get_temperature(self):
        return self._temperature

# Write your WeatherDisplay class here
class WeatherDisplay(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, temperature):
        print(f"Display {self.name}: Current temperature is {temperature}C")

# Create weather station and displays
station = WeatherStation()
phone_display = WeatherDisplay("Phone")
tablet_display = WeatherDisplay("Tablet")

# Attach displays to station
station.attach(phone_display)
station.attach(tablet_display)

# Update temperature - both displays will be notified
station.set_temperature(25.5)

# Output:
# Display Phone: Current temperature is 25.5C
# Display Tablet: Current temperature is 25.5C
