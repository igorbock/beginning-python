# TODO: Import the Vehicle class from vehicle.py
# TODO: Import the Car class from car.py
from car import Car
from vehicle import Vehicle

# TODO: Create a Vehicle object with make "Toyota" and model "Corolla"
vehicle = Vehicle("Toyota", "Corolla")

# TODO: Create a Car object with make "Honda" and model "Civic"
car = Car("Honda", "Civic")

# TODO: Call display_info() method on the vehicle object
# Expected output: "Vehicle: Toyota Corolla"
vehicle.display_info()

# TODO: Call display_info() method on the car object
# Expected output: "Vehicle: Honda Civic"
# Note: Car inherits display_info from Vehicle without modification
car.display_info()