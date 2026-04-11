from flask import Flask, request, jsonify

app = Flask(__name__)

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

lista_alunos_api = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"}
]

@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(lista_alunos_api), 200


@app.route('/alunos', methods=['POST'])
def post_alunos():
    aluno = request.get_json() 
    motivos = []
    
    if len(aluno.get("nome", "")) < 3:
        motivos.append("Nome com menos de 3 caracteres")
        
    email = aluno.get("email", "")
    if "@" in email:
        partes = email.split("@")
        if len(partes) < 2 or "." not in partes[1]:
            motivos.append("Email inválido")
    else:
        motivos.append("Email inválido")
        
    if aluno.get("idade", 0) < 16:
        motivos.append("Idade menor que 16 anos")
        
    if aluno.get("curso") not in cursos_disponiveis:
        motivos.append("Curso não disponível")

    if len(motivos) == 0:
        lista_alunos_api.append(aluno)
        return jsonify({"mensagem": "Aluno matriculado com sucesso!"}), 201
    else:
        return jsonify({"erro": "Aluno inválido", "motivos": motivos}), 400

if __name__ == '__main__':
    app.run(debug=True)