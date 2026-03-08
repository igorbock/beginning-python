# Crie uma função chamada clean_email_list que recebe uma lista de endereços de email e 
# retorna uma lista de endereços de email válidos e padronizados.

# Requisitos:
#     - Converta todos os emails para minúsculas e remova todos os espaços em branco no início ou no fim
#     - Mantenha apenas emails que:
#         - Contenham exatamente um símbolo '@'
#         - Tenham pelo menos um caractere antes do '@'
#         - Tenham pelo menos um caractere após o ‘@’

# Use map() e filter() para resolver o problema.

def clean_email_list(emails):
    # Write your code below
    minusculas = map(lambda x: x.lower().strip(), emails)
    valid_emails = filter(lambda x: x.count("@") == 1 and len(x.split("@")[0]) > 0 and len(x.split("@")[1]), minusculas)
    return list(valid_emails)

print(clean_email_list(['Test@EXAMPLE.com', 'invalid.email',  'user@domain@.com', '  space@email.com  ', ' valid@domain.com']))
print(clean_email_list(['user1@domain.com', ' user2@domain.com']))
print(clean_email_list(['@nodomain.com', ' noat', ' multiple@@ats.com']))
print(clean_email_list([]))
print(clean_email_list(['USER@DOMAIN.COM', '  space@domain.com ',  'NoSpaces@domain.com']))