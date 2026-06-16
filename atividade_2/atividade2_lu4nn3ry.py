class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


class Projeto:
    def __init__(self, descricao, prazo_em_dias, pontos_de_funcao):
        self.descricao = descricao
        self.prazo_em_dias = prazo_em_dias
        self.pontos_de_funcao = pontos_de_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)

    def calcular_capacidade_total(self):
        capacidade_total = 0

        for desenvolvedor in self.desenvolvedores:
            capacidade_total += desenvolvedor.pontos_por_dia

        return capacidade_total * self.prazo_em_dias

    def verificar_viabilidade(self):
        capacidade_total = self.calcular_capacidade_total()

        if capacidade_total >= self.pontos_de_funcao:
            return "projeto viavel"

        return "projeto inviavel"


projeto = Projeto("Sistema de controle de projetos", 10, 120)

desenvolvedor1 = Desenvolvedor("Luann", "Junior", 5, "Python")
desenvolvedor2 = Desenvolvedor("Joao", "Pleno", 8, "Python")
desenvolvedor3 = Desenvolvedor("Maria", "Senior", 10, "JavaScript")

projeto.adicionar_desenvolvedor(desenvolvedor1)
projeto.adicionar_desenvolvedor(desenvolvedor2)
projeto.adicionar_desenvolvedor(desenvolvedor3)

print("Projeto:", projeto.descricao)
print("Prazo em dias:", projeto.prazo_em_dias)
print("Pontos de funcao:", projeto.pontos_de_funcao)
print("Capacidade total:", projeto.calcular_capacidade_total())
print("Viabilidade:", projeto.verificar_viabilidade())
