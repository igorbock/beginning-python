# Neste desafio, você implementará um sistema bancário. Você criará uma classe BankAccount em um arquivo e a 
# usará em outro arquivo, demonstrando como organizar seu código para melhor manutenibilidade.

# Você precisa trabalhar com dois arquivos:

# bank_account.py: Onde você definirá sua classe BankAccount
# driver.py: Onde você importará a classe, criará uma conta e realizará transações
# Crie uma classe BankAccount em bank_account.py com:

# Um atributo de classe bank_name definido como "Python National Bank"
# Um método deposit que recebe um valor e o adiciona ao saldo da conta
# Um método withdraw que recebe um valor e o subtrai do saldo
# Um método get_balance que retorna o saldo atual
# Em seguida, em driver.py, importe sua classe BankAccount, crie uma conta, deposite $100, saque $30 e imprima 
# o saldo com o formato: f"Current balance: ${my_account.get_balance()}"

class BankAccount:
    # TODO: Add class attribute here
    bank_name = "Python National Bank"
    balance = 0
    
    # TODO: Add the methods here
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
