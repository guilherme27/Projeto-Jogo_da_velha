import time
import os

def local():
    return True
def web():
    return True
def ranking():
    return True
def maquina():
    return True

resposta = 'não'

game_over = 'não'
while game_over == 'não':
    print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n'
          'BBBBBBSrBBBr,.,LBBBBF:..:PBBBOi..:kBBBBBBii:::SBBBBB:5BBBBBBrYBBBBZ:Bri::::ZB:MBBBBPiBBBBLuBBBN,BBBBBBBBBBBBB\n'
          'BBBBBB: BM .kZU  BB. YEZv uBL r007 .BBBBM rk57 .BBB.  BBBBBBr BBBB .B ;OZ0PBM PBBBBi BBBB  BBB   BBBBBBBBBBBB\n'
          'BBBBBBr B  BBBBB iB BBBBBMBB uBBBBB NBBBB BBBBB EB0 B; BBBBBB  BBr BB ;k1UUBB GBBBBJ J77Y .BB..B 7BBBBBBBBBBB\n'
          'BBBBBBY B .BBBBB :B BBB::  B GBBBBB kBBBB MBBBB EB  Y; 7BBBBBB SB MBB ;FUJjBB MBBBBU UYY2 ,BM iL  BBBBBBBBBBB\n'
          'BBB LB, BM rBBBi BB  EBBB  Br 5BBG  BBBBB 2BME  B, BBB5 PBBBBBU  iBBB 5BBBBBB 5BOMBu BBBB  B rBBB  BBBBBBBBBB\n'
          'BBB7 :,BBBB, ..iBBBB7...,LBBB5....YBBBBBB....:jBB.BBBBB::BBBBBB;.BBBB:,:,..kB.....BM,BBBBruB.BBBBB XBBBBBBBBB\n'
          'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
    print('                                                         . .:, ...:.::. .                                   \n     '
          '                                                    ,.::::,:::::,,,,:::,                                  \n     '
          '                                                   .::,,,...........,,,,:.                                \n     '
          '                                                ..:,,...................::                                \n     '
          '                                               .::,.........::...........,::                              \n     '
          '                                             :i:...: ii,J::L7:Lr:........,:                               \n     '
          '                                               : .,rvi;i:::: .,.7L.........,,                             \n     '
          '                                                 ,i. .      ..  ii.........,.                             \n     '
          '                                                :,.,i::.::::::,.i,:........,                              \n     '
          '                                           ,i.. .:vi..7,      .FN7L,........                              \n     '
          '                                            ..  .:  .. :.    .:.,LXriv:..,i                               \n     '
          '                                              .:j, ...i.:i::i:    :7:.L:,:                                \n     '
          '                                               ..r:::iJ,..,,....  .i. ,.                                  \n     '
          '                                               :..:J: ,,..,....,,. ii.,                                   \n     '
          '                                              .:.. ,:rM: ..,...:UriL7                                     \n     '
          '                                               ,.... 5Bq ...... :YBX7r                                    \n     '
          '                                               ,.... 1BB: ......L7Lv                                      \n     '
          '                                               :...,:: .7.......: .7U.                                    \n     '
          '                                              .,...,.   .:...... .Liii7,                                  \n     '
          '                                             .:................. Jr:,:7Yi.                                \n     '
          '                                             ::................ v;::.:7r. r.                              \n     '
          '                                             ,r...::...ii......i7.,;,i::i;L::                             \n     '
          '                                              ,:,..riii:......,L.:: :i.:.:L..j:                           \n     '
          '                                                ;:............j;,.i  r:r7:; i7,i.                         \n     '
          '                                                 ,...........Y7::,ii:rr:.i..L::rr.                        \n     '
          '                                                 :..........i7;:..iiir.    :i.,r, i                       \n     '
          '                                                 L7........r: ...7i.i7: .  . i:rr77:                      \n     '
          '                                                .rU:......ii  :7.,:,,::....7.:.rrr:;r                     \n     '
          '                                                rr,...,..ri ..,.i:,,.,ri:,,:r:i:i:.iYL                    \n     '
          '                                               i:7......77::7..,:::ri.;7:. ,:::.:r.iir;                   \n     '
          '                                              r7:ri ..:Y,,.:7. ir.:r:,::, ir:,.:: ii.::i                  \n     '
          '                                            .v:::i7:7:,i.;7:;.:7  :::.:r7:::ii,,i .i,77r,                 \n     '
          '                                           /7::r;::,i:.ir:.i..7:::i::,r  ::ri::,i::rr::;i                 \n     '
          '                                          ,, ,,ir:..ii:r,  . :r..i. ,:.  ,:rr:..iiir.  ..i                \n     '
          '                                         :7i:   ...ri.i7: .  ..::;iii:i:,   : ,ri.i7. . .:.               \n     '
          '                                       :7:r7r:. :7.,:.,::. . r.:.;rr,,rri,  ir.::.:::.. .7,               \n     '
          '                                     :77,,rr. ..,.r:,..,ri:.,:r::ii:.:r;  ...:r,...:r::.:i7;              \n     '
          '                                   :L;:7:,i:i:r..,:::;;.i7:. .::i.:r.:::i:r .,:::ri.r7:. ,:7i             \n     '
          '                                .7vi,:i.,r.,.:7: i7.,ri,::, :7:,.:: :;:r.i7. ir.:r:,::. ir::i:            \n     '
          '                              ,riiii:.;  ;.ir:;..L. :::.:;v::::i,.i  ii5:,r :r .::,,:r7,::i;,r:           \n     '
          '                            :.i:ir::.:i,iri,i: ri,:ii:.r. ::r;::.i:,iL7,i..7:::ii:,7  ::rii::v            \n     '
          '                           ,i: ,:;ri..:iir,  . ,r,.i, .:,  ,:rr:..ii:ir. . :r.,i. ,:,  ,:rr:.:7r          \n     '
          '                          .v;:,.  .. 77iJ17.,   .,:ii:i:::,...:..i:,i:7..  ..::ri:i:::.   : :i::v.        \n     '
          '                          ,:;7r:  ,Uiir,,,:::i,r.,.iir:.iri:. :r.::.:.7.  .r.:,rrr,:rri.. i: iiiL:        \n     '
          '                           ;rr,.:::.r,.. .::.,i7j;::i:.:rr  ..,,r,,...2:..,ii,::i,.:ri  .:iYYir.          \n     '
          '                            rL7i;. .,:,ii,i7i.  :rYri7.,i:i:r...:::ii.FY;, ,i7L:iY:rLv7;;:.i7.:;          \n     '
          '                            :..,r: :7,,ri.::. .r:..,i:7J::,i7. :r.:r:.ii:.7U.,:,,,......   .Y iL,         \n     '
          '                         .r,:;,i: L, ,::.:iv,:::i:.i  r:7Lrj:iUi:r7:.,ir.:7        ........i :i:          \n     '
          '                          rrrr:;: i;,:iii.r: ::ir::.i:.ii::i, ri::ii:.7. :,J ...............v:irr,        \n     '
          '                         7i;:. . .7:.:: .:,  .:rr:..ii:;:  . :r..:. .:,  .:2................Y:  :;        \n     '
          '                        :i:ri .  ...:;;,i::,.. .:..ii,ir, .  ...:;i,i::,.  r: ............. Lr::ri        \n     '
          '                       .Y,:::. . i.:::r7:.;7r:. .7.:i.:::... i.:,ir7:.r7r, .r ............. L;r7,:        \n     '
          '                      r,. .:i.,.ir:,ii:.,;r.  .:,r,.. ,i:..,;;,,ii:.:rr   .Y...............Yii,,r         \n     '
          '                      .i::i:ivr,  :ir:.r,,rii,;...:::ii,rvi. .:ir,:r.:iii,; L...............J.:;.L:       \n     '
          '                      U:.r;,::, .ri,.,:,:r,,,:7: :7,:ri.::. ,r:,.,:.:r.,,i7.r..............,7.:.iv,       \n     '
          '                     ir .::.::v,,i:i:.;  r.:i,r. L, ,::,:i7.:::i,:i .i.i:,;:: ..............7:: :r.       \n     ')


    input('Precione enter para continuar!')
    os.system('cls')
    while resposta == 'não':
        try:
            quantidade_jogador = int(input(' 1 - Jogar com 2 jogadores \n 2 - Jogar com a maquina \n 3 - Acessar ranking\n '))
            if quantidade_jogador == 1:
                time.sleep(1)
                os.system('cls')
                try:
                    quantidade_jogador = int(input(' 1 - Jogar localmente \n 2 - Jogar em rede\n '))
                    if quantidade_jogador == 1:
                        from JogoBETA import *
                        resposta = 'sim'
                    elif quantidade_jogador == 2:
                        web()
                        resposta = 'sim'
                except ValueError:
                    print('Informe um valor válido\n ')
            elif quantidade_jogador == 2:
                maquina()
                resposta = 'sim'
            elif quantidade_jogador == 3:
                ranking()
                resposta = 'sim'
            else:
                print('\nInforme um dos valores citados acima\n')
                time.sleep(1)
                os.system('cls')
        except ValueError:
            print('\nInforme um número citado acima\n ')
            time.sleep(1)
            os.system('cls')
    game_over = 'sim'
input('Pressione enter para finalizar.')