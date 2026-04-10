from flask import Flask, jsonify, request

app = Flask(__name__)


cursos_permitidos = ["CCP", "ADS", "IA", "EGC"]
alunos_validos = []

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos_validos), 200


@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    aluno = request.get_json()
    motivos = []
    
  
    nome = aluno.get("nome", "")
    email = aluno.get("email", "")
    idade = aluno.get("idade", 0)
    curso = aluno.get("curso", "")
    
    arroba = email.split("@")

    if len(nome) < 3:
        motivos.append("Nome muito curto")

    if len(arroba) != 2 or "." not in arroba[1]:
        motivos.append("Email invalido")

    if curso not in cursos_permitidos:
        motivos.append("Curso invalido")

    if idade <= 16:
        motivos.append("Menor de idade")

    if not motivos:
        alunos_validos.append(aluno)
        return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "aluno": aluno}), 201
    else:
        return jsonify({"status": "Erro de validação", "motivos": motivos}), 400

if __name__ == '__main__':
    app.run(debug=True)


