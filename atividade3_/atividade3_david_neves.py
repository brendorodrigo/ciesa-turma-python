class Livro:
    def __init__ (self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


    def Cadastro_Livros(self):
        print(f"O titulo do livro:{self.titulo}")
        print(f"O autor do livro: {self.autor}")
        print(f"O ano do livro:{self.ano}")
        print(f"O isbn (ID) do livro {self.isbn}\n")

class Biblioteca:
    def __init__ (self):
        self.Livros = []

    def Adicionar_Livros(self, Livro):
        self.Livros.append(Livro)

    def Listar_Livros(self):
        for Livro in self.Livros:
            Livro.Cadastro_Livros()
    
    def Buscar_Livros_isbn(self, isbn):
        encontrado = False
        
        for livro in self.Livros:
            if livro.isbn == isbn:
                livro.Cadastro_Livros()
                encontrado = True
        if not encontrado:
            print("Não encontrado")

livro1 = Livro (1010,"O grande Lionel", "Lionel", "1990")
livro2 = Livro (2020, "Miri ar", "Tema", "1930")
livro3 = Livro (3030, "The demon", "Lana", "2015")

Biblioteca = Biblioteca()
Biblioteca.Adicionar_Livros(livro1)
Biblioteca.Adicionar_Livros(livro2)
Biblioteca.Adicionar_Livros(livro3)

Biblioteca.Listar_Livros()
Biblioteca.Buscar_Livros_isbn(2020)