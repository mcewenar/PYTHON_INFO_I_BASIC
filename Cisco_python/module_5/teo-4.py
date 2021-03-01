#Trabajando con módulos estándar
#Antes de comenzar a revisar algunos módulos estándar de Python, veamos la función dir(). No tiene nada que ver con el comando dir de las 
#terminales de Windows o Unix. El comando dir() no muestra el contenido de un directorio o carpeta de disco, pero no se puede negar que hace 
#algo similar: puede revelar todos los nombres proporcionados a través de un módulo en particular.

#Hay una condición: el módulo debe haberse importado previamente como un todo (es decir, utilizar la instrucción import module - from module 
#no es suficiente). Tiene que ser con "from module import *""

#OJO AQUÍ:
#La función devuelve una lista ordenada alfabéticamente la cual contiene todos los nombres de las entidades disponibles en el módulo:
#dir(module)

#Nota: Si el nombre del módulo tiene un alias, debe usar el alias, no el nombre original.

#Usar la función dentro de un script normal no tiene mucho sentido, pero aún así, es posible.


#Por ejemplo, se puede ejecutar el siguiente código para imprimir los nombres de todas las entidades dentro del módulo math:

import math

for name in dir(math):
    print(name, end="\t") #On this page: commenting with #, multi-line strings with """ """, printing multiple objects, the backslash "\" 
#as the escape character, '\t', '\n', '\r', and '\\'.

#El código de ejemplo debería producir el siguiente resultado:

#__doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	atan2	atanh	ceil	copysign	
#cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	factorial	floor	fmod	frexp	fsum	gamma	hypot	isfinite	isinf	
#isnan	ldexp	
#lgamma	log	log10	log1p	log2	modf	pi	pow	radians	sin	sinh	sqrt	tan	tanh	trunc	


#¿Has notado los nombres extraños que comienzan con __ al inicio de la lista? Se hablará más sobre ellos cuando hablemos sobre los problemas 
#relacionados con la escritura de módulos propios.

#Algunos de los nombres pueden traer recuerdos de las lecciones de matemáticas, y probablemente no tendrás ningún problema en adivinar su 
#significado.

#El emplear la función dir() dentro de un código puede no parecer muy útil; por lo general, se desea conocer el contenido de un módulo en 
#particular antes de escribir y ejecutar el código.

#Afortunadamente, se puede ejecutar la función directamente en la consola de Python (IDLE), sin necesidad de escribir y ejecutar un script 
#por separado.

#Así es como se puede hacer:

#FORMA SENCILLA, SIN NECESIDAD DE IMPORTAR TODO:
import math
dir(math)

#Deberías de ver algo similar a esto:

print("---2---")

#Funciones seleccionadas del módulo math
#Comencemos con una vista previa de algunas de las funciones proporcionadas por el módulo math.

#Se han elegido algunas arbitrariamente, pero esto no significa que las funciones no mencionadas aquí sean menos significativas. 
#Tomate el tiempo para revisar las demás por ti mismo: no tenemos el espacio ni el tiempo para hablar de todas a detalle.

#El primer grupo de funciones de módulo math están relacionadas con trigonometría:

#sin(x) → el seno de x.
#cos(x) → el coseno de x.
#tan(x) → la tangente de x.
#Todas estas funciones toman un argumento (una medida de ángulo expresada en radianes) y devuelven el resultado apropiado (ten cuidado con tan() 
#- no todos los argumentos son aceptados).

#También están sus versiones inversas:

#asin(x) → el arcoseno de x.
#acos(x) → el arcocoseno de x.
#atan(x) → el arcotangente de x.
#Estas funciones toman un argumento (verifica que sea correcto) y devuelven una medida de un ángulo en radianes.


#Para trabajar eficazmente con mediciones de ángulos, el módulo math proporciona las siguientes entidades:

#pi → una constante con un valor que es una aproximación de π.
#radians(x) → una función que convierte x de grados a radianes.
#degrees(x) → actuando en el otro sentido (de radianes a grados).
#Ahora observa el código en el editor. El programa de ejemplo no es muy sofisticado, pero ¿puedes predecir sus resultados?
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
print(ar)
ad = degrees(ar)
print(ad)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


#Además de las funciones circulares (enumeradas anteriormente), el módulo math también contiene un conjunto de sus análogos hiperbólicos:

#sinh(x) → el seno hiperbólico.
#cosh(x) → el coseno hiperbólico.
#tanh(x) → la tangente hiperbólico.
#asinh(x) → el arcoseno hiperbólico.
#acosh(x) → el arcocoseno hiperbólico.
#atanh(x) → el arcotangente hiperbólico.

print("---3---")
#Funciones seleccionadas del módulo math: continuación
#Existe otro grupo de las funciones math relacionadas con la exponenciación:

#e → una constante con un valor que es una aproximación del número de Euler (e).
#exp(x) → encontrar el valor de ex.
#log(x) → el logaritmo natural de x.
#log(x, b) → el logaritmo de x con base b.
#log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
#log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).
#Nota: la función pow():

#pow(x, y) → encontrar el valor de xy (toma en cuenta los dominios).
#Esta es una función incorporada y no se tiene que importar.

#Observa el código en el editor. ¿Puedes predecir su salida?
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

print("----4----")
#Funciones seleccionadas del módulo math: continuación
#El último grupo consta de algunas funciones de propósito general como:

#ceil(x) → devuelve el entero más pequeño mayor o igual que x.
#floor(x) → el entero más grande menor o igual que x.
#trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
#factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
#hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a x e y 
#(lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
#Mira el código en el editor. Analiza el programa cuidadosamente.

#Demuestra las diferencias fundamentales entre ceil(), floor() y trunc().

#Ejecuta el programa y verifica su salida.
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))