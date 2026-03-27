# Neste desafio, você implementará um sistema demonstrando duck typing com diferentes objetos semelhantes a arquivos:

# textfile.py: Implemente a classe TextFile com os métodos read() e write(data)
# database.py: Implemente a classe Database com assinaturas de métodos correspondentes
# networkresource.py: Implemente a classe NetworkResource com assinaturas de métodos correspondentes
# driver.py - Implemente casos de teste que verificarão se sua implementação funciona corretamente
# Cada arquivo contém comentários TODO detalhados que guiam sua implementação.

# TODO: Import the TextFile class from textfile.py
# TODO: Import the Database class from database.py
# TODO: Import the NetworkResource class from networkresource.py
from textfile import TextFile
from database import Database
from networkresource import NetworkResource

def process_data(data_source, data):
    # TODO: Call the read() method on data_source and print the result
    # TODO: Call the write(data) method on data_source and print the result
    print(data_source.read())
    print(data_source.write(data))


# Test with different data sources - DO NOT MODIFY THIS TEST CODE
text_file = TextFile()
database = Database()
network = NetworkResource()

print("Processing text file:")
process_data(text_file, "Hello, world!")

print("\
Processing database:")
process_data(database, "User record")

print("\
Processing network resource:")
process_data(network, "GET request")