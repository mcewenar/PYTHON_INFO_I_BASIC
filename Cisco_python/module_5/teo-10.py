#Errores, fallas y otras plagas.
#Cualquier cosa que pueda salir mal, saldrá mal.

#Esta es la ley de Murphy, y funciona en todo y siempre. Si la ejecución del código puede salir mal, lo hará.

#Observa el código en el editor. Hay al menos dos formas posibles de que "salga mal" la ejecución. ¿Puedes verlas?
import math

x = float(input("Ingresa x: "))
y = math.sqrt(x)

print("La raíz cuadrada de", x, "es igual a", y)

#Como el usuario puede ingresar una cadena de caracteres completamente arbitraria, no hay garantía de que la cadena se pueda convertir 
#en un valor flotante - esta es la primera vulnerabilidad del código.
#La segunda es que la función sqrt() fallará si se le ingresa un valor negativo.
#Puedes recibir alguno de los siguientes mensajes de error.

#Algo como esto:

#Ingresa x: Abracadabra

#Traceback (most recent call last):

 # File "sqrt.py", line 3, in 

#    x = float(input("Ingresa x: "))

#ValueError: could not convert string to float: 'Abracadabra'

#O algo como esto:

#Ingresa x: -1

#Traceback (most recent call last):

#  File "sqrt.py", line 4, in 

#    y = math.sqrt(x)

#ValueError: math domain error

#¿Puedes protegerte de tales sorpresas? Por supuesto que si. Además, tienes que hacerlo para ser considerado un buen programador.

print("---2---")
#Excepciones
#Cada vez que tu código intenta hacer algo erroneo, irresponsable o inaplicable, Python hace dos cosas:

#Detiene tu programa.
#Crea un tipo especial de dato, llamado excepción.
#Ambas actividades llevan por nombre lanzar una excepción. Podemos decir que Python siempre lanza una excepción (o que una excepción 
#ha sido lanzada) cuando no tiene idea de qué hacer con el código.

#¿Qué ocurre después?

#La excepción lanzada espera que alguien o algo lo note y haga algo al respecto.
#Si la excepción no es resuelta, el programa será terminado abruptamente, y verás un mensaje de error enviado a la consola por Python.
#De otra manera, si se atiende la excepción y es manejada apropiadamente, el programa puede reanudarse y su ejecución puede continuar.

#Python proporciona herramientas efectivas que permiten observar, identificar y manejar las excepciones eficientemente. 
#Esto es posible debido a que todas 
#las excepciones potenciales tienen un nombre específico, por lo que se pueden clasificar y reaccionar a ellas adecuadamente.

#Ya conoces algunos nombres de excepción.

#Observa el siguiente mensaje de diagnóstico:
#ValueError: math domain error 

#La palabra en rojo es solo el nombre de la excepción. Vamos a familiarizarnos con algunas otras excepciones.

print("---3---")
#Excepciones: continuación
#Observa el código en el editor. Ejecuta el (obviamente incorrecto) programa.
valor = 1
#valor /= 0 ERRORRRRRRR

#Verás el siguiente mensaje en respuesta:

#Traceback (most recent call last):
#File "div.py", line 2, in 
#valor /= 0
#ZeroDivisionError: division by zero

#Este error de excepción se llama ZeroDivisionError.

print("---4---")

#Excepciones: continuación
#Observa el código en el editor. ¿Qué pasará cuando lo ejecutes?
lista = []
#x = lista[0] ERRORRRRRRR

#Verás el siguiente mensaje en respuesta:

#Traceback (most recent call last):
#File "lst.py", line 2, in 
#x = lista[0]
#IndexError: list index out of range

#Este es el IndexError (error de índice).

print("---5---")
#Excepciones: continuación
#¿Cómo se manejan las excepciones? La palabra try es clave para la solución.

#Además, también es una palabra reservada.

#La receta para el éxito es la siguiente:

#Primero, se debe intentar (try) hacer algo.
#Después, tienes que comprobar si todo salió bien.
#Pero, ¿no sería mejor verificar primero todas las circunstancias y luego hacer algo solo si es seguro?

#Justo como el ejemplo en el editor.
primerNumero = int(input("Ingresa el primer numero: "))
segundoNumero = int(input("Ingresa el segundo numero: "))

if segundoNumero != 0:
    print(primerNumero / segundoNumero)
else:
    print("Esta operacion no puede ser realizada.")

print("FIN.")

#Es cierto que esta forma puede parecer la más natural y comprensible, pero en realidad, este método no facilita la programación. 
#Todas estas revisiones pueden hacer el código demasiado grande e ilegible.

#Python prefiere un enfoque completamente diferente.

print("---6---")

#Excepciones: continuación
#Observa el código en el editor. Este es el enfoque favorito de Python.
primerNumero = int(input("Ingresa el primer numero: "))
segundoNumero = int(input("Ingresa el segundo numero: "))

if segundoNumero != 0:
    print(primerNumero / segundoNumero)
else:
    print("Esta operacion no puede ser realizada.")

print("FIN.")

#Nota:

#La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
#Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
#La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal - 
#si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de la palabra 
#clave except debería proporcionar una reacción adecuada a la excepción planteada.
#Se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.
#Ejecute el código y prueba su comportamiento.


#Resumamos esto:

#try:
#    :
#    :
#except:
#    :
#    :

#En el primer paso, Python intenta realizar todas las instrucciones colocadas entre las instrucciones try: y except:.
#Si no hay ningún problema con la ejecución y todas las instrucciones se realizan con éxito, la ejecución salta al punto después de la 
#última línea del bloque except: , y la ejecución del bloque se considera completa.
#Si algo sale mal dentro del bloque try: o except:, la ejecución salta inmediatamente fuera del bloque y entra en la primera 
#instrucción ubicada después de la palabra reservada except: : esto significa que algunas de las instrucciones del bloque pueden ser 
#silenciosamente omitidas.

print("---7---")

#Excepciones: continuación
#Observa el código en el editor. Te ayudará a comprender este mecanismo.
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")

#Esta es la salida que produce:

#1
#Oh cielos, algo salio mal...
#3

#Nota: la instrucción print("2") se perdió en el proceso.
print("---8---")

#Excepciones: continuación
#Este enfoque tiene una desventaja importante: si existe la posibilidad de que más de una excepción se salte a un apartado except:
#puedes tener problemas para descubrir lo que realmente sucedió.

#Al igual que en el código en el editor. Ejecútalo y ve lo qué pasa.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")

#El mensaje: Oh cielos, algo salio mal... que aparece en la consola no dice nada acerca de la razón,
#mientras que hay dos posibles causas de la excepción:

#Datos no enteros fueron ingresados por el usuario.
#Un valor entero igual a 0 fue asignado a la variable x.

#Técnicamente, hay dos formas de resolver el problema:

#Construir dos bloques consecutivos try-except, uno por cada posible motivo de excepción 
#(fácil, pero provocará un crecimiento desfavorable del código).
#Emplear una variante más avanzada de la instrucción.
#Se parece a esto:

#try:
#   :
#except exc1:
#    :
#except exc2:
#    :
#except:
#    :

#Así es como funciona:

#Si el try lanza la excepción exc1, esta será manejada por el bloque except exc1:.
#De la misma manera, si el try lanza la excepción exc2, esta será manejada por el bloque except exc2:.
#Si el try lanza cualquier otra excepción, será manejado por el bloque sin nombre except.
#Pasemos a la siguiente parte del curso y veámoslo en acción.

print("---9---")
#Excepciones: continuación
#Mira el código en el editor. Nuestra solucion esta ahí.

#El código, cuando se ejecute, producirá una de las siguientes cuatro variantes de salida:
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")

#Si se ingresa un valor entero válido distinto de cero (por ejemplo, 5) dirá:

#0.2
#FIN.

#Si se ingresa 0, dirá:

#No puedes dividir entre cero, lo siento.
#FIN.

#Si se ingresa cualquier cadena no entera, verás:

#Debes ingresar un valor entero.
#FIN.

#(Localmente en tu máquina) si presionas Ctrl-C mientras el programa está esperando la entrada del usuario 
#(provocará una excepción denominada KeyboardInterrupt), el programa dirá:

#Oh cielos, algo salio mal...
#FIN.

print("---10---")

#Excepciones: continuación
#No olvides que:

#Los bloques except son analizados en el mismo orden en que aparecen en el código.
#No debes usar más de un bloque de excepción con el mismo nombre.
#El número de diferentes bloques except es arbitrario, la única condición es que si se emplea el try, debes poner al menos un except 
#(nombrado o no) después de el.
#La palabra reservada except no debe ser empleada sin que le preceda un try.
#Si uno de los bloques except es ejecutado, ningún otro lo será.
#Si ninguno de los bloques except especificados coincide con la excepción planteada, la excepción permanece sin manejar 
#(lo discutiremos pronto).
#Si un except sin nombre existe, tiene que especificarse como el último.
#try:
#    :
#except exc1:
#    :
#except exc2:
#    :
#except:
#    :

#Continuemos ahora con los experimentos.


#Observa el código en el editor. Hemos modificado el programa anterior, hemos eliminado el bloque ZeroDivisionError.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")

#¿Qué sucede ahora si el usuario ingresa un 0 como entrada?

#Como no existe un bloque declarado para la división entre cero, la excepción cae dentro del bloque general (sin nombre): 
#esto significa que en este caso, el programa dirá:

#Oh cielos, algo salio mal...
#FIN.

#Inténtalo tú mismo. Ejecuta el programa.
print("---11---")
#Excepciones: continuación
#Echemos a perder el código una vez más.

#Observa el programa en el editor. Esta vez, hemos eliminado el bloque sin nombre.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")

#El usuario ingresa nuevamente un 0, y:

#La excepción no será manejada por ValueError - no tiene nada que ver con ello.
#Como no hay otro bloque, deberías ver este mensaje:

#Traceback (most recent call last):
#File "exc.py", line 3, in 
#y = 1 / x
#ZeroDivisionError: division by zero

#Has aprendido mucho sobre el manejo de excepciones en Python. En la siguiente sección, nos centraremos en las excepciones 
#integradas de Python y sus jerarquías.





