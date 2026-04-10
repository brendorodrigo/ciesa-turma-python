class Desenvolvedor:
    def __init__(self, nome, senirioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senirioridade = senirioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem

class Projeto:
    def __init__(self, descricao, prazo, pontos):
        self.descricao = descricao
        self.prazo = prazo
        self.pontos = pontos
        self.desenvolvedores = []

    def add_dev(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)

    def capacidade_total(self):
        capacidade_total = 0
        for dev in self.desenvolvedores:
            capacidade_total += capacidade_total + dev.pontos_por_dia * self.prazo
        return capacidade_total

    def viabilidade(self):
        capacidade = self.capacidade_total()
        if capacidade >= self.pontos:
            return "Viavel"
        else:
            id = False
            return "Inviavel"

    def __str__(self):
        return f"O projeto é {self.viabilidade()}"

dev1 = Desenvolvedor("Carlos", "Senior", 3, "Python")
dev2 = Desenvolvedor("Ana", "Pleno", 1, "Java")
dev3 = Desenvolvedor("Lucas", "Junior", 1, "JavaScript")

projeto = Projeto("Sistema de Controle de Biblioteca", 10, 150)

projeto.add_dev(dev1)
projeto.add_dev(dev2)
projeto.add_dev(dev3)

print(projeto)