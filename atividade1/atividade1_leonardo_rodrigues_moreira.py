# Aluno: Leonardo Rodrigues Moreira

# Atividade 1 - Validação e Invalidação de Alunos
# Lista de alunos

# 1. Dados
alunos = [
    {"nome": "Leonardo", "email": "leonardo.rodmor@ciesa.br",
        "idade": 22, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesa.br", "idade": 12,
        "curso": "DIR"},  # Corrigi o email para ter o ponto
    {"nome": "Moanna", "email": "moanna@ciesa.br", "idade": 18, "curso": "ADS"},
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

# 2. A função de validação


def validar_alunos(lista_alunos, cursos):
    validos = []
    invalidos = []

    for aluno in lista_alunos:
        motivos = []

        # Critério: Nome (mínimo 3 caracteres)
        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")

        # Critério: Email (precisa de @ e .)
        if "@" not in aluno["email"] or "." not in aluno["email"]:
            motivos.append("Email inválido")

        # Critério: Idade (mínimo 16)
        if aluno["idade"] < 16:
            motivos.append("Idade menor que 16 anos")

        # Critério: Curso disponível
        if aluno["curso"] not in cursos:
            motivos.append("Curso não disponível")

        # Se não houve erros, vai para a lista de válidos
        if len(motivos) == 0:
            validos.append(aluno)
        else:
            # Caso contrário, vai para a de inválidos com os motivos
            invalidos.append({"nome": aluno["nome"], "motivos": motivos})

    return validos, invalidos


# 3. Execução
alunos_validos, alunos_invalidos = validar_alunos(alunos, cursos_disponiveis)

print("Alunos Válidos:", alunos_validos)
print("\nAlunos Inválidos:", alunos_invalidos)
