#Atividade 01 - Aula 02
#Carlos Johnatan Silva Souza Rodrigues

#Lista de Alunos
alunos = [
  {"nome": "Alexandre", "email": "jaocatao@exemplo.com", "idade": 20, "curso": "CCP"},
  {"nome": "Daniel", "email": "dani_el13@exemplo.com", "idade": 20, "curso": "ADS"},
  {"nome": "Julio", "email": "juliothiago2006@exemplo", "idade": 21, "curso": "DIR"},
  {"nome": "Jhemesson", "email": "condejms1@ex.br", "idade": 15, "curso": "ADS"},
]

#Lista de Cursos
cursos = ["CCP", "ADS", "IA", "EGC"]

#Função para validar atributos
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

#Validação de Alunos Válidos e Inválidos
validos, invalidos = validar_alunos(alunos)

#Laço para mostrar os alunos de forma visível e organizada:
print("\nAlunos Válidos\n")

for aluno in validos:
    print(f"    Nome: {aluno['nome']}")
    print(f"    Email: {aluno['email']}")
    print(f"    Idade: {aluno['idade']}")
    print(f"    Curso: {aluno['curso']}\n")

print("Alunos Inválidos:\n")

for item in invalidos:
    aluno = item["aluno"]
    erros = item["erros"]

    print(f"    Nome: {aluno['nome']}")
    print(f"    Email: {aluno['email']}")
    print(f"    Idade: {aluno['idade']}")
    print(f"    Curso: {aluno['curso']}")
    print("    Erros:", ", ".join(erros))
    print("")
