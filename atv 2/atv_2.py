''' detalhe importante antes de olhar o codigo, eu usei o copilot nos metodos, por preguiça de escrever e comentei por cima '''

class Projeto:

''' esta eh a classe onde a entidade objto ira trabaiar'''

    def __init__(self, descriçao, prazos, pontos_de_funçao, desenvolvedores):
        self. descriçao = descriçao
        self.prazos = prazos
        self.pontos_de_funçao = pontos_de_funçao
        self.desenvolvedores = desenvolvedores

'''a funçao def projetos aqui esta usando os argumnentos prazos, pontos e desenvolvedores para se tornarem instancias
 a serem usadas no restante do programa'''

    def adicionar_desenvolvedor(self, desenvolvedores):
        self.desenvolvedores.append(desenvolvedores) ''' essa instancia vai adicionar o desenvolvedor para desempenhar essas funçoes, quem esta fazendo esta apliçao eh o append'''

    def calcular_capacidade_total(self):
        capacidade_total = 0 ''' colocar em zero para n bugar com o 1'''
        for desenvolvedor in self.desenvolvedores: ''' aqui o metodo esta chamando a variavel desenvolvedor
        na sua instancia para aplicar na variavel abaixo. 
        esta em uma laço for para poder ser repetida varias vezes e nao ter que reiniciar o programa'''
            capacidade_total += desenvolvedor.pontos_por_dia ''' a capacidade total esta sendo somado com ela mesma mais a instancia pontos da classe projetos '''
        return capacidade_total ''' aqui so esta retornando o valor'''
 
    def verificar_viabilidade(self):
        capacidade_total = self.calcular_capacidade_total()
        pontos_necessarios = self.pontos_de_funçao / self.prazos
        if capacidade_total >= pontos_necessarios:
            return "Projeto viável"
        else:
            return "Projeto inviável"

''' aqui a capacidade total da funçao anterior esta passando por uma verificaçao se o projeto eh viavel ou nao. nao tem muito que comentar aqui'''

class Desenvolvedores:
    
    def __init__(self, nome, senioridade, pontos_por_dia, linguagem):
        self.nome = nome
        self.senioridade = senioridade
        self.pontos_por_dia = pontos_por_dia
        self.linguagem = linguagem


