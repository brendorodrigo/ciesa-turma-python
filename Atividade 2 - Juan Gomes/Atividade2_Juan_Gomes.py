class Desenvolvedor:
    def __init__(self, nome, antiguidade, pontos_por_dia, linguagem):
        self.nome = nome
        self.antiguidade = antiguidade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


class Projeto:
    def __init__(self, descricao, prazo_dias, pontos_funcao):
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []

    # Adicionar desenvolvedor
    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)

    # Calcular capacidade total do time
    def capacidade_total(self):
        total = 0
        for dev in self.desenvolvedores:
            total += dev.pontos_por_dia * self.prazo_dias
        return total

    # Verificar viabilidade do projeto
    def verificar_viabilidade(self):
        capacidade = self.capacidade_total()

        print(f"Capacidade total do time: {capacidade}")
        print(f"Pontos de função do projeto: {self.pontos_funcao}")

        if capacidade >= self.pontos_funcao:
            print("Projeto viável ")
        else:
            print("Projeto inviável ")