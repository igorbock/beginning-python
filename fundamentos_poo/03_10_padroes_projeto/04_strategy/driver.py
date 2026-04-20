# Implemente uma nova estratégia BitcoinPayment para o nosso sistema de compras.

# Sua tarefa é:

# Criar uma classe BitcoinPayment que implemente PaymentStrategy
# Ela deve aceitar um wallet_address no construtor
# O método pay deve imprimir exatamente: Paying $X using Bitcoin wallet: Y onde X é o valor e Y é o endereço da carteira
# O método pay deve retornar True após a impressão
# Escrever uma função main que:
# Crie um carrinho de compras
# Adicione um laptop custando $1200 e fones de ouvido custando $100 ao carrinho
# Crie um BitcoinPayment com o endereço de carteira "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
# Defina esta estratégia de pagamento no carrinho
# Chame o método checkout
# O código inicial já inclui if __name__ == "__main__": na parte inferior — você não precisa adicioná-lo. 
# Esta é uma convenção do Python que garante que sua função main() só seja executada quando o arquivo for executado diretamente 
# (não quando for importado por outro módulo). Basta definir sua função main() e o bloco fornecido a chamará automaticamente.

# Siga a mesma estrutura mostrada nos exemplos da lição.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card: {self.card_number}")
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal account: {self.email}")
        return True

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        else:
            raise ValueError("No payment strategy set")

# Create your BitcoinPayment strategy class here
class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin wallet: {self.wallet_address}")
        return True

def main():
    cart = ShoppingCart()
    cart.add_item("laptop", 1200)
    cart.add_item("fone", 100)
    cart.set_payment_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    cart.checkout()

if __name__ == "__main__":
    main()