class Projeto:
    def __init__ (self, descricao, prazo, pontos):
        self.descricao = descricao
        self.prazo = prazo
        self.pontos = pontos
        self.desenvolvedores = []
    
    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)

    def capacidade_total(self):
        capacidade_dia = sum(dev.pontos for dev in self.desenvolvedores)
        return capacidade_dia * self.prazo
    
    def verificar_viabilidade(self):
        capacidade = self.capacidade_total()

        if (capacidade >= self.pontos):
            print ("Projeto Viável")
        else:
            print ("Projeto Inviável")
    
class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos = pontos
        self.linguagem = linguagem

dev1 = Desenvolvedor("João", "Pleno", 5, "Python")
dev2 = Desenvolvedor("Eva", "Sênior", 8, "Java")
projeto = Projeto("Sistema de Biblioteca", 10, 100)
projeto.adicionar_desenvolvedor(dev1)
projeto.adicionar_desenvolvedor(dev2)
projeto.verificar_viabilidade()
