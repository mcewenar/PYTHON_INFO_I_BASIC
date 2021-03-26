#La pila - el enfoque orientado a objetos: continuación
#Cualquier cambio que realices dentro del constructor que modifique el estado del parámetro self se verá reflejado en el objeto recien creado.

#Esto significa que puedes agregar cualquier propiedad al objeto y la propiedad permanecerá 
#allí hasta que el objeto termine su vida o la propiedad se elimine explícitamente.

#Ahora agreguemos solo una propiedad al nuevo objeto - una lista para la pila. La nombraremos listaPila.

#Justo como aqui:

class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.listaPila))

#Nota:
#OJO:
#Hemos usado la notación punteada, al igual que cuando se invocan métodos. 
#Esta es la manera general para acceder a las propiedades de un objeto: debes nombrar el objeto, poner un punto (.) después de el,
# y especificar el nombre de la propiedad deseada, ¡no uses paréntesis! No deseas invocar un método, deseas acceder a una propiedad.
#Si estableces el valor de una propiedad por primera vez (como en el constructor), lo estás creando; a partir de ese momento,
# el objeto tiene la propiedad y está listo para usar su valor.
#Hemos hecho algo más en el código: hemos intentado acceder a la propiedad listaPila desde fuera de la clase inmediatamente 
#después de que se haya creado el objeto; queremos verificar la longitud actual de la pila, ¿lo hemos logrado?
#Sí, por supuesto: el código produce el siguiente resultado:

#0

#Esto no es lo que queremos de la pila. Nosotros queremos que listaPila este escondida del mundo exterior. ¿Es eso posible?
class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.listaPila))
#Sí, y es simple, pero no muy intuitivo.

print("---2---")

#La pila - el enfoque orientado a objetos: continuación
#Echa un vistazo: hemos agregado dos guiones bajos antes del nombre listaPila - nada mas:

class Pila:
    def __init__(self):
        self.__listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))

#El cambio invalida el programa..

#¿Por qué?
#IMPORTANTE:
#Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), 
#se vuelve privado - esto significa que solo se puede acceder desde la clase.

#No puedes verlo desde el mundo exterior. Así es como Python implementa el concepto de encapsulación.

#Ejecuta el programa para probar nuestras suposiciones: una excepción AttributeError debe ser lanzada.

class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))

print("---3---")

#El enfoque orientado a objetos: una pila desde cero
#Ahora es el momento de que las dos funciones (métodos) implementen las operaciones push y pop. 
#Python supone que una función de este tipo debería estar inmersa dentro del cuerpo de la clase - como el constructor.

#Queremos invocar estas funciones para agregar (push) y quitar (pop) valores de la pila. 
#Esto significa que ambos deben ser accesibles para el usuario de la clase (en contraste con la lista previamente construida, 
#que está oculta para los usuarios de la clase ordinaria).

#Tal componente es llamado publico, por ello no puede comenzar su nombre con dos (o más) guiones bajos. 
#Hay un requisito más - el nombre no debe tener más de un guión bajo.

#Las funciones en sí son simples. Echa un vistazo:

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())


#IMPORTANTE:
#Sin embargo, hay algo realmente extraño en el código. Las funciones parecen familiares, 
#pero tienen más parámetros que sus contrapartes procedimentales.

#Aquí, ambas funciones tienen un parámetro llamado self en la primera posición de la lista de parámetros.

#¿Es necesario? Si, lo es.
#TODOOOSSSSS
#Todos los métodos deben tener este parámetro. Desempeña el mismo papel que el primer parámetro constructor.

#Permite que el método acceda a entidades (propiedades y actividades / métodos) del objeto. No puedes omitirlo. 
#Cada vez que Python invoca un método, envía implícitamente el objeto actual como el primer argumento.

#Esto significa que el método está obligado a tener al menos un parámetro, que Python mismo utiliza - no tienes ninguna influencia sobre el.

#Si tu método no necesita ningún parámetro, este debe especificarse de todos modos. Si está diseñado para procesar solo un parámetro, 
#debes especificar dos, ya que la función del primero sigue siendo la misma.

#Hay una cosa más que requiere explicación: la forma en que se invocan los métodos desde la variable __listaPila.

#Afortunadamente, es mucho más simple de lo que parece:

#La primera etapa entrega el objeto como un todo → self.
#A continuación, debes llegar a la lista __listaPila → self.__listaPila.
#Con __listaPila lista para ser usada, puedes realizar el tercer y último paso → self.__listaPila.append(val).
#La declaración de la clase está completa y se han enumerado todos sus componentes. La clase está lista para usarse.

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())



print("---4---")

#El enfoque orientado a objetos: una pila desde cero
#Tener tal clase abre nuevas posibilidades. Por ejemplo, ahora puedes hacer que más de una pila se comporte de la misma manera. 
#Cada pila tendrá su propia copia de datos privados, pero utilizará el mismo conjunto de métodos.

#Esto es exactamente lo que queremos para este ejemplo.

#Analiza el código:

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())

#Existen dos pilas creadas a partir de la misma clase base. Trabajan independientemente. Puedes crear más si quieres.

#Ejecuta el código en el editor y ve qué sucede. Realiza tus propios experimentos.


class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())

print("---5---")

#El enfoque orientado a objetos: una pila desde cero (continuación)
#Analiza el fragmento a continuación: hemos creado tres objetos de la clase Pila. 
#Después, hemos hecho malabarismos. Intenta predecir el valor que se muestra en la pantalla.

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val 

pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())

#Entonces, ¿cuál es el resultado? Ejecuta el programa y comprueba si tenías razón.
#Salida 0.
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val    
    
# ingresa código aquí

pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())

print("---6---")

#El enfoque orientado a objetos: una pila desde cero (continuación)
#Ahora vamos un poco más lejos. Vamos a agregar una nueva clase para manejar pilas.

#La nueva clase debería poder evaluar la suma de todos los elementos almacenados actualmente en la pila.

#No queremos modificar la pila previamente definida. Ya es lo suficientemente buena en sus aplicaciones, 
#y no queremos que cambie de ninguna manera. Queremos una nueva pila con nuevas capacidades. 
#En otras palabras, queremos construir una subclase de la ya existente clase Pila.

#El primer paso es fácil: solo define una nueva subclase que apunte a la clase que se usará como superclase.

#Así es como se ve:

class SumarPila(Pila):
    pass

#La clase aún no define ningún componente nuevo, pero eso no significa que esté vacía. Obtiene (hereda) 
#todos los componentes definidos por su superclase - 
#el nombre de la superclase se escribe después de los dos puntos, después del nombre de la nueva clase.

#Esto es lo que queremos de la nueva pila:

#Queremos que el método push no solo inserte el valor en la pila, sino que también sume el valor a la variable sum.
#Queremos que la función pop no solo extraiga el valor de la pila, sino que también reste el valor de la variable sum.

#En primer lugar, agreguemos una nueva variable a la clase. Sera una variable privada, al igual que la lista de pila. 
#No queremos que nadie manipule el valor de la variable sum.

#Como ya sabes, el constructor agrega una nueva propiedad a la clase. Ya sabes cómo hacerlo, 
#pero hay algo realmente intrigante dentro del constructor. Echa un vistazo:

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

#La segunda línea del cuerpo del constructor crea una propiedad llamada __sum - almacenará el total de todos los valores de la pila.

#Pero la línea anterior se ve diferente. ¿Qué hace? ¿Es realmente necesaria? Sí lo es.

#IMPORTANTE:
#Al contrario de muchos otros lenguajes, Python te obliga a invocar explícitamente el constructor de una superclase. 
#Omitir este punto tendrá efectos nocivos: el objeto se verá privado de la lista __listaPila. Tal pila no funcionará correctamente.

#Esta es la única vez que puedes invocar a cualquiera de los constructores disponibles explícitamente;
#se puede hacer dentro del constructor de la superclase.

#Ten en cuenta la sintaxis:

#Se especifica el nombre de la superclase (esta es la clase cuyo constructor se desea ejecutar).
#Se pone un punto (.) después del nombre.
#Se especifica el nombre del constructor.
#Se debe señalar al objeto (la instancia de la clase) que debe ser inicializado por el constructor; 
#es por eso que se debe especificar el argumento y utilizar la variable self aquí; 
#recuerda: invocar cualquier método (incluidos los constructores) desde fuera de la clase nunca requiere colocar 
#el argumento self en la lista de argumentos - 
#invocar un método desde dentro de la clase exige el uso explícito del argumento self, y tiene que ser el primero en la lista.
#Nota: generalmente es una práctica recomendada invocar al constructor de la superclase antes de cualquier 
#otra inicialización que desees realizar dentro de la subclase. 
#Esta es la regla que hemos seguido en el código.