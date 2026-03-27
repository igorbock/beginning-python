# TODO: Import the Vehicle class from vehicle.py
# Use: from vehicle import Vehicle
from vehicle import Vehicle

class Car(Vehicle):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    # TODO: Override the start() method to return "Car engine started"
    def start(self):
        return "Car engine started"
    
    # TODO: Override the fuel_efficiency() method to return 25
    def fuel_efficiency(self):
        return 25