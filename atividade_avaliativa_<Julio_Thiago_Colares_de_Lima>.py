from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando banco em memória
desenvolvedores = []
projetos = []

class Desenvolvedor:
    def __init__(self, id, nome, senioridade, pontos_por_dia, linguagem):
        self.id = id
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem

class Projeto:
    def __init__(self, id, descricao, prazo_dias, pontos_funcao):
        self.id = id
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)

    def calcular_capacidade_total(self):
        total = sum(dev.pontos_por_dia for dev in self.desenvolvedores)
        return total * self.prazo_dias

    def verificar_viabilidade(self):
        capacidade = self.calcular_capacidade_total()
        if capacidade >= self.pontos_funcao:
            return "Projeto viável"
        else:
            return "Projeto inviável"

@app.route("/desenvolvedores", methods=["POST"])
def cadastrar_desenvolvedor():
    data = request.json
    novo_id = len(desenvolvedores) + 1

    dev = Desenvolvedor(
        novo_id,
        data["nome"],
        data["senioridade"],
        data["pontos_por_dia"],
        data["linguagem"]
    )

    desenvolvedores.append(dev)

    return jsonify({"id": dev.id, "mensagem": "Desenvolvedor cadastrado"}), 201


@app.route("/desenvolvedores", methods=["GET"])
def listar_desenvolvedores():
    return jsonify([dev.__dict__ for dev in desenvolvedores])


@app.route("/desenvolvedores/<int:id>", methods=["GET"])
def buscar_desenvolvedor(id):
    for dev in desenvolvedores:
        if dev.id == id:
            return jsonify(dev.__dict__)
    return jsonify({"erro": "Não encontrado"}), 404

@app.route("/projetos", methods=["POST"])
def criar_projeto():
    data = request.json
    novo_id = len(projetos) + 1

    proj = Projeto(
        novo_id,
        data["descricao"],
        data["prazo_dias"],
        data["pontos_funcao"]
    )

    projetos.append(proj)

    return jsonify({"id": proj.id, "mensagem": "Projeto criado"}), 201


@app.route("/projetos", methods=["GET"])
def listar_projetos():
    return jsonify([{
        **proj.__dict__,
        "desenvolvedores": [dev.__dict__ for dev in proj.desenvolvedores]
    } for proj in projetos])


@app.route("/projetos/<int:id>", methods=["GET"])
def buscar_projeto(id):
    for proj in projetos:
        if proj.id == id:
            return jsonify({
                **proj.__dict__,
                "desenvolvedores": [dev.__dict__ for dev in proj.desenvolvedores]
            })
    return jsonify({"erro": "Não encontrado"}), 404


@app.route("/projetos/<int:id>/desenvolvedores", methods=["POST"])
def adicionar_dev_projeto(id):
    data = request.json

    proj = next((p for p in projetos if p.id == id), None)
    dev = next((d for d in desenvolvedores if d.id == data["desenvolvedor_id"]), None)

    if not proj or not dev:
        return jsonify({"erro": "Projeto ou desenvolvedor não encontrado"}), 404

    proj.adicionar_desenvolvedor(dev)

    return jsonify({"mensagem": "Desenvolvedor adicionado ao projeto"})


@app.route("/projetos/<int:id>/desenvolvedores", methods=["GET"])
def listar_devs_projeto(id):
    proj = next((p for p in projetos if p.id == id), None)

    if not proj:
        return jsonify({"erro": "Projeto não encontrado"}), 404

    return jsonify([dev.__dict__ for dev in proj.desenvolvedores])


@app.route("/projetos/<int:id>/viabilidade", methods=["GET"])
def verificar_viabilidade(id):
    proj = next((p for p in projetos if p.id == id), None)

    if not proj:
        return jsonify({"erro": "Projeto não encontrado"}), 404

    return jsonify({
        "capacidade_total": proj.calcular_capacidade_total(),
        "pontos_funcao": proj.pontos_funcao,
        "resultado": proj.verificar_viabilidade()
    })


if __name__ == "__main__":
    app.run(debug=True)
