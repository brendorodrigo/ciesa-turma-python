# Atividade 2 - Gestão de Desenvolvedores - Vinicius Antony Silva Pereira
class Desenvolvedor:
    
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem
    
    def __str__(self):
        return f"{self.nome} ({self.senioridade}) - {self.linguagem} - {self.pontos_por_dia} pts/dia"


class Projeto:
       
    def __init__(self, descricao, prazo_dias, pontos_funcao):
   
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []
    
    def adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)
        print(f"Desenvolvedor {desenvolvedor.nome} adicionado ao projeto!")
    
    def calcular_capacidade_total(self):
        if not self.desenvolvedores:
            return 0
        
        capacidade_total = sum(dev.pontos_por_dia for dev in self.desenvolvedores)
        return capacidade_total
    
    def calcular_pontos_disponiveis(self):
        capacidade_total = self.calcular_capacidade_total()
        pontos_disponiveis = capacidade_total * self.prazo_dias
        return pontos_disponiveis
    
    def verificar_viabilidade(self):
        if not self.desenvolvedores:
            return {
                "viavel": False,
                "mensagem": "Projeto inviável: sem desenvolvedores alocados",
                "pontos_necessarios": self.pontos_funcao,
                "pontos_disponiveis": 0,
                "diferenca": self.pontos_funcao
            }
        
        capacidade_total = self.calcular_capacidade_total()
        pontos_disponiveis = self.calcular_pontos_disponiveis()
        diferenca = pontos_disponiveis - self.pontos_funcao
        
        if pontos_disponiveis >= self.pontos_funcao:
            return {
                "viavel": True,
                "mensagem": "Projeto viável!",
                "pontos_necessarios": self.pontos_funcao,
                "pontos_disponiveis": pontos_disponiveis,
                "diferenca": diferenca,
                "capacidade_diaria": capacidade_total
            }
        else:
            return {
                "viavel": False,
                "mensagem": "Projeto inviável!",
                "pontos_necessarios": self.pontos_funcao,
                "pontos_disponiveis": pontos_disponiveis,
                "diferenca": diferenca,
                "capacidade_diaria": capacidade_total
            }
    
    def exibir_detalhes(self):
        print(f"PROJETO: {self.descricao}")
        print(f"Prazo: {self.prazo_dias} dias")
        print(f"Pontos de Função: {self.pontos_funcao}")
        print(f"\nDEsenvolvedores ({len(self.desenvolvedores)}):")
        for dev in self.desenvolvedores:
            print(f"  - {dev}")
        print(f"\nCapacidade Total: {self.calcular_capacidade_total()} pontos/dia")
        print(f"Pontos Disponíveis: {self.calcular_pontos_disponiveis()} pontos")
dev1 = Desenvolvedor("Alice", "Senior", 10, "Python")
dev2 = Desenvolvedor("Antony", "Pleno", 8, "JavaScript")
dev3 = Desenvolvedor("Vinicius", "Junior", 1, "Python")


projeto1 = Projeto("Sistema de Gestão de Vendas", 30, 300)


projeto1.adicionar_desenvolvedor(dev1)
projeto1.adicionar_desenvolvedor(dev2)
projeto1.adicionar_desenvolvedor(dev3)


projeto1.exibir_detalhes()


resultado_viabilidade = projeto1.verificar_viabilidade()
print("RESULTADO DA VIABILIDADE:")
print(f"Status: {resultado_viabilidade['mensagem']}")
print(f"Pontos Necessários: {resultado_viabilidade['pontos_necessarios']}")
print(f"Pontos Disponíveis: {resultado_viabilidade['pontos_disponiveis']}")
print(f"Diferença: {resultado_viabilidade['diferenca']}")


print("SEGUNDO EXEMPLO - PROJETO INVIÁVEL")

projeto2 = Projeto("App Mobile Complexo", 10, 500)
projeto2.adicionar_desenvolvedor(dev3)

projeto2.exibir_detalhes()

resultado_viabilidade2 = projeto2.verificar_viabilidade()
print("RESULTADO DA VIABILIDADE:")
print(f"Status: {resultado_viabilidade2['mensagem']}")
print(f"Pontos Necessários: {resultado_viabilidade2['pontos_necessarios']}")
print(f"Pontos Disponíveis: {resultado_viabilidade2['pontos_disponiveis']}")
print(f"Diferença: {resultado_viabilidade2['diferenca']}")
