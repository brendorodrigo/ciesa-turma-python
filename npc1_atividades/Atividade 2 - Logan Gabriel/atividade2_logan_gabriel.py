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

    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)

    def calcular_capacidade_total(self):
        capacidade_diaria = sum(dev.pontos_por_dia for dev in self.desenvolvedores)
        return capacidade_diaria * self.prazo_dias

    def verificar_viabilidade(self):
        if self.calcular_capacidade_total() >= self.pontos_funcao:
            return "projeto viável"
        else:
            return "projeto inviável"

projeto_api = Projeto("API de Vendas", prazo_dias=10, pontos_funcao=100)

dev1 = Desenvolvedor("Logan", "Junior", 4, "Python")
dev2 = Desenvolvedor("Brendo", "Sênior", 8, "Python")
projeto_api.adicionar_desenvolvedor(dev1)
projeto_api.adicionar_desenvolvedor(dev2)

print(projeto_api.verificar_viabilidade()) 