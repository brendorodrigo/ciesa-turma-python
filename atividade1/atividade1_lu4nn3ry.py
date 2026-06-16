alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


def email_valido(email):
    if "@" not in email:
        return False

    partes_email = email.split("@")
    dominio = partes_email[1]

    return "." in dominio


def validar_alunos(lista_alunos):
    alunos_validos = []
    alunos_invalidos = []

    for aluno in lista_alunos:
        motivos = []

        if aluno["idade"] < 16:
            motivos.append("Idade menor que 16 anos")

        if aluno["curso"] not in cursos_disponiveis:
            motivos.append("Curso nao disponivel")

        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")

        if not email_valido(aluno["email"]):
            motivos.append("Email invalido")

        if len(motivos) == 0:
            alunos_validos.append(aluno)
        else:
            alunos_invalidos.append({"nome": aluno["nome"], "motivos": motivos})

    return alunos_validos, alunos_invalidos


validos, invalidos = validar_alunos(alunos)

print("alunos validos:", validos)
print("alunos invalidos:", invalidos)
