class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome 
        self.senioridade = senioridade
        self.pontos_por_dias = pontos_por_dia
        self.linguagem = linguagem

class Projeto:
    def __init__(self, descricao, prazo_em_dias, pontos_funcao):
        self.desenvolvedores = []
        self.descricao = descricao
        self.prazo_em_dias = prazo_em_dias
        self.pontos_funcao = pontos_funcao

    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)
    
    def calcular_capacidade_total(self):
        capacidade_pontos = 0
        for desenvolvedor in self.desenvolvedores:
            capacidade_pontos = capacidade_pontos + desenvolvedor.pontos_por_dias
        return capacidade_pontos
    
    def verificar_viabilidade(self):
        if self.calcular_capacidade_total()<self.pontos_funcao / self.prazo_em_dias:
            return "Projeto Inviável"
        return "Projeto viável"

if __name__=="__main__":
    projeto = Projeto(descricao="Projeto teste", prazo_em_dias = 10, pontos_funcao = 100)
    dev1 = Desenvolvedor(nome="Lia", senioridade="Sênior", pontos_por_dia=15, linguagem="Python")
    dev2 = Desenvolvedor(nome="Momo", senioridade="Especialista", pontos_por_dia=100, linguagem="Python")
    projeto.adicionar_desenvolvedor(dev1)
    projeto.adicionar_desenvolvedor(dev2)
  
    print(f"Capacidade Total do Time: {projeto.calcular_capacidade_total()} pts/dia")
    print(f"Status Final: {projeto.verificar_viabilidade()}")
    
      



