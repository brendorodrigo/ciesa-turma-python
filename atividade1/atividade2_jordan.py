class Desenvolvedor:
    def __init__(self, nome: str, senioridade: str, pontos_por_dia: float, linguagem: str):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


class Projeto:
    def __init__(self, descricao: str, prazo_em_dias: int, pontos_de_funcao: float):
        self.descricao = descricao
        self.prazo_em_dias = prazo_em_dias
        self.pontos_de_funcao = pontos_de_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, desenvolvedor: Desenvolvedor) -> None:
        self.desenvolvedores.append(desenvolvedor)

    def calcular_capacidade_total(self) -> float:
        pontos_por_dia_total = sum(dev.pontos_por_dia for dev in self.desenvolvedores)
        return pontos_por_dia_total * self.prazo_em_dias

    def verificar_viabilidade(self) -> bool:
        return self.calcular_capacidade_total() >= self.pontos_de_funcao


if __name__ == "__main__":
    projeto = Projeto("Sistema X", prazo_em_dias=10, pontos_de_funcao=80)

    projeto.adicionar_desenvolvedor(Desenvolvedor("Ana", "Pleno", 5, "Python"))
    projeto.adicionar_desenvolvedor(Desenvolvedor("Bruno", "Senior", 4, "Python"))

    capacidade = projeto.calcular_capacidade_total()
    viavel = projeto.verificar_viabilidade()

    print("Capacidade total:", capacidade)
    print("Projeto viável" if viavel else "Projeto inviável")