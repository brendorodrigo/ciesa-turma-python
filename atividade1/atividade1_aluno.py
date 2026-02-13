# Atividade 1 - Resumão

# Lista de alunos
alunos = [
    {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
    {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
    {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
    {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

# Lista de cursos disponíveis
cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]


def validar_alunos(lista_alunos, cursos):
    """
    Valida a lista de alunos segundo os critérios:
    - Nome deve conter pelo menos 3 caracteres
    - Email deve conter um "@" e um "."
    - Idade deve ser maior ou igual a 16 anos
    - Sigla do curso deve existir na lista de cursos disponíveis
    
    Retorna: (alunos_validos, alunos_invalidos_com_motivos)
    """
    alunos_validos = []
    alunos_invalidos = []
    
    for aluno in lista_alunos:
        motivos = []
        
        # Validar nome
        if len(aluno.get("nome", "")) < 3:
            motivos.append("Nome deve conter pelo menos 3 caracteres")
        
        # Validar email
        email = aluno.get("email", "")
        if "@" not in email or "." not in email:
            motivos.append("Email deve conter um '@' e um '.'")
        
        # Validar idade
        idade = aluno.get("idade", 0)
        if idade < 16:
            motivos.append("Idade deve ser maior ou igual a 16 anos")
        
        # Validar curso
        curso = aluno.get("curso", "")
        if curso not in cursos:
            motivos.append("Sigla do curso deve existir na lista de cursos disponíveis")
        
        # Classificar aluno
        if motivos:
            alunos_invalidos.append({"aluno": aluno, "motivos": motivos})
        else:
            alunos_validos.append(aluno)
    
    return alunos_validos, alunos_invalidos


# Executar validação
if __name__ == "__main__":
    validos, invalidos = validar_alunos(alunos, cursos_disponiveis)
    
    print("=" * 50)
    print("ALUNOS VÁLIDOS:")
    print("=" * 50)
    for aluno in validos:
        print(f"- {aluno['nome']} ({aluno['email']}) - {aluno['idade']} anos - {aluno['curso']}")
    
    print("\n" + "=" * 50)
    print("ALUNOS INVÁLIDOS:")
    print("=" * 50)
    for item in invalidos:
        aluno = item['aluno']
        print(f"\n- {aluno['nome']} ({aluno['email']}) - {aluno['idade']} anos - {aluno['curso']}")
        print("  Motivos:")
        for motivo in item['motivos']:
            print(f"    • {motivo}")
