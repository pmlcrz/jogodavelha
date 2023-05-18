import random

def desenhar_tabuleiro(tabuleiro):
    print('-------------')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(' ' + tabuleiro[i][j] + ' |', end='')
        print('\n-------------')

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogar():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'

    while True:
        desenhar_tabuleiro(tabuleiro)
        if jogador_atual == 'X':
            coordenadas = input("Digite as coordenadas (linha, coluna): ")
            linha, coluna = map(int, coordenadas.split(','))
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador_atual
                if verificar_vitoria(tabuleiro, jogador_atual):
                    desenhar_tabuleiro(tabuleiro)
                    print('Parabéns! Você venceu!')
                    break
                jogador_atual = 'O'
            else:
                print('Essa posição já está ocupada. Tente novamente.')
        else:
            
            movimento_computador(tabuleiro, jogador_atual)
            if verificar_vitoria(tabuleiro, jogador_atual):
                desenhar_tabuleiro(tabuleiro)
                print('Você perdeu! O computador venceu.')
                break
            jogador_atual = 'X'

def movimento_computador(tabuleiro, jogador):
    vazio = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                vazio.append((i, j))
    if vazio:
        linha, coluna = random.choice(vazio)
        tabuleiro[linha][coluna] = jogador

jogar()
