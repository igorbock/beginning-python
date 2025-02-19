class Horario :
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def __str__(self):
        return f"{self.hora}:{self.minuto}:{self.segundo}"

class Data :
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

class Agenda :
    def __init__(self):
        self.data = Data
        self.horario = Horario
        self.compromisso = None

    def __str__(self):
        return f"{self.data} - {self.horario} // {self.compromisso}"
    

nova_data = Data(18, "02", 2025)
novo_horario = Horario(23, 10, 55)
agenda = Agenda()
agenda.data = nova_data
agenda.horario = novo_horario
agenda.compromisso = "Seu novo comprimisso da noite"

print(agenda)