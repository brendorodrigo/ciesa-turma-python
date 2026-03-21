class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


class Projeto:
    def __init__(self, descricao, prazo_em_dias, pontos):
        self.descricao = descricao
        self.prazo_em_dias = prazo_em_dias
        self.pontos_total = pontos
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)

    def calcular_capacidade_total(self):
        capacidade_total = 0
        for desenvolvedor in self.desenvolvedores:
            capacidade_total += desenvolvedor.pontos_por_dia * self.prazo_em_dias
        return capacidade_total

    def verificar_viabilidade(self):
        capacidade = self.calcular_capacidade_total()

        print("Descrição do Projeto:", self.descricao)
        print("Prazo em dias:", self.prazo_em_dias)
        print("Pontos necessários:", self.pontos_total)
        print("Capacidade total da equipe:", capacidade)

        if capacidade >= self.pontos_total:
            print("Projeto viável")
        else:
            print("Projeto inviável")


# Criando desenvolvedores
dev1 = Desenvolvedor("Carlos", "Senior", 10, "Python")
dev2 = Desenvolvedor("Ana", "Pleno", 7, "Java")
dev3 = Desenvolvedor("Lucas", "Junior", 4, "JavaScript")

# Criando projeto
projeto = Projeto("Sistema de Controle de Biblioteca", 10, 150)

# Adicionando desenvolvedores ao projeto
projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)
projeto.adicionar_desenvolvedor(dev3)

# Verificando viabilidade do projeto
projeto.verificar_viabilidade()