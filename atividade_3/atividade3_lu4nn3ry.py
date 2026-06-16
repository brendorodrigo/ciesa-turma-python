class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def cadastrar_livro(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
        }


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(livro.cadastrar_livro())

    def buscar_livro_pelo_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro

        return None


biblioteca = Biblioteca()

livro1 = Livro("001", "Python para Iniciantes", "Joao Silva", 2020)
livro2 = Livro("002", "Orientacao a Objetos", "Maria Souza", 2021)
livro3 = Livro("003", "Banco de Dados", "Carlos Lima", 2022)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

print("Lista de livros:")
biblioteca.listar_livros()

isbn_busca = "002"
livro_encontrado = biblioteca.buscar_livro_pelo_isbn(isbn_busca)

if livro_encontrado:
    print("Livro encontrado:", livro_encontrado.cadastrar_livro())
else:
    print("Livro nao encontrado")
