from typing import List, Optional


class Livro:
	def __init__(self, isbn: str, titulo: str, autor: str, ano: int):
		self.isbn = isbn
		self.titulo = titulo
		self.autor = autor
		self.ano = ano

	@classmethod
	def cadastrar_livro(cls, isbn: str, titulo: str, autor: str, ano: int) -> "Livro":
		return cls(isbn=isbn, titulo=titulo, autor=autor, ano=ano)


class Biblioteca:
	def __init__(self):
		self.livros: List[Livro] = []

	def adicionar_livro(self, livro: Livro) -> None:
		self.livros.append(livro)

	def listar_livros(self) -> None:
		if not self.livros:
			print("Nenhum livro cadastrado.")
			return

		for livro in self.livros:
			print(f"ISBN: {livro.isbn} | Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano}")

	def buscar_livro_pelo_isbn(self, isbn: str) -> Optional[Livro]:
		for livro in self.livros:
			if livro.isbn == isbn:
				return livro
		return None


if __name__ == "__main__":
	biblioteca = Biblioteca()

	livro_1 = Livro.cadastrar_livro("978-85-333-0227-3", "Dom Casmurro", "Machado de Assis", 1899)
	livro_2 = Livro.cadastrar_livro("978-85-359-0277-4", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
	livro_3 = Livro.cadastrar_livro("978-85-359-1488-3", "Capitães da Areia", "Jorge Amado", 1937)

	biblioteca.adicionar_livro(livro_1)
	biblioteca.adicionar_livro(livro_2)
	biblioteca.adicionar_livro(livro_3)

	print("\nLista de livros:")
	biblioteca.listar_livros()

	print("\nBusca por ISBN:")
	isbn_para_buscar = "978-85-359-0277-4"
	encontrado = biblioteca.buscar_livro_pelo_isbn(isbn_para_buscar)

	if encontrado is None:
		print("Livro não encontrado.")
	else:
		print(f"Encontrado: {encontrado.titulo} ({encontrado.ano}) - {encontrado.autor}")
