# Você recebe arquivos Python (book.py e driver.py) para implementar um sistema de gerenciamento de livros. 
# Neste desafio, você definirá uma classe Book em um arquivo que será importada e usada em outro.

# Sua tarefa é:

# Complete a classe Book em book.py com um método __init__ que inicializa os atributos title, author e pages
# O arquivo driver.py importará e usará sua classe Book para criar um objeto de livro 
# para "Harry Potter" by "J.K. Rowling" with 400 pages
# Siga os comentários TODO detalhados em book.py

class Book:
    # TODO: Add the __init__ method that takes title, author, and pages parameters
    # TODO: Initialize the title, author, and pages attributes using self
    # Example: self.title = title
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    