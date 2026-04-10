class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"ISBN: {self.isbn} | Título: {self.titulo} ({self.ano}) - Autor: {self.autor}"


class Biblioteca:
    def __init__(self):
        
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def listar_livros(self):
        print("\n--- Catálogo da Biblioteca ---")
        if not self.livros:
            print("A biblioteca está vazia.")
        for livro in self.livros:
            print(livro)

    def buscar_por_isbn(self, isbn_procurado):
        for livro in self.livros:
            if livro.isbn == isbn_procurado:
                return livro
        return None
    
minha_biblioteca = Biblioteca()

l1 = Livro("978-8535914849", "1984", "George Orwell", 1949)
l2 = Livro("978-8572329286", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
l3 = Livro("978-8532511010", "Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

minha_biblioteca.adicionar_livro(l1)
minha_biblioteca.adicionar_livro(l2)
minha_biblioteca.adicionar_livro(l3)


minha_biblioteca.listar_livros()

print("\n--- Teste de Busca ---")
isbn_busca = "978-8535914849"
resultado = minha_biblioteca.buscar_por_isbn(isbn_busca)

if resultado:
    print(f"Resultado da busca para ISBN {isbn_busca}:")
    print(f"Livro encontrado: {resultado.titulo} de {resultado.autor}")
else:
    print("Livro não encontrado.")