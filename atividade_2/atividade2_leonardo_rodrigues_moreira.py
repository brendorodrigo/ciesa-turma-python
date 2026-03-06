class Projeto:
    def __init__(self, descricao, prazo_em_dias, pontos):
        self.descricao = descricao
        self.prazo_em_dias = prazo_em_dias
        self.pontos_total = pontos
        self.desenvolvedores = []

    def _adicionar_desenvolvedor(self, desenvolvedor):
        self.desenvolvedores.append(desenvolvedor)

    def _calcular_capacidade_total_desenvolvedores_por_dia(self):
        capacidade_pontos = 0
        for desenvolvedor in self.desenvolvedores:
            capacidade_pontos = capacidade_pontos + desenvolvedor.pontos_por_dia

        return capacidade_pontos

    def verificar_viabilidade(self):
        if (self._calcular_capacidade_total_desenvolvedores_por_dia()
                >= self.pontos_total / self.prazo_em_dias):
            return "Projeto viável"
        else:
            return "Projeto não viável"


class Desenvolvedor:
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


if __name__ == "__main__":
    projeto = Projeto(descricao="Projeto de teste",
                      prazo_em_dias=10, pontos=100)
    desenvolvedor1 = Desenvolvedor(
        nome="Leonardo", senioridade="Sênior", pontos_por_dia=15, linguagem="Python")
    desenvolvedor2 = Desenvolvedor(
        nome="Maria", senioridade="Pleno", pontos_por_dia=10, linguagem="Java")
    desenvolvedor3 = Desenvolvedor(
        nome="João", senioridade="Júnior", pontos_por_dia=5, linguagem="COBOL")

    projeto._adicionar_desenvolvedor(desenvolvedor1)
    projeto._adicionar_desenvolvedor(desenvolvedor2)
    projeto._adicionar_desenvolvedor(desenvolvedor3)

    print(projeto.verificar_viabilidade())
