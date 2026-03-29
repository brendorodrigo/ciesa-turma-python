
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 20, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesa.br", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos = ["CCP", "ADS", "IA", "EGC"]


def validate_aluno(aluno: dict, cursos_disponiveis=None):
    if cursos_disponiveis is None:
        cursos_disponiveis = cursos

    motivos = []

    if not isinstance(aluno, dict):
        return ["Aluno deve ser um objeto JSON"]

    nome = aluno.get("nome")
    email = aluno.get("email")
    idade = aluno.get("idade")
    curso = aluno.get("curso")

    if not isinstance(nome, str) or len(nome.strip()) < 3:
        motivos.append("Nome com menos de 3 caracteres")

    if not isinstance(email, str) or "@" not in email:
        motivos.append("Email invalido")
    else:
        dominio = email.split("@", 1)[1]
        if "." not in dominio:
            motivos.append("Email invalido")

    if not isinstance(idade, int):
        motivos.append("Idade invalida")
    elif idade < 16:
        motivos.append("Menor de 16 anos")

    if not isinstance(curso, str) or curso not in cursos_disponiveis:
        motivos.append("Curso não disponivel")

    return motivos


def validate_alunos(lista_alunos, cursos_disponiveis=None):
    if cursos_disponiveis is None:
        cursos_disponiveis = cursos

    alunos_validos = []
    alunos_invalidos = []

    for aluno in lista_alunos:
        motivos = validate_aluno(aluno, cursos_disponiveis=cursos_disponiveis)
        if len(motivos) == 0:
            alunos_validos.append(aluno)
        else:
            alunos_invalidos.append({
                "nome": aluno.get("nome") if isinstance(aluno, dict) else None,
                "motivos": motivos,
            })

    return alunos_validos, alunos_invalidos


if __name__ == "__main__":
    validos, invalidos = validate_alunos(alunos)
    print("Alunos validos: ", validos)
    print("Alunos invalidos: ", invalidos)




    
        

