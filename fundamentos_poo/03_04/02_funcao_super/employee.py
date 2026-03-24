# TODO: Import the Person class from person.py
# Use format: from person import Person
from person import Person

class Employee(Person):
    def __init__(self, name, age, job):
        # TODO: Call the parent class constructor with name and age using super()
        # TODO: Store job as an instance attribute (self.job)
        super().__init__(name, age)
        self.job = job
    
    def introduce(self):
        # TODO: Override the introduce method to extend parent functionality
        # TODO: First call the parent's introduce method using super()
        # TODO: Then print exactly: "I work as a [job]" using self.job
        super().introduce()
        print(f"I work as a {self.job}")