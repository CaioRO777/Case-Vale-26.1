import json
from processador import calcular_acertos, calcular_percentual, calcular_media_geral

def executar():
    # 1. Carregando os dados do arquivo JSON
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    gabarito = dados['gabarito']
    alunos = dados['alunos']
    total_questoes = len(gabarito)
    
    total_acertos_turma = 0
    total_alunos = len(alunos)

    print("--- RESULTADOS DO SIMULADO ---\n")

    # 2. Processando os dados de cada aluno
    for aluno in alunos:
        nome = aluno['nome']
        respostas = aluno['respostas']
        
        # Usando as funções do nosso módulo processador
        acertos = calcular_acertos(gabarito, respostas)
        percentual = calcular_percentual(acertos, total_questoes)
        
        # Somando para calcular a média geral depois
        total_acertos_turma += acertos
        
        # Exibindo os resultados individuais
        print(f"Aluno: {nome}")
        print(f"Acertos: {acertos}/{total_questoes}")
        print(f"Aproveitamento: {percentual:.2f}%\n")

    # 3. Calculando e exibindo os dados gerais da turma
    media_geral = calcular_media_geral(total_acertos_turma, total_alunos)
    
    print("-" * 30)
    print(f"MÉDIA GERAL DA TURMA: {media_geral:.2f} acertos por aluno")
    print("-" * 30)

# Isso garante que o código só rode se executarmos este arquivo diretamente
if __name__ == "__main__":
    executar()