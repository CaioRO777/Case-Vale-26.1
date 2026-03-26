# Case Vale do Silício - Einstein Floripa 🚀

Este projeto foi desenvolvido como resolução da **Opção 2 - Case de Programação (Automação de Dados)** para o processo seletivo do departamento Vale do Silício do Einstein Floripa.

## 🎯 Objetivo
Automatizar o tratamento de dados de simulados da organização. O programa recebe o gabarito oficial e as respostas dos alunos, gerando métricas essenciais como o número de acertos, percentual individual e a média geral da turma.

## 🛠️ Tecnologias Utilizadas
* **Python 3:** Linguagem principal escolhida por ser eficiente na manipulação de dados e alinhada com as tecnologias do Einstein Floripa.
* **JSON:** Utilizado para simular a entrada de dados (banco de dados fictício), facilitando a leitura e escalabilidade futura.

## 🗂️ Arquitetura e Organização do Código
Pensando em boas práticas, escalabilidade e manutenabilidade, o projeto foi estruturado da seguinte forma:
* **case-einstein/dados.json:** Armazena os dados fictícios (gabarito oficial e respostas dos alunos).
* **case-einstein/processador.py:** Contém as funções lógicas para os cálculos (acertos, percentuais e médias). A regra de negócio está isolada aqui.
* **case-einstein/main.py:** O ficheiro principal que faz a leitura dos dados, chama as funções e exibe os resultados no terminal.

## 🚀 Como Executar o Projeto

**Passo 1:** Certifique-se de ter o Python 3 instalado no seu computador.

**Passo 2:** Clone este repositório ou descarregue os ficheiros.

**Passo 3:** Abra o terminal na raiz do projeto e entre na pasta do código digitando:
> cd case-einstein

**Passo 4:** Em seguida, execute o ficheiro principal com o comando:
> python main.py

**Passo 5:** Os resultados do processamento (acertos, aproveitamento individual e média geral) serão exibidos diretamente no terminal.