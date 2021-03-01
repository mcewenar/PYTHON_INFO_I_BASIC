#Importando un módulo: continuación
#Observa el fragmento a continuación, esta es la forma en que se habilitan los nombres de pi y sin con el nombre de su módulo de origen:
import math
print(math.sin(math.pi/2))
math.pi
math.sin

#Es sencillo, se pone:

#El nombre del módulo (math).
#Un punto.
#Y el nombre de la entidad (pi).
#Tal forma indica claramente el namespace en el que existe el nombre.

#Nota: el uso de esto es obligatorio si un módulo ha sido importado con la instrucción import. No importa si alguno de los nombres del 
#código y del namespace del módulo están en conflicto o no.


#Este primer ejemplo no será muy avanzado: solo se desea imprimir el valor de sin(1/2π).

#Observa el código en el editor. Así es como se prueba.

#El código genera el valor esperado: 1.0.

#Nota: el eliminar cualquiera de las dos indicaciones hará que el código sea erróneo. No hay otra forma de entrar al namespace de 
#math si se hizo lo siguiente:

#import math

print("---2---")

#Importando un módulo: continuación
#Ahora te mostraremos como pueden dos namespaces (el tuyo y el del módulo) coexistir.

#Echa un vistazo al ejemplo en la ventana del editor.

#IMPORTANTE:
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))
print(pi, "variable definida dentro de código")
print(math.pi,"módulo math(está en radianes)")

#Se ha definido una variable y función propia para pi y sin respectivamente, y se emplean junto con los de la librería math.

#Ejecuta el programa. El código debe producir la siguiente salida:
#0.99999999
#1.0
# #Como puedes ver, las entidades no se afectan entre sí.
#POR EL NAMESPACE NO HAY CONFLICTOS
print("---3---")
#Importando un módulo: continuación
#En el segundo método, la sintaxis del import señala con precisión qué entidad (o entidades) del módulo son aceptables en el código:
#ES ASÍ COMO NO NECESITAREMOS USAR SIEMPRE EL MATH COMO OBJETO PARA TRAER DICHOS MÉTODOS

from math import pi

#La instrucción consta de los siguientes elementos:

#La palabra reservada from.
#El nombre del módulo a ser (selectivamente) importado.
#La palabra reservada import.
#El nombre o lista de nombres de la entidad o entidades las cuales estan siendo importadas al namespace.
#La instrucción tiene este efecto:

#Las entidades listadas son las unicas que son importadas del módulo indicado.
#Los nombres de las entidades importadas pueden ser accedidas dentro del programa.
#Nota: no se importan otras entidades, únicamente las especificadas. Además, no se pueden importar entidades adicionales utilizando una 
#línea como esta:

print(math.e)

#Esto ocasionará un error, (e es la constante de Euler: 2.71828...).

#Reescribamos el código anterior para incorporar esta nueva técnica.

#Aquí esta:

from math import sin, pi

print(sin(pi/2))

#El resultado debe de ser el mismo que el anterior, se han empleado las mismas entidades: 1.0. Copia y pega el código en el editor, 
#y ejecuta el programa.

#¿El código parece más simple? Quizás, pero el aspecto no es el único efecto de este tipo de importación. Veamos mas a detalle esto.
print("---4---")
#Importando un módulo: continuación
#Observa el código en el editor. Analízalo cuidadosamente:
from math import sin, pi

print(sin(pi/2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

#La línea 01: lleva a cabo la importación selectiva.
#La línea 03: hace uso de las entidades importadas y obtiene el resultado esperado (1.0).
#La línea 05 a la 11: redefine el significado de pi y sin - en efecto, reemplazan las definiciones originales (importadas) dentro del 
#namespace del código.
#La línea 13: retorna 0.99999999, lo cual confirma nuestras conclusiones.


#Hagamos otra prueba. Observa el código a continuación:
pi = 3.14	# linea 01

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None	# linea 07

print(sin(pi/2))	# linea 09


from math import sin, pi	# linea 12

print(sin(pi/2))	# linea 14

#Aquí, se ha invertido la secuencia de las operaciones del código:

#Las líneas del 01 al 07: definen nuestro propio pi y sin.
#La línea 09: hace uso de ellas ( 0.99999999 aparece en pantalla).
#La línea 12: lleva a cabo la importación - los símbolos importados reemplazan sus definiciones anteriores dentro del namespace.
#La línea 14: retorna 1.0 como resultado.

print("---5---")
#IMPORTANTE:
#Importando un Módulo: *
#En el tercer método, la sintaxis del import es una forma más agresiva que la presentada anteriormente:

#from module import *

#Como puedes ver, el nombre de una entidad (o la lista de nombres de entidades) se reemplaza con un solo asterisco (*).

#Tal instrucción importa todas las entidades del módulo indicado.

#¿Es conveniente? Sí, lo es, ya que libera del deber de enumerar todos los nombres que se necesiten. NO HACE FALTA USAR EL NOMBRE DEL MÓDULO

#¿Es inseguro? Sí, a menos que conozca todos los nombres proporcionados por el módulo, es posible que no puedas evitar conflictos de nombres. 
#Trata esto como una solución temporal e intenta no usarlo en un código regular.


#Importando un módulo: la palabra reservada as (IMPORTANTÍSIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO)
#Si se importa un módulo y no se esta conforme con el nombre del módulo en particular (por ejemplo, sí es el mismo que el de una de sus 
#entidades ya definidas) puede darsele otro nombre: esto se llama "aliasing o renombrado".

#Aliasing (renombrado) hace que el módulo se identifique con un nombre diferente al original. (esto evita conflictos)

#La creación de un alias se realiza junto con la importación del módulo, y exige la siguiente forma de la instrucción import:

#import module as alias

#el "module" identifica el nombre del módulo original mientras que el "alias" es el nombre que se desea usar en lugar del original.

#Nota: as es una palabra reservada.