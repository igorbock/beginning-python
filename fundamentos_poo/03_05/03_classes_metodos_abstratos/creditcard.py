from paymentmethod import PaymentMethod

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"
    
    def payment_details(self):
        # Mask all but last 4 digits
        last_four = self.card_number[-4:]
        masked = "*" * (len(self.card_number) - 4) + last_four
        return f"Credit Card: {masked}"