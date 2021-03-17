#Índice del Módulo de Python
#Aquí solo hemos cubierto los conceptos básicos de los módulos de Python. Los módulos de Python conforman su propio universo, en el que Python 
#es solo una galaxia, y nos aventuraríamos a decir que explorar las profundidades de estos módulos puede llevar mucho más tiempo que 
#familiarizarse con Python "puro".

#Además, la comunidad de Python en todo el mundo crea y mantiene cientos de módulos adicionales utilizados en aplicaciones muy específicas 
#como la genética, la psicología o incluso la astrología.

#Estos módulos no están (y no serán) distribuidos junto con Python, o a través de canales oficiales, lo que hace que el universo de Python 
#sea más amplio, casi infinito.

#Puedes leer sobre todos los módulos estándar de Python aquí: 
# IMPORTANTE: https://docs.python.org/3/py-modindex.html.

#No te preocupes, no necesitarás todos estos módulos. Muchos de ellos son muy específicos.

#Todo lo que se necesita hacer es encontrar los módulos que se desean y aprender a cómo usarlos. Es fácil.

print("---2---")

#¿Qué es un paquete?
#Escribir tus propios módulos no difiere mucho de escribir scripts comunes.

#Existen algunos aspectos específicos que se deben tomar en cuenta, pero definitivamente no es algo complicado. Lo verás pronto.


#Resumamos algunos aspectos importantes:

#Un módulo es un contenedor lleno de funciones - puedes empaquetar tantas funciones como desees en un módulo y distribuirlo por todo el mundo.
#Por supuesto, no es una buena idea mezclar funciones con diferentes áreas de aplicación dentro de un módulo (al igual que en una biblioteca: 
#nadie espera que los trabajos científicos se incluyan entre los cómics), así que se deben agrupar las funciones cuidadosamente y 
#asignar un nombre claro e intuitivo al módulo que las contiene (por ejemplo, no le des el nombre videojuegos a un módulo que contiene funciones 
#estinadas a particionar y formatear discos duros).
#Crear muchos módulos puede causar desorden: tarde que temprano querrás agrupar tus módulos de la misma manera que previamente has agrupado 
#funciones: ¿Existe un contenedor más general que un módulo?.
#Sí lo hay, es un paquete: en el mundo de los módulos, un paquete juega un papel similar al de una carpeta o directorio en el mundo de los 
#archivos.
print("----3----")
#Tu primer módulo
#En esta sección, trabajarás localmente en tu máquina. Comencemos desde cero, de la siguiente manera:

#Se necesitan dos archivos para realizar estos experimentos. Uno de ellos será el módulo en sí. Está vacío ahora. No te preocupes, 
#lo vas a llenar con el código real.

#El archivo lleva por nombre module.py. No muy creativo, pero es simple y claro.

#El segundo archivo contiene el código usando el nuevo módulo. Su nombre es main.py.

#Su contenido es muy breve hasta ahora:

#Nota: ambos archivos deben estar ubicados en la misma carpeta. Te recomendamos crear una carpeta nueva y vacía para ambos archivos. 
#Esto hará que las cosas sean más fáciles.

#Inicia el IDLE y ejecuta el archivo main.py.¿Que ves?

#No deberías ver nada. Esto significa que Python ha importado con éxito el contenido del archivo module.py. 
#No importa que el módulo esté vacío por ahora. El primer paso ya está hecho, pero antes de dar el siguiente paso, 
#queremos que eches un vistazo a 
#la carpeta en la que se encuentran ambos archivos.

#¿Notas algo interesante?

#Ha aparecido una nueva subcarpeta, ¿puedes verla? Su nombre es __pycache__. Echa un vistazo adentro. ¿Que ves?

#Hay un archivo llamado (más o menos) module.cpython-xy.pyc donde x y y son dígitos derivados de tu versión de Python 
#(por ejemplo, serán 3 y 4 si utilizas Python 3.4).

#El nombre del archivo es el mismo que el de tu módulo. La parte posterior al primer punto dice qué implementación de 
#Python ha creado el archivo (CPython) y su número de versión. La ultima parte (pyc) viene de las palabras Python y 
#compilado.

#Puedes mirar dentro del archivo: el contenido es completamente ilegible para los humanos. Tiene que ser así, 
#ya que el archivo está destinado solo para uso de Python.

#Cuando Python importa un módulo por primera vez, traduce el contenido a una forma "semi" compilada. 
#El archivo no contiene código en lenguaje máquina: es código semi-compilado interno de Python, listo para ser 
#ejecutado por el intérprete de Python. Como tal archivo no requiere tantas comprobaciones como las de un archivo fuente, 
#la ejecución comienza más rápido y también se ejecuta más rápido.

#Gracias a eso, cada importación posterior será más rápida que interpretar el código fuente desde cero.

#Python puede verificar si el archivo fuente del módulo ha sido modificado (en este caso, el archivo pyc será reconstruido) 
#o no (cuando el archivo pyc pueda ser ejecutado al instante). Este proceso es completamente automático y transparente, 
#no se tiene que estar tomando en cuenta.
print("---4---")

#Tu primer módulo: continuación
#Ahora hemos puesto algo en el archivo del módulo:

#¿Puedes notar alguna diferencia entre un módulo y un script ordinario? No hay ninguna hasta ahora.

#Es posible ejecutar este archivo como cualquier otro script. Pruébalo por ti mismo.

#¿Que es lo que pasa? Deberías de ver la siguiente línea dentro de tu consola:

#"Me gusta ser un módulo".

#Volvamos al archivo main.py:


#Ejecuta el archivo. ¿Que ves? Con suerte, verás algo como esto:

#Me gusta ser un módulo.
#IMPORTANTE:
#¿Qué significa realmente?

#Cuando un módulo es importado, su contenido es ejecutado implícitamente por Python. 
#Le da al módulo la oportunidad de inicializar algunos de sus aspectos internos 
#(por ejemplo, puede asignar a algunas variables valores útiles).
# Nota: la inicialización se realiza solo una vez, 
# cuando se produce la primera importación, por lo que las asignaciones realizadas por el módulo no se repiten innecesariamente.

#Imagina el siguiente contexto:

#Existe un módulo llamado mod1.
#Existe un módulo llamado mod2 el cual contiene la instrucción import mod1.
#Hay un archivo principal que contiene las instrucciones import mod1 y import mod2.
#A primera vista, se puede pensar que mod1 será importado dos veces - afortunadamente, solo se produce la primera importación. 
#Python recuerda los módulos importados y omite silenciosamente todas las importaciones posteriores.

#OJO AQUÍ (IMPORTANTE):
#Python puede hacer mucho más. También crea una variable llamada __name__.
#Además, cada archivo fuente usa su propia versión separada de la variable, no se comparte entre módulos.
#Te mostraremos cómo usarlo. Modifica el módulo un poco:

#Ahora ejecuta el archivo module.py. Deberías ver las siguientes líneas:

#Me gusta ser un módulo.
#__main__

#Ahora ejecuta el archivo main.py. ¿Y? ¿Ves lo mismo que nosotros?
#Me gusta ser un módulo.
#module

#Podemos decir que:

#Cuando se ejecuta un archivo directamente, su variable __name__ se establece a __main__.
#Cuando un archivo se importa como un módulo, su variable __name__ se establece al nombre del archivo (excluyendo a .py).

#Así es como puedes hacer uso de la variable __main__ para detectar el contexto en el cual se activó tu código:
# module.py

#if __name__ == "__main__":
#    print("I prefer to be a module")
#else:
#    print("I like to be a module")


#Sin embargo, hay una forma más inteligente de utilizar la variable. Si escribes un módulo lleno de varias funciones complejas, 
#puedes usarla para colocar una serie de pruebas para verificar si las funciones trabajan correctamente.

#Cada vez que modifiques alguna de estas funciones, 
#simplemente puedes ejecutar el módulo para asegurarte de que sus enmiendas no estropeen el código. 
#Estas pruebas se omitirán cuando el código se importe como un módulo.

print("----5----")

##Tu primer módulo: continuación
#Este módulo contendrá dos funciones simples, y si deseas saber cuántas veces se han invocado las funciones, 
#necesitas un contador inicializado en cero cuando se importa el módulo. 
#Puedes hacerlo de esta manera:
# module.py

#counter = 0

#if __name__ == "__main__":
#    print("I prefer to be a module")
#else:
#    print("I like to be a module")

#MUY IMPORTANTE:
#Como puedes ver, el archivo principal intenta acceder a la variable de contador del módulo. ¿Es esto legal? 
#Sí lo es. ¿Es utilizable? Claro. ¿Es seguro? Eso depende: si confías en los usuarios de tu módulo, no hay problema; 
#sin embargo, es posible que no desees que el resto del mundo vea tu variable personal o privada.

#A diferencia de muchos otros lenguajes de programación, Python no tiene medios para permitirte ocultar tales variables a los ojos 
#de los usuarios del módulo. Solo puedes informar a tus usuarios que esta es tu variable, que pueden leerla, pero que no deben 
#modificarla bajo ninguna circunstancia.

#Esto se hace anteponiendo al nombre de la variable _ (un guión bajo) o __ (dos guiones bajos), pero recuerda, es solo un acuerdo. 
#Los usuarios de tu módulo pueden obedecerlo o no.

#Nosotros por supuesto, lo respetaremos. Ahora pongamos dos funciones en el módulo: evaluarán la suma y el producto de los números 
#recopilados en una lista.

#Además, agreguemos algunos adornos allí y eliminemos los restos superfluos.
#CÓDIGO QUE VA EN MODULE:# module.py

#!/usr/bin/env python3 

#""" module.py - an example of Python module """

#__counter = 0

#def suml(list):
#	global __counter
#	__counter += 1
#	sum = 0
#	for el in list:
#		sum += el
#	return sum

#def prodl(list):
#	global __counter	
#	__counter += 1
#	prod = 1
#	for el in list:
#		prod *= el
#	return prod

#if __name__ == "__main__":
#	print("I prefer to be a module, but I can do some tests for you")
#	l = [i+1 for i in range(5)]
#	print(suml(l) == 15)
#	print(prodl(l) == 120)

#El módulo está listo:
#Algunos elementos necesitan explicación:

#La línea que comienza con #! desde el punto de vista de Python, es solo un comentario debido a que comienza con #. 
# Para sistemas operativos Unix y similares a Unix (incluido MacOS), dicha línea indica al sistema operativo cómo ejecutar el contenido 
# del archivo (en otras palabras, qué programa debe lanzarse para interpretar el texto). En algunos entornos (especialmente aquellos 
# conectados con servidores web) la ausencia de esa línea causará problemas.
#Una cadena (quizás una multilínea) colocada antes de las instrucciones de cualquier módulo (incluidas las importaciones) 
# se denomina doc-string, y debe explicar brevemente el propósito y el contenido del módulo.
#Las funciones definidas dentro del módulo (suml() y prodl()) están disponibles para ser importadas.
#Se ha utilizado la variable __name__ para detectar cuándo se ejecuta el archivo de forma independiente.

#Ahora es posible usar el nuevo módulo, esta es una forma de hacerlo:
# main.py
#CÓDIGO DE MAIN.PY
#from module import suml, prodl

#zeroes = [0 for i in range(5)]
#ones = [1 for i in range(5)]
#print(suml(zeroes))
#print(prodl(ones))

