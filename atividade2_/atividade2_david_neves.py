class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem

class Projeto:
    def __init__(self, descricao, prazo_dias, pontos):
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos = pontos
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)

    def calcular_capacidade_total(self):
        total = 0
        for dev in self.desenvolvedores:
            total = total + dev.pontos_por_dia * self.prazo_dias 
        return total

    def verificar_viabilidade(self):
        if self.calcular_capacidade_total() >= self.pontos:
            print("Projeto VIÁVEL")
        else:
            print("Projeto INVIÁVEL")

dev1 = Desenvolvedor("Deivid", "Junior", 8, "Python")
dev2 = Desenvolvedor("Leticia", "Pleno", 50, "Python")

projeto = Projeto("Sistema de vendas", 15, 300)

projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)

projeto.verificar_viabilidade()

