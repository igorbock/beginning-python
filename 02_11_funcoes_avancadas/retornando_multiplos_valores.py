# Crie uma função chamada get_student_info que não recebe argumentos. 
# A função deve retornar uma tupla contendo as seguintes informações sobre um aluno:

# Nome: "Bob"
# Idade: 20
# Curso: "Computer Science"
# Após definir a função, chame-a e desempacote os valores retornados em três variáveis: 
# student_name, student_age e student_major. Em seguida, imprima os valores dessas variáveis.

def get_student_info():
    name = "Bob"
    age = 20
    course = "Computer Science"
    return name, age, course

student_name, student_age, student_major = get_student_info()
print(student_name)
print(student_age)
print(student_major)