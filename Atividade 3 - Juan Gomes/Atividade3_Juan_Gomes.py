class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def cadastrar_livro(self):
        return {
            "ISBN": self.isbn,
            "Título": self.titulo,
            "Autor": self.autor,
            "Ano": self.ano
        }


class Biblioteca:
    def __init__(self):
        self.livros = []

    # Adicionar livro
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    # Listar livros
    def listar_livros(self):
        for livro in self.livros:
            print(livro.cadastrar_livro())

    # Buscar livro por ISBN
    def buscar_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro.cadastrar_livro()
        return "Livro não encontrado"