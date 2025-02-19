class Aluno:
    def __init__(self):
        self.nome = str
        self.matricula = int
        self.curso = str

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.curso}"

i = 1
alunos = list()
try:
    while i < 6:
        novoAluno = Aluno()
        novoAluno.nome = input(f"Digite o nome do {i}º aluno: ")
        novoAluno.matricula = int(input(f"Digite a matrícula do {i}º aluno: "))
        novoAluno.curso = input(f"Digite o curso do {i}º aluno: ")
        alunos.append(novoAluno)
        i += 1
except Exception as erro:
    print(f"Um erro aconteceu: {erro}")

for aluno in alunos:
    print(aluno)
