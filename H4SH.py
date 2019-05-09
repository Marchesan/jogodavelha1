pos = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

    #definindo uma funcao para as posicoes

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def mostra_tabuleiro():
    print("     |     |     ")
    print("",pos[0][0],"  | ",pos[0][1]," | ",pos[0][2],"")
    print("_____|_____|_____")
    print("     |     |     ")
    print("",pos[1][0],"  | ",pos[1][1]," | ",pos[1][2],"")
    print("_____|_____|_____")
    print("     |     |     ")
    print("",pos[2][0],"  | ",pos[2][1]," | ",pos[2][2],"")
    print("     |     |     ")

    #definindo uma funcao para o tabuleiro

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def casa_ocupada(posicao):
    if posicao == "1":
        if pos[0][0] != "1":
            print("Casa ja ocupada")
            return True

    elif posicao == "2":
        if pos[0][1] != "2":
            print("Casa ja ocupada...")
            return True

    elif posicao == "3":
        if pos[0][2] != "3":
            print("Casa ja oculpada...")
            return True

    elif posicao == "4":
        if pos[1][0] != "4":
            print("Casa ja oculpada...")
            return True

    elif posicao == "5":
        if pos[1][1] != "5":
            print("Casa ja oculpada...")
            return True

    elif posicao == "6":
        if pos[1][2] != "6":
            print("Casa ja oculpada...")
            return True

    elif posicao == "7":
        if pos[2][0] != "7":
            print("Casa ja oculpada...")
            return True

    elif posicao == "8":
        if pos[2][1] != "8":
            print("Casa ja oculpada...")
            return True

    elif posicao == "9":
        if pos[2][2] != "9":
            print("Casa ja oculpada...")
            return True
    
    return False

    #definindo funcoes para checar se as casas estao ocupadas

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def tem_ganhador():
    horizontal3 = [pos[2][0],pos[2][1],pos[2][2]]
    horizontal2 = [pos[1][0],pos[1][1],pos[1][2]]
    horizontal1 = [pos[0][0],pos[0][1],pos[0][2]]
    vertical1 = [pos[2][0],pos[1][0],pos[0][0]]
    vertical2 = [pos[2][1],pos[1][1],pos[0][1]]
    vertical3 = [pos[2][2],pos[1][2],pos[0][2]]
    diagonal1 = [pos[2][0],pos[1][1],pos[0][2]]
    diagonal2 = [pos[2][2],pos[1][1],pos[0][0]]

    if horizontal1 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif horizontal1 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif horizontal2 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif horizontal2 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif horizontal3 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif horizontal3 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif vertical1 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif vertical1 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif vertical2 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif vertical2 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif vertical3 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif vertical1 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif diagonal1 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif diagonal1 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True
    elif diagonal2 == ["X","X","X"]:
        print ("PLAYER 1 Ganhou!")
        return True
    elif diagonal2 == ["O","O","O"]:
        print ("PLAYER 2 Ganhou!")
        return True

    return False

    #definindo uma funcao para checar se alguem ganhou

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def jogador1():
    posicao = input("Digite a posição onde X vai jogar: ")
    while ((posicao != "1") and (posicao != "2") and (posicao != "3") and (posicao != "4") and (posicao != "5") and (posicao != "6") and (posicao != "7") and (posicao != "8") and (posicao != "9")) or casa_ocupada(posicao):
        print("casa invalida!")
        posicao = input("Digite a posição onde X vai jogar: ")
    if posicao == "1":
        pos[0][0] = "X"
    elif posicao == "2":
        pos[0][1] = "X"
    elif posicao == "3":
        pos[0][2] = "X"
    elif posicao == "4":
        pos[1][0] = "X"
    elif posicao == "5":
        pos[1][1] = "X"
    elif posicao == "6":
        pos[1][2] = "X"
    elif posicao == "7":
        pos[2][0] = "X"
    elif posicao == "8":
        pos[2][1] = "X"
    elif posicao == "9":
        pos[2][2] = "X"

    #definindo uma funcao para marcar a casa desejada pelo usuario

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def jogador2():
    posicao = str(input("Digite a posição onde O vai jogar: "))
    while (posicao != "1") and (posicao != "2") and (posicao != "3") and (posicao != "4") and (posicao != "5") and (posicao != "6") and (posicao != "7") and (posicao != "8") and (posicao != "9"):
        print("numero invalido!")
        posicao = str(input("Digite a posição onde O vai jogar: "))
    if posicao == "1":
        pos[0][0] = "O"
    elif posicao == "2":
        pos[0][1] = "O"
    elif posicao == "3":
        pos[0][2] = "O"
    elif posicao == "4":
        pos[1][0] = "O"
    elif posicao == "5":
        pos[1][1] = "O"
    elif posicao == "6":
        pos[1][2] = "O"
    elif posicao == "7":
        pos[2][0] = "O"
    elif posicao == "8":
        pos[2][1] = "O"
    elif posicao == "9":
        pos[2][2] = "O"

    #definindo uma funcao para marcar a casa desejada pelo usuario

#----------------------------------------------------------------------------------------------------------------------------------------------------------

print ("                                               ")
print (" Olá seja bem vindo ao H4SH Game! ")
print (" Para jogar basta digitar o número que corresponde a posição desejada e pressionar enter.")
print (" O primeiro a jogar fica com o 'X' e o segundo com o 'O'. Boa Sorte! ")
print ("                                         ")
print("Meus criadores foram Gabriel Bergamo e Mateus Marchesan...porem só consegui pela ajuda dos professores Tiago Mazzutti e Hewerton de Oliveira...")

#introducao

#----------------------------------------------------------------------------------------------------------------------------------------------------------

contador = 0
decisao = str(input("Digite j para jogar e s para sair: "))
while decisao == "j":
    pos = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]    
    while True:
        mostra_tabuleiro()
        jogador1()
        if tem_ganhador():
            mostra_tabuleiro()
            break
        else:
            contador = contador + 1
        if contador == 9:
            mostra_tabuleiro()
            print("Deu velha...")
            break
        mostra_tabuleiro()
        #jogador 2
        jogador2()
        if tem_ganhador():
            mostra_tabuleiro()
            break
        else:
            contador = contador + 1
        if contador == 9:
            mostra_tabuleiro()
            print("Deu velha...")
            break
    decisao = str(input("Digite j para jogar e s para sair: "))
else:
    print("OK entao...")

#uso de todas as funcoes criadas ateriormente, fazendo o jogo funcionar

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 1 - Mostrar Tabuleiro
# 2 - Pede a posicao que deseja jogar
# 3 - Ver se a posicao está diponivel
# 4 - Marcar a posicao
# 5 - Verificar se teve ganhador ou se deu velha
