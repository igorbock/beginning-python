# Complete a classe Temperature em temperature.py que converte entre Celsius e Fahrenheit. 
# Em seguida, use esta classe em driver.py para testar conversões de temperatura. 
# Siga os comentários TODO em ambos os arquivos para instruções passo a passo.

class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self._celsius = celsius
    
    # TODO: Create a property decorator for celsius that returns self._celsius
    @property
    def temperature(self):
        return self._celsius
    
    # TODO: Create a celsius.setter that validates the temperature is above absolute zero (-273.15°C)
    @temperature.setter
    def temperature(self, value):
    # TODO: If value < -273.15, raise ValueError with message "Temperature cannot be below absolute zero (-273.15°C)"
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        else:
            # TODO: Otherwise, set self._celsius to the value
            self._celsius = value
    
    # TODO: Create a property decorator for fahrenheit that converts Celsius to Fahrenheit
    # TODO: Use the formula: F = C × 9/5 + 32
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    # TODO: Create a fahrenheit.setter that converts Fahrenheit to Celsius
    # TODO: Use the formula: C = (F - 32) × 5/9
    # TODO: Set self.celsius to this converted value (this will use your celsius setter for validation)
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
