##¿Cómo saber dónde estás?
#A veces, puede ser necesario encontrar información no relacionada con Python. Por ejemplo,
#es posible que necesites conocer la ubicación de tu programa dentro del entorno de la computadora.

#Imagina el entorno de tu programa como una pirámide que consta de varias capas o plataformas.

#Las capas son:

#El código (en ejecución) se encuentra en la parte superior.
#Python (mejor dicho, su entorno de ejecución) se encuentra directamente debajo de él.
#La siguiente capa de la pirámide se llena con el SO (sistema operativo): el entorno de Python proporciona algunas de sus funcionalidades 
#utilizando los servicios del sistema operativo. Python, aunque es muy potente, no es omnipotente: se ve obligado a usar muchos ayudantes 
#si va a procesar archivos o comunicarse con dispositivos físicos.
#La capa más inferior es el hardware: el procesador (o procesadores), las interfaces de red, los dispositivos de interfaz humana 
#(ratones, teclados, etc.) y toda otra maquinaria necesaria para hacer funcionar la computadora: el sistema operativo sabe cómo emplearlos 
#y utiliza muchos trucos para trabajar con todas las partes en un ritmo constante.

#Esto significa que algunas de las acciones del programa tienen que recorrer un largo camino para ejecutarse con éxito, imagina que:

#Tu código quiere crear un archivo, por lo que invoca una de las funciones de Python.
#Python acepta la orden, la reorganiza para cumplir con los requisitos del sistema operativo local (es como poner el sello "aprobado" en una solicitud) y lo envía.
#El SO comprueba si la solicitud es razonable y válida (por ejemplo, si el nombre del archivo se ajusta a algunas reglas de sintaxis) 
# e intenta crear el archivo. Tal operación, 
#aparentemente es muy simple, no es atómica: consiste de muchos pasos menores tomados por...
#El hardware, el cual es responsable de activar los dispositivos de almacenamiento (disco duro, dispositivos de estado sólido, etc.) 
#para satisfacer las necesidades del sistema operativo.
#Por lo general, no eres consciente de todo ese alboroto: quieres que se cree el archivo y eso es todo.

#Pero a veces quieres saber más, por ejemplo, el nombre del sistema operativo que aloja Python y algunas características que describen el 
#hardware que aloja el sistema operativo.

#Hay un módulo que proporciona algunos medios para permitir saber dónde se encuentra y qué componentes funcionan. El módulo se llama platform. 
#Veamos algunas de las funciones que brinda.

print("---2---")
#Funciones seleccionadas del módulo platform
#El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información 
#sobre la versión del intérprete.

#Existe también una función que puede mostrar todas las capas subyacentes en un solo vistazo, llamada platform.
#Simplemente devuelve una cadena que describe el entorno; por lo tanto, su salida está más dirigida a los humanos que al procesamiento automatizado (lo veremos pronto).

#Así es como se puede invocar: platform(aliased = False, terse = False).

#Ahora:

#aliased → cuando se establece a True (o cualquier valor distinto de cero) puede hacer que la función presente los nombres de 
# capa subyacentes alternativos en lugar de los comunes.
#terse → cuando se establece a True (o cualquier valor distinto de cero) puede convencer a la función de presentar una forma 
# más breve del resultado (si lo fuera posible).
#Ejecutamos el programa usando tres plataformas diferentes: esto es lo que se obtuvo:

#Intel x86 + Windows ® Vista (32 bit):

#Windows-Vista-6.0.6002-SP2
#Windows-Vista-6.0.6002-SP2
#Windows-Vista

#Intel x86 + Gentoo Linux (64 bit):

#Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
#Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
#Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-glibc2.3.4

#Raspberry PI2 + Raspbian Linux (32 bit):

#Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
#Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
#Linux-4.4.0-1-rpi2-armv7l-with-glibc2.9

#También puedes ejecutar el programa en el IDLE de tu máquina local para verificar qué salida tendrá.


#FORMA PARA SABER MI SO:
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

print("----3----")
#Funciones seleccionadas del módulo platform: continuación
#A veces, es posible que solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo junto 
#con Python y el código, una función llamada machine() te lo dirá. Como anteriormente, la función devuelve una cadena.

#Nuevamente, ejecutamos el programa en tres plataformas diferentes:
from platform import machine

print(machine())

#Intel x86 + Windows ® Vista (32 bit):

#x86

#Intel x86 + Gentoo Linux (64 bit):

#x86_64

#Raspberry PI2 + Raspbian Linux (32 bit):

#armv7l
print("---4---")
#Funciones seleccionadas del módulo platform: continuación
#La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).

#Una vez más, ejecutamos el programa en tres plataformas diferentes:

#Intel x86 + Windows ® Vista (32 bit):
#x86
#Intel x86 + Gentoo Linux (64 bit):

#Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz

#Raspberry PI2 + Raspbian Linux (32 bit):

#armv7l

from platform import processor

print(processor())

print("---5---")
#Funciones seleccionadas del módulo platform: continuación
#Una función llamada system() devuelve el nombre genérico del sistema operativo en una cadena.

#Nuestras plataformas de ejemplo se presentaron así:

#Intel x86 + Windows ® Vista (32 bit):

#Windows

#Intel x86 + Gentoo Linux (64 bit):

#Linux

#Raspberry PI2 + Raspbian Linux (32 bit):

#Linux

from platform import system

print(system())

print("---6---")

#Funciones seleccionadas del módulo platform: continuación
#La versión del sistema operativo se proporciona como una cadena por la función version().

#Ejecuta el código y verifica su salida. Esto es lo que tenemos:

#Intel x86 + Windows ® Vista (32 bit):

#6.0.6002

#Intel x86 + Gentoo Linux (64 bit):

#1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017

#Raspberry PI2 + Raspbian Linux (32 bit):

#1 SMP Debian 4.4.6-1+rpi14 (2016-05-05)

from platform import version

print(version())
print("---7---")
#Funciones seleccionadas del módulo platform: continuación
#Si necesitas saber qué versión de Python está ejecutando tu código, puedes verificarlo utilizando una serie de funciones dedicadas, 
#aquí hay dos de ellas:

#python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar 
#cualquier rama de Python no canónica).
#python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
#la parte mayor de la versión de Python.
#la parte menor,
#el número de nivel del patch.
#Nuestro programa ejemplo produjo el siguiente resultado:

#CPython
#3
#6
#4

#Es muy probable que tu versión de Python sea diferente.
from platform import python_implementation, python_version_tuple

print(python_implementation()) #TE DICE LA VERSIÓN DEL COMPILADOR DE PYTHON (CPYTHON)
print("j3j3")
for atr in python_version_tuple():
    print(atr)