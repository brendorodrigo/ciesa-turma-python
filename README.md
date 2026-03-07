<<<<<<< HEAD
# Atividade 1 - Python II

## Instituição e Contexto
- **Instituição**: Centro Universitário de Ensino Superior do Amazonas (CIESA)
- **Curso**: Ciência da Computação
- **Disciplina**: Python II
- **Professor**: Brendo Matos

---

## Descrição do Projeto
Esta é a primeira atividade da disciplina de Python II. O objetivo principal foi colocar em prática conceitos de manipulação de listas, dicionários e funções em Python, através de um sistema de gerenciamento de dados de alunos.

O script realiza as seguintes operações:
- Processamento de uma base de dados de alunos.
- Extração de siglas únicas de cursos oferecidos.
- Validação automática de integridade de dados (nome, e-mail e idade).
- Menu interativo para consulta de informações.

## Uso de Inteligência Artificial
Para otimizar o tempo de desenvolvimento e focar na lógica de programação, utilizei **Inteligência Artificial (IA)** nas seguintes tarefas:
- **Geração de Dados**: Criação da lista de dados dos alunos (`lista_dados_dos_alunos`), contendo mais de 100 registros realistas de forma instantânea.
- **Tarefas Repetitivas**: Automação de preenchimento e estruturação de dicionários, poupando o esforço manual de digitação de strings repetitivas.

## Funcionalidades Principais
1. **Consulta Geral**: Visualização de todos os alunos cadastrados no sistema.
2. **Mapeamento de Cursos**: Identificação de todos os cursos presentes na base de dados através de suas siglas, com contagem total.
3. **Validação de Inscrições**: Sistema que analisa se os dados dos alunos estão corretos (tamanho do nome, formato de e-mail e critério de idade), categorizando-os em listas de aprovados ou reprovados.

## Como Executar
Basta ter o Python instalado e executar o arquivo principal:
```bash
python atividade1_david_neves.py
```

## Autor
- **nevext**
- Estudante de Ciência da Computação - CIESA
=======
# Repositório de atividades de Programação em Python II


## Instrução aos alunos
- A atividades devem ser commitadas em seus respectivos diretórios;
- O padrão do nome do arquivo deve ser: `atividadeX_<nome_do_aluno>.py`;
- Uma PR deve ser aberta e comentada/respondida na atividade correspondente no Classrrom (https://classroom.google.com/c/ODQ0MTEzMTUwMDM1?cjc=wn3z536f);

## Atividades

<details>
<summary>Atividade 1 - Resumão</summary>
<ul>
<li>Crie uma lista de alunos contendo: nome, email, idade e sigla do curso;</li>
<pre>
[
  {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
  {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
  {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
  {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]
</pre>
<li>Crie uma lista de cursos disponíveis contendo a sigla;</li>
<pre>
["CCP", "ADS", "IA", "EGC"]
</pre>
<li>Crie uma função que receba a lista de alunos e valide segundo os seguintes critérios: </li>
  <ul>
  <li>O nome deve conter pelo menos 3 caracteres;</li>
  <li>O email deve conter um "@" e um "." após o @;</li>
  <li>A idade deve ser maior ou igual a 16 anos;</li>
  <liA sigla do curso deve existir no dicionário de cursos disponíveis;<li
  </ul>
<li>A função deve retornar uma lista de alunos válidos e uma lista de alunos inválidos, juntamente com a lista de motivos da invalidação.</li>

<pre>
alunos validos: [{'nome': 'Brendo', 'email': 'brendo.matos@ciesa.br', 'idade': 32, 'curso': 'CCP'}, {'nome': 'Joao', 'email': 'joao@cies.abr', 'idade': 18, 'curso': 'ADS'}]
alunos invalidos:  [{'nome': 'Eva', 'motivos': ['Idade menor que 16 anos']}, {'nome': 'Ed', 'motivos': ['Idade menor que 16 anos', 'Curso não disponível', 'Nome com menos de 3 caracteres', 'Email inválido']}]
</pre>
</ul>
</details>
>>>>>>> 2006c6eaf5ac7a6f28190df2765312ebe08208d9
