#Métodos a detalle:
#Resumamos todos los hechos relacionados con el uso de métodos en las clases de Python.

#Como ya sabes, un método es una función que está dentro de una clase.

#Hay un requisito fundamental: un método está obligado a tener al menos un parámetro (no existen métodos sin parámetros; 
# un método puede invocarse sin un argumento, pero no puede declararse sin parámetros).

#El primer (o único) parámetro generalmente se denomina self. Te sugerimos que lo sigas nombrando de esta manera, 
#darle otros nombres puede causar sorpresas inesperadas.

#OJO:
#El nombre self sugiere el propósito del parámetro - identifica el objeto para el cual se invoca el método.

#Si vas a invocar un método, no debes pasar el argumento para el parámetro self - Python lo configurará por ti.

#El ejemplo en el editor muestra la diferencia.

#El código da como salida:
class conClase:
    def metodo(self):
        print("método")

obj = conClase() #Se pasa como función
obj.metodo() #No hay que especificar la palabra self del parámetro de dicho método
#Salida:
#método

#Toma en cuenta la forma en que hemos creado el objeto - hemos tratado el nombre de la clase como una función, 
#y devuelve un objeto recién instanciado de la clase.

#Si deseas que el método acepte parámetros distintos a self, debes:

#OJO ACÁ:
#Colocarlos después de self en la definición del método.
#Pasarlos como argumentos durante la invocación sin especificar self.
#Justo como aqui:

class conClase:
    def metodo(self, par):
        print("método:", par)

obj = conClase()
obj.metodo(1)
obj.metodo(2)
obj.metodo(3)

#El código da como salida:
#método: 1
#método: 2
#método: 3

print("---2---")

#Métodos a detalle: continuación
#IMPORTANTE:
#El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.

#El ejemplo muestra ambas formas de utilizar el parámetro self:
class conClase:
    varia = 2
    def metodo(self):
        print(self.varia, self.var) #Así accede a la instancia de objeto y variables de clases, RESPECTIVAMENTE.
        #Sin el self, no se reconocieran dentro del método. INTERESANTE

obj = conClase()
obj.var = 3
obj.metodo()

#El código da como salida:

#2 3

#OJOOOOOOOOOO:
#El parámetro self también se usa para invocar otros métodos desde dentro de la clase.

#Justo como aquí:

class conClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = conClase()
obj.metodo()

#El código da como salida:

#método
#otro

print("---3---")

#Métodos a detalle: continuación
#DEFINICIÓN DE CONSTRUCTOR (UN MÉTODO CON EL NOMBRE INIT)
#Si se nombra un método de esta manera: __init__, no será un método regular, será un constructor.

#Si una clase tiene un constructor, este se invoca automática e implícitamente cuando se instancia el objeto de la clase.

#El constructor:

#Esta obligado a tener el parámetro self (se configura automáticamente).
#Pudiera (pero no necesariamente) tener mas parámetros que solo self; si esto sucede, 
#la forma en que se usa el nombre de la clase para crear el objeto debe tener la definición __init__.
#Se puede utilizar para configurar el objeto, es decir, inicializa adecuadamente su estado interno, 
#crea variables de instancia, crea instancias de cualquier otro objeto si es necesario, etc.
#Observa el código en el editor. El ejemplo muestra un constructor muy simple pero funcional.
class conClase:
    def __init__(self, valor):
        self.var = valor

obj1 = conClase("objeto")

print(obj1.var)

#Ejecutalo. El código da como salida:

#objeto


#IMPORTANTE:
#Ten en cuenta que el constructor:

#No puede retornar un valor, ya que está diseñado para devolver un objeto recién creado y nada más.
#No se puede invocar directamente desde el objeto o desde dentro de la clase 
#(puedes invocar un constructor desde cualquiera de las superclases del objeto, pero discutiremos esto más adelante).

print("---4---")

#Métodos a detalle: continuación
#Como __init__ es un método, y un método es una función, 
#puedes hacer los mismos trucos con constructores y métodos que con las funciones ordinarias.

#El ejemplo en el editor muestra cómo definir un constructor con un valor de argumento (también parámetro) predeterminado. Pruébalo.
class conClase:
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)

#El código da como salida:

#objeto
#None


#Todo lo que hemos dicho sobre el manejo de los nombres también se aplica a los nombres de métodos, 
#un método cuyo nombre comienza con __ está (parcialmente) oculto.

#El ejemplo muestra este efecto:

class conClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._conClase__oculto() #Así se llaman los métodos o atributos ocultos, o, simplemente, creamos un un método que retorne valores (como en la U.)
#Lo mismo para los atributos
#Forma general:
#object._class__variable
#Forma general con método:
#objeto._clase__métodoOculto()


#El código da como salida:

#visible
#fallido
#oculto

#Ejecuta el programa y pruébalo.


#INCISO: FORMA 2 DE OBTENER LOS VALORES DE UNA PROPIEDAD PRIVADA
#Indagando en internet, encontré este forma de acceder externamente de la clase:

class Administrativo():
    def __init__(self):
        self.__cedula=10366694853
 
Javier = Administrativo() #Instancia

print(Javier._Administrativo__cedula); #La forma general es: object._class__variable de obtener un atributo privado

#Al no poder acceder a este dato normalmente, se debe crear un método que retorne el valor de la variable.
class Administrativo():
    def __init__(self):
        self.__cedula=10366694853
    def obtenerCedula(self):
        return self.__cedula
 
Javier=Administrativo()
print(Javier.obtenerCedula())


print("----5----")

#La vida interna de clases y objetos
#Cada clase de Python y cada objeto de Python está pre-equipado con un conjunto de atributos útiles que 
#pueden usarse para examinar sus capacidades.

#Ya conoces uno de estos: es la propiedad __dict__.

#Observemos cómo esta propiedad trata con los métodos: mira el código en el editor.
class conClase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)

#Ejecútalo para ver qué produce. Verifica el resultado.

#Encuentra todos los métodos y atributos definidos. Localiza el contexto en el que existen: dentro del objeto o dentro de la clase.


#otra forma:

class conClase:
    varia = 1
    def __init__(self,var):
        self.var = var

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase(5)

print(obj.__dict__) #Muestra solo los atributos instanciados
print(conClase.__dict__) #Muestra todos los métodos y atributos definidos