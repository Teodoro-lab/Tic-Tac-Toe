from random import *
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


DisplayBoard(board)

def mov():
    fil = int(input("Ingrese su fila: "))
    col = int(input("Ingrese su columna: "))
    board[fil][col] = "o"
    condition = True
    while condition:
        fil_mach = randrange(0, 2)
        col_mach = randrange(0, 2)
        if type(board[fil_mach][col_mach]) == int:
            board[fil_mach][col_mach] = "x"
            break
        else:
            continue
    DisplayBoard(board)


def cel_W():
    cont = 0
    for x in range(3):
        for i in range(3):
            if type(board[x][i]) == int:
                cont += 1
    if cont == 0:
        print("Empataste\n", DisplayBoard(board))
    return cont


def win():
    contador = 0
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == "o":
            contador += 3
            break
        elif board[c][0] == board[c][1] == board[c][2] == "o":
            contador += 3
            break
        elif board[0][0] == board[1][1] == board[2][2]=="o":
            contador += 3
            break
        elif board[0][2] == board[1][1] == board[2][0] == "o":
            contador += 3
            break
    if contador == 3:
        print("Ganaste\n", DisplayBoard(board))
    else:
        return None


for movements in range(9):
    if win() == None and cel_W() != 0:
        mov()
    if win() != None or cel_W() == 0:
        print("Se acabó el juego")
        break

