# TODO: Import the Screen class from screen.py
# TODO: Import the Computer class from computer.py
from screen import Screen
from computer import Computer

class Laptop(Screen, Computer):
    # TODO: Notice that Laptop inherits from both Screen and Computer
    # TODO: The order of inheritance is important (Screen first, then Computer)
    # TODO: No need to override power_on() - it will use the MRO to determine which method to call
    pass