# Dados iniciais
alunos = [
  {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
  {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
  {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
  {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]
cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]
def validar_alunos(lista_alunos, cursos):
    validos = []
    invalidos = []
    for aluno in lista_alunos:
        motivos = []
        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")
        partes_email = aluno["email"].split("@")
        if len(partes_email) != 2 or "." not in partes_email[1]:
            motivos.append("Email inválido")
        if aluno["idade"] < 16:
            motivos.append("Idade menor que 16 anos")
        if aluno["curso"] not in cursos:
            motivos.append("Curso não disponível")
        if len(motivos) > 0:
            invalidos.append({"nome": aluno["nome"], "motivos": motivos})
        else:
            validos.append(aluno)

    return validos, invalidos
alunos_validos, alunos_invalidos = validar_alunos(alunos, cursos_disponiveis)
print("alunos validos:", alunos_validos)
print("alunos invalidos:", alunos_invalidos)