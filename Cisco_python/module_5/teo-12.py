#Excepciones: continuación
#La instrucción raise genera la excepción especificada denominada exc como si fuese generada de manera natural:

#raise exc

#Nota: raise es una palabra reservada.

#La instrucción permite:

#Simular excepciones reales (por ejemplo, para probar tu estrategia de manejo de excepciones).
#Parcialmente manejar una excepción y hacer que otra parte del código sea responsable de completar el manejo.

#Observa el código en el editor. Así es como puedes usarlo en la práctica.
def badFun(n):
    raise ZeroDivisionError #LEVANTA ESTA EXCEPCIÓN DE FORMA INTENCIONAL

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

#La salida del programa permanece sin cambios.

#De esta manera, puedes probar tu rutina de manejo de excepciones sin forzar al código a hacer cosas incorrectas.
print("--2--")

#Excepciones: continuación
#La instrucción raise también se puede utilizar de la siguiente manera (toma en cuenta la ausencia del nombre de la excepción):

#raise

#Existe una seria restricción: esta variante de la instrucción raise puede ser utilizada solamente dentro de la rama except;
#usarla en cualquier otro contexto causa un error.

#La instrucción volverá a generar la misma excepción que se maneja actualmente.


#Gracias a esto, puedes distribuir el manejo de excepciones entre diferentes partes del código.

#Observa el código en el editor. Ejecútalo, lo veremos en acción.

#La excepción ZeroDivisionError es generada dos veces:

#Primero, dentro del try debido a que se intentó realizar una división entre cero.
#Segundo, dentro de la parte except por la instrucción raise.
#En efecto, la salida del código es:

#¡Lo hice otra vez!
#¡Ya veo!
#FIN.

print("---3---")

#Excepciones: continuación
#La instrucción raise también se puede utilizar de la siguiente manera (toma en cuenta la ausencia del nombre de la excepción):

#raise

#Existe una seria restricción: esta variante de la instrucción raise puede ser utilizada solamente dentro de la rama except; 
#usarla en cualquier otro contexto causa un error.

#La instrucción volverá a generar la misma excepción que se maneja actualmente.


#Gracias a esto, puedes distribuir el manejo de excepciones entre diferentes partes del código.

#Observa el código en el editor. Ejecútalo, lo veremos en acción.
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

#La excepción ZeroDivisionError es generada dos veces:

#Primero, dentro del try debido a que se intentó realizar una división entre cero.
#Segundo, dentro de la parte except por la instrucción raise.
#En efecto, la salida del código es:

#¡Lo hice otra vez!
#¡Ya veo!
#FIN.
print("---4---")
#Excepciones: continuación
#Ahora es un buen momento para mostrarte otra instrucción de Python, llamada assert (afirmar). Esta es una palabra reservada.

#assert expresión

#¿Como funciona?

#Evalúa la expresión.
#Si la expresión se evalúa como True (verdadero), o un valor numérico distinto de cero, o una cadena no vacía, 
#o cualquier otro valor diferente de None, no hará nada más.
#De lo contrario, automáticamente e inmediatamente genera una excepción llamada AssertionError 
#(en este caso, decimos que la afirmación ha fallado).
#¿Cómo puede ser utilizada?

#Puedes ponerlo en la parte del código donde quieras estar absolutamente a salvo de datos incorrectos, 
#y donde no estés absolutamente seguro de que los datos hayan sido examinados cuidadosamente antes 
#(por ejemplo, dentro de una función utilizada por otra persona).
#El generar una excepción AssertionError asegura que tu código no produzca resultados no válidos 
#y muestra claramente la naturaleza de la falla.
#Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.
#Si las excepciones y la validación de datos son como conducir con cuidado, 
#la aserción puede desempeñar el papel de una bolsa de aire.


#Veamos a la instrucción assert en acción. Mira el código en el editor. Ejecutarlo.
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#El programa se ejecuta sin problemas si se ingresa un valor numérico válido mayor o igual a cero; de lo contrario, 
#se detiene y emite el siguiente mensaje:

#Traceback (most recent call last):
#  File ".main.py", line 4, in 
#    assert x >= 0.0
#AssertionError

print("---5---")
#Excepciones integradas
#Te mostraremos una breve lista de las excepciones más útiles. Si bien puede sonar extraño llamar "útil" a una cosa o un fenómeno 
#que es un signo visible de una falla o retroceso, como sabes, errar es humano y si algo puede salir mal, saldrá mal.

#Las excepciones son tan rutinarias y normales como cualquier otro aspecto de la vida de un programador.

#Para cada excepción, te mostraremos:

#Su nombre.
#Su ubicación en el árbol de excepciones.
#Una breve descripción.
#Un fragmento de código conciso que muestre las circunstancias en las que se puede generar la excepción.
#Hay muchas otras excepciones para explorar: simplemente no tenemos el espacio para revisarlas todas aquí.

#ArithmeticError
#Ubicación:

#BaseException ← Exception ← ArithmeticError

#Descripción:

#Una excepción abstracta que incluye todas las excepciones causadas por operaciones aritméticas como división cero o dominio 
#inválido de un argumento.

#AssertionError
#Ubicación:

#BaseException ← Exception ← AssertionError

#Descripción:

#Una excepción concreta generada por la instrucción de aserción cuando su argumento se evalúa como False (falso), None (ninguno), 
#0, o una cadena vacía.

#Código :

from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# debemos estar seguros de ese angulo != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))

#BaseException
#Ubicación:

#BaseException

#Descripción:

#La excepción más general (abstracta) de todas las excepciones de Python: todas las demás excepciones se incluyen en esta; se puede decir 
#que las siguientes dos excepciones son equivalentes: except: y except BaseException:.

#IndexError
#Ubicación:

#BaseException ← Exception ← LookupError ← IndexError

#Descripción:

#Una excepción concreta que surge cuando se intenta acceder al elemento de una secuencia inexistente (por ejemplo, el elemento de una lista).

#Código:

# el codigo muestra una forma extravagante
# de dejar el bucle

lista = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lista[ix])
        ix += 1
    except IndexError:
        doit = False

print('Listo')

print("---6---")

#KeyboardInterrupt
#Ubicación:

#BaseException ← KeyboardInterrupt

#Descripción:

#Una excepción concreta que surge cuando el usuario usa un atajo de teclado diseñado para terminar la ejecución de un programa 
#(Ctrl-C en la mayoría de los Sistemas Operativos); si manejar esta excepción no conduce a la terminación del programa, 
#el programa continúa su ejecución. Nota: esta excepción no se deriva de la clase Exception. Ejecuta el programa en IDLE.

#Código:

# este código no puede ser terminado
# presionando Ctrl-C

#PENDIENTE:
from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1) #Segundos
    except KeyboardInterrupt:
        print("¡No hagas eso!")

#LookupError
#Ubicación:

#BaseException ← Exception ← LookupError

#Descripción:
#Una excepción abstracta que incluye todas las excepciones causadas por errores resultantes de referencias no válidas a diferentes colecciones 
#(listas, diccionarios, tuplas, etc.).

