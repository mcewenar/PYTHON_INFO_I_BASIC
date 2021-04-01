#Generadores, dónde encontrarlos
#Generador - ¿Con qué asocias esta palabra? Quizás se refiere a algún dispositivo electrónico. 
#O tal vez se refiere a una máquina pesada diseñada para producir energía eléctrica u otra cosa.

#Un generador de Python es un fragmento de código especializado capaz de producir una serie de valores y controlar el proceso de iteración. 
#Esta es la razón por la cual los generadores a menudo se llaman iteradores, 
#y aunque hay quienes pueden encontrar una diferencia entre estos dos, aquí los trataremos como uno mismo.

#Puede que no te hayas dado cuenta, pero te has topado con generadores muchas, muchas veces antes. Echa un vistazo al fragmento de código:

for i in range(5):
    print(i)

#La función range() es un generador, la cual también es un iterador.

#¿Cuál es la diferencia?

#Una función devuelve un valor bien definido, el cual, puede ser el resultado de una evaluación compleja, por ejemplo, de un polinomio, 
#y se invoca una vez, solo una vez.

#Un generador devuelve una serie de valores, y en general, se invoca (implícitamente) más de una vez.

#En el ejemplo, el generador range() se invoca seis veces, proporcionando cinco valores de cero a cuatro.

#El proceso anterior es completamente transparente. Vamos a arrojar algo de luz sobre el. Vamos a mostrarte el protocolo iterador.

for i in range(5):
    print(i)

print("---2---")

#Generadores, dónde encontrarlos: continuación
#El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las reglas impuestas por el contexto de las sentencias 
#for e in. Un objeto conforme al protocolo iterador se llama iterador.

#Un iterador debe proporcionar dos métodos:

#__iter__() el cual debe devolver el objeto en sí y que se invoca una vez (es necesario para que Python inicie con éxito la iteración).
#__next__() el cual debe devolver el siguiente valor (primero, segundo, etc.) de la serie deseada: será invocado 
# por las sentencias for/in para pasar a la siguiente iteración; si no hay más valores a proporcionar, el método deberá lanzar 
# la excepción StopIteration.
#¿Suena extraño? De ningúna manera. Mira el ejemplo en el editor.

#Hemos creado una clase capaz de iterar a través de los primeros n valores (donde n es un parámetro del constructor) 
# de los números de Fibonacci.

#Permítenos recordarte: los números de Fibonacci(Fibi) se definen de la siguiente manera:

#Fib1 = 1
#Fib2 = 1
#Fibi = Fibi-1 + Fibi-2

#En otras palabras:

#Los primeros dos números de la serie Fibonacci son 1.
#Cualquier otro número de Fibonacci es la suma de los dos anteriores (por ejemplo, Fib3 = 2, Fib4 = 3, Fib5 = 5, y así sucesivamente).
#Vamos a ver el código:
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")		
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
	print(i)

#Líneas 2 a 6: el constructor de la clase imprime un mensaje (lo usaremos para rastrear el comportamiento de la clase), se preparan algunas variables: (__n para almacenar el límite de la serie, __i para rastrear el número actual de la serie Fibonacci, y __p1 junto con __p2 para guardar los dos números anteriores).

#Líneas 8 a 10: el método __iter__ está obligado a devolver el objeto iterador en sí mismo; su propósito puede ser un poco ambiguo aquí, pero no hay misterio; trata de imaginar un objeto que no sea un iterador (por ejemplo, es una colección de algunas entidades), pero uno de sus componentes es un iterador capaz de escanear la colección; el método __iter__ debe extraer el iterador y confiarle la ejecución del protocolo de iteración; como puedes ver, el método comienza su acción imprimiendo un mensaje.

#Líneas 12 a 21: el método __next__ es responsable de crear la secuencia; es algo largo, pero esto debería hacerlo más legible; primero, imprime un mensaje, luego actualiza el número de valores deseados y, si llega al final de la secuencia, el método interrumpe la iteración al generar la excepción StopIteration; el resto del código es simple y refleja con precisión la definición que te mostramos anteriormente.

#Las líneas 23 y 24 hacen uso del iterador.

#El código produce el siguiente resultado:

#__init__
#__iter__
#__next__
#1
#__next__
#1
#__next__
#2
#__next__
#3
#__next__
#5
#__next__
#8
#__next__
#13
#__next__
#21
#__next__
#34
#__next__
#55
#__next__

#Observa:

#El objeto iterador se instancia primero.
#Después, Python invoca el método __iter__ para acceder al iterador real.
#El método __next__ se invoca once veces: las primeras diez veces produce valores útiles, mientras que la ultima finaliza la iteración.

print("---3---")

#Generadores, dónde encontrarlos: continuación
#El ejemplo muestra una solución donde el objeto iterador es parte de una clase más compleja.

#El código no es sofisticado, pero presenta el concepto de una manera clara.

#Echa un vistazo al código en el editor.
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
	def __init__(self, n):
		self.__iter = Fib(n)

	def __iter__(self):
		print("Class iter")
		return self.__iter;

object = Class(8)

for i in object:
	print(i)

#Hemos puesto el iterador Fib dentro de otra clase (podemos decir que lo hemos compuesto dentro de la clase Class). 
#Se instancia junto con el objeto de Class.

#El objeto de la clase se puede usar como un iterador cuando (y solo cuando) 
#responde positivamente a la invocación __iter__ - esta clase puede hacerlo, y si se invoca de esta manera, 
#proporciona un objeto capaz de obedecer el protocolo de iteración.

#Es por eso que la salida del código es la misma que anteriormente, 
#aunque el objeto de la clase Fib no se usa explícitamente dentro del contexto del bucle for.

print("---4---")

#La sentencia yield
#El protocolo iterador no es difícil de entender y usar, pero también es indiscutible que el protocolo es bastante inconveniente.

#La principal molestia que tiene es que necesita guardar el estado de la iteración en las invocaciones subsequentes de __iter__.

#Por ejemplo, el iterador Fib se ve obligado a almacenar con precisión el lugar en el que se detuvo la última invocación 
#(es decir, el número evaluado y los valores de los dos elementos anteriores). Esto hace que el código sea más grande y menos comprensible.

#Es por eso que Python ofrece una forma mucho más efectiva, conveniente y elegante de escribir iteradores.

#El concepto se basa fundamentalmente en un mecanismo muy específico proporcionado por la palabra clave reservada yield.

#Se puede ver a la palabra clave reservada yield como un hermano más inteligente de la sentencia return, con una diferencia esencial.

#Echa un vistazo a esta función:

def fun(n):
    for i in range(n):
        return i
#Se frena:
def fun(n):
    for i in range(n):
        return i
y=fun(5)
print(y)
#Se ve extraño, ¿no? Está claro que el bucle for no tiene posibilidad de terminar 
#su primera ejecución, ya que el return lo romperá irrevocablemente.

#Además, invocar la función no cambiará nada: el bucle for comenzará desde cero y se romperá inmediatamente.

#Podemos decir que dicha función no puede guardar y restaurar su estado en invocaciones posteriores.

#Esto también significa que una función como esta no se puede usar como generador.

#Hemos reemplazado exactamente una palabra en el código, ¿puedes verla?

def fun(n):
    for i in range(n):
        yield i #Convierte la función en un generador

#Hemos puesto yield en lugar de return. Esta pequeña enmienda convierte la función en un generador, y el ejecutar la 
#sentencia yield tiene algunos efectos muy interesantes.

#Primeramente, proporciona el valor de la expresión especificada después de la palabra clave reservada yield, al igual que return, 
#pero no pierde el estado de la función.

#Todos los valores de las variables están congelados y esperan la próxima invocación, cuando se reanuda la ejecución 
#(no desde cero, como ocurre después de un return).

#Hay una limitación importante: dicha función no debe invocarse explícitamente ya que no es una función; es un objeto generador.

#La invocación devolverá el identificador del objeto, no la serie que esperamos del generador.

#Debido a las mismas razones, la función anterior (la que tiene el return) solo se puede invocar explícitamente 
#y no se debe usar como generador.

#Cómo construir un generador:
#Permítenos mostrarte el nuevo generador en acción.

#Así es como podemos usarlo:
print("final")
def fun(n):
    for i in range(n):
        yield i
#v=fun(5)
for v in fun(5):
	print(v)
#print(v) #Muestra sólo el valor del objeto iterado

#¿Puedes adivinar la salida?
#Salida:
#0
#1
#2
#3
#4