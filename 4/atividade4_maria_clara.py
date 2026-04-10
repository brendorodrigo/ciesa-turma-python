from flask import Flask, jsonify, request

app = Flask(__name__)

class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def to_dict(self):
        return {"isbn": self.isbn, "titulo": self.titulo, "autor": self.autor, "ano": self.ano}

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)


minha_biblioteca = Biblioteca()



@app.route('/livros', methods=['GET'])
def listar_livros():
    
    lista_json = [livro.to_dict() for livro in minha_biblioteca.livros]
    return jsonify(lista_json), 200

@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    dados = request.get_json()

    
    if not all(k in dados for k in ("isbn", "titulo", "autor", "ano")):
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    
    novo_livro = Livro(dados['isbn'], dados['titulo'], dados['autor'], dados['ano'])
    minha_biblioteca.adicionar_livro(novo_livro)

    return jsonify({"mensagem": "Livro cadastrado com sucesso!", "livro": novo_livro.to_dict()}), 201

@app.route('/livros/<string:isbn>', methods=['GET'])
def buscar_livro(isbn):
    for livro in minha_biblioteca.livros:
        if livro.isbn == isbn:
            return jsonify(livro.to_dict()), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)