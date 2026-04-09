class Livro:
    def __init__ (self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def buscar_livro(self, isbn):
        for livro in self.livros:
          if (livro.isbn == isbn):
            return livro.titulo
    
    def listar_livros(self):
        for livro in self.livros:
            print (f"{livro.titulo} - {livro.autor}")

b = Biblioteca()
l1 = Livro("001", "Python Básico", "João Silva", 2022)
l2 = Livro("002", "Flask Avançado", "Maria Souza", 2024)
b.adicionar_livro(l1)
b.adicionar_livro(l2)
b.listar_livros()
print (f"{b.buscar_livro("002")}")
