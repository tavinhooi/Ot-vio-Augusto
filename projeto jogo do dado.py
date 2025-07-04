'''
Projeto: Dado Virtual
2025.06.25
Otávio Augusto Machado Ott
'''


# Objetivo: Criar um jogo de dado virtual, onde o usuário pode jogar um dado e receber um número aleatório entre 1 e 6. 
# O jogador escolhe jogar e vê o resultado de um dado de 6 lados.

#BIBLIOTECAS --> Espaço reservado para a declaração das bibliotecas e funções
import random    # Importa a biblioteca random para gerar números aleatórios
import time      # Importa a biblioteca time para criar atrasos na execução do programa

# CONSTANTES --> Espaço reservado para a declaração de constantes
DADOS = [1, 2, 3, 4, 5, 6]  # Lista de valores possíveis do dado      

# VARIÁVEIS --> Espaço reservado para a declaração de variáveis
resultado = 0  # Variável que guarda o resultado do dado

# função para limpar a tela
def limpar_tela():
    print('\n' * 40)

# função para desenhar uma linha
def desenha_linha(tam=40):      # Função para desenhar uma linha de tamanho tam
    print('-' * tam)            # imprime uma linha de traços com o tamanho especificado

# função para exibir o cabeçalho do jogo
def cabecalho():                # Função para exibir o cabeçalho do jogo
    limpar_tela()               # Limpa a tela antes de exibir o cabeçalho
    desenha_linha()             # Desenha uma linha no topo
    print('JOGO DO DADO VIRTUAL'.center(40))  # Exibe o título do jogo centralizado
    print('Desenvolvido por Otávio Augusto Machado Ott'.center(40))   # Exibe o nome do desenvolvedor centralizado
    desenha_linha()         # Desenha uma linha no final do cabeçalho

# função para exibir o menu principal
def menu():             # Função para exibir o menu principal
    print('[1] Jogar dado') # Opção para jogar o dado
    print('[0] Sair')       # Opção para sair do jogo
    while True:             # Loop para garantir que o usuário escolha uma opção válida
        opcao = input('Escolha uma opção: ')  # Solicita ao usuário que escolha uma opção
        if opcao in ['1', '0']:               # Verifica se a opção é válida
            return opcao                      # Retorna a opção escolhida
        print('Opção inválida. Tente novamente.')  # Exibe mensagem de erro se a opção for inválida

# função para jogar o dado
def jogar_dado():              # Função para jogar o dado
    print('Jogando o dado...') # Exibe mensagem informando que o dado está sendo jogado
    time.sleep(1)              # Atraso de 1 segundo para simular o lançamento do dado
    resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
    print(f'Você tirou: {resultado}') # Exibe o resultado do dado
    desenha_linha()                   # Desenha uma linha após o resultado

# função para perguntar se o jogador quer jogar novamente
def jogar_novamente():             # Função para perguntar se o jogador quer jogar novamente
    print('[1] Jogar novamente')   # Opção para jogar novamente
    print('[0] Sair')              # Opção para sair do jogo
    while True:                    # Loop para garantir que o usuário escolha uma opção válida
        resp = input('Escolha uma opção: ')   # Solicita ao usuário que escolha uma opção
        if resp in ['1', '0']:                # Verifica se a opção é válida
            return resp == '1'                # Retorna True se o usuário escolher jogar novamente, False se escolher sair
        print('Opção inválida. Tente novamente.')   # Exibe mensagem de erro se a opção for inválida

def main():               # Função principal do jogo
    while True:           # Loop principal do jogo
        limpar_tela()     # Limpa a tela antes de iniciar o jogo
        cabecalho()       # Exibe o cabeçalho do jogo
        opcao = menu()    # Exibe o menu principal e obtém a opção escolhida pelo usuário
        if opcao == '1':  # Se o usuário escolher jogar o dado
            limpar_tela() # Limpa a tela antes de jogar o dado
            cabecalho()   # Exibe o cabeçalho do jogo novamente
            jogar_dado()   # Chama a função para jogar o dado
            if not jogar_novamente():   # Pergunta se o usuário quer jogar novamente
                print('Obrigado por jogar!')   # Exibe mensagem de agradecimento
                break
        else:
            print('Saindo do jogo. Até logo!')  # Se o usuário escolher sair do jogo
            break

if __name__ == '__main__':   # Verifica se o script está sendo executado diretamente
    main()
