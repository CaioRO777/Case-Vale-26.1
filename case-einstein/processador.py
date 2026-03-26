def calcular_acertos(gabarito: list, respostas_aluno: list) -> int:
    """
    Compara as respostas do aluno com o gabarito e retorna o número total de acertos.
    """
    acertos = 0
    # O zip junta as duas listas lado a lado para compararmos questão por questão
    for resp_correta, resp_aluno in zip(gabarito, respostas_aluno):
        if resp_correta == resp_aluno:
            acertos += 1
    return acertos

def calcular_percentual(acertos: int, total_questoes: int) -> float:
    """
    Calcula a porcentagem de acertos baseada no total de questões.
    """
    if total_questoes == 0:
        return 0.0
    return (acertos / total_questoes) * 100

def calcular_media_geral(total_acertos_turma: int, total_alunos: int) -> float:
    """
    Calcula a média de acertos de todos os alunos.
    """
    if total_alunos == 0:
        return 0.0
    return total_acertos_turma / total_alunos