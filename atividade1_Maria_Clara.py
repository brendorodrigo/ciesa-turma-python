alunos = [
  {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
  {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
  {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
  {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos = ["CCP", "ADS", "IA", "EGC"]


def  dadosalunos(alunos, cursos):
  validos = []
  invalidos = []

  for aluno in alunos:
    motivos = []
    email = aluno["email"]
    arroba = email.split("@")

    if len(aluno["nome"]) < 3:
      motivos.append("Nome muito curto")

    if len(arroba) != 2 or "." not in arroba[1]:
      motivos.append("Email invalido")

    if aluno["curso"] not in cursos:
      motivos.append("Curso invalido")

    if aluno["idade"] <= 16:
      motivos.append("Menor de idade")

    if not motivos:
        validos.append(aluno)
    else:
        invalidos.append({"aluno": aluno, "motivos": motivos})

  return validos, invalidos

val, inv = dadosalunos(alunos, cursos)
print(" VÁLIDOS ")
for nome in val:
  print(f"{nome}")

print(" INVALIDOS ")
for item in inv:
  nomealuno = item["aluno"]["nome"]
  erros = ", ".join(item["motivos"])
  print(f"{nomealuno}: {erros}")

#entrega finalizada Clara
