class Livro:

    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def cadastrar_livro(self):
        print("Livro cadastrado:")
        print("ISBN:", self.isbn)
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Ano:", self.ano)


class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("\nLista de livros:")
        for livro in self.livros:
            print(livro.isbn, "-", livro.titulo, "-", livro.autor, "-", livro.ano)

    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                print("\nLivro encontrado:")
                print(livro.isbn, "-", livro.titulo, "-", livro.autor, "-", livro.ano)
                return
        print("\nLivro não encontrado")


# Criando vários livros
livro1 = Livro("111", "Python Básico", "João Silva", 2020)
livro2 = Livro("222", "Banco de Dados", "Maria Souza", 2019)
livro3 = Livro("333", "Algoritmos", "Carlos Lima", 2021)

# Criando biblioteca
biblioteca = Biblioteca()

# Adicionando livros na biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros
biblioteca.listar_livros()

# Testando busca por ISBN
biblioteca.buscar_livro("222")
