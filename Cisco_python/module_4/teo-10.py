#Como interactúa la función con sus argumentos (IMPORTANTE):

#Ahora descubramos como la función interactúa con sus argumentos.

#El código en editor nos enseña algo. Como puedes observar, la función cambia el valor de su parámetro. ¿Este cambio afecta el argumento?

#Ejecuta el programa y verifícalo.

def miFuncion(n):
    print("Yo obtuve", n)
    n += 1
    print("Yo ahora tengo", n)

var = 1
miFuncion(var)
print(var)

#La salida del código es:
#Yo obtuve 1
#Yo ahora tengo 2
#1


#La conclusión es obvia - al cambiar el valor del parámetro este no se propaga fuera de la función 
#(más específicamente, no cuando la variable es un valor escalar, como en el ejemplo).

#IMPORTANTE:
#Esto también significa que una función recibe el valor del argumento, no el argumento en sí. Esto es cierto para los valores escalares.

#Vale la pena revisar cómo funciona esto con las listas (¿Recuerdas las peculiaridades de asignar rodajas de listas en lugar 
#de asignar la lista entera?
#El siguiente ejemplo arrojará luz sobre el asunto:

def miFuncion(miLista1):
    print(miLista1)
    miLista1 = [0, 1]

miLista2 = [2, 3]
miFuncion(miLista2)
print(miLista2)

#La salida del código es:
#[2, 3]
#[2, 3]

#Parece ser que se sigue aplicando la misma regla.

#La diferencia se puede observar en el siguiente ejemplo:

def miFuncion(miLista1):
    print(miLista1)
    del miLista1[0] #Borra elemento 0 de miLista2

miLista2 = [2, 3]
miFuncion(miLista2)
print(miLista2)

#No se modifica el valor del parámetro miLista1 (ya se sabe que no afectará el argumento), en lugar de ello se modificará la lista 
#identificada por el.

#El resultado puede ser sorprendente. Ejecuta el código y verifícalo:

#[2, 3]
#[3]

#¿Lo puedes explicar?

#Intentémoslo:

#Si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista (Recuerda: las variables 
#que contienen listas son almacenadas de manera diferente que las escalares).
#Pero si se modifica la lista identificada por el parámetro (Nota: ¡La lista no el parámetro!), la lista reflejará el cambio.
#Es tiempo de escribir algunos ejemplos de funciones. Lo harás en la siguiente sección.



#PUNTOS CLAVES

#1. Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función. (Ejemplo 1) al menos 
#que la función defina una variable con el mismo nombre. (Ejemplo 2, y Ejemplo 3), por ejemplo:

#Ejemplo 1:

var = 2
def multByVar(x):
    return x * var

print(multByVar(7))    # salida: 14

#Ejemplo 2:

def mult(x):
    var = 5
    return x * var

print(mult(7))    # salida: 35


#Ejemplo 3:

def multip(x):
    var = 7
    return x * var

var = 3
print(multip(7))    # salida: 49

#2. Una variable que existe dentro de una función tiene un alcance solo dentro del cuerpo de la función (Ejemplo 4), por ejemplo:

#Ejemplo 4:

def sum(x):
    var = 7
    return x + var

print(sum(4))    # salida: 11

#print(var) # NameError

#3. Se puede emplear la palabra reservada global seguida por el nombre de una variable para que el alcance de la variable sea global, 
#por ejemplo:

var = 2
print(var)    # salida: 2

def retVar():
    global var
    var = 5
    return var

print(retVar())    # salida: 5

print(var)    # salida: 5

#EJERCICIOS:
#Ejercicio 1
print("------2------")
#¿Qué ocurrirá cuando se intente ejecutar el siguiente código?

def message():
    alt = 1
    print("Hola, mundo!")

#print(alt) NO ESTÁ DEFINIDO POR FUERA

#Se arrojará una excepción NameError(NameError: name 'alt' is not defined)


#Ejercicio 2

#¿Cuál es la salida del siguiente fragmento de código?

a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)
#2
#1

#Ejercicio 3

#¿Cuál es la salida del siguiente fragmento de código?
print("------3------")
a = 1
def fun():
    global a
    a = 2
    print(a)
print(a)
fun()
print(a) #Después de invocar la función, la variable a se convierte en 2, hasta que no se redefina por tercera vez.
a = 3 #SE REDEFINE NUEVAMENTE LA VARIABLE A, PERO, DE NO REDEFINIRSE, PUES EL VALOR SERÍA IGUAL A 2 (GLOBAL VARIABLE)
print(a)
#Salida:
#2
#3

print("------4------")
#Ejercicio 4
#¿Cuál es la salida del siguiente fragmento de código?

a = 1
def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)