# Atividade 1 - Validação de Alunos - Vinicius Antony Silva Pereira
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
    {"nome": "Vinicius", "email": "viniciusPereira@ciesa.br", "idade": 20, "curso": "CCP"}
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


def validar_alunos(lista_alunos, cursos):
    alunos_validos = []
    alunos_invalidos = []
    
    for aluno in lista_alunos:
        motivos = []
        
        
        if len(aluno["nome"]) < 3:
            motivos.append("Nome com menos de 3 caracteres")
        
        
        if "@" not in aluno["email"] or "." not in aluno["email"].split("@")[1]:
            motivos.append("Email inválido")
        
        
        if aluno["idade"] < 16:
            motivos.append("Idade menor que 16 anos")
        
        
        if aluno["curso"] not in cursos:
            motivos.append("Curso não disponível")
        
        
        if not motivos:
            alunos_validos.append(aluno)
        else:
            alunos_invalidos.append({
                "nome": aluno["nome"],
                "motivos": motivos
            })
    
    return alunos_validos, alunos_invalidos



alunos_validos, alunos_invalidos = validar_alunos(alunos, cursos_disponiveis)


print("Alunos válidos:")
print(alunos_validos)
print("\nAlunos inválidos:")
print(alunos_invalidos)
