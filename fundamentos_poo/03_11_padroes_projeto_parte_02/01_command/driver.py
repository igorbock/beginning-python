# Neste desafio, você implementará a classe base fundamental Command em command.py — o bloco de construção essencial do Command Pattern. 
# Este exercício foca especificamente no encapsulamento: armazenar dados de forma privada e expô-los de forma segura através de uma propriedade.

# Modifique apenas o arquivo command.py de acordo com os comentários TODO. Os comentários TODO guiarão você para:

# Armazenar o nome do comando como um atributo privado (_name)
# Expô-lo através de uma propriedade somente leitura (name)
# Implementar um método display_info() que imprime o nome do comando
# Nota: Este desafio cobre apenas a classe base Command — o Invoker, o Receiver e a funcionalidade de desfazer (undo) são introduzidos em lições posteriores. 
# Concluir esta etapa fornece a base de encapsulamento sobre a qual o padrão completo é construído.

# Sua implementação será testada pelo driver.py, que valida:

# Funcionalidade básica e formato de saída
# Casos de borda (entradas vazias, caracteres especiais, nomes longos)
# Proteção de propriedade somente leitura (tentar obj.name = ... deve gerar um AttributeError)
# Presença do atributo privado _name

# Import the Command class from command.py
from command import Command

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    obj = Command("Test Name")
    obj.display_info()
elif test_case == "validation_test":
    obj = Command("Validation Test")
    print(f"Name: {obj.name}")
elif test_case == "empty_name_test":
    obj = Command("")
    obj.display_info()
    print(f"Empty name handled: {'Yes' if obj.name == '' else 'No'}")
elif test_case == "property_access_test":
    obj = Command("Property Test")
    original_name = obj.name
    try:
        # This should fail since name is a read-only property
        obj.name = "Modified Name"
        print("Property protection failed")
    except AttributeError:
        print("Property protected successfully")
    print(f"Name unchanged: {obj.name == original_name}")
elif test_case == "multiple_commands_test":
    commands = [
        Command("First Command"),
        Command("Second Command"),
        Command("Third Command")
    ]
    for cmd in commands:
        cmd.display_info()
elif test_case == "attribute_test":
    obj = Command("Attribute Test")
    has_private_name = hasattr(obj, "_name")
    print(f"Has _name attribute: {has_private_name}")
elif test_case == "special_chars_test":
    obj = Command("!@#$%^&*()_+{}[]|\\:;\"'<>,.?/")
    obj.display_info()
elif test_case == "long_name_test":
    long_name = "A" * 100
    obj = Command(long_name)
    obj.display_info()
    print(f"Name length: {len(obj.name)}")