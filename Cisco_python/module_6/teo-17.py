#La función lambda
#La función lambda es un concepto tomado de las matemáticas, más específicamente, de una parte llamada el cálculo Lambda,
#pero estos dos fenómenos no son iguales.

#Los matemáticos usan el cálculo Lambda en sistemas formales conectados con: la lógica, la recursividad o la demostrabilidad de teoremas.
#Los programadores usan la función lambda para simplificar el código, hacerlo más claro y fácil de entender.

#Una función lambda es una función sin nombre (también puedes llamarla una función anónima). Por supuesto,
#tal afirmación plantea inmediatamente la pregunta: ¿cómo se usa algo que no se puede identificar?

#Afortunadamente, no es un problema, ya que se puede mandar llamar dicha función si realmente se necesita,
#pero, en muchos casos la función lambda puede existir y funcionar mientras permanece completamente de incógnito.

#La declaración de la función lambda no se parece a una declaración de función normal; compruébalo tu mismo:

#lambda parámetros: expresión

#Tal cláusula devuelve el valor de la expresión al tomar en cuenta el valor del argumento lambda actual.

#Como de costumbre, un ejemplo será útil. Nuestro ejemplo usa tres funciones lambda, pero con nombres. Analizalo cuidadosamente:

dos = lambda : 2
cuadrado = lambda x : x * x
potencia = lambda x, y : x ** y

for a in range(-2, 3): #-2,-1,0,1,2 recuerda que es un generador de función range()
    print(cuadrado(a), end=" ")
    print(potencia(a, dos()))


#Vamos a analizarlo:

#La primer lambda es una función anónima sin parametros que siempre devuelve un 2. Como se ha asignado a una variable llamada dos,
#podemos decir que la función ya no es anónima, y se puede usar su nombre para invocarla.

#La segunda es una función anónima de un parámetro que devuelve el valor de su argumento al cuadrado. Se ha nombrado también como tal.

#La tercer lambda toma dos parametros y devuelve el valor del primero elevado al segundo. El nombre de la variable que lleva la lambda habla por si mismo.

#El programa produce el siguiente resultado:

#4 4
#1 1
#0 0
#1 1
#4 4

#Este ejemplo es lo suficientemente claro como para mostrar cómo se declaran las funciones lambda y cómo se comportan, 
# pero no dice nada acerca de por qué son necesarias y para qué se usan, ya que se pueden reemplazar con funciones de Python de rutina.

#¿Dónde está el beneficio?

print("---2---")

#¿Cómo usar lambdas y para qué?
#La parte más interesante de usar lambdas aparece cuando puedes usarlas en su forma pura - como partes anónimas de código destinadas a 
#evaluar un resultado.

#Imagina que necesitamos una función (la nombraremos imprimirfuncion) que imprime los valores de una (otra) 
#función dada para un conjunto de argumentos seleccionados.

#Queremos que imprimirfuncion sea universal - debería aceptar un conjunto de argumentos incluidos en una lista y una función a ser evaluada, 
#ambos como argumentos; no queremos codificar nada.

#Mira el ejemplo en el editor. Así es como hemos implementado la idea.
def imprimirfuncion(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

def poli(x):
	return 2 * x**2 - 4 * x + 2

imprimirfuncion([x for x in range(-2, 3)], poli) #Segundo argumento sólo hace mención de la función, pero no toma argumentos.
print(imprimirfuncion) #Ejemplo

#Analicémoslo. La función imprimirfuncion() toma dos parámetros:

#El primero, una lista de argumentos para los que queremos imprimir los resultados.
#El segundo, una función que debe invocarse tantas veces como el número de valores que se recopilan dentro del primer parámetro.
#Nota: También hemos definido una función llamada poli() - esta es la función cuyos valores vamos a imprimir. 
#El cálculo que realiza la función no es muy sofisticado: es el polinomio (de ahí su nombre) de la forma:

#f(x) = 2x2 - 4x + 2

#El nombre de la función se pasa a imprimirfuncion() junto con un conjunto de cinco argumentos diferentes: 
#el conjunto está construido con una cláusula de comprensión de la lista.

#El código imprime las siguientes líneas:

#f(-2)=18
#f(-1)=8
#f(0)=2
#f(1)=0
#f(2)=2

#¿Podemos evitar definir la función poli(), ya que no la vamos a usar más de una vez? Sí, podemos: 
#este es el beneficio que puede aportar una función lambda.

#Mira el ejemplo de abajo. ¿Puedes ver la diferencia?

def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

#La función imprimirfuncion()se ha mantenido exactamente igual, pero no hay una función poli(). 
#Ya no la necesitamos, ya que el polinomio ahora está directamente dentro de la invocación de la función imprimirfuncion() en forma de una 
#lambda definida de la siguiente manera: lambda x: 2 * x**2 - 4 * x + 2.

#El código se ha vuelto más corto, más claro y más legible.

#Permítenos mostrarte otro lugar donde las lambdas pueden ser útiles. Comenzaremos con una descripción de map(), 
#una función de Python incorporada. Su nombre no es demasiado descriptivo, su idea es simple y la función en sí es muy utilizable.



#NOTA SÚPER IMPORTANTE:
#Se pueden invocar funciones sin paréntesis.
#Las funciones en Python son los bloques de código definidos que realizan una tarea específica. En esta sección, 
#discutiremos la diferencia al invocar funciones con y sin paréntesis.

#Cuando llamamos a una función entre paréntesis, la función se ejecuta y devuelve el resultado al invocable.
#En otro caso, cuando llamamos a una función sin paréntesis, se envía una referencia de función al invocable 
#en lugar de ejecutar la función en sí.




print("---3---")

#Lambdas y la función map()
#En el más simple de todos los casos posibles, la función map() toma dos argumentos:

#Una función.
#Una lista.
#map(función, lista)

#La descripción anterior está extremadamente simplificada, ya que:

#El segundo argumento map() puede ser cualquier entidad que se pueda iterar (por ejemplo, una tupla o un generador).
#map() puede aceptar más de dos argumentos.
#La función map() aplica la función pasada por su primer argumento a todos los elementos de su segundo argumento 
#y devuelve un iterador que entrega todos los resultados de funciones posteriores. Puedes usar el iterador resultante en un bucle o convertirlo 
#en una lista usando la función list().

#¿Puedes ver un papel para una lambda aquí?

#Observa el código en el editor: hemos usado dos lambdas en él.
lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()
#Salida:
#[1, 2, 4, 8, 16]
#1 4 16 64 256 

#Esta es la explicación:

#Se construye la lista1 con valores del 0 al 4.
#Después, se utiliza map junto con la primer lambda para crear una nueva lista en la que todos los elementos 
#han sido evaluados como 2 elevado a la potencia tomada del elemento correspondiente de lista1.
#lista2 es entonces impresa.
#En el siguiente paso, se usa nuevamente la función map() para hacer uso del generador que devuelve, 
#e imprimir directamente todos los valores que entrega; como puedes ver, hemos usado el segundo lambda aquí - solo eleva al cuadrado cada 
#elemento de lista2.
#Intenta imaginar el mismo código sin lambdas. ¿Sería mejor? Es improbable.

print("---4---")

#Lambdas y la función filter()
#Otra función de Python que se puede embellecer significativamente mediante la aplicación de una lambda es filter().

#Espera el mismo tipo de argumentos que map(), pero hace algo diferente - filtra su segundo argumento mientras es guiado por direcciones 
#que fluyen desde la función especificada en el primer argumento (la función se invoca para cada elemento de la lista, al igual que en map() ).

#Ojo:
#Los elementos que regresan True de la función pasan el filtro - los otros son rechazados.

#El ejemplo en el editor muestra la función filter() en acción.
from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data)) #Sin la función list, sólo te daría el nombre del espacio de la lista con filter
print(data)
print(filtered)
#Nota: hemos hecho uso del módulo random para inicializar el generador de números aleatorios (que no debe confundirse 
#con los generadores de los que acabamos de hablar) con la función seed(), para producir cinco valores enteros 
#aleatorios de -10 a 10 usando la función randint().

#Luego se filtra la lista y solo se aceptan los números que son pares y mayores que cero.

#Por supuesto, no es probable que recibas los mismos resultados, pero así es como se veían nuestros resultados:

#[6, 3, 3, 2, -7]
#[6, 2]


print("---5---")

#Una breve explicación de cierres
#Comencemos con una definición: cierres es una técnica que permite almacenar valores a pesar de que 
#el contexto en el que se crearon ya no existe.. ¿Complicado? Un poco.

#Analicemos un ejemplo simple:

def exterior(par):
    loc = par

var = 1
exterior(var)


print(var)
#print(par) GENERA ERROR PORQUE LA VARIABLE ES DE SCOPE DE LA FUNCIÓN
#print(loc) GENERA ERROR PORQUE LA VARIABLE ES DE SCOPE DE LA FUNCIÓN

#El ejemplo es obviamente erróneo.

#Las dos últimas líneas provocarán una excepción NameError - ni par ni loc son accesibles fuera de la función. 
#Ambas variables existen cuando y solo cuando la función exterior() esta siendo ejecutada.

#Mira el ejemplo en el editor. Hemos modificado el código significativamente.
def exterior(par):
    loc = par
    def interior():
        return loc  
    return interior

var = 1
fun = exterior(var)
print(fun()) #Devuelve: 1, porque como función guarda el valor 1 ingresado al invocar la función exterior
print(fun) #Devuelve: <function exterior.<locals>.interior at 0x7f0e02b420e0>

#Hay un elemento completamente nuevo - una función (llamada interior) dentro de otra función (llamada exterior).

#¿Como funciona? Como cualquier otra función excepto por el hecho de que interior() solo se puede invocar desde dentro de exterior().
#Podemos decir que interior() es una herramienta privada de exterior(), ninguna otra parte del código la puede acceder.

#Observa cuidadosamente:

#ATENCIÓN:
#La función interior() devuelve el valor de la variable accesible dentro de su alcance, ya que interior() 
#puede utilizar cualquiera de las entidades a disposición de exterior().
#La función exterior() devuelve la función interior() por si misma; mejor dicho, devuelve una copia de la función interior() 
#al momento de la invocación de la función exterior(); la función congelada contiene su entorno completo, 
#incluido el estado de todas las variables locales, lo que también significa que el valor de loc se retiene con éxito, 
#aunque exterior() ya ha dejado de existir.
#En efecto, el código es totalmente válido y genera:

#1

#FINALMENTE:
#La función devuelta durante la invocación de exterior() es un cierre.


print("---6---")

#Una breve explicación de cierres: continuación
#Un cierre se debe invocar exactamente de la misma manera en que se ha declarado.

#En el ejemplo anterior (vea el código a continuación):

def exterior(par):
	loc = par
	def interior():
		return loc
	return interior

var = 1
fun = exterior(var)
print(fun())

#La función interior() no tenía parámetros, por lo que tuvimos que invocarla sin argumentos.

#Ahora mira el código en el editor. Es totalmente posible declarar un cierre equipado con un número arbitrario de parámetros, 
#por ejemplo, al igual que la función potencia().
def crearcierre(par):
    loc = par
    def potencia(p):
        return p ** loc
    return potencia

fsqr = crearcierre(2) #Los argumentos de la invocación se convierten en p en la función interior llamada potencia
fcub = crearcierre(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))

#Esto significa que el cierre no solo utiliza el ambiente congelado, sino que también puede modificar su 
#comportamiento utilizando valores tomados del exterior.

#Este ejemplo muestra una circunstancia más interesante: puedes crear tantos cierres como quieras usando el mismo código. 
#Esto se hace con una función llamada crearcierre(). Nota:

#El primer cierre obtenido de crearcierre() define una herramienta que eleva al cuadrado su argumento.
#El segundo está diseñado para elevar el argumento al cubo.
#Es por eso que el código produce el siguiente resultado:

#0 0 0
#1 1 1
#2 4 8
#3 9 27
#4 16 64

#Realiza tus propias pruebas.



