from abc import ABC, abstractmethod

# Create the abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def payment_details(self):
        pass
    
    def validate(self, amount):
        return amount > 0