# Neste desafio, você implementará um sistema de processamento de pagamentos.

# Você precisa completar a implementação nestes arquivos:

# paymentmethod.py - Classe base abstrata com lógica de validação
# creditcard.py - Implementação de pagamento com cartão de crédito
# paypal.py - Implementação de pagamento com PayPal
# Siga os comentários TODO em cada arquivo para implementar a funcionalidade necessária. 
# Os comentários o guiarão passo a passo na criação de métodos abstratos, implementação de subclasses 
# concretas e estabelecimento de relacionamentos de importação adequados entre arquivos.

# O arquivo driver.py contém casos de teste que verificarão se sua implementação funciona corretamente, processando
# diferentes cenários de pagamento e exibindo detalhes apropriados para cada método de pagamento.

from creditcard import CreditCard
from paypal import PayPal

# Test the implementations - DO NOT MODIFY THIS TEST CODE
cc = CreditCard("1234567890123456")
pp = PayPal("user@example.com")

# Process valid payments
if cc.validate(100):
    print(cc.process_payment(100))
    print(cc.payment_details())

if pp.validate(200):
    print(pp.process_payment(200))
    print(pp.payment_details())

# Try an invalid amount
if not pp.validate(0):
    print("Invalid payment amount")

# This would raise an error if uncommented:
# pm = PaymentMethod()  # Can't instantiate abstract class