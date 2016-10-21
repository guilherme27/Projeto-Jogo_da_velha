import os,time


def imprimir(matriz):
    cont = 1
    x = 1
    print("     [a] [b] [c] ")
    for i in range (3):
        print('', x, '- ', matriz[i][0], '|', matriz[i][1], '|', matriz[i][2])
        if cont <= 2:
            print('     ---+---+---')
            cont += 1
        x += 1
    x = 1
def mudar(matriz, jogador = ' ', linha = 0, coluna = 0):
    if matriz[linha][coluna] == ' ':
        matriz[linha][coluna] = jogador

    else:
        print('Não é possivel colocar nesta posição, escolha outra.')
        time.sleep(1.5)
        global vez,jogadas
        vez -= 1
        jogadas -= 1

jogo = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
erro = 0
posição = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
vencedor = ' '
jogadas = 0
vez = 0
while True:
    print('\n')
    os.system('cls')
    print('\n')
    imprimir(jogo)
    if (vez % 2) == 0:
        jogada = input('\n\nJogador 1 (X): ')
        jogada = jogada.lower()
    else:
        jogada = input('\n\nJogador 2 (O): ')
        jogada = jogada.lower()
    for i in range(9):
        if posição[i] == jogada:
            vez += 1
            coluna = int(i/3)
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
            if vez != 0:
                vez -= 1
            if jogadas != 0:
                jogadas -= 1
            time.sleep(1.5)

    if (vez % 2) == 1:
        try:
            mudar(jogo, 'X', linha, coluna)
        except:
            nada = 0
        erro = 0
    else:
        try:
            mudar(jogo, 'O', linha, coluna)
        except:
            nada = 0
        erro = 0

    if jogo[0][0] == jogo[0][1] and jogo[0][1] == jogo[0][2] and jogo[0][2] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[1][0] == jogo[1][1] and jogo[1][1] == jogo[1][2] and jogo[1][2] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[2][0] == jogo[2][1] and jogo[2][1] == jogo[2][2] and jogo[2][2] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][0] == jogo[1][0] and jogo[1][0] == jogo[2][0] and jogo[2][0] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][1] == jogo[1][1] and jogo[1][1] == jogo[2][1] and jogo[2][1] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][2] == jogo[1][2] and jogo[1][2] == jogo[2][2] and jogo[2][2] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2] and jogo[2][2] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    elif jogo[0][2] == jogo[1][1] and jogo[1][1] == jogo[2][0] and jogo[2][0] != ' ':
        if (vez % 2) == 1:
            vencedor = 'x'
            break
        else:
            vencedor = 'o'
            break
    if jogadas == 9:
        break

print('\n')
os.system('cls')
print('\n')
imprimir(jogo)
print('\n')
if vencedor == 'x':
    print('\n Jogador 1 (X) - Venceu!!')
elif vencedor == 'o':
    print('\n Jogador 2 (O) - Venceu!!')
else:
    print('\n Não houve vitória, deu velha!!')
