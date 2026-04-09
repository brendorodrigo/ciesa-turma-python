#Atividade 2 - Andrey Dantas

class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


class Projeto:
    def __init__(self, descricao, prazo_dias, pontos_funcao):
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)
        print("Desenvolvedor adicionado:", desenvolvedor.nome)

    def calcular_capacidade_total(self):
        total = 0
        for dev in self.desenvolvedores:
            total = total + (dev.pontos_por_dia * self.prazo_dias)
        return total

    def verificar_viabilidade(self):
        capacidade = self.calcular_capacidade_total()
        if capacidade >= self.pontos_funcao:
            print("projeto viável!")
        else:
            print("projeto inviável!")


projeto = Projeto("Sistema de Controle", 15, 500)

dev1 = Desenvolvedor("Carlos", "Pleno", 20, "Python")
dev2 = Desenvolvedor("Ana", "Senior", 30, "Java")
dev3 = Desenvolvedor("Lucas", "Junior", 10, "JavaScript")

projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)
projeto.adicionar_desenvolvedor(dev3)

projeto.verificar_viabilidade()
