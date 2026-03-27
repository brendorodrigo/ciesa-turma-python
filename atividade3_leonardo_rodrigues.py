class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"ISBN: {self.isbn} | Título: {self.titulo} | Autor: {self.autor} ({self.ano})"


class Biblioteca:
    def __init__(self):
        self.livros = []  # Array (lista) de livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def listar_livros(self):
        print("\n--- Catálogo da Biblioteca ---")
        if not self.livros:
            print("A biblioteca está vazia.")
        for livro in self.livros:
            print(livro)

    def buscar_por_isbn(self, isbn_busca):
        for livro in self.livros:
            if livro.isbn == isbn_busca:
                return livro
        return None


# Criando a instância da Biblioteca
minha_biblioteca = Biblioteca()

# Criando vários livros
livro1 = Livro("978-1", "Algoritmos e Estruturas de Dados", "Guimarães", 2021)
livro2 = Livro("978-2", "Clean Code", "Robert C. Martin", 2008)
livro3 = Livro("978-3", "Banco de Dados Relacional", "Navathe", 2011)

# Adicionando-os na biblioteca
minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)

# Listando todos para conferir
minha_biblioteca.listar_livros()

# Testando o método de busca
print("\n--- Teste de Busca ---")
isbn_para_testar = "978-2"
resultado = minha_biblioteca.buscar_por_isbn(isbn_para_testar)

if resultado:
    print(f"Resultado da busca para ISBN {isbn_para_testar}:")
    print(f"-> {resultado.titulo} ({resultado.autor})")
else:
    print(f"Livro com ISBN {isbn_para_testar} não encontrado.")