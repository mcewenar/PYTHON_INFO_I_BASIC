#MemoryError
#Ubicación:

#BaseException ← Exception ← MemoryError

#Descripción:

#Se produce una excepción concreta cuando no se puede completar una operación debido a la falta de memoria libre.

#Código:

# este código causa la excepción MemoryError
# advertencia: ejecutar este código puede ser crucial
# para tu sistema operativo
# ¡no lo ejecutes en entornos de producción!
#OJO CON EJECUTAR ESTO:
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')

#OverflowError
#Ubicación:

#BaseException ← Exception ← ArithmeticError ← OverflowError

#Descripción:

#Una excepción concreta que surge cuando una operación produce un número demasiado grande para ser almacenado con éxito.

#Código:

# el código imprime los valores subsequentes 
# de exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')