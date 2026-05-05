# Let's challenge your naming conventions skills!

# challenge icon
# Desafio

# Fácil
# You are given code which violates the naming conventions of Python, locate this problems and fix them!

# Use restart button when needed.

# What this code do?

# Don't change unnecessary code as we test against regex :)

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_voice(self):
        pass

class RedTiger(Animal):
    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(self.voice)

DEFAULT_VOICE = "Woof"

if __name__ == "__main__":
    default_tiger = RedTiger(DEFAULT_VOICE)
    real_tiger = RedTiger("Arrgh!")
    default_tiger.make_voice()
    real_tiger.make_voice()

    
