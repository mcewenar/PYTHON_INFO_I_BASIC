#Algunas funciones simples: factoriales
#La siguiente función a definir calcula factoriales. ¿Recuerdas cómo se calcula un factorial?

#0! = 1 (¡Si!, es verdad.)
#1! = 1
#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4
#:
#:
#n! = 1 * 2 ** 3 * 4 * ... * n-1 * n


#Se expresa con un signo de exclamación, y es igual al producto de todos los números naturales previos al argumento o número dado.

#Escribamos el código. Creemos una función con el nombre factorialFun. Aquí esta el código:

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6): # probando
    print(n,"--->", factorialFun(n))

#Observa como se sigue el procedimiento matemático, y como se emplea el bucle for para encontrar el producto.

#Estos son los resultados obtenidos de un código de prueba:

#1 1
#2 2
#3 6
#4 24
#5 120