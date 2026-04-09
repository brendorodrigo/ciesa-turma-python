from flask import Flask, request, jsonify

app = Flask(__name__)

alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 20, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesa.br", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

cursos = ["CCP", "ADS", "IA", "EGC"]


@app.route("/alunos", methods=["GET"])
def listar():
    return jsonify(alunos)


@app.route("/alunos", methods=["POST"])
def adicionar():
    aluno = request.get_json()
    erros = []

    if len(aluno["nome"]) < 3:
        erros.append("nome errado")

    if "@" not in aluno["email"] or "." not in aluno["email"]:
        erros.append("email errado")

    if aluno["idade"] < 16:
        erros.append("idade menor")

    if aluno["curso"] not in cursos:
        erros.append("curso errado")

    if len(erros) == 0:
        alunos.append(aluno)
        return jsonify({"msg": "ok"})
    else:
        return jsonify({"erros": erros})


if __name__ == "__main__":
    app.run(debug=True)
