# TODO: Import the Vehicle class from vehicle.py
# Use: from vehicle import Vehicle
from vehicle import Vehicle

class Motorcycle(Vehicle):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    # TODO: Override the start() method to return "Motorcycle engine roared to life"
    def start(self):
        return "Motorcycle engine roared to life"
    
    # TODO: Override the fuel_efficiency() method to return 40
    def fuel_efficiency(self):
        return 40