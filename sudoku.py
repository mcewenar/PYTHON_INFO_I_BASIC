#INVESTIGAR LUEGO:

#Escenario
#Como probablemente sabes, Sudoku es un rompecabezas de colocación de números jugado en un tablero de 9x9. 
#El jugador tiene que llenar el tablero de una manera muy específica:

#Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
#Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
#Cada subcuadro de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.
#Si necesitas más detalles, puedes encontrarlos aquí.

#Tu tarea es escribir un programa que:

#Lea las 9 filas del Sudoku, cada una con 9 dígitos (verifica cuidadosamente si los datos ingresados son válidos).
#Da como salida Si si el Sudoku es válido y No de lo contrario.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada de Muestra:

#295743861
#431865927
#876192543
#387459216
#612387495
#549216738
#763524189
#928671354
#154938672

#Salida de la Muestra:

#Yes

#Entrada de Muestra:

#195743862
#431865927
#876192543
#387459216
#612387495
#549216738
#763524189
#928671354
#254938671

#Salida de la Muestra

#No

#https://github.com/israelem/aceptaelreto/blob/master/codes/2017-06-05-sudokus_correctos.py
# Comprobar sudoku leído desde teclado
def f_leer_sudoku():
    r_sudoku = []
    for iteracion in range(9):
        l_str = str(input("Ingrese otra: ")).split(' ')
        r_sudoku.append([int(x) for x in l_str])
    return r_sudoku


def f_comprobar_linea(p_linea):
    return list(range(1, 10)) == sorted(p_linea)

if __name__ == '__main__':
    correcto = True
    columnas = [[] for i in range(9)]
    cuadrantes = [[] for i in range(9)]
    posicion_fila = 0
    veces = int(input("Ingresa los valores: "))
    for vez in range(veces):
        sudoku = f_leer_sudoku()
        for fila in sudoku:
            correcto = correcto and f_comprobar_linea(fila)
            posicion_columna = 0
            for casilla in fila:
                columnas[posicion_columna].append(casilla)
                posicion_cuadrante = (posicion_fila // 3) * 3 + (posicion_columna // 3)
                cuadrantes[posicion_cuadrante].append(casilla)
                posicion_columna += 1
            posicion_fila += 1
        for fila in columnas:
            correcto = correcto and f_comprobar_linea(fila)
        for fila in cuadrantes:
            correcto = correcto and f_comprobar_linea(fila)
        if correcto:
            print("SI")
        else:
            print("NO")