# Atividade 3 - Biblioteca - Vinicius Antony Silva Pereira

class Livro:
    
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def cadastrar_livro(self):
        dados_livro = {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano
        }
        print(f"Livro '{self.titulo}' cadastrado com sucesso!")
        return dados_livro
    
    def __str__(self):
        return f"ISBN: {self.isbn} | Título: {self.titulo} | Autor: {self.autor} | Ano: {self.ano}"


class Biblioteca:
    
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca '{self.nome}'!")
    
    def listar_livros(self):
        if not self.livros:
            print(f"A biblioteca '{self.nome}' não possui livros cadastrados.")
            return []
        
        print(f"LIVROS DA BIBLIOTECA '{self.nome.upper()}'")
        for i, livro in enumerate(self.livros, 1):
            print(f"{i}. {livro}")
        print(f"Total de livros: {len(self.livros)}")
        return self.livros
    
    def buscar_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        
        print(f"Livro com ISBN '{isbn}' não encontrado na biblioteca '{self.nome}'.")
        return None
    
    def exibir_detalhes_livro(self, livro):
        if livro:
            print("DETALHES DO LIVRO")
            print(f"ISBN: {livro.isbn}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano}")
biblioteca = Biblioteca("Biblioteca Central")

livro1 = Livro("978-3-16-148410-0", "Python para Iniciantes", "João Silva", 2020)
livro2 = Livro("978-0-12-345678-9", "Algoritmos e Estruturas de Dados", "Maria Santos", 2019)
livro3 = Livro("978-1-23-456789-0", "Programação Orientada a Objetos", "Pedro Oliveira", 2021)
livro4 = Livro("978-2-34-567890-1", "Banco de Dados SQL", "Ana Costa", 2018)
livro5 = Livro("978-3-45-678901-2", "Machine Learning Básico", "Carlos Pereira", 2022)


print("CADASTRANDO LIVROS:")
livro1.cadastrar_livro()
livro2.cadastrar_livro()
livro3.cadastrar_livro()
livro4.cadastrar_livro()
livro5.cadastrar_livro()


print(f"\nADICIONANDO LIVROS À BIBLIOTECA:")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)
biblioteca.adicionar_livro(livro5)


biblioteca.listar_livros()

isbn_busca1 = "978-3-16-148410-0"
livro_encontrado1 = biblioteca.buscar_livro_por_isbn(isbn_busca1)
if livro_encontrado1:
    biblioteca.exibir_detalhes_livro(livro_encontrado1)

isbn_busca2 = "978-2-34-567890-1"
livro_encontrado2 = biblioteca.buscar_livro_por_isbn(isbn_busca2)
if livro_encontrado2:
    biblioteca.exibir_detalhes_livro(livro_encontrado2)

isbn_busca3 = "999-9-99-999999-9"
livro_encontrado3 = biblioteca.buscar_livro_por_isbn(isbn_busca3)
if livro_encontrado3:
    biblioteca.exibir_detalhes_livro(livro_encontrado3)
