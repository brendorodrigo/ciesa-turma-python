
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 20, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesa.br", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos = ["CCP", "ADS", "IA", "EGC"]

alunos_validos = []
alunos_invalidos = []


def check(alunos):
    for aluno in alunos:
        motivos =[]

        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")

        if "@" not in aluno["email"]:
            motivos.append("Email invalido")
        elif "." not in aluno["email"].split("@")[1]:
            motivos.append("Email invalido")

        if aluno["idade"] < 16:
            motivos.append("Menor de 16 anos")

        if aluno["curso"] not in cursos:
            motivos.append("Curso não disponivel")

        if len(motivos) == 0:
            alunos_validos.append(aluno)
        
        else:
            alunos_invalidos.append({
                "nome": aluno["nome"],
                "motivos": motivos
            })

    return alunos_validos, alunos_invalidos

validos, invalidos = check(alunos)
print("Alunos validos: ", alunos_validos)
print("Alunos invalidos: ", alunos_invalidos)




    
        

