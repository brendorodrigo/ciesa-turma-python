class Desenvolvedor:
    def __init__(self, nome, antiguidade, pontos_por_dia, linguagem):
        self.nome = nome
        self.antiguidade = antiguidade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem

    def __repr__(self):
        return f"{self.nome} ({self.linguagem})"


class Projeto:
    def __init__(self, descricao, prazo_dias, pontos_funcao):
        self.descricao = descricao
        self.prazo_dias = prazo_dias
        self.pontos_funcao = pontos_funcao
        self.desenvolvedores = []

    def adicionar_desenvolvedor(self, dev):
        self.desenvolvedores.append(dev)

    def capacidade_total(self):
        return sum(dev.pontos_por_dia for dev in self.desenvolvedores) * self.prazo_dias

    def verificar_viabilidade(self):
        capacidade = self.capacidade_total()
        if capacidade >= self.pontos_funcao:
            return f"Projeto '{self.descricao}' é viável (Capacidade: {capacidade}, Necessário: {self.pontos_funcao})"
        else:
            return f"Projeto '{self.descricao}' é inviável (Capacidade: {capacidade}, Necessário: {self.pontos_funcao})"


if __name__ == "__main__":
    # Criando desenvolvedores
    dev1 = Desenvolvedor("Brendo", 5, 10, "Python")
    dev2 = Desenvolvedor("Eva", 2, 8, "Java")

    # Criando projeto
    projeto = Projeto("Sistema de Controle", prazo_dias=30, pontos_funcao=250)

    # Adicionando desenvolvedores
    projeto.adicionar_desenvolvedor(dev1)
    projeto.adicionar_desenvolvedor(dev2)

    # Validando projeto
    print(projeto.verificar_viabilidade())
