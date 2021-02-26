#Escenario
#Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. 
#Para hacerlo más fácil, Hemos decidido simplificar el juego. Aquí están nuestras reglas:

#La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
#El usuario (por ejemplo, tu) jugará utilizando las 'O's.
#El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
#Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
#El usuario ingresa su movimiento introduciendo el numero de cuadro elegido. El numero debe de ser valido, 
#por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
#El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, 
#el juego termina en empate, tu ganas, o la maquina gana.
#La maquina responde con su movimiento y se verifica el estado del juego.
#No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, 
#eso es suficiente para este juego.
#El ejemplo del programa es el siguiente:

#+-------+-------+-------+
#|       |       |       |
#|   1   |   2   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 1
#+-------+-------+-------+
#|       |       |       |
#|   O   |   2   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 8
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 4
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 7
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#¡Has Ganado!

#Requerimientos
#Implementa las siguientes características:

#El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos 
#(la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

#board[fila][columna]


#Escenario
#Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. 
#Para hacerlo más fácil, Hemos decidido simplificar el juego. Aquí están nuestras reglas:

#La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
#El usuario (por ejemplo, tu) jugará utilizando las 'O's.
#El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
#Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
#El usuario ingresa su movimiento introduciendo el numero de cuadro elegido. El numero debe de ser valido, 
#por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
#El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, 
#el juego termina en empate, tu ganas, o la maquina gana.
#La maquina responde con su movimiento y se verifica el estado del juego.
#No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, 
#eso es suficiente para este juego.
#El ejemplo del programa es el siguiente:

#+-------+-------+-------+
#|       |       |       |
#|   1   |   2   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 1
#+-------+-------+-------+
#|       |       |       |
#|   O   |   2   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   8   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 8
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   6   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   4   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 4
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   3   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   7   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#Ingresa tu movimiento: 7
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   X   |   X   |
#|       |       |       |
#+-------+-------+-------+
#|       |       |       |
#|   O   |   O   |   9   |
#|       |       |       |
#+-------+-------+-------+
#¡Has Ganado!

#Requerimientos
#Implementa las siguientes características:

#El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos 
#(la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

#board[fila][columna]


#Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro 
#(dicho cuadro se considera como libre).
#La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
#Implementa las funciones definidas para ti en el editor.

#Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). 
#El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

#Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

from random import randrange
#board[fila][columna]


def displayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

def enterMove(board):
    while True:
        try:
            o = int(input("Ingrese el la casilla que desea (1-9): "))
            if o < 1 or o > 9:
                print("Valor fuera de rango")
                continue
            elif str(o) not in board[0] and str(o) not in board[1] and str(o) not in board[2]: #SI EL STRING DE NÚMERO, NO SE ENCUENTRA, 
                #QUIERE DECIR QUE HAY UNA X O UNA O, POR TANTO, ESTÁ OCUPADO.
                print("Esta casilla está ocupada")
                continue
            elif o == 1:
                board[0][0]= "O"
            elif o == 2:
                board[0][1]= "O"
            elif o == 3:
                board[0][2]= "O"
            elif o == 4:
                board[1][0]= "O"
            elif o == 6:
                board[1][2]= "O"
            elif o == 7:
                board[2][0]= "O"
            elif o == 8:
                board[2][1]= "O"
            elif o == 9:
                board[2][2]= "O"
            break
        #FORMA ÓPTIMA:
            for row in range(0,3):
                for column in range(0,3):
                    if board[row][column]==str(o):
                        board[row][column]= "O"
        except ValueError:
            print("No se permite ingresar carácteres")
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

def makeListOfFreeFields(board):
    global espacios
    espacios=[ ]
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == "X" or board[row][column] == "O":
                pass
            else:
                espacios.append(([row],[column]))
                #tuple(espacios)
                #print(type(espacios))
    print(espacios)
    #return espacios
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

def victoryFor(board, sign):
    if sign == "O":
        print("Probando que el jugador es el ganador")
    else:
        print("Probando si el computador ha ganado")
    if board[0][0] == sign and board[0][1] == sign and board[0][2]== sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2]== sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2]== sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0]== sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1]== sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2]== sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2]== sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0]== sign:
        return True 
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

def drawMove(board):
    while True:
        row = randrange(3)
        column = randrange(3)

        if ([row],[column]) not in espacios: #makeListOfFreeFields(board)
            continue
        else:
            board[row][column]= "X"
            return
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
board = [["1","2","3"],["4","X","6"],["7","8","9"]]
num_movi = 1
jugador = "O"
maquina = "X"


print("Bienvenido al juego de Tic-Tac-Toe")
print("Estado actual del juego: ")
displayBoard(board)
print()
while num_movi < 9:
#Turno del jugador
    enterMove(board)
    num_movi += 1
    displayBoard(board)
    if victoryFor(board,jugador)== True:
        print("El", jugador, "ha ganado")
        break 
    else: 
        print("Aquí hay una lista de espacios libres en el tablero")
        makeListOfFreeFields(board)
        print()
        displayBoard(board)
#Aquí entra el turno de la máquina        
    print()
    print("Turno de la máquina de hacer su movimiento")
    drawMove(board)
    num_movi += 1
    displayBoard(board)
    print()
    if victoryFor(board,maquina) == True:
        print("El", maquina, "ha ganado")
        break 
    else:
        print("Lista de los espacios vacíos en el tablero")
        makeListOfFreeFields(board)
        print()
        displayBoard(board)
else: 
    print("Empate\n")
print("Gracias por jugar. Vuelva pronto")