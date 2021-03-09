#Excepciones
#Python 3 define 63 excepciones integradas, y todos ellos forman una jerarquía en forma de árbol, 
#aunque el árbol es un poco extraño ya que su raíz se encuentra en la parte superior.

#Algunas de las excepciones integradas son más generales (incluyen otras excepciones) mientras que otras son completamente concretas 
#(solo se representan a sí mismas). Podemos decir que cuanto más cerca de la raíz se encuentra una excepción, más general 
#(abstracta) es. A su vez, las excepciones ubicadas en los extremos del árbol (podemos llamarlas hojas) son concretas.

#RAMMA PRINCIPAL: BaseException
#Echa un vistazo a la figura:

#Nota:

#ZeroDivisionError es un caso especial de una clase de excepción más general llamada ArithmeticError.
#ArithmeticError es un caso especial de una clase de excepción más general llamada solo Exception.
#Exception es un caso especial de una clase más general llamada BaseException.
#Podemos describirlo de la siguiente manera (observa la dirección de las flechas; siempre apuntan a la entidad más general):

#BaseException
     #↑
#Exception
    #↑
#ArithmeticError
    #↑
#ZeroDivisionError
#Te mostraremos cómo funciona esta generalización. Comencemos con un código realmente simple.

print("---2---")

#Excepciones: continuación
#Observa el código en el editor. Es un ejemplo simple para comenzar. Ejecutalo.
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuuppsss...")

print("FIN.")

#La salida que esperamos ver se ve así:

#Uuuppsss...
#FIN.

#Ahora observa el código a continuación:

try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.")

#Algo ha cambiado: hemos reemplazado ZeroDivisionError con ArithmeticError.

#Ya se sabe que ArithmeticError es una clase general que incluye (entre otras) la excepción ZeroDivisionError.

#Por lo tanto, la salida del código permanece sin cambios. Pruébalo.

#Esto también significa que reemplazar el nombre de la excepción ya sea con Exception o BaseException no cambiará el comportamiento 
#del programa.


#Vamos a resumir:

#Cada excepción cae en la primer coincidencia.
#La coincidencia correspondiente no tiene que especificar exactamente la misma excepción, es suficiente que la excepción sea mas general 
#(mas abstracta) que la lanzada.


print("---3---")

#Excepciones: continuación
#Mira el código en el editor. ¿Qué pasará aquí?
try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema aritmético!")

print("FIN.")

#La primera coincidencia es la que contiene ZeroDivisionError. Significa que la consola mostrará:

#¡División entre Cero!
#FIN.

#¿Cambiará algo si intercambiamos los dos except? Justo como aquí abajo:

try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre Cero!")

print("FIN.")

#El cambio es radical: la salida del código es ahora:

#¡Problema aritmético!
#FIN.

#¿Por qué, si la excepción planteada es la misma que antes?

#La excepción es la misma, pero la excepción más general ahora aparece primero: también capturará todas las divisiones entre cero. 
#También significa que no hay posibilidad de que alguna excepción llegue a ZeroDivisionError. Ahora es completamente inalcanzable.


#IMPORTANTE:
#Recuerda:

#¡El orden de las excepciones importa!
#No pongas excepciones más generales antes que otras más concretas.
#Esto hará que el último sea inalcanzable e inútil.
#Además, hará que el código sea desordenado e inconsistente.
#Python no generará ningún mensaje de error con respecto a este problema.

print("---4---")
#Excepciones: continuación
#Si deseas manejar dos o mas excepciones de la misma manera, puedes usar la siguiente sintaxis:

#try:
#    :
#except (exc1, exc2):
#    :

#Simplemente tienes que poner todos los nombres de excepción empleados en una lista separada por comas y no olvidar los paréntesis.


#Si una excepción se genera dentro de una función, puede ser manejada:

#Dentro de la función.
#Fuera de la función.
#Comencemos con la primera variante: observa el código en el editor.
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

badFun(0)

print("FIN.")

#La excepción ZeroDivisionError (la cual es un caso concreto de la clase ArithmeticError) es lanzada dentro de la función badfun(), 
#y la función en sí misma se encarga de su caso.

#La salida del programa es:

#¡Problema aritmético!
#FIN.

#También es posible dejar que la excepción se propague fuera de la función. Probémoslo ahora.

#Observa el código a continuación:

#def badFun(n):
#    return 1 / n

#try:
#    badFun(0)
#except ArithmeticError:
#    print("¿Que pasó? ¡Se lanzo una excepción!")

#print("FIN.")

#El problema tiene que ser resuelto por el invocador (o por el invocador del invocador, y así sucesivamente.).

#La salida del programa es:

#¿Que pasó? ¡Se lanzo una excepción!
#FIN.

#Nota: la excepción planteada puede cruzar la función y los límites del módulo, y viajar a través de la cadena de invocación
# buscando una cláusula except capaz de manejarla.

#Si no existe tal cláusula, la excepción no se controla y Python resuelve el problema de la manera estándar - 
#terminando el código y emitiendo un mensaje de diagnóstico.

#Ahora vamos a suspender esta discusión, ya que queremos presentarte una nueva instrucción de Python.