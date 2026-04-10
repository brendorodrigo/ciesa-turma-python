from flask import Flask, jsonify, request

app = Flask(__name__)

lista_alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"}
]

lista_cursos = ["CCP", "ADS", "IA", "EGC"]

def validar_aluno(aluno, cursos):
    erros = []
    
    if len(aluno["nome"]) < 3:
        erros.append("O nome deve conter pelo menos 3 caracteres")
    
    email = aluno["email"]
    if "@" not in email or "." not in email.split("@")[-1]:
        erros.append("O email deve conter um '@' e um '.' após o @")
        
    if aluno["idade"] < 16:
        erros.append("A idade deve ser maior ou igual a 16 anos")
        
    if aluno["curso"] not in cursos:
        erros.append(f"Curso '{aluno['curso']}' não está na lista de cursos disponíveis")

    return erros

@app.route("/alunos", methods=["GET"])
def get_alunos():
    return jsonify(lista_alunos), 200

@app.route("/alunos", methods=["POST"])
def create_aluno():
    novo_aluno = request.get_json()
    erros = validar_aluno(novo_aluno, lista_cursos)
    
    if erros:
        return jsonify({"erros": erros}), 400

    lista_alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

if __name__ == "__main__":
    app.run(debug=True)
