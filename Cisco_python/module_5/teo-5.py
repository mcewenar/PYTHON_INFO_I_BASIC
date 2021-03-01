#¿Existe aleatoriedad real en las computadoras?
#Otro módulo que vale la pena mencionar es el que se llama random.

#Ofrece algunos mecanismos que permiten operar con números pseudoaleatorios.

#Toma en cuenta el prefijo pseudo - los números generados por los módulos pueden parecer aleatorios en el sentido de que no se pueden predecir, 
#pero no hay que olvidar que todos se calculan utilizando algoritmos muy refinados.


#Los algoritmos no son aleatorios, son deterministas y predecibles. Solo aquellos procesos físicos que se salgan 
#completamente de nuestro control (como la intensidad de la radiación cósmica) pueden usarse como fuente de datos aleatorios reales. 
#Los datos producidos por computadoras deterministas no pueden ser aleatorios de ninguna manera.

#Un generador de números aleatorios toma un valor llamado semilla, lo trata como un valor de entrada, calcula un número "aleatorio" 
#basado en él (el método depende de un algoritmo elegido) y produce una nueva semilla.

#La duración de un ciclo en el que todos los valores semilla son únicos puede ser muy largo, pero no es infinito: 
#tarde o temprano los valores iniciales comenzarán a repetirse y los valores generadores también se repetirán. 
#Esto es normal. Es una característica, no un error.

#El valor de la semilla inicial, establecido durante el inicio del programa, determina el orden en que aparecerán los valores generados.

#El factor aleatorio del proceso puede ser aumentado al establecer la semilla tomando un número de la hora actual - 
#esto puede garantizar que cada lanzamiento del programa comience desde un valor semilla diferente 
#(por lo tanto, usará diferentes números aleatorios).

#Afortunadamente, Python realiza dicha inicialización al importar el módulo.

print("---2---")
#Funciones seleccionadas del módulo random
#La función general llamada random() (no debe confundirse con el nombre del módulo) produce un número flotante x entre el rango (0.0, 1.0) 
#- en otras palabras: (0.0 <= x < 1.0).

#El programa de ejemplo en el editor producirá cinco valores pseudoaleatorios, ya que sus valores están determinados por el valor semilla 
#(un valor impredecible) actual, no se pueden adivinar. Ejecuta el programa.
from random import random

for i in range(5):
    print(random())

#La función seed() es capaz de establecer la semilla del generador. Te mostraremos dos de sus variantes:

#seed() - establece la semilla con la hora actual.
#seed(int_value) - establece la semilla con el valor entero int_value.

#Hemos modificado el programa anterior; de hecho, hemos eliminado cualquier rastro de aleatoriedad del código:
from random import random, seed

seed(0)

for i in range(5):
    print(random())

#Debido al hecho de que la semilla siempre se establece con el mismo valor, la secuencia de valores generados siempre se ve igual.

#Ejecuta el programa. Esto es lo que tenemos:

#0.844421851525
#0.75795440294
#0.420571580831
#0.258916750293
#0.511274721369

#¿Y tú?

#Nota: sus valores pueden ser ligeramente diferentes si tu sistema utiliza aritmética de punto flotante más precisa o menos precisa, 
#pero la diferencia se verá bastante lejos del punto decimal.
print("---3---")

#Funciones seleccionadas del módulo random: continuación
#Si deseas valores aleatorios enteros, una de las siguientes funciones encajaría mejor:

#randrange(fin)x
#randrange(inico, fin)
#randrange(inicio, fin, incremento)
#randint(izquierda, derecha)


#Las primeras tres invocaciones generarán un número entero tomado (pseudoaleatoriamente) del rango:
#range(fin)
#range(inicio, fin)
#range(inicio, fin, incremento)
#Toma en cuenta la exclusión implícita del lado derecho.

#La última función es equivalente a randrange(izquierda, derecha+1) - genera el valor entero i, el cual cae en el rango 
#[izquierda, derecha] (sin exclusión en el lado derecho).

#Observa el código en el editor. Este programa generará una línea que consta de tres ceros y un cero o un uno en el cuarto lugar.

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

print("---4---")

#Funciones seleccionadas del módulo random: continuación
#Las funciones anteriores tienen una desventaja importante: pueden producir valores repetidos incluso si el número de invocaciones 
#posteriores no es mayor que el rango especificado.

#Observa el código en el editor. Es muy probable que el programa genere un conjunto de números en el que algunos elementos no sean únicos.
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

#Esto es lo que se obtiene al ejecutarlo:

#9,4,5,4,5,8,9,4,8,4,

#Como puedes ver, esta no es una buena herramienta para generar números para la lotería. Afortunadamente, 
#existe una mejor solución que escribir tu propio código para verificar la singularidad de los números "sorteados".


#Es una función con el nombre de - choice:

#choice(secuencia)
#sample(secuencia, elementos_a_elegir=1)
#La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.

#El segundo crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) "sorteado" de la secuencia de 
#entrada.

#En otras palabras, la función elige algunos de los elementos de entrada, devolviendo una lista con la elección. Los elementos de la 
#muestra se colocan en orden aleatorio. Nota que elementos_a_elegir no debe ser mayor que la longitud de la secuencia de entrada.

#Observa el código a continuación:

from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))

#Nuevamente, la salida del programa no es predecible. Nuestros resultados se ven así:
#4
#[3, 1, 8, 9, 10]
#[10, 8, 5, 1, 6, 4, 3, 9, 7, 2]