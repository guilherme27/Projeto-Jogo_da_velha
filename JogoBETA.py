from IA import *
import os,time
from termcolor import *

continuar = True

while continuar == True:
    def imprimir(matriz):
        cont = 1
        x = 1
        print(colored("     [A] [B] [C] ",'green'))
        for i in range (3):
            print('', colored(str(x) + ' - ','green'), matriz[i][0], '|', matriz[i][1], '|', matriz[i][2])
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

    def local():
        return True
    def web():
        return True
    def ranking():
        return True
    def maquina():
        return True

    os.system('cls')

    jogo = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    erro = 0
    posição = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
    vencedor = ' '
    jogadas = 0
    jogador2 = 'ia'
    vez = 0

    while True:
        letreiro = ("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n"
                    "BBBBBBBB''BB''''''''BB''''''''BB''''''''BBBBB'''''''BBBBBBB'''BBBBBBB''BBBBB''BB''''''''BB''BBBBBBBB''BBBB''BBBBB'''BBBBB\n"
                    "BBBBBBBB  BB  BBBB  BB  BBBBBMBB  BBBB  BBBBB  BBBBB  BBBB  B  BBBBBB  BBBBB  BB  BBBBBBBB  BBBBBBBB  BBBB  BBBB  B  BBBB\n"
                    "BBBBBBBB  BB  BBBB  BB  BB..  BB  BBBB  BBBBB  BBBBB  BBB  BBB  BBBBBB  BBB  BBB  ....BBBB  BBBBBBBB  ''''  BBB  BBB  BBB\n"
                    "BBB  BBB  BB  BBBB  BB  EBBB  BB  BBBB  BBBBB  BBBBB  BB  :::::  BBBBBB  B  BBBB  BBBBBBBB  BBBBBBBB  BBBB  BB  :::::  BB\n"
                    "BBB.......BB........BB........BB........BBBBB.......BBBB..BBBBB..BBBBBBB...BBBBB........BB........BB  BBBB  BB..BBBBB..BB\n"
                    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n")
        print(letreiro)


        try:
            quantidade_jogador = int(input(' 1 - Jogar com 2 jogadores \n 2 - Jogar com a maquina \n 3 - Jogar em rede \n Qualquer outra tecla - sair\n '))
            if quantidade_jogador == 1:
                os.system('cls')
                try:
                    while True:
                        print(letreiro)
                        quantidade_jogador = int(input(' 1 - Jogar localmente \n 2 - Jogar em rede\n '))
                        if quantidade_jogador == 1:
                            jogador2 = 'humano'
                            break
                        elif quantidade_jogador == 2:
                            web()
                            break
                        else:
                            print('Informe um valor válido\n')
                            time.sleep(1.5)
                            os.system('cls')
                except ValueError:
                    print('Informe um valor válido\n')
            elif quantidade_jogador == 2:
                jogador2 = 'ia'
            elif quantidade_jogador == 3:
                jogador2 = 'humano'
            else:
                break
            break
        except ValueError:
            continuar = False
            break
    if continuar == True:
        def define(jogador):
            global jogador2
            jogador2 = jogador

        while True:
            print('\n')
            os.system('cls')
            print('\n')
            imprimir(jogo)
            if (vez % 2) == 0:
                jogada = input('\n\nJogador 1 (X): ')
                jogada = jogada.lower()
            else:
                if jogador2 == 'humano':
                    jogada = input('\n\nJogador 2 (O): ')
                    jogada = jogada.lower()
                elif jogador2 == 'ia':
                    jogada = IA(jogo)
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
                    pass
                erro = 0
            else:
                try:
                    mudar(jogo, 'O', linha, coluna)
                except:
                    pass
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

        condição = str(input('Deseja reiniciar o jogo?\n1 - sim, quero jogar novamente\nQualquer outra tecla - não, desejo sair:\n '))

        if condição == '1':
            continuar = True
        else:
            os.system('cls')
            print("\n\nAté logo!")
            time.sleep(1.5)
            continuar = False
    else:
        os.system('cls')
        print("\n\nAté logo!")
        time.sleep(1.5)
        break
