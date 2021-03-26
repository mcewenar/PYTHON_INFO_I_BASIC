#Cómo construir una jerarquía de clases: continuación

#IMPORTANTE:
#La herencia no es la única forma de construir clases adaptables. Puedes lograr los mismos objetivos 
#(no siempre, pero muy a menudo) utilizando una técnica llamada composición.

#La composición es el proceso de componer un objeto usando otros objetos diferentes. 
#Los objetos utilizados en la composición entregan un conjunto de rasgos deseados 
#(propiedades y / o métodos), podemos decir que actúan como bloques utilizados para construir una estructura más complicada.

#Puede decirse que:

#La herencia extiende las capacidades de una clase agregando nuevos componentes y modificando los existentes; en otras palabras, 
#la receta completa está contenida dentro de la clase misma y todos sus ancestros; el objeto toma todas las pertenencias de la clase y las usa.
#La composición proyecta una clase como contenedor capaz de almacenar y usar otros objetos 
#(derivados de otras clases) donde cada uno de los objetos implementa una parte del comportamiento de una clase.

#Permítenos ilustrar la diferencia usando los vehículos previamente definidos. 
#El enfoque anterior nos condujo a una jerarquía de clases en la que la clase más alta conocía las reglas generales 
#utilizadas para girar el vehículo, pero no sabía cómo controlar los componentes apropiados (ruedas o pistas).

#Las subclases implementaron esta capacidad mediante la introducción de mecanismos especializados.
#Hagamos (casi) lo mismo, pero usando composición. La clase, como en el ejemplo anterior, sabe cómo girar el vehículo,
#pero el giro real lo realiza un objeto especializado almacenado en una propiedad llamada controlador.
#El controlador es capaz de controlar el vehículo manipulando las partes relevantes del vehículo.

#Echa un vistazo al editor: así es como podría verse.
import time

class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True) #esto genera que el constructor (controlador) obtenga los como 
        #atributo los demás métodos de las otras clases
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)

#Existen dos clases llamadas Pistas y Ruedas - ellas saben cómo controlar la dirección del vehículo.
#También hay una clase llamada Vehiculo que puede usar cualquiera de los controladores disponibles
#(los dos ya definidos o cualquier otro definido en el futuro): el controlador se pasa a la clase durante la inicialización.

#De esta manera, la capacidad de giro del vehículo se compone de un objeto externo, no implementado dentro de la clase Vehiculo.

#En otras palabras, tenemos un vehículo universal y podemos instalar pistas o ruedas en él.

#El código produce el siguiente resultado:

#ruedas:  True True
#ruedas:  True False
#pistas:  False True
#pistas:  False False


print("---2---")

#Herencia simple versus herencia múltiple (HERENCIA MÚLTIPLE NO RECOMENDADA)
#Como ya sabes, no hay obstáculos para usar la herencia múltiple en Python. 
#Puedes derivar cualquier clase nueva de más de una clase definida previamente.

#Solo hay un "pero". El hecho de que puedas hacerlo no significa que tengas que hacerlo.

#No olvides que:

#Una sola clase de herencia siempre es más simple, segura y fácil de entender y mantener.

#La herencia múltiple siempre es arriesgada, ya que tienes muchas más oportunidades de cometer un error 
#al identificar estas partes de las superclases que influirán efectivamente en la nueva clase.

#La herencia múltiple puede hacer que la anulación sea extremadamente difícil; además, el emplear la función super() se vuelve ambiguo.

#La herencia múltiple viola el principio de responsabilidad única 
#IMPORTANTE:
#(mas detalles aquí: https://en.wikipedia.org/wiki/Single_responsibility_principle) ya que forma una nueva clase de dos (o más) 
#clases que no saben nada una de la otra.

#IMPORTANTE TENER EN CUENTA:
#Sugerimos encarecidamente la herencia múltiple como la última de todas las posibles soluciones: 
#si realmente necesitas las diferentes funcionalidades que ofrecen las diferentes clases, la composición puede ser una mejor alternativa.


#Diamantes y porque no los quieres
#El espectro de problemas que posiblemente provienen de la herencia múltiple se ilustra mediante un problema 
#clásico denominado problema de diamantes. El nombre refleja la forma del diagrama de herencia: echa un vistazo a la imagen.

#Existe la superclase superior nombrada A.
#Aquí hay dos subclases derivadas de A - B y C.
##Y también está la subclase inferior llamada D, derivada de B y C (o C y B, ya que estas dos variantes significan cosas diferentes en Python).
#¿Puedes ver el diamante allí?

#NO SE PERMITE IMPLEMENTAR AMBAS FORMAS.
#A Python, sin embargo, no le gustan los diamantes, y no te permitirá implementar algo como esto. 
#Si intentas construir una jerarquía como esta:

#class A:
#    pass

#class B(A):
#    pass

#class C(A):
#    pass

#class D(A, B):
#    pass

#d = D()

#Obtendrás una excepción TypeError, junto con el siguiente mensaje:

#Cannot create a consistent method resolution
#order (MRO) for bases B, A

#Donde MRO significa Method Resolution Order. 
#Este es el algoritmo que Python utiliza para buscar el árbol de herencia y encontrar los métodos necesarios.

#Los diamantes son preciosos y valiosos ... pero no en la programación. Evítalos por tu propio bien.


print("---3---")

#Más sobre excepciones
#El discutir sobre la programación orientada a objetos ofrece una muy buena oportunidad para volver a las excepciones.
#La naturaleza orientada a objetos de las excepciones de Python las convierte en una herramienta muy flexible, 
#capaz de adaptarse a necesidades específicas, incluso aquellas que aún no conoces.

#Antes de adentrarnos en el lado orientado a objetos de las excepciones, 
#queremos mostrarte algunos aspectos sintácticos y semánticos de la forma en que Python trata el bloque try-except, 
#ya que ofrece un poco más de lo que hemos presentado hasta ahora.

#La primera característica que queremos analizar aquí es una rama adicional posible que se puede colocar dentro 
#(o más bien, directamente detrás) del bloque try-except: es la parte del código que comienza con else - justo como el ejemplo en el editor.
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n

print(reciproco(2))
print(reciproco(0))

#Un código etiquetado de esta manera se ejecuta cuando (y solo cuando) no se ha generado ninguna excepción dentro de la parte del try:. 
#Podemos decir que esta rama se ejecuta después del try: - ya sea el que comienza con except 
#(no olvides que puede haber más de una rama de este tipo) o la que comienza con else.

#Nota: la rama else: debe ubicarse después de la última rama except.

#El código de ejemplo produce el siguiente resultado:

#Todo salió bien
#0.5
#División fallida
#None

print("---4---")

#Más sobre excepciones
#El bloque try-except se puede extender de una manera más: agregando una parte encabezada por la palabra clave reservada finally 
#(debe ser la última rama del código diseñada para manejar excepciones).

#Nota: estas dos variantes (else y finally) no son dependientes entre si, y pueden coexistir u ocurrir de manera independiente.

#El bloque finally siempre se ejecuta (finaliza la ejecución del bloque try-except, de ahí su nombre), sin importar lo que sucedió antes, 
#incluso cuando se genera o lanza una excepción, sin importar si esta se ha manejado o no.

#Mira el código en el editor. Su salida es:
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))

#SALIDA:

#Todo salió bien
#Es el momento de decir adiós
#0.5
#División fallida
#Es el momento de decir adiós
#None

print("---5---")

#Las excepciones son clases
#Los ejemplos anteriores se centraron en detectar un tipo específico de excepción y responder de manera apropiada. 
#Ahora vamos a profundizar más y mirar dentro de la excepción misma.

#Probablemente no te sorprenderá saber que las excepciones son clases. Además, cuando se genera una excepción, 
#se crea una instancia de un objeto de la clase y pasa por todos los niveles de ejecución del programa, 
#buscando la rama "except" que está preparada para tratar con la excepción.

#Tal objeto lleva información útil que puede ayudarte a identificar con precisión todos los aspectos de la situación pendiente. 
#Para lograr ese objetivo, Python ofrece una variante especial de la cláusula de excepción: puedes encontrarla en el editor.

try:
    i = int("Hola!")
except Exception as e:
    print(e)
    print(e.__str__())
#Salida:
#invalid literal for int() with base 10: 'Hola!'
#invalid literal for int() with base 10: 'Hola!'

#Como puedes ver, la sentencia except se extendió y contiene una frase adicional que comienza con la palabra clave reservada as, 
#seguida por un identificador. El identificador está diseñado para capturar la excepción con el fin de analizar su naturaleza 
#y sacar conclusiones adecuadas.

#Nota: el alcance del identificador solo es dentro del except, y no va más allá.

#El ejemplo presenta una forma muy simple de utilizar el objeto recibido: simplemente imprímelo 
#(como puedes ver, la salida es producida por el método del objeto __str__()) y contiene un breve mensaje que describe la razón.

#Se imprimirá el mismo mensaje si no hay un bloque except en el código, y Python se verá obligado a manejarlo por si mismo.