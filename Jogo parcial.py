<<<<<<< HEAD
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
        print('Não é possivel colocar nesta posição, escolha outra.')


jogo = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
erro = 0
posição = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
vencedor = ' '
jogadas = 0
vez = 0
while True:
    print('\n')
    os.system('cls')
    print('\n')
    local(jogo)
    if (vez % 2) == 0:
        try:
            jogada = input('\n\nJogador 1 (X): ')
        except:
            print('Informe valores posíveis')
            vez += 1
            linha = ' '
            coluna = ' '
        jogada = jogada.lower()
    else:
        try:
            jogada = input('\n\nJogador 2 (O): ')
        except:
            print('Informe valores posíveis')
            vez += 1
            linha = ' '
            coluna = ' '
        jogada = jogada.lower()
    for i in range(9):
        if posição[i] == jogada:
            vez += 1
            coluna = int(i/3)
            if coluna == 0:
                coluna = 1
            elif coluna == 1:
                coluna = 5
            else:
                coluna = 9
            if i == 0 or i == 3 or i == 6:
                linha = 0
                jogadas += 1
            elif i == 1 or i == 4 or i == 7:
                linha = 1
                jogadas += 1
            else:
                linha = 2
                jogadas += 1
        else:
            erro += 1
        if erro == 9:
            print('Informe uma posição existente\n')
            if vez > 0 :
                vez -= 1
            time.sleep(1)
            os.system('cls')

    if (vez % 2) == 1:
        try:
            local(jogo, 'X', linha, coluna)
        except:
            nada = 0
        erro = 0
    else:
        try:
            local(jogo, 'O', linha, coluna)
        except:
            nada = 0
        erro = 0

    if jogo[0][1] == jogo[0][5] and jogo[0][5] == jogo[0][9] and jogo[0][1] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[1][1] == jogo[1][5] and jogo[1][5] == jogo[1][9] and jogo[1][1] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[2][1] == jogo[2][5] and jogo[2][5] == jogo[2][9] and jogo[2][1] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][1] == jogo[1][1] and jogo[1][1] == jogo[2][1] and jogo[0][1] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][5] == jogo[1][5] and jogo[1][5] == jogo[2][5] and jogo[0][5] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][9] == jogo[1][9] and jogo[1][9] == jogo[2][9] and jogo[0][9] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][1] == jogo[1][5] and jogo[1][5] == jogo[2][9] and jogo[0][1] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][9] == jogo[1][5] and jogo[1][5] == jogo[2][1] and jogo[0][9] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    if jogadas == 9:
        print('\nDeu velha, ninguém venceu!')
        break

os.system('cls')
print('\n')
local(jogo)
if vencedor == 'x':
    print('\n Jogador 1 (X) - Venceu!!')
elif vencedor == 'o':
    print('\n Jogador 2 (O) - Venceu!!')
else:
    print('\n Não houve vitória, deu velha!!')
=======
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
>>>>>>> 1078a961b55e192dad420fbfebe598b2be93fa11
