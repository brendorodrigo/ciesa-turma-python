class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def cadastrar_livro(self):
        print("livro cadastrado:")
        print(self.isbn, self.titulo, self.autor, self.ano)


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("lista de livros:")
        for livro in self.livros:
            print(livro.isbn, "-", livro.titulo)

    def buscar_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None


livro1 = Livro("111", "python basico", "joao", 2020)
livro2 = Livro("222", "aprendendo c", "maria", 2019)
livro3 = Livro("333", "logica", "carlos", 2018)

bib = Biblioteca()

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
bib.adicionar_livro(livro3)

bib.listar_livros()

isbn_busca = "222"
resultado = bib.buscar_por_isbn(isbn_busca)

if resultado:
    print("livro encontrado:")
    print(resultado.titulo, "-", resultado.autor)
else:
    print("livro nao encontrado")
