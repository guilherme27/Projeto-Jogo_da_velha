import os,time


def local(matriz, jogador = ' ', linha = 0, coluna = 0):
    cont = 1
    mudar(matriz, jogador, linha, coluna)
    for i in range (3):
        for j in range (11):
            print(matriz[i][j], end = '')
        if cont <= 2:
            print('\n---+---+---')
            cont += 1
def mudar(matriz, jogador = ' ', linha = 0, coluna = 0):
    if matriz[linha][coluna] == ' ':
        matriz[linha][coluna] = jogador
    else:
        return (print('Não é possivel colocar nesta posição, essa posição já foi utilizada'))


jogo = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
erro = 0
local(jogo)
posição = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
resposta = 'errada'
while resposta == 'errada':
    jogada = input('\n\nJogador 1 (X): ')
    jogada = jogada.lower()
    for i in range(9):
        if posição[i] == jogada:
            if i == 0:
                linha = 0
                coluna = 0
                resposta = 'certa'
            else:
                coluna = int(i/3)
                if coluna == 0:
                    coluna = 1
                elif coluna == 1:
                    coluna = 5
                elif coluna == 2:
                    coluna = 9
                if i == 0 or i == 3 or i == 6:
                    linha = 0
                    resposta = 'certa'
                elif i == 1 or i == 4 or i == 7:
                    linha = 1
                    resposta = 'certa'
                else:
                    linha = 2
                    resposta = 'certa'
        else:
            erro += 1
        if erro == 9:
            print('Informe uma posição existente')
            erro = 0
            time.sleep(1)
            os.system('cls')

local(jogo,'X',linha,coluna)
os.system('cls')
local(jogo)

resposta = 'errada'
erro = 0
while resposta == 'errada':
    jogada = input('\n\nJogador 2 (O): ')
    jogada = jogada.lower()
    for i in range(9):
        if posição[i] == jogada:
            if i == 0:
                linha = 0
                coluna = 1
                resposta = 'certa'
            else:
                coluna = int(i/3)
                if coluna == 0:
                    coluna = 1
                elif coluna == 1:
                    coluna = 5
                elif coluna == 2:
                    coluna = 9
                if i == 0 or i == 3 or i == 6:
                    linha = 0
                    resposta = 'certa'
                elif i == 1 or i == 4 or i == 7:
                    linha = 1
                    resposta = 'certa'
                else:
                    linha = 2
                    resposta = 'certa'
        else:
            erro += 1
        if erro == 9:
            print('Informe uma posição existente')
            erro = 0
            time.sleep(1)
            os.system('cls')

local(jogo,'O',linha,coluna)
os.system('cls')
local(jogo)
