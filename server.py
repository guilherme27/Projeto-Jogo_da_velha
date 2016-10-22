from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
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
        time.sleep(1.5)
        global vez,jogadas
        vez -= 1
        jogadas -= 1

jogo = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
erro = 0
posição = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
vencedor = ' '
jogadas = 0
vez = 0
jogada = " "
O = " "

def jogodavelha():
    global jogada, vez, jogadas, erro, linha, coluna, nada, O, msg
    while True:
        print('\n')
        os.system('cls')
        print('\n')
        local(jogo)
        if (vez % 2) == 0 and msg != " ":
            try:
                jogada = msg
            except:
                print('Informe valores posíveis')
                vez += 1
                linha = ' '
                coluna = ' '
            jogada = jogada.lower()
            print(jogada)
            msg = " "
        elif O != " ":
            try:
                jogada = O
            except:
                print('Informe valores posíveis')
                vez += 1
                linha = ' '
                coluna = ' '
            jogada = jogada.lower()
            O = " "
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
                time.sleep(1.5)
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
        break








# classe para manipular o socket
class Send:
    def __init__(self):
        self.__msg = ''
        self.new = True
        self.con = None

    def put(self, msg):
        self.__msg = msg
        if self.con != None:
            # envia um mensagem atravez de uma conexão socket
            self.con.send(str.encode(self.__msg))

    def get(self):
        return self.__msg

    def loop(self):
        return self.new


# função esperar - Thread
def esperar(tcp, send, host='', port=5000):
    global O
    origem = (host, port)
    # cria um vinculo
    tcp.bind(origem)
    # deixa em espera
    tcp.listen(1)

    while True:
        # aceita um conexão
        con, cliente = tcp.accept()
        print('Cliente ', cliente, ' conectado!')
        # atribui a conexão ao manipulador
        send.con = con

        while True:
            # aceita uma mensagem
            msg = con.recv(1024)
            O = str(msg, 'utf-8')
            jogodavelha()
            if not msg: break




if __name__ == '__main__':
    # cria um socket
    tcp = socket(AF_INET, SOCK_STREAM)
    send = Send()
    # cria um Thread e usa a função esperar com dois argumentos
    processo = Thread(target=esperar, args=(tcp, send))
    processo.start()

    print('Iniciando o servidor de chat!')
    print('Aguarde alguém conectar!')

    msg = input()
    while True:
        send.put(msg)
        msg = input()
        jogodavelha()


    processo.join()
    tcp.close()
    exit()


