from flask import Flask, jsonify, request

app = Flask(__name__)

# --- GET /alunos ---


@app.get("/alunos")
def alunos():
    # Substituímos os alunos de exemplo pelos dados que você passou
    alunos_lista = [
        {"nome": "Leonardo", "email": "leonardo@ciesa.br",
            "idade": 22, "curso": "CCP"},
        {"nome": "Moanna", "email": "moanna@ciesa.br", "idade": 36, "curso": "CCP"},
        {"nome": "Dassayeff", "email": "dassa@ciesa.br", "idade": 22, "curso": "CCP"},
        {"nome": "Jhemesson", "email": "jhemesson@ciesa.br",
            "idade": 18, "curso": "CCP"}
    ]
    # Retornamos apenas a lista de alunos (para simular a Atividade 1)
    return jsonify(alunos_lista)


# --- POST /alunos ---
@app.post("/alunos")
def post_alunos():
    dados = request.get_json()
    # Esta linha chama a função de validação abaixo e retorna o que ela devolver
    return valida_aluno(dados)


# --- FUNÇÃO DE VALIDAÇÃO (Transfirmei da imagem) ---
def valida_aluno(aluno):
    motivos = []
    # Usamos o get() para evitar erro de chave se o JSON estiver incompleto
    cursos = ["CCP", "ADS", "IA", "EGC"]

    # Validação do Nome (corrigido para get() para ser seguro)
    nome = aluno.get("nome", "")
    if len(nome) < 3:
        motivos.append("Nome com menos de 3 caracteres")

    # Validação do Email
    email = aluno.get("email", "")
    if "@" not in email:
        motivos.append("Email invalido")
    # Simplifiquei a lógica para verificar o ponto após o @
    elif "." not in email.split("@")[-1]:
        motivos.append("Email invalido")

    # Validação da Idade
    idade = aluno.get("idade", 0)
    if idade < 16:
        motivos.append("Menor de 16 anos")

    # Validação do Curso
    curso = aluno.get("curso", "")
    if curso not in cursos:
        motivos.append("Curso não disponível")

    # Retorno
    if len(motivos) == 0:
        # Retorna o aluno e status 201 (Created) se estiver tudo certo
        return aluno, 201
    else:
        # Retorna a lista de motivos e status 400 (Bad Request) se houver erros
        return jsonify(motivos), 400


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
