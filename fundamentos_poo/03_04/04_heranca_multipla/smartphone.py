# TODO: Import the Device class from device.py
# TODO: Import the Internet class from internet.py
from device import Device
from internet import Internet

class Smartphone(Device, Internet):
    def __init__(self, brand, model):
        # TODO: Call the parent class (Device) constructor with the brand parameter using super()
        # TODO: Store the model parameter as an instance attribute (self.model)
        super().__init__(brand)
        self.model = model
    
    def make_call(self, number):
        # TODO: Return a formatted string "Calling {number}" where {number} is the parameter value
        return f"Calling {number}"