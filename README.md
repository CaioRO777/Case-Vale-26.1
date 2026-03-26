# Case Vale do Silício - Einstein Floripa 🚀

Este projeto foi desenvolvido como resolução da **Opção 2 - Case de Programação (Automação de Dados)** para o processo seletivo do departamento Vale do Silício do Einstein Floripa.

## 🎯 Objetivo

Automatizar o tratamento de dados de simulados da organização. O programa recebe o gabarito oficial e as respostas dos alunos, gerando métricas essenciais como o número de acertos, percentual individual e a média geral da turma.

## 🛠️ Tecnologias Utilizadas

- **Python 3:** Linguagem principal escolhida por sua eficiência na manipulação de dados e alinhamento com a stack do Einstein Floripa.
- **JSON:** Utilizado para simular a entrada de dados (banco de dados fictício), facilitando a leitura e escalabilidade futura.

## 🗂️ Arquitetura e Organização do Código

Pensando em boas práticas, escalabilidade e manutenabilidade, o projeto foi estruturado da seguinte forma:

- `case-einstein/dados.json`: Armazena o mock de dados (gabarito oficial e respostas dos alunos).
- `case-einstein/processador.py`: Contém as funções lógicas puras para cálculos (acertos, percentuais e médias). Isolamos a regra de negócio aqui.
- `case-einstein/main.py`: O arquivo principal que orquestra a leitura dos dados, chama as funções de processamento e exibe os resultados no terminal.

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos para o seu computador.
3. Abra o terminal na raiz do projeto e entre na pasta do código digitando:

```bash
cd case-einstein

Em seguida, execute o arquivo principal com o comando:

python main.py

Os resultados do processamento (acertos, aproveitamento individual e média geral) serão exibidos diretamente no terminal.
