


lista_dados_dos_alunos = [ 
    
    #interessante que são dicionarios dentro de uma lista por exemplo foi criado a lista lista_dados_dos_alunos e dentro dela tem varios dicionarios com as chaves nome, email, idade e curso, e cada dicionario tem um valor diferente para cada chave, ou seja, cada dicionario representa um aluno diferente com suas informações. lista de dados de alunos e dentro o dicionario com  o nome de nome (chave) e o valor do nome (valor)
    
    {"nome": "Brendo", "email": "brendo.matos@ciesa.com", "idade": 32, "curso": "CC"},
    {"nome": "evan", "email": "evan.silva@ciesa.com", "idade": 15, "curso": "ADS"},
    {"nome": "ed", "email": "ed.santos@ciesa.com", "idade": 12, "curso": "DIR"},
    {"nome": "joao", "email": "joao.souza@ciesa.com", "idade": 18, "curso": "ADS"},
    {"nome": "Maria Oliveira", "email": "maria.oliveira@ciesa.com", "idade": 21, "curso": "ADS"},
    {"nome": "Ana Pereira", "email": "ana.pereira@ciesa.com", "idade": 28, "curso": "ADM"},
    {"nome": "Carlos Ferreira", "email": "carlos.ferreira@ciesa.com", "idade": 34, "curso": "ENGC"},
    {"nome": "Fernanda Costa", "email": "fernanda.costa@ciesa.com", "idade": 45, "curso": "PSI"},
    {"nome": "Lucas Almeida", "email": "lucas.almeida@ciesa.com", "idade": 19, "curso": "CC"},
    {"nome": "Rafael Souza", "email": "rafael.souza@ciesa.com", "idade": 23, "curso": "SI"},
    {"nome": "Beatriz Ramos", "email": "beatriz.ramos@ciesa.com", "idade": 29, "curso": "ENF"},
    {"nome": "Tiago Martins", "email": "tiago.martins@ciesa.com", "idade": 17, "curso": "EF"},
    {"nome": "Sofia Lima", "email": "sofia.lima@ciesa.com", "idade": 20, "curso": "DG"},
    {"nome": "Pedro Gomes", "email": "pedro.gomes@ciesa.com", "idade": 52, "curso": "DIR"},
    {"nome": "Carolina Nunes", "email": "carolina.nunes@ciesa.com", "idade": 26, "curso": "MKT"},
    {"nome": "Mariana Rocha", "email": "mariana.rocha@ciesa.com", "idade": 31, "curso": "NUT"},
    {"nome": "Felipe Cardoso", "email": "felipe.cardoso@ciesa.com", "idade": 40, "curso": "GAS"},
    {"nome": "Igor Silva", "email": "igor.silva@ciesa.com", "idade": 22, "curso": "MED"},
    {"nome": "Daniela Pinto", "email": "daniela.pinto@ciesa.com", "idade": 36, "curso": "QUI"},
    {"nome": "Vinicius Alves", "email": "vinicius.alves@ciesa.com", "idade": 27, "curso": "FIS"},
    {"nome": "Juliana Moreira", "email": "juliana.moreira@ciesa.com", "idade": 24, "curso": "ARQ"},
    {"nome": "Mateus Fernandes", "email": "mateus.fernandes@ciesa.com", "idade": 30, "curso": "ENGE"},
    {"nome": "Rodrigo Carvalho", "email": "rodrigo.carvalho@ciesa.com", "idade": 28, "curso": "ENGM"},
    {"nome": "Paula Mendes", "email": "paula.mendes@ciesa.com", "idade": 22, "curso": "MKT"},
    {"nome": "Gustavo Nascimento", "email": "gustavo.nascimento@ciesa.com", "idade": 33, "curso": "RH"},
    {"nome": "Helena Araujo", "email": "helena.araujo@ciesa.com", "idade": 27, "curso": "DIR"},
    {"nome": "Eduardo Lopes", "email": "eduardo.lopes@ciesa.com", "idade": 41, "curso": "ADM"},
    {"nome": "Leticia Castro", "email": "leticia.castro@ciesa.com", "idade": 19, "curso": "DG"},
    {"nome": "Vitor Ribeiro", "email": "vitor.ribeiro@ciesa.com", "idade": 23, "curso": "CC"},
    {"nome": "Amanda Dias", "email": "amanda.dias@ciesa.com", "idade": 20, "curso": "ENF"},
    {"nome": "Bruno Barros", "email": "bruno.barros@ciesa.com", "idade": 35, "curso": "ENGC"},
    {"nome": "Luiza Santana", "email": "luiza.santana@ciesa.com", "idade": 26, "curso": "GAS"},
    {"nome": "Thais Gomes", "email": "thais.gomes@ciesa.com", "idade": 29, "curso": "PSI"},
    {"nome": "Diego Teixeira", "email": "diego.teixeira@ciesa.com", "idade": 24, "curso": "AD"},
    {"nome": "Patricia Rocha", "email": "patricia.rocha@ciesa.com", "idade": 38, "curso": "FISIO"},
    {"nome": "Samuel Correia", "email": "samuel.correia@ciesa.com", "idade": 21, "curso": "SI"},
    {"nome": "Aline Freitas", "email": "aline.freitas@ciesa.com", "idade": 32, "curso": "QUI"},
    {"nome": "Igor Pereira", "email": "igor.pereira@ciesa.com", "idade": 25, "curso": "MED"},
    {"nome": "Marina Costa", "email": "marina.costa@ciesa.com", "idade": 22, "curso": "BIOM"},
    {"nome": "Andre Oliveira", "email": "andre.oliveira@ciesa.com", "idade": 44, "curso": "GF"},
    {"nome": "Camila Ribeiro", "email": "camila.ribeiro@ciesa.com", "idade": 18, "curso": "EF"},
    {"nome": "Nelson Souza", "email": "nelson.souza@ciesa.com", "idade": 50, "curso": "HIST"},
    {"nome": "Renata Martins", "email": "renata.martins@ciesa.com", "idade": 31, "curso": "ECO"},
    {"nome": "Lucas Ferreira", "email": "lucas.ferreira@ciesa.com", "idade": 23, "curso": "TI"},
    {"nome": "Denise Cardoso", "email": "denise.cardoso@ciesa.com", "idade": 37, "curso": "FARM"},
    {"nome": "Marcelo Alves", "email": "marcelo.alves@ciesa.com", "idade": 29, "curso": "ENGP"},
    {"nome": "Gabriela Pinto", "email": "gabriela.pinto@ciesa.com", "idade": 24, "curso": "ENF"},
    {"nome": "Henrique Silva", "email": "henrique.silva@ciesa.com", "idade": 27, "curso": "CC"},
    {"nome": "Rosa Mendes", "email": "rosa.mendes@ciesa.com", "idade": 46, "curso": "SOC"},
    {"nome": "Elias Rocha", "email": "elias.rocha@ciesa.com", "idade": 39, "curso": "ODONTO"},
    {"nome": "Bianca Nunes", "email": "bianca.nunes@ciesa.com", "idade": 20, "curso": "LET"},
    {"nome": "Fabio Teixeira", "email": "fabio.teixeira@ciesa.com", "idade": 34, "curso": "LOG"},
    {"nome": "Isabela Motta", "email": "isabela.motta@ciesa.com", "idade": 21, "curso": "NUT"},
    {"nome": "Otavio Campos", "email": "otavio.campos@ciesa.com", "idade": 28, "curso": "SST"},
    {"nome": "Lucia Pereira", "email": "lucia.pereira@ciesa.com", "idade": 42, "curso": "RH"},
    {"nome": "Walisson Duarte", "email": "walisson.duarte@ciesa.com", "idade": 26, "curso": "ADS"},
    {"nome": "Elaine Soares", "email": "elaine.soares@ciesa.com", "idade": 30, "curso": "MKT"},
    {"nome": "Caio Ribeiro", "email": "caio.ribeiro@ciesa.com", "idade": 19, "curso": "CC"},
    {"nome": "Sabrina Santos", "email": "sabrina.santos@ciesa.com", "idade": 25, "curso": "DG"},
    {"nome": "Gustavo Pinto", "email": "gustavo.pinto@ciesa.com", "idade": 31, "curso": "ENGC"},
    {"nome": "Milena Rocha", "email": "milena.rocha@ciesa.com", "idade": 22, "curso": "VET"},
    {"nome": "Adriano Lima", "email": "adriano.lima@ciesa.com", "idade": 36, "curso": "DIR"},
    {"nome": "Karina Alves", "email": "karina.alves@ciesa.com", "idade": 28, "curso": "MKT"},
    {"nome": "Jonas Moreira", "email": "jonas.moreira@ciesa.com", "idade": 24, "curso": "GEO"},
    {"nome": "Natalia Campos", "email": "natalia.campos@ciesa.com", "idade": 23, "curso": "BIOM"},
    {"nome": "Yuri Carvalho", "email": "yuri.carvalho@ciesa.com", "idade": 21, "curso": "SI"},
    {"nome": "Luan Almeida", "email": "luan.almeida@ciesa.com", "idade": 20, "curso": "CC"},
    {"nome": "Maira Oliveira", "email": "maira.oliveira@ciesa.com", "idade": 33, "curso": "ENF"},
    {"nome": "Victor Santos", "email": "victor.santos@ciesa.com", "idade": 29, "curso": "ENGM"},
    {"nome": "Sabrina Melo", "email": "sabrina.melo@ciesa.com", "idade": 27, "curso": "MKT"},
    {"nome": "Iago Nascimento", "email": "iago.nascimento@ciesa.com", "idade": 22, "curso": "ADM"},
    {"nome": "Tania Araujo", "email": "tania.araujo@ciesa.com", "idade": 41, "curso": "EDU"},
    {"nome": "Wesley Borges", "email": "wesley.borges@ciesa.com", "idade": 35, "curso": "AD"},
    {"nome": "Cintia Rocha", "email": "cintia.rocha@ciesa.com", "idade": 30, "curso": "QUI"},
    {"nome": "Fabio Martins", "email": "fabio.martins@ciesa.com", "idade": 26, "curso": "MAT"},
    {"nome": "Elisa Fernandes", "email": "elisa.fernandes@ciesa.com", "idade": 24, "curso": "PSI"},
    {"nome": "Guilherme Costa", "email": "guilherme.costa@ciesa.com", "idade": 32, "curso": "ENGE"},
    {"nome": "Jorge Lima", "email": "jorge.lima@ciesa.com", "idade": 45, "curso": "ADM"},
    {"nome": "Mayara Silva", "email": "mayara.silva@ciesa.com", "idade": 19, "curso": "DG"},
    {"nome": "Romulo Teixeira", "email": "romulo.teixeira@ciesa.com", "idade": 38, "curso": "DIR"},
    {"nome": "Priscila Guerreiro", "email": "priscila.guerreiro@ciesa.com", "idade": 27, "curso": "ENF"},
    {"nome": "Nelson Andrade", "email": "nelson.andrade@ciesa.com", "idade": 49, "curso": "ECO"},
    {"nome": "Denise Rocha", "email": "denise.rocha@ciesa.com", "idade": 33, "curso": "GAS"},
    {"nome": "Igor Cardoso", "email": "igor.cardoso@ciesa.com", "idade": 24, "curso": "FIS"},
    {"nome": "Bruna Dias", "email": "bruna.dias@ciesa.com", "idade": 21, "curso": "ENF"},
    {"nome": "Cesar Monteiro", "email": "cesar.monteiro@ciesa.com", "idade": 50, "curso": "ENGC"},
    {"nome": "Paula Farias", "email": "paula.farias@ciesa.com", "idade": 29, "curso": "MKT"},
    {"nome": "Mateus Oliveira", "email": "mateus.oliveira@ciesa.com", "idade": 22, "curso": "TI"},
    {"nome": "Renan Sousa", "email": "renan.sousa@ciesa.com", "idade": 31, "curso": "SI"},
    {"nome": "Karla Batista", "email": "karla.batista@ciesa.com", "idade": 26, "curso": "ARQ"},
    {"nome": "Leandro Ribeiro", "email": "leandro.ribeiro@ciesa.com", "idade": 37, "curso": "ENGM"},
    {"nome": "Jessica Rodrigues", "email": "jessica.rodrigues@ciesa.com", "idade": 23, "curso": "SOC"},
    {"nome": "Wilson Barros", "email": "wilson.barros@ciesa.com", "idade": 44, "curso": "SST"},
    {"nome": "Fabiana Goncalves", "email": "fabiana.goncalves@ciesa.com", "idade": 28, "curso": "FISIO"},
    {"nome": "Daniel Souza", "email": "daniel.souza@ciesa.com", "idade": 34, "curso": "ENGP"},
    {"nome": "Vanessa Lopes", "email": "vanessa.lopes@ciesa.com", "idade": 25, "curso": "LET"},
    {"nome": "Rodrigo Azevedo", "email": "rodrigo.azevedo@ciesa.com", "idade": 30, "curso": "ENGE"},
    {"nome": "Sabrina Rocha", "email": "sabrina.rocha@ciesa.com", "idade": 22, "curso": "BIOM"},
    {"nome": "Murilo Pinto", "email": "murilo.pinto@ciesa.com", "idade": 27, "curso": "SI"},
    {"nome": "Tadeu Moreira", "email": "tadeu.moreira@ciesa.com", "idade": 35, "curso": "GF"},
    {"nome": "Livia Mendes", "email": "livia.mendes@ciesa.com", "idade": 21, "curso": "DG"},
    {"nome": "Henrique Nogueira", "email": "henrique.nogueira@ciesa.com", "idade": 29, "curso": "ENGC"},
    {"nome": "Valeska Fernandes", "email": "valeska.fernandes@ciesa.com", "idade": 33, "curso": "ENF"},
    {"nome": "Otavio Souza", "email": "otavio.souza@ciesa.com", "idade": 40, "curso": "DIR"},
    {"nome": "Sabrina Lima", "email": "sabrina.lima@ciesa.com", "idade": 24, "curso": "MKT"},
    {"nome": "Breno Castro", "email": "breno.castro@ciesa.com", "idade": 28, "curso": "CC"},
    {"nome": "Rafaela Moreira", "email": "rafaela.moreira@ciesa.com", "idade": 26, "curso": "ADM"},
    {"nome": "Igor Mendes", "email": "igor.mendes@ciesa.com", "idade": 22, "curso": "EF"},
    {"nome": "Elaine Martins", "email": "elaine.martins@ciesa.com", "idade": 31, "curso": "QUI"},
    {"nome": "Murilo Santos", "email": "murilo.santos@ciesa.com", "idade": 23, "curso": "ADS"},
    {"nome": "Clarice Ribeiro", "email": "clarice.ribeiro@ciesa.com", "idade": 36, "curso": "LET"},
    {"nome": "Emanoel Costa", "email": "emanoel.costa@ciesa.com", "idade": 45, "curso": "ENGM"},
    {"nome": "Bianca Oliveira", "email": "bianca.oliveira@ciesa.com", "idade": 20, "curso": "ECO"},
    {"nome": "Flavio Almeida", "email": "flavio.almeida@ciesa.com", "idade": 39, "curso": "ENGE"},
    {"nome": "Monique Torres", "email": "monique.torres@ciesa.com", "idade": 27, "curso": "PSI"},
    {"nome": "Yuri Mendes", "email": "yuri.mendes@ciesa.com", "idade": 22, "curso": "CC"},
    {"nome": "Solange Dias", "email": "solange.dias@ciesa.com", "idade": 48, "curso": "ENF"},
    {"nome": "Nicolas Barbosa", "email": "nicolas.barbosa@ciesa.com", "idade": 19, "curso": "ADS"},
    {"nome": "Helio Nunes", "email": "helio.nunes@ciesa.com", "idade": 55, "curso": "DIR"},
    {"nome": "Luan Santos", "email": "luan.santos@ciesa.com", "idade": 24, "curso": "MKT"}
]

def coleta_siglas(lista_dados_dos_alunos):
    cont = 0
    siglas = []
    for aluno in lista_dados_dos_alunos:
        curso = aluno["curso"].upper()
        if curso not in siglas:
            siglas.append(curso)
            cont = cont + 1

    return siglas

siglas = coleta_siglas(lista_dados_dos_alunos)
        
def validacao_de_alunos(lista_dados_dos_alunos):
    aprovados = []
    reprovados = []
    cont_a = 0
    cont_r = 0

    for aluno in lista_dados_dos_alunos:
        motivo = []
        if len(aluno["nome"]) < 3:
            motivo.append("Nome menor que 3 caracteres")

        email = aluno ["email"]

        if "@" not in email or "." not in email.split("@") [-1]: 
            motivo.append("Email com origem desconhecida")
        if (aluno["idade"]) >= 16:
            motivo.append("Menor de idade, não pode")
        
        if motivo:
            reprovados.append({"nome": aluno["nome"], "motivos": motivo})
            cont_r = cont_r + 1
        
        else:
            aprovados.append(aluno)
            cont_a = cont_a + 1
    return aprovados, reprovados, cont_a, cont_r

nome = input ("Digite seu nome:\n\t")
print(f"Olá {nome} ! \n")

resp = input("O que voce quer fazer?\n digite 1 para ler os dados coletados\n digite 2 para ver os cursos disponíveis por siglas e a quantidade disponíveis\n digite 3 para ver a validação de alunos aprovados e reprovados na inscrição\n 4 para ver tudo:")

if resp == "1": 
    print("\nlista dos alunos", lista_dados_dos_alunos)
    print("\n muita coisa né? \n voce que pediu lol")

elif resp == "2":
    siglas = coleta_siglas(lista_dados_dos_alunos)
    print("\ncursos disponíveis", siglas)
    print(f"\nQuantidade de cursos em siglas é: {len(siglas)}")

elif resp == "3":
    aprovados, reprovados, cont_a, cont_r = validacao_de_alunos(lista_dados_dos_alunos)
    print("\nAlunos aprovados:", aprovados)
    print(f"\nQuantidade de aprovados", len(aprovados))

    print("\nAlunos reprovados", reprovados)
    print(f"\nQuantidade de reprovados:", len(reprovados))

elif resp == "4":
    print("\nLista de alunos:", lista_dados_dos_alunos)
    siglas = coleta_siglas(lista_dados_dos_alunos)
    print("\nCursos disponíveis:", siglas)
    print(f"\nTotal de cursos: {len(siglas)}")
    aprovados, reprovados, cont_a, cont_r = validacao_de_alunos(lista_dados_dos_alunos)
    print("\nAlunos aprovados:", aprovados)
    print("\nTotal aprovados:", cont_a)
    print("\nAlunos reprovados:", reprovados)
    print("\nTotal reprovados:", cont_r)

else:
    print(f"Valor invalido {nome}")
