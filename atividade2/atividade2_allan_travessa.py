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
        self.desenvolvedores = [] # Começa como uma lista vazia

    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)
        print(f"Desenvolvedor(a) {dev.nome} adicionado(a) ao projeto.")

    def calcular_capacidade_total(self):
        # Soma os pontos por dia de todos os devs do projeto
        pontos_diarios_equipe = sum(dev.pontos_por_dia for dev in self.desenvolvedores)
        # Multiplica pelo prazo de dias do projeto
        return pontos_diarios_equipe * self.prazo_em_dias

    def verificar_viabilidade(self):
        capacidade = self.calcular_capacidade_total()
        print(f"\nAnalisando viabilidade do projeto: {self.descricao}")
        print(f"Capacidade da equipe no prazo: {capacidade} pontos | Necessário: {self.pontos_de_funcao} pontos")
        
        if capacidade >= self.pontos_de_funcao:
            print("Resultado: Projeto viável!")
        else:
            print("Resultado: Projeto inviável.")

projeto_app = Projeto(descricao="App de Gestão", prazo_em_dias=10, pontos_de_funcao=80
)
dev1 = Desenvolvedor("Ana", "Sênior", 6, "Python")
dev2 = Desenvolvedor("Brendo", "Júnior", 3, "Python")
projeto_app.adicionar_desenvolvedor(dev1)
projeto_app.adicionar_desenvolvedor(dev2)
projeto_app.verificar_viabilidade()