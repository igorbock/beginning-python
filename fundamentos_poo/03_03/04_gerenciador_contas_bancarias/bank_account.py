# Crie uma classe BankAccount completa que demonstre conceitos de programação orientada a objetos, incluindo variáveis 
# de classe, atributos privados, propriedades, getters, setters e métodos. 

# 1. Crie uma classe BankAccount com:
# Uma variável de classe interest_rate definida como 0.02 (2%)
# Atributos de instância privados para __owner_name e __balance
# Um construtor que inicializa esses atributos
# 2. Implemente getters e setters de propriedades: 
# Uma propriedade somente leitura owner_name que retorna o nome do proprietário da conta
# Uma propriedade balance com:
# Um getter que retorna o saldo atual
# Um setter que valida depósitos (rejeitando valores negativos)
# Se a validação falhar, imprima: "Balance cannot be negative"
# 3. Implemente métodos:
# deposit(amount) que:
# Adiciona ao saldo se o valor for positivo
# Imprime "Deposit amount must be positive" e retorna False se o valor não for positivo
# Retorna True em caso de sucesso
# withdraw(amount) que:
# Subtrai do saldo se o valor for positivo e os fundos forem suficientes
# Imprime "Withdrawal amount must be positive" e retorna False se o valor não for positivo
# Imprime "Insufficient funds" e retorna False se o valor exceder o saldo
# Retorna True em caso de sucesso
# apply_interest() que:
# Adiciona juros ao saldo com base na taxa de juros da classe
# Retorna o valor dos juros
# display_info() que imprime os detalhes da conta neste formato:

# Account Owner: [owner_name]
# Balance: $[balance]
# Interest Rate: [interest_rate]%
# Requisitos de Formato de Saída
# Todas as mensagens de erro de validação devem ser impressas exatamente como especificado
# O método display_info() deve formatar a saída exatamente como mostrado acima
# A taxa de juros deve ser exibida como porcentagem (multiplique por 100)

class BankAccount:
    # TODO: Define class variable for interest rate (2% = 0.02)
    interest_rate = 0.02
    
    def __init__(self, owner_name, initial_balance):
        """Initialize a new bank account.
        
        Args:
            owner_name (str): Name of the account owner
            initial_balance (float): Starting balance for the account
        
        TODO:
        - Store owner_name as private attribute (__owner_name)
        - Validate that initial_balance is not negative
        - If negative, raise ValueError with message "Initial balance cannot be negative"
        - Store initial_balance as private attribute (__balance)
        """
        self.__owner_name = owner_name
        if  initial_balance >= 0:
            self.__balance = initial_balance
        else:
            raise ValueError("Initial balance cannot be negative")
    
    @property
    def owner_name(self):
        """Get the account owner's name.
        
        TODO: Return the private __owner_name attribute
        """
        return self.__owner_name
    
    @property
    def balance(self):
        """Get the current account balance.
        
        TODO: Return the private __balance attribute
        """
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """Set the account balance with validation.
        
        Args:
            value (float): New balance value
        
        TODO:
        - Check if value is negative
        - If negative, print exactly: "Balance cannot be negative"
        - If negative, return without setting the balance
        - Otherwise, set __balance to the new value
        """
        if value < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = value
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if successful, False if failed
        
        TODO:
        - Check if amount is <= 0
        - If invalid, print exactly: "Deposit amount must be positive"
        - If invalid, return False
        - Otherwise, add amount to __balance and return True
        """
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        else:
            self.__balance += amount
            return True
    
    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if successful, False if failed
        
        TODO:
        - Check if amount is <= 0
        - If invalid, print exactly: "Withdrawal amount must be positive"
        - If invalid, return False
        - Check if amount > current balance
        - If insufficient funds, print exactly: "Insufficient funds"
        - If insufficient funds, return False
        - Otherwise, subtract amount from __balance and return True
        """
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        else:
            self.__balance -= amount
            return True
    
    def apply_interest(self):
        """Apply interest to the current balance.
        
        Returns:
            float: The interest amount that was added
        
        TODO:
        - Calculate interest: __balance * interest_rate
        - Add the interest to __balance
        - Return the interest amount
        """
        interest_amount = self.__balance * self.interest_rate
        self.__balance += interest_amount
        return interest_amount
    
    def display_info(self):
        """Display account information.
        
        TODO: Print the following format exactly:
        Account Owner: {owner_name}
        Balance: ${balance}
        Interest Rate: {interest_rate_as_percentage}%
        
        Example output:
        Account Owner: John Doe
        Balance: $1000.0
        Interest Rate: 2.0%
        """
        print(f"Account Owner: {self.__owner_name}")
        print(f"Balance: ${self.__balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")