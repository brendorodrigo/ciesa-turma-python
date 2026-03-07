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
        capacidade_total = self.calcular_capacidade_total()

        if capacidade_total >= self.pontos_funcao:
            print("Projeto viável")
        else:
            print("Projeto inviável")


# Criando desenvolvedores
dev1 = Desenvolvedor("Ana", "Senior", 10, "Python")
dev2 = Desenvolvedor("Carlos", "Pleno", 7, "Java")
dev3 = Desenvolvedor("Maria", "Junior", 4, "JavaScript")

# Criando projeto
projeto = Projeto("Sistema de Vendas", 10, 150)

# Adicionando desenvolvedores
projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)
projeto.adicionar_desenvolvedor(dev3)

# Verificando viabilidade
projeto.verificar_viabilidade()
