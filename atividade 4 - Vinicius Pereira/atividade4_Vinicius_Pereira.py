# Atividade 4 - API de Validação de Alunos - Vinicius Antony Silva Pereira

from flask import Flask, request, jsonify

alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
    {"nome": "Vinicius", "email": "viniciusPereira@ciesa.br", "idade": 20, "curso": "CCP"}
]

cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

app = Flask(__name__)

def validar_aluno(aluno, cursos):
    
    motivos = []

    if len(aluno.get("nome", "")) < 3:
        motivos.append("Nome com menos de 3 caracteres")

    email = aluno.get("email", "")
    if "@" not in email or "." not in email.split("@")[1]:
        motivos.append("Email inválido")

    idade = aluno.get("idade", 0)
    if idade < 16:
        motivos.append("Idade menor que 16 anos")

    curso = aluno.get("curso", "")
    if curso not in cursos:
        motivos.append("Curso não disponível")

    if not motivos:
        return {
            "valido": True,
            "mensagem": "Aluno válido",
            "aluno": aluno
        }
    else:
        return {
            "valido": False,
            "mensagem": "Aluno inválido",
            "motivos": motivos,
            "aluno": aluno
        }

@app.route('/alunos', methods=['GET'])
def get_alunos():

    return jsonify({
        "status": "success",
        "data": alunos,
        "total": len(alunos)
    })

@app.route('/alunos', methods=['POST'])
def post_aluno():
    
    try:
        aluno_data = request.get_json()

        if not aluno_data:
            return jsonify({
                "status": "error",
                "message": "Dados do aluno não fornecidos"
            }), 400

        resultado = validar_aluno(aluno_data, cursos_disponiveis)

        return jsonify({
            "status": "success",
            "data": resultado
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro ao processar requisição: {str(e)}"
        }), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": "API de Validação de Alunos - Atividade 4",
        "endpoints": {
            "GET /alunos": "Retorna lista de alunos",
            "POST /alunos": "Valida um aluno (envie JSON com nome, email, idade, curso)"
        },
        "cursos_disponiveis": cursos_disponiveis
    })

if __name__ == '__main__':
    print("Iniciando API Flask - Atividade 4")
    print("Acesse: http://localhost:5000")
    print("GET / - Informações sobre a API")
    print("GET /alunos - Lista de alunos")
    print("POST /alunos - Validar aluno")
    app.run(debug=True, host='0.0.0.0', port=5000)
