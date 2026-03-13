def transform_dataset(data):
    # Inicializando os dicionários para alunos qualificados e resumo de disciplinas
    qualified_students = {}
    subject_summary = {}

    # Iterando sobre cada registro de aluno
    for record in data:
        student_id = record["student_id"]
        grades = record["grades"]
        subjects = record["subjects"]

        # Verificando se todas as notas estão acima de 70
        if all(grade > 70 for grade in grades):
            # Calculando a média de notas
            average_grade = round(sum(grades) / len(grades), 2)
            qualified_students[student_id] = average_grade
            
            # Atualizando o resumo de disciplinas
            for subject in subjects:
                if subject in subject_summary:
                    subject_summary[subject] += 1
                else:
                    subject_summary[subject] = 1

    # Retornando o dicionário final
    return {
        'qualified_students': qualified_students,
        'subject_summary': subject_summary
    }


# Exemplo de uso
data = [{"student_id": "S123", "grades": [88, 92, 85], "subjects": ["Math", "Science", "History"]}, {"student_id": "S124", "grades": [65, 95, 80], "subjects": ["Math", "Science", "English"]}, {"student_id": "S125", "grades": [91, 89, 92], "subjects": ["Math", "Physics", "History"]}]

result = transform_dataset(data)
print(result)