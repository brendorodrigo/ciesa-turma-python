def validacao(a):
    validados = []
    invalidos = []
    for pos in a:
        erros = []
        if len(pos["nome"]) < 3:
            erros.append("Nome invalido")
        if "@" not in pos["email"]:
            erros.append("Email invalido")
        if pos["idade"] < 16:
            erros.append("Idade invalida")
        if erros:
            invalidos.append({"aluno": pos, "erros": erros})
        else:
            validados.append(pos)
    return validados, invalidos

aluno1 = {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"}
aluno2 = {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"}
aluno3 = {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"}
aluno4 = {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"}
list1 = [aluno1, aluno2, aluno3, aluno4]
cursos = ["CCP", "ADS", "IA", "EGC"]

validados, invalidos = validacao(list1)
print("Alunos validados:")
for val in validados:
    print(f"\t-{val["nome"]}, {val["email"]}, {val["idade"]}, {val["curso"]}")
print("Alunos invalidos")
for val in invalidos:
    print(f"\t-{val["aluno"]["nome"]}, {val["aluno"]["email"]}, {val["aluno"]["idade"]}, {val["aluno"]["curso"]}. Erros: {val["erros"]}")