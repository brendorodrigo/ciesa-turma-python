from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista inicial de alunos
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "João", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

# Cursos disponíveis
cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


# Função de validação
def validar_aluno(aluno):
    motivos = []

    # Nome
    if len(aluno.get("nome", "")) < 3:
        motivos.append("Nome com menos de 3 caracteres")

    # Email
    email = aluno.get("email", "")
    if "@" not in email or "." not in email.split("@")[-1]:
        motivos.append("E-mail inválido")

    # Idade
    if aluno.get("idade", 0) < 16:
        motivos.append("Idade menor que 16 anos")

    # Curso
    if aluno.get("curso") not in cursos_disponiveis:
        motivos.append("Curso não disponível")

    return motivos


# GET /alunos
@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(alunos)


# POST /alunos
@app.route("/alunos", methods=["POST"])
def post_aluno():
    novo_aluno = request.json

    motivos = validar_aluno(novo_aluno)

    if not motivos:
        alunos.append(novo_aluno)
        return jsonify({
            "mensagem": "Aluno cadastrado com sucesso",
            "aluno": novo_aluno
        }), 201
    else:
        return jsonify({
            "mensagem": "Aluno inválido",
            "motivos": motivos
        }), 400


if __name__ == "__main__":
    app.run(debug=True)