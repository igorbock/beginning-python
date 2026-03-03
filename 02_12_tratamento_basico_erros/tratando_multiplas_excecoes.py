# Crie uma função chamada process_data que:

# Recebe uma entrada de string representando dados potenciais
# Tenta convertê-la para um inteiro, depois calcula 100 dividido por esse inteiro
# Retorna o resultado
# Lida com pelo menos 3 exceções possíveis: 
# ValueError se a entrada não puder ser convertida para um inteiro (imprima "Input must be a number!")
# ZeroDivisionError se a entrada for 0 (imprima "Cannot divide by zero!")
# Qualquer outra exceção com um manipulador genérico (imprima "An unexpected error occurred!")

def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        integer = int(input_string)
        # Calculate 100 divided by the input value
        result = 100 / integer
        # Return the result
        return result        
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        print("Input must be a number!")
    except ZeroDivisionError:
        # Handle the case where input is zero
        print("Cannot divide by zero!")
    except:
        # Handle any other unexpected exceptions
        print("An unexpected error occurred!")
    return None

print(process_data(input()))