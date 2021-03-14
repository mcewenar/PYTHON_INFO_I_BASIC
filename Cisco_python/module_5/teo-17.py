#Rodajas o Rebanadas (O CORTES DE LISTAS)
#Todo lo que sabes sobre rodajas o rebanadas es utilizable.

#Hemos reunido algunos ejemplos que muestran cómo funcionan las rodajas en el mundo de las cadenas. 
#Mira el código en el editor, analizalo y ejecútalo.
# Rodajas o rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:]) #3 a final
print(alpha[:3]) #0 a d, no llega al 3 porque se ucenta de 0
print(alpha[3:-2]) #de 3 a -2 (-2 tirando de derecha a izquierda) O sea, e
print(alpha[-3:4]) # -3 y luego se cuenta 4 de izq a derecha. Dando e.
print(alpha[::2]) #toda la lista con paso 2. (::2)
print(alpha[1::2]) #a partir de la posición 1 hasta el final con paso 2
#No verás nada nuevo en el ejemplo, pero queremos que estés seguro de entender todas las líneas del código.

#La salida del código es:

#bd
#efg
#abd
#e
#e
#adf
#beg

#Ahora haz tus propios experimentos.

print("---2---")
#Los operadores in y not in
#El operador in no debería sorprenderte cuando se aplica a cadenas, simplemente comprueba si el argumento izquierdo (una cadena) 
#se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).

#El resultado es simplemente True (Verdadero) o False (Falso).

#Observa el ejemplo en el editor. Así es como el operador in funciona.
alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)

#El resultado de ejemplo es:
#True
#False
#False
#True
#False

#Como probablemente puedas deducir, el operador not in también es aplicable aquí.

#Así es como funciona:

alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alfabeto)
print("F" not in alfabeto)
print("1" not in alfabeto)
print("ghi" not in alfabeto)
print("Xyz" not in alfabeto)

#El resultado de ejemplo es:

#False
#True
#True
#False
#True

print("---3---")
#IMPORTANTE:
#Las cadenas de Python son inmutables
#También te hemos dicho que las cadenas de Python son inmutables. Esta es una característica muy importante. ¿Qué significa?

#Esto significa principalmente que la similitud de cadenas y listas es limitada. No todo lo que puede hacerse con una lista puede 
#hacerse con una cadena.

#La primera diferencia importante no te permite usar la instrucción del para eliminar cualquier cosa de una cadena.

#El ejemplo siguiente no funcionará:

alfabeto = "abcdefghijklmnopqrstuvwxyz"

#del alfabeto[0] ERRORRRRRRR (NO SE PUEDE ELIMINAR CARÁCTERES DE UNA CADENA)

#OJO AQUÍ:
#Lo único que puedes hacer con del y una cadena es eliminar la cadena como un todo. Intenta hacerlo.


#Las cadenas de Python no tienen el método append() - no se pueden expander de ninguna manera.

#El siguiente ejemplo es erróneo:

alfabeto = "abcdefghijklmnopqrstuvwxyz"

#alfabeto.append("A") ERRRRRORRRRRR

#Con la ausencia del método append(), el método insert() también es ilegal:

alfabeto = "abcdefghijklmnopqrstuvwxyz"

#alfabeto.insert(0, "A") ERRORRRR

print("--4--")
#Operaciones con cadenas: continuación
#No pienses que la inmutabilidad de una cadena limita tu capacidad de operar con ellas.

#La única consecuencia es que debes recordarlo e implementar tu código de una manera ligeramente diferente: 
#observa el código en el editor.
alfabeto = "bcdefghijklmnopqrstuvwxy"

alfabeto = "a" + alfabeto
alfabeto = alfabeto + "z"

print(alfabeto)

#Esta forma de código es totalmente aceptable, funcionará sin doblar las reglas de Python y traerá el alfabeto 
#latino completo a tu pantalla:

#Salida:
#abcdefghijklmnopqrstuvwxyz

#Es posible que desees preguntar si el crear una nueva copia de una cadena cada vez que se 
#modifica su contenido empeora la efectividad del código.

#Sí lo hace. Un poco. Sin embargo, no es un problema en absoluto.

print("--5--")
#Operaciones con cadenas: min()
#Ahora que comprendes que las cadenas son secuencias, podemos mostrarte algunas capacidades de secuencia menos obvias. 
#Las presentaremos utilizando cadenas, pero no olvides que las listas también pueden adoptar los mismos trucos.

#Comenzaremos con la función llamada min().

#Esta función encuentra el elemento mínimo de la secuencia pasada como argumento. Existe una condición - 
#la secuencia (cadena o lista) no puede estar vacía, de lo contrario obtendrás una excepción ValueError.
# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ"))


# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

#El programa Ejemplo 1 da la siguiente salida:

#A

#Nota: Es una A mayúscula. ¿Por qué? Recuerda la tabla ASCII, ¿qué letras ocupan las primeras posiciones, mayúsculas o minúsculas?


#Hemos preparado dos ejemplos más para analizar: Ejemplos 2 y 3.

#Como puedes ver, presentan más que solo cadenas. El resultado esperado se ve de la siguiente manera:

#[ ]
#0

#Nota: hemos utilizado corchetes para evitar que el espacio se pase por alto en tu pantalla.

print("---6---")

#Operaciones con cadenas: max()
#Del mismo modo, una función llamada max() encuentra el elemento máximo de la secuencia.

#Observa el Ejemplo 1 en el editor. La salida del programa es:
# Demostrando max() - Ejemplo 1
print(max("aAbByYzZ"))


# Demonstrando max() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))
#Salida:
#z porque primero van las mayúsculas

#Nota: es una z minúscula.


#Ahora veamos la función max() a los mismos datos del ejemplo anterior. Observa los Ejemplos 2 y 3 en el editor.

#La salida esperada es:

#[¡]
#2

#Realiza tus propios experimentos.

print("---7---")
#MÉTODO NO FUNCIÓN
#Operaciones con cadenas: el método index()
#El método index() (es un método, no una función) busca la secuencia desde el principio, para encontrar el primer elemento del valor 
#especificado en su argumento.

#Nota: el elemento buscado debe aparecer en la secuencia - su ausencia causará una excepción ValueError.

#El método devuelve el índice de la primera aparición del argumento (lo que significa que el resultado más bajo posible es 0, 
#mientras que el más alto es la longitud del argumento decrementado por 1).
# Demonstrando el método index()
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#Por lo tanto, el ejemplo en la salida del editor es:

#2
#7
#1
print("---8---")

#Operaciones con cadenas: la función list()
#La función list() toma su argumento (una cadena) y crea una nueva lista que contiene todos los caracteres de la cadena,
#uno por elemento de la lista.

#Nota: no es estrictamente una función de cadenas - list() es capaz de crear una nueva lista de muchas otras entidades (por ejemplo,
#de tuplas y diccionarios).

#Observa el código de ejemplo en el editor.
# Demostrando la función list()
print(list("abcabc"))

# Demostrando el método count()
print("abcabc".count("b"))
print('abcabc'.count("d"))

#La salida es:

#['a', 'b', 'c', 'a', 'b', 'c']

#CON DICCIONARIO:
# Demostrando la función list()
dictio = {"a":"b","c":"d"}
print(list(dictio)) #Toma sólo las claves

# Demostrando el método count()
#ESTO ES APARTE:
print("abcabc".count("b"))
print('abcabc'.count("d"))

#Operaciones con cadenas: el método count()
#El método count() cuenta todas las apariciones del elemento dentro de la secuencia. La ausencia de tal elemento no causa ningún problema.

#Observa el segundo ejemplo en el editor. ¿Puedes adivinar su salida?

#Es:

#2
#0

#Las cadenas de Python tienen un número significativo de métodos destinados exclusivamente al procesamiento de caracteres.
#No esperes que trabajen con otras colecciones. 

#Pendiente:
#La lista completa se presenta aquí: https://docs.python.org/3.4/library/stdtypes.html#string-methods.

#Te mostraremos los que consideramos más útiles.