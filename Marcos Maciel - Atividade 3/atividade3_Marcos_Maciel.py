class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def cadastrar_livro(self):
        print("Livro cadastrado:")
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print("----------------------")


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("Lista de livros:")
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} ({livro.ano}) | ISBN: {livro.isbn}")

    def buscar_livro_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                print("Livro encontrado:")
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Ano: {livro.ano}")
                return
        print("Livro não encontrado.")


# Criando vários livros
livro1 = Livro("111", "Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("222", "1984", "George Orwell", 1949)
livro3 = Livro("333", "O Hobbit", "J.R.R. Tolkien", 1937)

# Criando biblioteca
biblioteca = Biblioteca()

# Adicionando livros na biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listar livros
biblioteca.listar_livros()

print("\nBuscando livro pelo ISBN:")
biblioteca.buscar_livro_isbn("222")