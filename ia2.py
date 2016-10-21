def IA (matriz):
    if (matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == ' ') or (matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == ' ') or (matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == ' '):
        jogada = 'c3'
    elif (matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == ' ') or (matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == ' ') or (matriz[2][2] == 'O' and matriz[2][1] == 'O' and matriz[2][0] == ' '):
        jogada = 'a3'
    elif (matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == ' '):
        jogada = 'b3'
    elif (matriz[0][2] == 'O' and matriz[0][1] == 'O' and matriz[0][0] == ' ') or (matriz[2][0] == 'O' and matriz[1][0] == 'O' and matriz[0][0] == ' ') or (matriz[2][2] == 'O' and matriz[1][1] == 'O' and matriz[0][0] == ' '):
        jogada = 'a1'
    elif (matriz[1][2] == 'O' and matriz[1][1] == 'O' and matriz[1][0] == ' ') or (matriz[0][0] == 'O' and matriz[2][0] == 'O' and matriz[1][0] == ' '):
        jogada = 'a2'
    elif (matriz[2][1] == 'O' and matriz[1][1] == 'O' and matriz[0][1] == ' ') or (matriz[0][0] == 'O' and matriz[0][2] == 'O' and matriz[0][1] == ' '):
        jogada = 'b1'
    elif (matriz[2][2] == 'O' and matriz[1][2] == 'O' and matriz[0][2] == ' ') or (matriz[2][0] == 'O' and matriz[1][1] == 'O' and matriz[0][2] == ' ') or (matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == ' '):
        jogada = 'c1'
    elif (matriz[1][0] == 'O' and matriz[1][2] == 'O' and matriz[1][1] == ' ') or (matriz[0][1] == 'O' and matriz[2][1] == 'O' and matriz[1][1] == ' ') or (matriz[0][0] == 'O' and matriz[2][2] == 'O' and matriz[1][1] == ' ') or (matriz[0][2] == 'O' and matriz[2][0] == 'O' and matriz[1][1] == ' '):
        jogada = 'b2'
    elif (matriz[2][0] == 'O' and matriz[2][2] == 'O' and matriz[2][1] == ' ') or (matriz[0][2] == 'O' and matriz[2][2] == 'O' and matriz[1][2] == ' ') or (matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == ' '):
        jogada = 'c2'
    elif (matriz[0][0] == 'X' and matriz[2][2] == 'X') or (matriz[0][2] == 'X' and matriz[2][0] == 'X'):
        if matriz[0][1] == ' ':
            jogada = 'b1'
        elif matriz[1][0] == ' ':
            jogada = 'a2'
        elif matriz[1][2] == ' ':
            jogada = 'c2'
        elif matriz[2][1] == ' ':
            jogada = 'b3'
    elif (matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == ' ') or (matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == ' ') or (matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == ' '):
        jogada = 'c3'
    elif (matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == ' ') or (matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == ' ') or (matriz[2][2] == 'X' and matriz[2][1] == 'X' and matriz[2][0] == ' '):
        jogada = 'a3'
    elif (matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == ' '):
        jogada = 'b3'
    elif (matriz[0][2] == 'X' and matriz[0][1] == 'X' and matriz[0][0] == ' ') or (matriz[2][0] == 'X' and matriz[1][0] == 'X' and matriz[0][0] == ' ') or (matriz[2][2] == 'X' and matriz[1][1] == 'X' and matriz[0][0] == ' '):
        jogada = 'a1'
    elif (matriz[1][2] == 'X' and matriz[1][1] == 'X' and matriz[1][0] == ' ') or (matriz[0][0] == 'X' and matriz[2][0] == 'X' and matriz[1][0] == ' '):
        jogada = 'a2'
    elif (matriz[2][1] == 'X' and matriz[1][1] == 'X' and matriz[0][1] == ' ') or (matriz[0][0] == 'X' and matriz[0][2] == 'X' and matriz[0][1] == ' '):
        jogada = 'b1'
    elif (matriz[2][2] == 'X' and matriz[1][2] == 'X' and matriz[0][2] == ' ') or (matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == ' ') or (matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == ' '):
        jogada = 'c1'
    elif (matriz[1][0] == 'X' and matriz[1][2] == 'X' and matriz[1][1] == ' ') or (matriz[0][1] == 'X' and matriz[2][1] == 'X' and matriz[1][1] == ' ') or (matriz[0][0] == 'X' and matriz[2][2] == 'X' and matriz[1][1] == ' ') or (matriz[0][2] == 'X' and matriz[2][0] == 'X' and matriz[1][1] == ' '):
        jogada = 'b2'
    elif (matriz[2][0] == 'X' and matriz[2][2] == 'X' and matriz[2][1] == ' ') or (matriz[0][2] == 'X' and matriz[2][2] == 'X' and matriz[1][2] == ' ') or (matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == ' '):
        jogada = 'c2'

    else:
        if matriz[1][1] == ' ':
            jogada = 'b2'
        elif matriz [1][1] != ' ':
            if matriz[0][0] == ' ':
                jogada = 'a1'
            elif matriz[0][2] == ' ':
                jogada = 'c1'
            elif matriz[2][0] == ' ':
                jogada = 'a3'
            elif matriz[2][2] == ' ':
                jogada = 'c3'
    return (jogada)