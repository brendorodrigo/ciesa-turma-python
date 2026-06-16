from flask import Flask, jsonify, request


app = Flask(__name__)

alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


def email_valido(email):
    if "@" not in email:
        return False

    partes_email = email.split("@")
    dominio = partes_email[1]

    return "." in dominio


def validar_aluno(aluno):
    motivos = []
    idade = aluno.get("idade", 0)

    if not isinstance(idade, int) or idade < 16:
        motivos.append("Idade menor que 16 anos")

    if aluno.get("curso") not in cursos_disponiveis:
        motivos.append("Curso nao disponivel")

    if len(aluno.get("nome", "")) < 3:
        motivos.append("Nome com menos de 3 caracteres")

    if not email_valido(aluno.get("email", "")):
        motivos.append("Email invalido")

    return motivos


@app.get("/alunos")
def listar_alunos():
    return jsonify(alunos)


@app.post("/alunos")
def cadastrar_aluno():
    aluno = request.get_json() or {}
    motivos = validar_aluno(aluno)

    if len(motivos) > 0:
        return jsonify({"aluno": aluno.get("nome"), "motivos": motivos}), 400

    alunos.append(aluno)
    return jsonify(aluno), 201


if __name__ == "__main__":
    app.run(debug=True)
