#Cómo construir tu propio generador
#¿Qué pasa si necesitas un generador para producir las primeras n potencias de 2 ?
#CÓMO CONVERTIR UNA FUNCIÓN EN UN GENERADOR, SIN EL INCONVENIENTE DEL RETURN

#Nada difícil. Solo mira el código en el editor.
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia #si fuese return, sólo pasaría un int
        potencia *= 2

for v in potenciasDe2(8):
    print(v)
#¿Puedes adivinar la salida? Ejecuta el código para verificar tus conjeturas.
#2ala0
#2ala1
#2ala2
#2ala3
#2ala4
#2ala5
#. 
#.
#.
#Forma 2 más sencilla:
#FORMA 2, MÁS SENCILLA:
def potencia(n):
    for i in range(n):
        print(pow(2, i))
        
        
potencia(8)


#Los generadores también pueden usarse dentro de listas de comprensión, como aqui:

def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = [x for x in potenciasDe2(5)] #RECORDAR LISTA DE COMPRESIÓN
#El resultado se imprime dentro de una lista
print(t)

#Ejecuta el ejemplo y verifica la salida.
#Lo muestra en forma de lista

#La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista real:

def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = list(potenciasDe2(3))

print(t)

#Nuevamente, intenta predecir el resultado y ejecuta el código para verificar tus predicciones.
#Salida:
#[1,2,4]
#Además, el contexto creado por el operador in también te permite usar un generador.

#El ejemplo muestra cómo hacerlo:

def potenciasDe2(n):
    potencia= 1
    for i in range(n):
        yield potencia
        potencia*= 2

for i in range(20):
    if i in potenciasDe2(4):
        print(i)

#¿Cuál es la salida del código? Ejecuta el programa y verifica.
#Salida: 
#Intersección de las dos listas

#Ahora veamos un Generador de números de la serie Fibonacci implementando lo anterior.

#Aquí está:

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)

#Adivina la salida (una lista) producida por el generador y ejecuta el código para verificar si tenías razón.


print("---3---")

#Más sobre comprensión de listas
#Debes poder recordar las reglas que rigen la creación y el uso de un fenómeno de Python llamado comprensión de listas: 
#una forma simple de crear listas y sus contenidos.

#En caso de que lo necesites, te proporcionamos un recordatorio en el editor.
listaUno = []
for ex in range(6):
    listaUno.append(10 ** ex)

#esto es igual a:
listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)

#Existen dos partes dentro del código, ambas crean una lista que contiene algunas de las primeras potencias naturales de diez.

#La primer parte utiliza una forma rutinaria del bucle for, mientras que la segunda hace uso de la comprensión de listas y 
#construye la lista en el momento, sin necesidad de un bucle o cualquier otro código.

#Pareciera que la lista se crea dentro de sí misma; esto es falso, ya que Python tiene que realizar casi las mismas operaciones 
#que en la primera parte, pero el segundo formalismo es simplemente más elegante y le evita al lector cualquier detalle innecesario.

#El ejemplo genera dos líneas idénticas que contienen el siguiente texto:

#[1, 10, 100, 1000, 10000, 100000]

#Ejecuta el código para verificar si tenemos razón.

print("---4---")

#Más sobre comprensión de listas: continuación
#Hay una sintaxis muy interesante que queremos mostrarte ahora. Su usabilidad no se limita a la comprensión de listas.

#Es una expresión condicional: una forma de seleccionar uno de dos valores diferentes en función del resultado de una expresión booleana.

#Observa :

#expresión_uno if condición else expresión_dos

#Puede parecer un poco sorprendente a primera vista, pero hay que tener en cuenta que no es una instrucción condicional. Además, 
#no es una instrucción en lo absoluto. Es un operador.

#El valor que proporciona es expresión_uno cuando la condición es True (verdadero), y expresión_dos cuando sea falso.

#Un buen ejemplo te dirá más. Mira el código en el editor.
lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

print(lst)

#Salida:
#[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#El código llena una lista con unos y ceros, si el índice de un elemento particular es impar, el elemento se establece en 0, 
#y a 1 de lo contrario.

#¿Simple? Quizás no a primera vista. ¿Elegante? Indiscutiblemente.

#¿Se puede usar el mismo truco dentro de una lista de comprensión? Sí, por supuesto.

print("---5---")

#Más sobre comprensión de listas: continuación
#Mira el ejemplo en el editor.
lst = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lst)
#Salida:
#[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#Compacidad y elegancia: estas dos palabras vienen a la mente al mirar el código.

#Entonces, ¿qué tienen en común, generadores y listas de comprensión? ¿Hay alguna conexión entre ellos? Sí. 
#Una conexión algo suelta, pero inequívoca.

#Solo un cambio puede convertir cualquier comprensión en un generador.

#Ahora mira el código a continuación y ve si puedes encontrar el detalle que convierte una comprensión de la lista en un generador:
lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()
#IMPORTANTE: LOS GENERADORES USAN PARÉNTESIS
#Son los paréntesis. Los corchetes hacen una comprensión, los paréntesis hacen un generador.

#El código, cuando se ejecuta, produce dos líneas idénticas:

#1 0 1 0 1 0 1 0 1 0
#1 0 1 0 1 0 1 0 1 0

#¿Cómo puedes saber que la segunda asignación crea un generador, no una lista?

#Hay algunas pruebas que podemos mostrarte. Aplica la función len() a ambas entidades.

#OJOOOOOOOOOOO:
#len(lst) dará como resultado 10, claro y predecible, len(genr) provocará una excepción y verás el siguiente mensaje:
#TypeError: object of type 'generator' has no len()

#Por supuesto, guardar la lista o el generador no es necesario; puedes crearlos exactamente en el lugar donde los necesites, como aquí:

for v in [1 if x % 2 == 0 else 0 for x in range(10)]: #Lista por comprensión
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)): #GENERADOR
    print(v, end=" ")
print()

#Nota: la misma apariencia de la salida no significa que ambos bucles funcionen de la misma manera. En el primer bucle,
#la lista se crea (y se itera) como un todo; en realidad, existe cuando se ejecuta el bucle.

#En el segundo bucle, no hay ninguna lista, solo hay valores subsequentes producidos por el generador, uno por uno.

#Realiza tus propios experimentos.


