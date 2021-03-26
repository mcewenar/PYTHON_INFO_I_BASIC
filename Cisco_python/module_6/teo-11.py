#Cómo Python encuentra propiedades y métodos: continuación (HERENCIA MÚLTIPLE)
#La herencia múltiple ocurre cuando una clase tiene más de una superclase.

#Sintácticamente, dicha herencia se presenta como una lista de superclases separadas por comas entre 
#paréntesis después del nombre de la nueva clase, al igual que aquí:

class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def __init__(self):
        self.nombre=45
    def funB(self):
        return 21

class Sub(SuperA, SuperB):#Puede heredar variables de clase y  métodos de ambas clases por herencia múltiple, pero no sus atributos (sin el pass)
    pass # si se crea un constructor, sin usar este pass, generaría error invocar un atributo de una súper clase
    #def __init__(self):
    #    SuperB.__init__(self)

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())
print(obj.nombre) #ESTE GENERA ERROR

#La clase Sub tiene dos superclases: SuperA y SuperB. Esto significa que la clase 
#Sub hereda todos los bienes ofrecidos por ambas clases SuperA y SuperB.

#El código imprime:

#10 11
#20 21

#Ahora es el momento de introducir un nuevo término - overriding (anulación).

class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())

#¿Qué crees que sucederá si más de una de las superclases define una entidad con un nombre en particular?

print("----2----")
#Cómo Python encuentra propiedades y métodos: continuación
#Analicemos el ejemplo en el editor.
class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2:
    var = 200
    def fun(self):
        return 201

class Nivel3(Nivel2):
    pass

obj = Nivel3()

print(obj.var, obj.fun())
#IMPORTANTE:
#Tanto la clase Nivel1 como la Nivel2 definen un método llamado fun() y una propiedad llamada var. 
#¿Significará esto el objeto de la clase Nivel3 podrá acceder a dos copias de cada entidad? De ningún modo.

#La entidad definida después (en el sentido de herencia) anula la misma entidad definida anteriormente. 
#Es por eso que el código produce el siguiente resultado:

#200 201

#PENDIENTE:
#Como puedes ver, la variable de clase var y el método fun() de la clase Nivel2 anula las entidades de los mismos nombres derivados 
#de la clase Nivel1.

#Esta característica se puede usar intencionalmente para modificar el comportamiento predeterminado de las clases 
#(o definido previamente) cuando cualquiera de tus clases necesite actuar de manera diferente a su ancestro.

#Otra forma de verse:
#También podemos decir que Python busca una entidad (clase) de abajo hacia arriba, y está completamente satisfecho con la primera entidad 
#del nombre deseado que encuentre.

#¿Qué ocurre cuando una clase tiene dos ancestros que ofrecen la misma entidad y se encuentran en el mismo nivel? En otras palabras, 
#¿Qué se debe esperar cuando surge una clase usando herencia múltiple? Miremos lo siguiente.


print("---3---")

#Cómo Python encuentra propiedades y métodos: continuación
#Echemos un vistazo al ejemplo en el editor.
class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"


class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"

class Sub(Izquierda, Derecha):
#class Sub(Derecha, Izquierda):
    pass


obj = Sub()

print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())

#Salida:
#I II DD Izquierda

#La clase Sub hereda todos los bienes de dos superclases, Izquierda y Derecha (estos nombres están destinados a ser significativos).

#No hay duda de que la variable de clase varDerecha proviene de la clase Derecha, y la variable varIzquierda proviene 
#de la clase Izquierda respectivamente.

#Esto es claro. Pero, ¿De donde proviene la variable var? ¿Es posible adivinarlo? 
#El mismo problema se encuentra con el método fun() - ¿Será invocado desde Izquierda o desde Derecha? Ejecutemos el programa: la salida será:

#I II DD Izquierda

#Esto prueba que ambos casos poco claros tienen una solución dentro de la clase Izquierda. 
#¿Es esta una premisa suficiente para formular una regla general? Sí lo es.

#Podemos decir que Python busca componentes de objetos en el siguiente orden:

#OJOOO:
#Dentro del objeto mismo.
#En sus superclases, de abajo hacia arriba.
#Si hay más de una clase en una ruta de herencia, Python las escanea de izquierda a derecha.
#¿Necesitas algo más? Simplemente haz una pequeña enmienda en el código - reemplaza:class Sub(Izquierda, Derecha): 
#con: class Sub(Derecha, Izquierda):, luego ejecuta el programa nuevamente y observa qué sucede.

#¿Qué ves ahora? Vemos:

#D II DD Derecha

#¿Ves lo mismo o algo diferente?

print("---4---")

#Cómo construir una jerarquía de clases
#Construir una jerarquía de clases no es solo por amor al arte.

#Si divides un problema entre las clases y decides cuál de ellas debe ubicarse en la parte superior 
#y cuál debe ubicarse en la parte inferior de la jerarquía, debes analizar cuidadosamente el problema, pero antes de mostrarte 
#cómo hacerlo (y cómo no hacerlo), queremos resaltar un efecto interesante. No es nada extraordinario 
#(es solo una consecuencia de las reglas generales presentadas anteriormente), 
#pero recordarlo puede ser clave para comprender cómo funcionan algunos códigos 
#y cómo se puede usar este efecto para construir un conjunto flexible de clases.

#Echa un vistazo al código en el editor. Analicémoslo:
class Uno:
    def hazlo(self):
        print("hazlo de Uno")

    def haz_algo(self):
        self.hazlo()

class Dos(Uno):
    def hazlo(self):
        print("hazlo de Dos")

uno = Uno()
dos = Dos()

uno.haz_algo()
dos.haz_algo()

#Salida:
#hazlo de Uno
#hazlo de Dos

#Existen dos clases llamadas Uno y Dos, se entiende que Dos es derivada de Uno. Nada especial. 
#Sin embargo, algo es notable: el método doit() (hazlo()).
#El método doit() está definido dos veces: originalmente dentro de Uno y posteriormente dentro de Dos. 
#La esencia del ejemplo radica en el hecho de que es invocado solo una vez - dentro de Uno.
#La pregunta es: ¿cuál de los dos métodos será invocado por las dos últimas líneas del código?


#La primera invocación parece ser simple, el invocar el método haz_algo() del objeto uno obviamente activará el primero de los métodos.

#La segunda invocación necesita algo de atención. También es simple si tienes en cuenta cómo Python encuentra los componentes de la clase. 
#La segunda invocación lanzará el método hazlo() en la forma existente dentro de la clase Dos, 
#independientemente del hecho de que la invocación se lleva a cabo dentro de la clase Uno.

#En efecto, el código genera el siguiente resultado:

#hazlo de Uno
#hazlo de Dos

#IMPORTANTÍSIMO:
#Nota: la situación en la cual la subclase puede modificar el comportamiento de su superclase (como en el ejemplo) se llama polimorfismo.
#La palabra proviene del griego (polys: "muchos, mucho" y morphe, "forma, forma"), 
#lo que significa que una misma clase puede tomar varias formas dependiendo de las redefiniciones realizadas por cualquiera de sus subclases.

#El método, redefinido en cualquiera de las superclases, que cambia el comportamiento de la superclase, se llama virtual.

#En otras palabras, ninguna clase se da por hecho. El comportamiento de cada clase puede ser modificado en cualquier momento por cualquiera 
#de sus subclases.

#Te mostraremos cómo usar el polimorfismo para extender la flexibilidad de la clase.

print("---5---")

#Cómo construir una jerarquía de clases: continuación
#Mira el ejemplo en el editor.
import time

class VehiculoOruga:
    def control_de_pista(izquierda, alto):
        pass

    def girar(izquierda):
        control_de_pista(izquierda, True)
        time.sleep(0.25)
        control_de_pista(izquierda, False)


class VehiculoTerrestre:
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def girar(izquierda):
        girar_ruedas_delanteras(izquierda, True)
        time.sleep(0.25)
        girar_ruedas_delanteras(izquierda, False)

#¿Se parece a algo? Sí, por supuesto que lo hace. Se refiere al ejemplo que se muestra al comienzo 
#del módulo cuando hablamos de los conceptos generales 
#de la programación orientada a objetos.

#Puede parecer extraño, pero no utilizamos herencia en este ejemplo, solo queríamos mostrarte que no nos limita.

#Definimos dos clases separadas capaces de producir dos tipos diferentes de vehículos terrestres. 
#La principal diferencia entre ellos está en cómo giran. Un vehículo con ruedas solo gira las ruedas delanteras (generalmente). 
#Un vehículo oruga tiene que detener una de las pistas.

#¿Puedes seguir el código?

#Un vehículo oruga realiza un giro deteniéndose y moviéndose en una de sus pistas (esto lo hace el método control_de_pista(),
#el cual se implementará más tarde).
#Un vehículo con ruedas gira cuando sus ruedas delanteras giran (esto lo hace el método girar_ruedas_delanteras()).
#El método girar() utiliza el método adecuado para cada vehículo en particular.
#¿Puedes detectar el error del código?

#Los métodos girar()son muy similares como para dejarlos en esta forma.

#Vamos a reconstruir el código: vamos a presentar una superclase para reunir todos los aspectos similares de los vehículos, 
#trasladando todos los detalles a las subclases.

print("---6---")
#Cómo construir una jerarquía de clases: continuación
#Mira el código en el editor nuevamente. Esto es lo que hemos hecho:
import time

class Vehiculo:
    def cambiardireccion(izquierda, on):
        pass

    def girar(izquierda):
        cambiardireccion(izquierda, True)
        time.sleep(0.25)
        cambiardireccion(izquierda, False)

class VehiculoOruga(Vehiculo):
    def control_de_pista(izquierda, alto):
        pass

    def cambiardireccion(izquierda, on):
        control_de_pista(izquierda, on)

class VehiculoTerrestre(Vehiculo):
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def cambiardireccion(izquierda, on):
        girar_ruedas_delanteras(izquierda, on)

#Definimos una superclase llamada Vehiculo, la cual utiliza el método girar() para implementar un esquema para poder girar, 
#mientras que el giro en si es realizado por cambiardireccion(); nota: dicho método está vacío, ya que vamos a poner todos los detalles 
#en la subclase (dicho método a menudo se denomina método abstracto, ya que solo demuestra alguna posibilidad que será instanciada más tarde).
#Definimos una subclase llamada VehiculoOruga (nota: es derivada de la clase Vehiculo) la cual instancia el método cambiardireccion() 
#utilizando el método denominado control_de_pista().
#Respectivamente, la subclase llamada VehiculoTerrestre hace lo mismo, pero usa el método girar_ruedas_delanteras() para obligar al vehículo 
#a girar.
#La ventaja más importante (omitiendo los problemas de legibilidad) es que esta forma de código 
#te permite implementar un nuevo algoritmo de giro simplemente modificando el método girar(), 
#lo cual se puede hacer en un solo lugar, ya que todos los vehículos lo obedecerán.

#Así es como el el polimorfismo ayuda al desarrollador a mantener el código limpio y consistente.






