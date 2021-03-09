#Tu primer paquete
#Imagina que en un futuro no muy lejano, tu y tus socios escriben una gran cantidad de funciones en Python.

#Tu equipo decide agrupar las funciones en módulos separados, y este es el resultado final:




#Nota: hemos presentado todo el contenido solo para el módulo omega: supongamos que todos los módulos tienen un aspecto similar 
#(contienen una función denominada funX, donde X es la primera letra del nombre del módulo).

#De repente, alguien se da cuenta de que estos módulos forman su propia jerarquía, por lo que colocarlos a todos en una estructura 
#plana no será una buena idea.

#Después de algo de discusión, el equipo llega a la conclusión de que los módulos deben agruparse. Todos los participantes están de acuerdo 
#n que la siguiente estructura de árbol refleja 
#perfectamente las relaciones mutuas entre los módulos:

#Repasemos esto de abajo hacia arriba:

#El grupo ugly contiene dos módulos: psi y omega.
#El grupo best contiene dos módulos: sigma y tau.
#El grupo good contiene dos módulos: (alpha y beta) y un subgrupo (best).
#El grupo extra contiene dos subgrupos: (good y bad) y un módulo (iota).
#¿Se ve mal? De ninguna manera: analiza la estructura cuidadosamente. Se parece a algo, ¿no?

#Parece la estructura de un directorio.


print("----2----")

#Tu primer paquete: continuación
#Así es como se ve actualmente la relación entre módulos:

#Tal estructura es casi un paquete (en el sentido de Python). Carece del detalle fino para ser funcional y operativo. 
#Lo completaremos en un momento.

#Si asumes que extra es el nombre de un recientemente creado paquete (piensa en el como la raíz del paquete), 
#impondrá una regla de nomenclatura que te permitirá nombrar claramente cada entidad del árbol.

#Por ejemplo:

#La ubicación de una función llamada funT() del paquete tau puede describirse como:
#extra.good.best.tau.funT()

#Una función marcada como:
#extra.ugly.psi.funP()

#proviene del módulo psi el cual esta almacenado en subpaquete ugly del paquete extra.

#Se deben responder dos preguntas:

#¿Cómo se transforma este árbol (en realidad, un subárbol) en un paquete real de Python (en otras palabras, ¿cómo convence a Python de 
# que dicho 
#árbol no es solo un montón de archivos basura, 
#sino un conjunto de módulos)?
#¿Dónde se coloca el subárbol para que Python pueda acceder a él?

#IMPORTANTE:
#La primer pregunta tiene una respuesta sorprendente: los paquetes, como los módulos, pueden requerir inicialización.

#La inicialización de un módulo se realiza mediante un código independiente (que no forma parte de ninguna función) 
#ubicado dentro del archivo del módulo. Como un paquete no es un archivo, esta técnica es inútil para inicializar paquetes.

#En su lugar, debes usar un truco diferente: Python espera que haya un archivo con un nombre 
#muy exclusivo dentro de la carpeta del paquete: __init__.py.

#El contenido del archivo se ejecuta cuando se importa cualquiera de los módulos del paquete. 
#Si no deseas ninguna inicialización especial, puedes dejar el archivo vacío, pero no debes omitirlo.

print("---3---")
#Tu primer paquete: continuación
#La presencia del archivo __init.py__ finalmente compone el paquete:

#TOCA TENER UN ARCHIVO LLAMADO __init__.py para ejecutar el paquete

#NOTA:
#no solo la carpeta raiz puede contener el archivo __init.py__ - también puedes ponerlo dentro de cualquiera de sus subcarpetas 
#(subpaquetes). Puede ser útil si algunos de los subpaquetes requieren tratamiento individual o un tipo especial de inicialización.

#Ahora es el momento de responder la segunda pregunta: la respuesta es simple: donde quiera. Solo tienes que asegurarte de que Python 
#conozca la ubicación del paquete. Ya sabes cómo hacer eso.

#Estás listo para usar tu primer paquete.

#Hemos preparado un archivo zip que contiene todos los archivos de la rama de paquetes. Puedes descargarlo y 
#usarlo para tus propios experimentos, pero recuerda desempaquetarlo en la carpeta presentada en el esquema, de lo contrario, 
#no será accesible para el código.

#DESCARGAR   Archivo ZIP Módulos y paquetes

#Continuarás tus experimentos usando el archivo main2.py.

print("----4----")

#Tu primer paquete: continuación
#Vamos a acceder a la función funI() del módulo iota del paquete extra. Nos obliga a usar nombres de 
#paquetes calificados (asocia esto al nombramiento de carpetas y subcarpetas).

#Asi es como se hace:

#Nota:

#Hemos modificado la variable path para que sea accesible a Python.
#El import no apunta directamente al módulo, pero especifica la ruta completa desde la parte superior del paquete.
#El reemplazar import extra.iota con import iota causará un error.

#La siguiente variante también es válida:

print("---5---")

#Tu primer paquete: continuación
#Ahora vamos hasta el final del árbol: así es como se obtiene acceso a los módulos sigma y tau.
from sys import path
path.append("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_5\\extra\\good\\best\\sigma.py")
#path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())

#Puedes hacer tu vida más fácil usando un alias:

#otra forma:
# main2.py

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())


#Supongamos que hemos comprimido todo el subdirectorio, comenzando desde la carpeta extra ( incluyéndola), 
#y se obtuvo un archivo llamado extrapack.zip. Después, colocamos el archivo dentro de la carpeta packages.

#Ahora podemos usar el archivo zip en un rol de paquetes:
# main2.py

from sys import path

path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())

#Si deseas realizar tus propios experimentos con el paquete que hemos creado, puedes descargarlo a continuación. 
#Te alentamos a que lo hagas.

#DESCARGAR   Archivo ZIP Extrapack

#Ahora puedes crear módulos y combinarlos en paquetes. Es hora de comenzar una discusión completamente diferente: 
#sobre errores y fallas.







