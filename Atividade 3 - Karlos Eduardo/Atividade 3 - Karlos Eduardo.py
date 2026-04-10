class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.isbn}, {self.titulo}, {self.autor}, {self.ano}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def add_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("nenhum livro cadastrado")
            return

        else:
            for livro in self.livros:
                print(f"{livro.isbn}, {livro.titulo}, {livro.autor}, {livro.ano}")

    def buscar_livro(self, isbn):
        for livro in self.livros:
            if isbn in livro.isbn:
                print(f"O livro de isbn: {isbn} e {livro.titulo}")


livro1 = Livro("111", "Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("222", "1984", "George Orwell", 1949)
livro3 = Livro("333", "O Hobbit", "J.R.R. Tolkien", 1937)

biblioteca = Biblioteca()

biblioteca.add_livro(livro1)
biblioteca.add_livro(livro2)
biblioteca.add_livro(livro3)

biblioteca.listar_livros()


biblioteca.buscar_livro("111")