alunos = [
  {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
  {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
  {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
  {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos = ["CCP", "ADS", "IA", "EGC"]

def validar_alunos(lista):
    validos = []
    invalidos = []

    for aluno in lista:
        erros = []

        if len(aluno["nome"]) < 3:
            erros.append("Nome inválido")

        if "@" not in aluno["email"] or "." not in aluno["email"]:
            erros.append("Email inválido")

        if aluno["idade"] < 16:
            erros.append("Idade inválida")

        if aluno["curso"] not in cursos:
            erros.append("Curso inválido")

        if erros:
            invalidos.append({"aluno": aluno, "erros": erros})
        else:
            validos.append(aluno)

    return validos, invalidos


validos, invalidos = validar_alunos(alunos)

print("Válidos:", validos)
print("Inválidos:", invalidos)
