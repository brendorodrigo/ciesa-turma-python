alunos = [
  {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
  {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
  {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
  {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"}
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

def validar_alunos(lista_alunos):
    validos = []
    invalidos = []

    for aluno in lista_alunos:
        motivos = []
        
        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")
            
        email = aluno["email"]
        if "@" in email:
            partes = email.split("@")
            if "." not in partes[1]:
                motivos.append("Email inválido")
        else:
            motivos.append("Email inválido")
            
        if aluno["idade"] < 16:
            motivos.append("Idade menor que 16 anos")
            
        if aluno["curso"] not in cursos_disponiveis:
            motivos.append("Curso não disponível")

        if len(motivos) == 0:
            validos.append(aluno)
        else:
            invalidos.append({"nome": aluno["nome"], "motivos": motivos})

    return validos, invalidos

v, inv = validar_alunos(alunos)
print("alunos validos:", v)
print("alunos invalidos:", inv)