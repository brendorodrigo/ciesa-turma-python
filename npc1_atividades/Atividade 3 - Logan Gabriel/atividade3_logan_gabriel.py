class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livros(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"ISBN: {livro.isbn} - Titulo: {livro.titulo}")

    def buscar_livros_pelo_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro 
        return None 

b = Biblioteca()
livro1 = Livro("123", "Harry Potter", "J.K", 1997)
livro2 = Livro("456", "Senhor dos Anéis", "Tolkien", 1954)

b.adicionar_livros(livro1)
b.adicionar_livros(livro2)

resultado = b.buscar_livros_pelo_isbn("123")
if resultado:
    print("Achamos:", resultado.titulo)