#El enfoque orientado a objetos: una pila desde cero (continuación):
#En segundo lugar, agreguemos dos métodos. Pero, ¿realmente estamos agregándolos? Ya tenemos estos métodos en la superclase. 
#¿Podemos hacer algo así?

#Si podemos. Significa que vamos a cambiar la funcionalidad de los métodos, no sus nombres. 
#Podemos decir con mayor precisión que la interfaz (la forma en que se manejan los objetos) 
#de la clase permanece igual al cambiar la implementación al mismo tiempo.

#Comencemos con la implementación de la función push. Esto es lo que esperamos de la función:

#Agregar el valor a la variable __sum.
#Agregar el valor a la pila.
#Nota: la segunda actividad ya se implementó dentro de la superclase, por lo que podemos usarla. Además, 
#tenemos que usarla, ya que no hay otra forma de acceder a la variable __listaPila.

#Así es como se mira el método push dentro de la subclase:

#def push(self, val):
#    self.__sum += val
#    Pila.push(self, val)

#Toma en cuenta la forma en que hemos invocado la implementación anterior del método push (el disponible en la superclase):

#Tenemos que especificar el nombre de la superclase; esto es necesario para indicar claramente la clase que contiene el método, 
#para evitar confundirlo con cualquier otra función del mismo nombre.
#Tenemos que especificar el objeto de destino y pasarlo como primer argumento (no se agrega implícitamente a la invocación en este contexto).
#Se dice que el método push ha sido anulado - el mismo nombre que en la superclase ahora representa una funcionalidad diferente.

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

# ingresa código aquí
    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

#No importa:
pila = Pila()
sumaPila = SumarPila()

c=sumaPila.push(1)
pila.push(c)
print(pila)

print("---2---")

#El enfoque orientado a objetos: una pila desde cero (continuación)
#Esta es la nueva función pop:

def pop(self):
    val = Pila.pop(self)
    self.__sum -= val
    return val

#IMPORTANTE:
#Hasta ahora, hemos definido la variable __sum, pero no hemos proporcionado un método para obtener su valor. 
#Parece estar escondido. ¿Cómo podemos mostrarlo y que al mismo tiempo se proteja de modificaciones?

#Tenemos que definir un nuevo método. Lo nombraremos getSuma. Su única tarea será devolver el valor de __sum.

#Aquí está:
#Forma de obtener valores privados "__" sin hacerlo públicos 
def getSuma(self):
    return self.__sum

#Entonces, veamos el programa en el editor. El código completo de la clase está ahí. Podemos ahora verificar su funcionamiento, 
#y lo hacemos con la ayuda de unas pocas líneas de código adicionales.
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0


    def getSuma(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


objetoPila = SumarPila()

for i in range(5): 
    objetoPila.push(i)
print(objetoPila.getSuma()) #Hace una suma de toda la iteración, dando lugar a 10, luego pasa al otro for

for i in range(5):
    print(objetoPila.pop())

#Como puedes ver, agregamos cinco valores subsiguientes en la pila, imprimimos su suma y los sacamos todos de la pila.

#Bien, esta ha sido una breve introducción a la programación de orientada a objetos de Python. Pronto te contaremos todo con más detalle.


print("---3---")

#Variables de instancia
#En general, una clase puede equiparse con dos tipos diferentes de datos para formar las propiedades de una clase. 
#Ya viste uno de ellos cuando estábamos estudiando pilas.

#Este tipo de propiedad existe solo cuando se crea explícitamente y se agrega a un objeto. Como ya sabes, 
#esto se puede hacer durante la inicialización del objeto, realizada por el constructor.

#Además, se puede hacer en cualquier momento de la vida del objeto. 
#Es importante mencionar también que cualquier propiedad existente se puede eliminar en cualquier momento.

#Tal enfoque tiene algunas consecuencias importantes:

#Diferentes objetos de la misma clase pueden poseer diferentes conjuntos de propiedades.
#Debe haber una manera de verificar con seguridad si un objeto específico posee la propiedad que deseas utilizar 
#(a menos que quieras provocar una excepción, siempre vale la pena considerarlo).
#Cada objeto lleva su propio conjunto de propiedades - no interfieren entre sí de ninguna manera.
#Tales variables (propiedades) se llaman variables de instancia.

#La palabra instancia sugiere que están estrechamente conectadas a los objetos (que son instancias de clase), 
#no a las clases mismas. Echemos un vistazo más de cerca a ellas.

#Aquí hay un ejemplo:

class ClaseEjemplo:
    def __init__(self, val = 1):
        self.primera = val

    def setSegunda(self, val):
        self.segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2) #Se le tira un 2 predeterminado que se verá como un valor en el diccionario

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.tercera = 5


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__) #crea una propiedad nueva llamada tercera con valor 5

#Se necesita una explicación adicional antes de entrar en más detalles. Echa un vistazo a las últimas tres líneas del código.
#IMPORTANTE:
#Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto de propiedades y métodos predefinidos. 
#Cada objeto los tiene, los quieras o no. Uno de ellos es una variable llamada __dict__ (es un diccionario).

#La variable contiene los nombres y valores de todas las propiedades (variables) que el objeto contiene actualmente. 
#Vamos a usarla para presentar de forma segura el contenido de un objeto.

#Vamos a sumergirnos en el código ahora:

#La clase llamada ClaseEjemplo tiene un constructor, el cual crea incondicionalmente una variable de instancia llamada primera, 
#y le asigna el valor pasado a través del primer argumento (desde la perspectiva del usuario de la clase) 
#o el segundo argumento (desde la perspectiva del constructor); ten en cuenta el valor predeterminado del parámetro: 
#cualquier cosa que puedas hacer con un parámetro de función regular también se puede aplicar a los métodos.

#La clase también tiene un método que crea otra variable de instancia, llamada segunda.

#Hemos creado tres objetos de la clase ClaseEjemplo, pero todas estas instancias difieren:

#objetoEjemplo1 solo tiene una propiedad llamada primera.

#objetoEjemplo2 tiene dos propiedades: primera y segunda.

#objetoEjemplo3 ha sido enriquecido sobre la marcha con una propiedad llamada tercera, fuera del código de la clase: 
#esto es posible y totalmente permisible.

#La salida del programa muestra claramente que nuestras suposiciones son correctas: aquí están:
#Salida:
#{'primera': 1}
#{'primera': 2, 'segunda': 3}
#{'primera': 4, 'tercera': 5}

#Ojo:
#Hay una conclusión adicional que debería mencionarse aquí: 
#el modificar una variable de instancia de cualquier objeto no tiene impacto en todos los objetos restantes. 
#Las variables de instancia están perfectamente aisladas unas de otras.


