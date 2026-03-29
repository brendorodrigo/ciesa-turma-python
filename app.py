from flask import Flask, jsonify, request

from atividade1.atividade1_jordan_ import alunos, validate_aluno


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/alunos")
    def get_alunos():
        # Retorna a lista de alunos definida na atividade 1
        return jsonify(alunos)

    @app.post("/alunos")
    def post_alunos():
        payload = request.get_json(silent=True)
        if payload is None:
            return jsonify({"error": "Corpo JSON ausente ou invalido"}), 400

        motivos = validate_aluno(payload)
        if motivos:
            return jsonify({"valido": False, "motivos": motivos}), 400

        return jsonify({"valido": True, "aluno": payload}), 201

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
