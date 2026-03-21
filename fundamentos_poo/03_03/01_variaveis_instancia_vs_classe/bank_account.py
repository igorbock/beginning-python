# Complete um sistema bancário.. Você definirá uma classe BankAccount em um arquivo e a usará em outro.

# Você trabalhará com:

# bank_account.py: Defina a classe BankAccount com atributos e métodos
# driver.py: Importe a classe, crie contas e demonstre variáveis de classe
# Siga os comentários TODO em ambos os arquivos para instruções passo a passo. 
# Os comentários o guiarão na criação da classe com variáveis e métodos apropriados, e na 
# demonstração de como as variáveis de classe afetam todas as instâncias.

class BankAccount:
    # TODO: Add class variable interest_rate set to 0.02 (2%)
    interest_rate = 0.02

    def __init__(self, account_holder, balance):
        # TODO: Initialize instance variables:
        # - account_holder: the name of the account holder
        # - balance: the account balance
        self.account_holder = account_holder
        self.balance = balance
    
    def display_info(self):
        # TODO: Print account information in this exact format:
        # "Account: [account_holder]"
        # "Balance: $[balance]"
        # "Interest Rate: [interest_rate]%"
        # Don't forget to multiply interest_rate by 100 for percentage display
        # Add a blank line after the information
        rate_100 = self.interest_rate * 100
        print(f"Account: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {rate_100}%")
        print("")