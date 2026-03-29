from paymentmethod import PaymentMethod

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"
    
    def payment_details(self):
        return f"PayPal account: {self.email}"