def validar_aluno(alunos, cursos):
    alunos_validos = []
    alunos_invalidos = []

    for aluno in alunos:
        erros = []
        
        if len(aluno["nome"]) < 3:
            erros.append("O nome deve conter pelo menos 3 caracteres")
        
        email = aluno["email"]
        if "@" not in email or "." not in email.split("@")[-1]:
            erros.append("O email deve conter um '@' e um '.' após o @")
            
        if aluno["idade"] < 16:
            erros.append("A idade deve ser maior ou igual a 16 anos")
            
        if aluno["curso"] not in cursos:
            erros.append(f"Curso '{aluno['curso']}' não está na lista de cursos disponíveis")

        if not erros:
            alunos_validos.append(aluno)
        else:
            alunos_invalidos.append({
                "nome": aluno["nome"],
                "motivos": erros
            })

    return {"validos": alunos_validos, "invalidos": alunos_invalidos}

lista_alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"}
]

lista_cursos = ["CCP", "ADS", "IA", "EGC"]

resultado = validar_aluno(lista_alunos, lista_cursos)

print("--- ALUNOS VÁLIDOS ---")
for v in resultado["validos"]:
    print(v)

print("\n--- ALUNOS INVÁLIDOS ---")
for inv in resultado["invalidos"]:
    print(inv)
