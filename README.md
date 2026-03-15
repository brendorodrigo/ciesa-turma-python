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

<details>
<summary>Atividade 2 - Orientação a Objetos - Controle de Projetos</summary>
<ul>
<li>Implemente a organização das classes Projetos e Desenvolvedores</li>
<pre>
Projeto:
  Atributos:
    - Descrição
    - Prazo em dias
    - Pontos de função
    - **Desenvolvedores**
  Metodos:
    - adicionar_desenvolvedor
    - calcular_capacidade_total
    - verificar_viabilidade
      - projeto viável
      - projeto inviável
</pre>
<pre>
Desenvolvedor:
  - Nome
  - Senioridade
  - Pontos por dia
  - Linguagem
</pre>
<li>Crie um Projeto</li>
<li>Adicione Desenvolvedores ao Projeto</li>
<li>Validar viabilidade</li>

</ul>
</details>
