# -Variaveis das vitórias
vit1=0
vit2=0
# -Variaveis das vitórias

#   -Menu inicial do jogo-
def menu():
    continuar=1
    while continuar:
        
        continuar = int(input("\n0. Sair \n"+
                              "1. Jogar\n"))
        if continuar:
            game()
        else:
            print("Saindo...")
            exit(0)
#   -Menu inicial do jogo-

#   -Sistema de turnos e fim do jogo-
def game():
    global vit1
    global vit2
    jogada=0
    jogadaSobrar = 8; 
    while ganhou() == 0:
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha  = int(input("\nLinha: "))
        coluna = int(input("Coluna: "))

        if board[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                board[linha-1][coluna-1]=1
            else:
                board[linha-1][coluna-1]=-1
        else:
            print("Ocupada")
            jogadaSobrar+=1

        if (jogadaSobrar>0 and ganhou()==1):
            vit1+=1
            print("\nJogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")
            print("\nVitórias:\nJogador 1:", vit1,"\nJogador 2:", vit2, "\n")
            reset()
        elif (jogadaSobrar>0 and ganhou()==-1):
            vit2+=1
            print("\nJogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")
            print("\nVitórias:\nJogador 1:", vit1,"\nJogador 2:", vit2, "\n")
            reset()
        elif(jogadaSobrar==0):
            print("\nEmpate")
            print("\nVitórias:\nJogador 1:", vit1,"\nJogador 2:", vit2, "\n")
            reset()
        

        jogada +=1
        jogadaSobrar -=1        
#   -Sistema de turnos e fim do jogo-



#   -Sistema de reset de dados-
def reset():
    for i in range(3):
        for j in range (3):
            board[i][j] = 0
    menu()
#   -Sistema de reset de dados-


def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if (soma==3):
            return 1 
        elif (soma ==-3):
            return -1

     #checando colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if (soma==3):
            return 1 
        elif (soma ==-3):
            return -1

    #checando diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if(diagonal1==3 or diagonal2==3):
        return 1 
    elif (diagonal1==-3 or diagonal2==-3):
        return -1

    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print("-", end=' | ')
            elif board[i][j] == 1:
                print("X", end=' | ')
            elif board[i][j] == -1:
                print("O", end=' | ')

        print()
                

board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

menu()