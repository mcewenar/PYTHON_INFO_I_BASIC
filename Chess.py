EMPTY = "-"
TORRE = "TORRE"
CABALLO = "CABALLO"
PEON = "PEÓN"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE #Torre blancas y negras
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
#Si deseas agregar un caballo a C4, hazlo de la siguiente manera:
tablero[4][2] = CABALLO
#Y ahora un peón a E5:
tablero[3][4] = PEON

print(tablero)