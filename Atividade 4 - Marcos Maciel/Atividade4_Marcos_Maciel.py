from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de alunos (dados iniciais)
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

# Lista de cursos disponíveis
cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


def validar_aluno(aluno):
    """
    Valida um aluno de acordo com as regras da atividade 1.
    Retorna: (is_valid: bool, motivos: list)
    """
    motivos = []

    # Validação do nome
    if "nome" not in aluno or not isinstance(aluno["nome"], str):
        motivos.append("Campo 'nome' obrigatório e deve ser string")
    elif len(aluno["nome"]) < 3:
        motivos.append("Nome com menos de 3 caracteres")

    # Validação do email
    if "email" not in aluno or not isinstance(aluno["email"], str):
        motivos.append("Campo 'email' obrigatório e deve ser string")
    else:
        email = aluno["email"]
        if "@" not in email or "." not in email.split("@")[-1]:
            motivos.append("Email inválido")

    # Validação da idade
    if "idade" not in aluno or not isinstance(aluno["idade"], int):
        motivos.append("Campo 'idade' obrigatório e deve ser número inteiro")
    elif aluno["idade"] < 16:
        motivos.append("Idade menor que 16 anos")

    # Validação do curso
    if "curso" not in aluno or not isinstance(aluno["curso"], str):
        motivos.append("Campo 'curso' obrigatório e deve ser string")
    elif aluno["curso"] not in cursos_disponiveis:
        motivos.append(f"Curso não disponível. Cursos válidos: {', '.join(cursos_disponiveis)}")

    return len(motivos) == 0, motivos


@app.route("/alunos", methods=["GET"])
def listar_alunos():
    """
    GET /alunos
    Retorna a lista de alunos válidos de acordo com as regras da atividade 1
    """
    alunos_validos = []
    alunos_invalidos = []

    for aluno in alunos:
        is_valid, motivos = validar_aluno(aluno)
        if is_valid:
            alunos_validos.append(aluno)
        else:
            alunos_invalidos.append({
                "nome": aluno.get("nome", "N/A"),
                "motivos": motivos
            })

    return jsonify({
        "total": len(alunos),
        "validos": len(alunos_validos),
        "invalidos": len(alunos_invalidos),
        "alunos_validos": alunos_validos,
        "alunos_invalidos": alunos_invalidos
    }), 200


@app.route("/alunos", methods=["POST"])
def criar_aluno():
    """
    POST /alunos
    Recebe um objeto de Aluno e valida de acordo com as regras da atividade 1
    Retorna erro se inválido, ou o aluno adicionado se válido
    """
    # Verifica se o corpo da requisição é JSON
    if not request.is_json:
        return jsonify({
            "erro": "Corpo da requisição deve ser JSON"
        }), 400

    novo_aluno = request.get_json()

    # Valida o aluno
    is_valid, motivos = validar_aluno(novo_aluno)

    if not is_valid:
        return jsonify({
            "erro": "Aluno inválido",
            "motivos": motivos
        }), 400

    # Adiciona o aluno à lista
    alunos.append(novo_aluno)

    return jsonify({
        "mensagem": "Aluno adicionado com sucesso",
        "aluno": novo_aluno
    }), 201


@app.route("/health", methods=["GET"])
def health():
    """Endpoint de health check"""
    return jsonify({
        "status": "API funcionando",
        "total_alunos": len(alunos)
    }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
