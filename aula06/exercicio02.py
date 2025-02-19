class Pessoa :
    def __init__(self):
        self.nome = str
        self.idade = int
        self.endereco = str

    def __str__(self):
        return f"{self.nome} - {self.idade} anos // {self.endereco}"
    
pessoa = Pessoa()
try:
    pessoa.nome = input("Digite o nome: ")
    pessoa.idade = int(input("Digite a idade: "))
    pessoa.endereco = input("Digite o endereço: ")

    print(pessoa)
except Exception as erro:
    print(f"Um erro aconteceu: {erro}")
