#La vida interna de clases y objetos: continuación
#__dict__ es un diccionario. Otra propiedad incorporada que vale la pena mencionar es una cadena llamada __name__.

#La propiedad contiene el nombre de la clase. No es nada emocionante, es solo una cadena.

#Nota: el atributo __name__ está ausente del objeto - existe solo dentro de las clases.


#Si deseas encontrar la clase de un objeto en particular, puedes usar una función llamada type(), 
#la cual es capaz (entre otras cosas) de encontrar una clase que se haya utilizado para crear instancias de cualquier objeto.

#Mira el código en el editor, ejecútalo y compruébalo tu mismo.
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)

#La salida del código es:
#conClase
#conClase

#Nota: algo como esto print(obj.__name__) causará un error.

print("---2---")

#La vida interna de clases y objetos: continuación
#__module__ es una cadena, también almacena el nombre del módulo que contiene la definición de la clase.

#Vamos a comprobarlo: ejecuta el código en el editor.
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__)

#La salida del código es:

#__main__
#__main__

#Como sabes, cualquier módulo llamado __main__ en realidad no es un módulo, sino es el archivo actualmente en ejecución.


#NOTA: __main__ es el archivo en ejecución, no un módulo. "__module__" te dice el archivo que actualmente está en ejecución

print("---3---")
#La vida interna de clases y objetos: continuación
#__bases__ es una tupla. La tupla contiene clases (no nombres de clases) que son superclases directas para la clase.

#El orden es el mismo que el utilizado dentro de la definición de clase.

#Te mostraremos solo un ejemplo muy básico, ya que queremos resaltar como funciona la herencia.

#Además, te mostraremos cómo usar este atributo cuando discutamos los aspectos orientados a objetos de las excepciones.

#Nota: solo las clases tienen este atributo - los objetos no.

#Hemos definido una función llamada printBases(), diseñada para presentar claramente el contenido de la tupla.

#Observa el código en el editor. Ejecútalo. 
class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos): #Se puede heredar varias clases independientes
    pass

#OJO AQUÍ:
def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ') #Recordar que End==' ' quita los saltos de línea automáticos
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)



# Su salida es:

#( object )
#( object )
#( SuperUno SuperDos )

#IMPORTANTE:
#Nota: una clase sin superclases explícitas apunta al objeto (una clase de Python predefinida) como su antecesor directo.

print("---4---")

#Reflexión e introspección
#Todo esto permite que el programador de Python realice dos actividades importantes específicas para muchos lenguajes objetivos. 
#Las cuales son:

#Introspección, que es la capacidad de un programa para examinar el tipo o las propiedades de un objeto en tiempo de ejecución.
#Reflexión, que va un paso más allá, y es la capacidad de un programa para manipular los valores, 
#propiedades y/o funciones de un objeto en tiempo de ejecución.
#En otras palabras, no tienes que conocer la definición completa de clase/objeto para manipular el objeto,
#ya que el objeto y/o su clase contienen los metadatos que te permiten reconocer sus características durante la ejecución del programa.


print("---5---")

#Investigando Clases
#¿Qué puedes descubrir acerca de las clases en Python? La respuesta es simple: todo.

#Tanto la reflexión como la introspección permiten al programador hacer cualquier cosa con cada objeto, sin importar de dónde provenga.

#Analiza el código en el editor.
class MiClase:
    pass

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

#La función llamada incIntsI() obtiene un objeto de cualquier clase, 
#escanea su contenido para encontrar todos los atributos enteros con nombres que comienzan con i, y los incrementa en uno.

#¿Imposible? ¡De ningúna manera!

#Así es como funciona:

#La línea 1: define una clase simple...
#Líneas 3 a la 10: ... la llenan con algunos atributos.
#Línea 12: ¡esta es nuestra función!
#Línea 13: escanea el atributo __dict__, buscando todos los nombres de atributos.
#Línea 14: si un nombre comienza con i...
#Línea 15: ... utiliza la función getattr() para obtener su valor actual; 
#nota: getattr() toma dos argumentos: un objeto y su nombre de propiedad (como una cadena) y devuelve el valor del atributo actual.
#Línea 16: comprueba si el valor es de tipo entero, emplea la función isinstance() para este propósito (discutiremos esto más adelante).
#Línea 17: si la comprobación sale bien, incrementa el valor de la propiedad haciendo uso de la función setattr(); 
#la función toma tres argumentos: un objeto, el nombre de la propiedad (como una cadena) y el nuevo valor de la propiedad.
#El código da como salida:

#{'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'entero': 4, 'z': 5}
#{'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'entero': 4, 'z': 5}

#¡Eso es todo!
