# Crie uma função chamada organize_contacts que processa uma lista de dicionários de contatos para criar um banco de dados
# de contatos limpo.

# Cada dicionário de contato na lista de entrada possui estas chaves:

# name: O nome da pessoa
# email: O endereço de e-mail da pessoa
# phone: O número de telefone da pessoa
# Sua função deve:

# Remover contatos duplicados (contatos com o mesmo e-mail ou número de telefone)
# Padronizar todos os e-mails para minúsculas
# Filtrar contatos com endereços de e-mail inválidos
# Filtrar contatos com números de telefone inválidos
# Retornar uma lista de dicionários de contatos limpos
# Regras de validação:

# E-mail válido: Deve conter '@' e '.', e não deve ter espaços
# Telefone válido: Deve conter exatamente 10 dígitos (ignore caracteres não numéricos como hifens ou parênteses)
# Para limpar números de telefone, você deve usar o método str.isdigit() do Python para extrair apenas os dígitos 
# numéricos dos números de telefone. Este método retorna True se um caractere for um dígito (0-9) e False caso contrário, 
# tornando-o perfeito para filtrar caracteres não numéricos.

# Entrada de Exemplo:
# contacts = [
#     {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"}
# ]
# Saída Esperada:
# [
#     {"name": "John Doe", "email": "john@email.com", "phone": "1234567890"}
# ]

def organize_contacts(contact_list):
    # Your solution here
    
    for item in contact_list:
        valid_emails = filter(lambda x: x["email"].count("@") == 1 and len(x["email"].split("@")[0]) > 0 and len(x["email"].split("@")[1] and x["email"].split("@")[1].count(".") == 1), item)
        item["email"] = map(lambda x: x.lower().trim(), valid_emails)
    # 1. Create helper functions for validation
    # - Function to validate email format
    
    # - Function to clean and validate phone numbers
    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    
    # 3. Return the clean contact list
    pass

print(organize_contacts([{"name": "John Doe", "email": "JOHN@email.com", "phone": "123-456-7890"}, {"name": "Jane Doe", "email": "jane@email.com", "phone": "123.456.7890"}, {"name": "Bob Smith", "email": "invalid.email", "phone": "12345"}]))