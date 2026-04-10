# Lista de alunos
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

# Lista de cursos disponíveis
cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


def validar_alunos(lista_alunos):
    alunos_validos = []
    alunos_invalidos = []

    for aluno in lista_alunos:
        motivos = []

        # Validação do nome
        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")

        # Validação do email
        email = aluno["email"]
        if "@" not in email or "." not in email.split("@")[-1]:
            motivos.append("Email inválido")

        # Validação da idade
        if aluno["idade"] < 16:
            motivos.append("Idade menor que 16 anos")

        # Validação do curso
        if aluno["curso"] not in cursos_disponiveis:
            motivos.append("Curso não disponível")

        # Separação entre válidos e inválidos
        if len(motivos) == 0:
            alunos_validos.append(aluno)
        else:
            alunos_invalidos.append({
                "nome": aluno["nome"],
                "motivos": motivos
            })

    return alunos_validos, alunos_invalidos


# Executando a função
validos, invalidos = validar_alunos(alunos)

print("alunos validos:", validos)
print("alunos invalidos:", invalidos)