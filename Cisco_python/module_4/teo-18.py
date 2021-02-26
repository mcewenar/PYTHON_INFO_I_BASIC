#¿Qué es un diccionario? (importante)

#El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento 
# secuencial) y además es mutable.

#Para explicar lo que es un diccionario en Python, es importante comprender de manera literal lo que es un diccionario.

#Un diccionario en Python funciona de la misma manera que un diccionario bilingüe. Por ejemplo, se tiene la palabra en español "gato" 
#y se necesita su equivalente en francés. Lo que se haría es buscar en el diccionario para encontrar la palabra "gato". Eventualmente 
#la encontrarás, y sabrás que la palabra equivalente en francés es "chat".

#En el mundo de Python, la palabra que se esta buscando se denomina clave(key). La palabra que se obtiene del diccionario es denominada valor.

#Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:

#IMPORTANTE:
#Cada clave debe de ser única. No es posible tener una clave duplicada.
#Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante), o incluso una cadena.
#Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores.
#La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
#Un diccionario es una herramienta de un solo sentido. Si fuese un diccionario español-francés, podríamos buscar en español para encontrar 
#su contraparte en francés mas no viceversa.
#A continuación veamos algunos ejemplos:

#¿Cómo crear un diccionario?
#Si deseas asignar algunos pares iniciales a un diccionario, utiliza la siguiente sintaxis:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

#En este primer ejemplo, el diccionario emplea claves y valores las cuales ambas son cadenas. En el segundo, las claves con cadenas 
#pero los valores son enteros. 
#El orden inverso (claves → números, valores → cadenas) también es posible, así como la combinación número a número.

#La lista de todos los pares es encerrada con llaves, mientras que los pares son separados por comas, y las claves y valores por dos puntos.

#El primer diccionario es muy simple, es un diccionario Español-Francés. El segundo es un directorio telefónico muy pequeño.

#Los diccionarios vacíos son construidos por un par vacío de llaves - nada inusual.


#El diccionario entero se puede imprimir con una invocación a la función print(). El fragmento de código puede producir la siguiente salida:

#{'perro': 'chien', 'caballo': 'cheval', 'gato': 'chat'}
#{'Suzy': 5557654321, 'boss': 5551234567}
#{}

#¿Has notado que el orden de los pares impresos es diferente a la asignación inicial?, ¿Qué significa esto?

#Primeramente, recordemos que los diccionarios no son listas - no guardan el orden de sus datos, el orden no tiene significado 
#(a diferencia de los diccionarios reales). El orden en que un diccionario almacena sus datos esta fuera de nuestro control. Esto es normal. (*)

#NOTA: (IMPORTANTE)
#(*) En Python 3.6x los diccionarios se han convertido en colecciones ordenadas de manera predeterminada. 
#Tu resultado puede variar dependiendo en la versión de Python que se este utilizando.

print("----2----")

#¿Cómo utilizar un diccionario?
#Si deseas obtener cualquiera de los valores, debes de proporcionar una clave válida:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict['gato'])
print(numerosTelefono['Suzy'])
#El obtener el valor de un diccionario es semejante a la indexación, gracias a los corchetes alrededor del valor de la clave.

#Nota:

#Si una clave es una cadena, se tiene que especificar como una cadena.
#Las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.

#El fragmento de código da las siguientes salidas:
#salidas:
#chat
#5557654321

#Ahora algo muy importante: No se puede utilizar una clave que no exista. Hacer algo como lo siguiente:

#print(numerosTelefono['presidente'])

#Provocará un error de ejecución. Inténtalo.

#Afortunadamente, existe una manera simple de evitar dicha situación. El operador in, junto con su acompañante, not in,
#pueden salvarnos de esta situación.

#El siguiente código busca de manera segura palabras en francés:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word]) #Muestra el valor, no la clave.
    else:
        print(word, "no está en el diccionario")


#La salida del código es la siguiente:

#gato -> chat
#leon no está en el diccionario
#caballo -> cheval

print("----3----")

#¿Cómo utilizar un diccionario? El método keys()
#¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?

#No y si.

#No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.

#Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los requerimientos del bucle for 
#(en otras palabras, se construye un enlace intermedio entre el diccionario y una entidad secuencial temporal).

#El primero de ellos es un método denominado keys(), el cual es parte de todo diccionario. El método retorna o regresa una lista 
#de todas las claves dentro del diccionario. Al tener una lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.

#A continuación se muestra un ejemplo:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])

#El código produce la siguiente salida:

#caballo -> cheval
#perro -> chien
#gato -> chat

#La función sorted():
#¿Deseas que la salida este ordenada? Solo hay que agregar al bucle for lo siguiente:

for key in sorted(dict.keys()):
   print(key, "->", dict[key])

#La función sorted() hará su mejor esfuerzo y la salida será la siguiente:

#caballo -> cheval
#gato -> chat
#perro -> chien

print("----4-----")

#IMPORTANTE
#¿Cómo utilizar un diccionario? Los métodos item() y values()
#Otra manera de hacerlo es utilizar el método items(). Este método regresa una lista de tuplas 
#(este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.

#Así es como funciona:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items():
    print(spanish, "->", french)

#Nota la manera en que la tupla ha sido utilizada como una variable del bucle for.

#El ejemplo imprime lo siguiente:

#cat -> chat
#dog -> chien
#horse -> cheval

#También existe un método denominado values(), funciona de manera muy similar al de keys(), pero regresa una lista de valores. (REGRESA VALOR)

#Este es un ejemplo sencillo:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dict.values():
    print(french)

#Como el diccionario no es capaz de automáticamente encontrar la clave de un valor dado, el rol de este método es algo limitado.

#Esta es la salida esperada:

#cheval
#chien
#chat

print("----5----")

#¿Cómo utilizar un diccionario? Modificar, agregar y eliminar valores
#El asignar un nuevo valor a una clave existente es sencillo, debido a que los diccionarios son completamente mutables, 
#no existen obstáculos para modificarlos.


#MODIFICACIÓN:
#Se va a reemplazar el valor "chat" por "minou", lo cual no es muy adecuado, pero funcionará con nuestro ejemplo.

#Observa:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['gato'] = 'minou' #Se usa la clave para seleccionar y es el VALOR el que se modifica. La clave sólo sirve para seleccionar el diccionario
print(dict)

#La salida es:
#{'perro': 'chien', 'caballo': 'cheval', 'gato': 'minou'}

#Agregando nuevas claves:
#El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor. Solo se tiene que asignar un valor a 
#una nueva clave que no haya existido antes.

#Nota: este es un comportamiento muy diferente comparado a las listas, las cuales no permiten asignar valores a índices no existentes.

#A continuación se agrega un par nuevo al diccionario, un poco extraño pero valido:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

#El ejemplo muestra como salida:

#{'cisne': 'cygne', 'caballo': 'cheval', 'perro': 'chien', 'gato': 'chat'}


#EXTRA:
#IMPORTANTE:
#También es posible insertar un elemento al diccionario utilizando el método update(), por ejemplo:
print("forma 2 de añadir una clave valor nueva")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.update({"pato" : "canard"})
print(dict)

#Eliminado claves
#¿Puedes deducir como eliminar una clave de un diccionario?

#Nota: al eliminar la clave también se removerá el valor asociado. Los valores no pueden existir sin sus claves.

#Esto se logra con la instrucción del.

#A continuación un ejemplo:

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)

#Nota: el eliminar una clave no existente, provocará un error.

#El ejemplo da como salida:

#{'gato': 'chat', 'caballo': 'cheval'}


#EXTRA:

#Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem():
print("FORMA 2 PARA ELEMINAR UN ELEMENTO DE UN DICCIONARIO")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.popitem()
print(dict)    # outputs: {'gato' : 'chat', 'perro' : 'chien'}

#En versiones anteriores de Python, por ejemplo, antes de la 3.6.7, el método popitem() elimina un elemento al azar del diccionario.

print("Inciso:")
#NO SE REPITEN LAS CLAVES
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval", "perro": "pizza"} #SI SE REPIRE UNA CLAVE, LA SEGUNDA NO APARECE. 
#LAS CLAVES SON ÚNICAS

print(dict)


print("Inciso 2:")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items(): #GENERA UNA TUPLA
    print(spanish, "->", french)

for spanish in dict.items():
    print(spanish,"--->") #itera cada elemento como una tupla, clave: elemento[0] y valor: elemento[1]

#Cada clave debe de ser única. No es posible tener una clave duplicada.


print("----6----")
#Las tuplas y los diccionarios pueden trabajar juntos:
#Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los diccionarios pueden trabajar juntos.

#Imaginemos el siguiente problema:

#Necesitas un programa para calcular los promedios de tus alumnos.
#El programa pide el nombre del alumno seguido de su calificación.
#Los nombres son ingresados en cualquier orden.
#El ingresar la palabra exit da por terminado el ingreso de nombres.
#Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.

#Observa el código en el editor, se muestra la solución.
grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)



#Ahora se analizará línea por línea:

#Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las 
#calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).
#Línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado).
#Línea 4: se lee el nombre del alumno.
#Línea 5-6: si el nombre es exit, nos salimos del bucle.
#Línea 8: se pide la calificación del alumno (un valor entero en el rango del 1-10).
#Línea 10-11: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación 
#(observa el operador +=).
#Línea 12-13: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo 
#elemento la cual contiene la calificación ingresada.
#Línea 15: se itera a través de los nombres ordenados de los estudiantes.
#Línea 16-17: inicializa los datos necesarios para calcular el promedio (sumador y contador).
#Línea 18-20: Se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
#Línea 21: se calcula e imprime el promedio del alumno junto con su nombre.
#Este es un ejemplo del programa:

#Ingresa el nombre del estudiante (o exit para detenerse): Bob
#Ingresa la calificación del alumno (0-10): 7
#Ingresa el nombre del estudiante (o exit para detenerse): Andy
#Ingresa la calificación del alumno (0-10): 3
#Ingresa el nombre del estudiante (o exit para detenerse): Bob
#Ingresa la calificación del alumno (0-10): 2
#Ingresa el nombre del estudiante (o exit para detenerse): Andy
#Ingresa la calificación del alumno (0-10): 10
#Ingresa el nombre del estudiante (o exit para detenerse): Andy
#Ingresa la calificación del alumno (0-10): 3
#Ingresa el nombre del estudiante (o exit para detenerse): Bob
#Ingresa la calificación del alumno (0-10): 9
#Ingresa el nombre del estudiante (o exit para detenerse): exit
#Andy : 5.333333333333333
#Bob : 6.0

