#¿Qué contiene un objeto?
#La programación orientada a objetos supone que cada objeto existente puede estar equipado con tres grupos de atributos:

#Un objeto tiene un nombre que lo identifica de forma exclusiva dentro de su namespace 
#(aunque también puede haber algunos objetos anónimos).
#Un objeto tiene un conjunto de propiedades individuales que lo hacen original, 
#único o sobresaliente (aunque es posible que algunos objetos no tengan propiedades).
#Un objeto tiene un conjunto de habilidades para realizar actividades específicas, 
#capaz de cambiar el objeto en sí, o algunos de los otros objetos.
#Hay una pista (aunque esto no siempre funciona) que te puede ayudar a identificar cualquiera de las tres esferas anteriores. 
#Cada vez que se describe un objeto y se usa:

#Un sustantivo: probablemente se este definiendo el nombre del objeto.
#Un adjetivo: probablemente se este definiendo una propiedad del objeto.
#Un verbo: probablemente se este definiendo una actividad del objeto.


#Dos ejemplos deberían servir como un buen ejemplo:

#Max es un gato grande que duerme todo el día.

#Nombre del objeto = Max
#Clase de inicio = Gato
#Propiedad = Tamaño (grande)
#Actividad = Dormir (todo el día)

#Un Cadillac rosa pasó rápidamente.

#Nombre del objeto = Cadillac
#Clase de inicio = Vehículo terrestre
#Propiedad = Color (rosa)
#Actividad = Pasar (rápidamente)

print("---2---")

#Tu primera clase
#La programación orientada a objetos es el arte de definir y expandir clases. Una clase es un modelo de una parte muy específica de la realidad, 
#que refleja las propiedades y actividades que se encuentran en el mundo real.

#Las clases definidas al principio son demasiado generales e imprecisas para cubrir el mayor número posible de casos reales.

#No hay obstáculo para definir nuevas subclases más precisas. Heredarán todo de su superclase, por lo que el trabajo que se utilizó 
#para su creación no se desperdicia.

#La nueva clase puede agregar nuevas propiedades y nuevas actividades y, por lo tanto, puede ser más útil en aplicaciones específicas. 
#Obviamente, se puede usar como una superclase para cualquier número de subclases recién creadas.

#El proceso no necesita tener un final. Puedes crear tantas clases como necesites.

#La clase que se define no tiene nada que ver con el objeto: la existencia de una clase no significa que ninguno de los objetos compatibles 
#se creará automáticamente. La clase en sí misma no puede crear un objeto: debes crearlo tu mismo y Python te permite hacerlo.

#Es hora de definir la clase más simple y crear un objeto. Echa un vistazo al siguiente ejemplo:

class ClaseSimple:
    pass

#Hemos definido una clase. La clase es bastante pobre: no contiene propiedades ni actividades. Esta vacía, pero eso no importa por ahora. 
#Cuanto más simple sea la clase, mejor para nuestros propósitos.

#La definición comienza con la palabra clave reservada class. La palabra clave reservada es seguida por un identificador que nombrará la clase 
#(nota: no lo confundas con el nombre del objeto: estas son dos cosas diferentes).

#A continuación, se agregan dos puntos:), como clases, como funciones, forman su propio bloque anidado. El contenido dentro del bloque define 
#todas las propiedades y actividades de la clase.

#La palabra clave reservada pass llena la clase con nada. No contiene ningún método ni propiedades.

#PENDIENTE:
#Tu primer objeto
#La clase recién definida se convierte en una herramienta que puede crear nuevos objetos. La herramienta debe usarse explícitamente, 
#bajo demanda.

#Imagina que deseas crear un objeto (exactamente uno) de la clase ClaseSimple.

#Para hacer esto, debes asignar una variable para almacenar el objeto recién creado de esa clase y crear un objeto al mismo tiempo.

#Se hace de la siguiente manera:

miPrimerObjeto = ClaseSimple()

#Nota:

#El nombre de la clase intenta fingir que es una función, ¿puedes ver esto? Lo discutiremos pronto.
#El objeto recién creado está equipado con todo lo que trae la clase; Como esta clase está completamente vacía, el objeto también está vacío.
#El acto de crear un objeto de la clase seleccionada también se llama instanciación (ya que el objeto se convierte en una instancia de la clase).

#Dejemos las clases en paz por un breve momento, ya que ahora diremos algunas palabras sobre pilas.
#Sabemos que el concepto de clases y objetos puede no estar completamente claro todavía. No te preocupes, te explicaremos todo muy pronto.


print("---3---")
#¿Qué es una pila?
#Una pila es una estructura desarrollada para almacenar datos de una manera muy específica.. Imagina una pila de monedas. 
#No puedes poner una moneda en ningún otro lugar sino en la parte superior de la pila. Del mismo modo, 
#no puedes sacar una moneda de la pila desde ningún lugar que no sea la parte superior de la pila. 
#Si deseas obtener la moneda que se encuentra en la parte inferior, debes eliminar todas las monedas de los niveles superiores.

#El nombre alternativo para una pila (pero solo en la terminología de TI) es UEPS (LIFO son sus siglas en íngles). 
#Es una abreviatura para una descripción muy clara del comportamiento de la pila: Último en Entrar - Primero en Salir (Last In - First Out).
#La moneda que quedó en último lugar en la pila saldrá primero.

#Una pila es un objeto con dos operaciones elementales, denominadas convencionalmente push 
#(cuando un nuevo elemento se coloca en la parte superior) y pop (cuando un elemento existente se retira de la parte superior).

#Las pilas se usan muy a menudo en muchos algoritmos clásicos, 
#y es difícil imaginar la implementación de muchas herramientas ampliamente utilizadas sin el uso de pilas.

#Implementemos una pila en Python. Esta será una pila muy simple, y te mostraremos cómo hacerlo en dos enfoques independientes: 
#de manera procedimental y orientado a objetos.

#Comencemos con el primero:

#La pila: el enfoque procedimental
#Primero, debes decidir cómo almacenar los valores que llegarán a la pila. Sugerimos utilizar el método más simple, 
#y emplear una lista para esta tarea. Supongamos que el tamaño de la pila no está limitado de ninguna manera. 
#Supongamos también que el último elemento de la lista almacena el elemento superior.

#La pila en sí ya está creada:

pila = []

#Estamos listos para definir una función que pone un valor en la pila. Aquí están las presuposiciones para ello:

#El nombre para la función es push.
#La función obtiene un parámetro (este es el valor que se debe colocar en la pila).
#La función no devuelve nada.
#La función agrega el valor del parámetro al final de la pila.
#Así es como lo hemos hecho, echa un vistazo:

def push(val):
    pila.append(val)

#Ahora es tiempo de que una función quite un valor de la pila. Así es como puedes hacerlo:

#El nombre de la función es pop.
#La función no obtiene ningún parámetro.
#La función devuelve el valor tomado de la pila.
#La función lee el valor de la parte superior de la pila y lo elimina.
#La función esta aqui:

def pop():
    val = pila[-1]
    del pila[-1]
    return val

#Nota: la función no verifica si hay algún elemento en la pila.

#Armemos todas las piezas juntas para poner la pila en movimiento. El programa completo empuja (push) tres números a la pila, 
#los saca e imprime sus valores en pantalla. Puedes verlo en la ventana del editor.
pila = []

def push(val): #función que pega un valor a la pila
    pila.append(val)


def pop(): #Función que quita un valor de la pila
    val = pila[-1] #[:] mostraría todo en caso de ser así
    del pila[-1]
    return val

push(3)
push(2)
push(1)

print(pop()) #Está mostrando los valores que se eliminan (1)
print(pop()) #2
print(pop()) #3

#El programa muestra el siguiente texto en pantalla:

#1
#2
#3
#Salida si: [:]
#[3, 2, 1]
#[3, 2]
#[3]
#Pruébalo.

print("---4---")

#La pila: el enfoque procedimental frente al enfoque orientado a objetos:

##La pila procedimental está lista. Por supuesto, hay algunas debilidades, y la implementación podría mejorarse de muchas maneras 
#(aprovechar las excepciones es una buena idea), pero en general la pila está completamente implementada, y puedes usarla si lo necesitas.

#Pero cuanto más la uses, más desventajas encontrarás. Éstas son algunas de ellas:

#La variable esencial (la lista de la pila) es altamente vulnerable; cualquiera puede modificarla de forma incontrolable, destruyendo la pila; 
#esto no significa que se haya hecho de manera maliciosa; por el contrario, puede ocurrir como resultado de un descuido, por ejemplo, 
#cuando alguien confunde nombres de variables; imagina que accidentalmente has escrito algo como esto:

pila[0] = 0

#El funcionamiento de la pila estará completamente desorganizado.

#También puede suceder que un día necesites más de una pila; tendrás que crear otra lista para el almacenamiento de la pila, 
#y probablemente otras funciones push y pop.

#También puede suceder que no solo necesites funciones push y pop, pero también algunas otras funciones; ciertamente podrías implementarlas, 
#pero intenta imaginar qué sucedería si tuvieras docenas de pilas implementadas por separado.

#El enfoque orientado a objetos ofrece soluciones para cada uno de los problemas anteriores. Vamos a nombrarlos primero:

#La capacidad de ocultar (proteger) los valores seleccionados contra el acceso no autorizado se llama encapsulamiento; 
#no se puede acceder a los valores encapsulados 
#ni modificarlos si deseas utilizarlos exclusivamente.

#Cuando tienes una clase que implementa todos los comportamientos de pila necesarios, puedes producir tantas pilas como desees; 
#no necesitas copiar ni replicar ninguna parte del código.

#La capacidad de enriquecer la pila con nuevas funciones proviene de la herencia; puedes crear una nueva clase (una subclase) 
#que herede todos los rasgos existentes de la superclase y agregue algunos nuevos.

#Ahora escribamos una nueva implementación de pila desde cero. Esta vez, utilizaremos el enfoque orientado a objetos, 
#que te guiará paso a paso en el mundo de la programación de objetos.


print("---5---")

#La pila - el enfoque orientado a objetos
#Por supuesto, la idea principal sigue siendo la misma. Usaremos una lista como almacenamiento de la pila. 
#Solo tenemos que saber cómo poner la lista en la clase.

#Comencemos desde el principio: así es como comienza la pila de orientada a objetos:

class Pila:
    pass

#Ahora, esperamos dos cosas de la clase:

#Queremos que la clase tenga una propiedad como el almacenamiento de la pila - tenemos que "instalar" una lista dentro de cada objeto de la 
#clase (nota: cada objeto debe tener su propia lista; la lista no debe compartirse entre diferentes pilas).
#Despues, queremos que la lista esté oculta de la vista de los usuarios de la clase.
#¿Cómo se hace esto?

#A diferencia de otros lenguajes de programación, Python no tiene medios para permitirte declarar una propiedad como esa.

#En su lugar, debes agregar una instrucción específica. Las propiedades deben agregarse a la clase manualmente.

#¿Cómo garantizar que dicha actividad tiene lugar cada vez que se crea una nueva pila?

#Hay una manera simple de hacerlo - tienes que equipar a la clase con una función específica:

#Tiene que ser nombrada de forma estricta.
#Se invoca implícitamente cuando se crea el nuevo objeto.
#Tal función es llamada el constructor, ya que su propósito general es construir un nuevo objeto. 
#El constructor debe saber todo acerca de la estructura del objeto y debe realizar todas las inicializaciones necesarias.

#Agreguemos un constructor muy simple a la nueva clase. Echa un vistazo al código:

class Pila:
    def __init__(self):
        print("¡Hola!")

objetoPila = Pila()

#Expliquemos más a detalle:

#El nombre del constructor es siempre __init__.
#Tiene que tener al menos un parámetro (discutiremos esto más tarde); el parámetro se usa para representar el objeto recién creado: 
#puedes usar el parámetro para manipular el objeto y enriquecerlo con las propiedades necesarias; harás uso de esto pronto.
#Nota: el parámetro obligatorio generalmente se denomina self - es solo una sugerencía, pero deberías seguirla - 
#simplifica el proceso de lectura y comprensión de tu código.
#El código está en el editor. Ejecútalo ahora.
class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        print("¡Hola!")

objetoPila = Pila()    # instanciando el objeto

#Aquí está su salida:

#¡Hola!

#Nota: no hay rastro de la invocación del constructor dentro del código. Ha sido invocado implícita y automáticamente. 
#Hagamos uso de eso ahora.
