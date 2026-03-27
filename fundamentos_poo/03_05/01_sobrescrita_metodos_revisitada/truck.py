# TODO: Import the Vehicle class from vehicle.py
# Use: from vehicle import Vehicle
from vehicle import Vehicle

class Truck(Vehicle):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    # TODO: Override the start() method to return "Truck diesel engine started"
    def start(self):
        return "Truck diesel engine started"
    
    # TODO: Override the fuel_efficiency() method to return 15
    def fuel_efficiency(self):
        return 15