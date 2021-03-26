#Herencia: el operador is
#También existe un operador de Python que vale la pena mencionar, ya que se refiere directamente a los objetos: aquí está:

#objetoUno is objetoDos


#IMPORTANTE:
#El operador is verifica si dos variables (en este caso objetoUno y objetoDos) se refieren al mismo objeto.

#No olvides que las variables no almacenan los objetos en sí, sino solo los identificadores que apuntan a la memoria interna de Python.

#OJO:
#Asignar un valor de una variable de objeto a otra variable no copia el objeto, sino solo su identificador. 
#Es por ello que un operador como is puede ser muy útil en ciertas circunstancias.

#Echa un vistazo al código en el editor. Analicémoslo:
class ClaseMuestra:
    def __init__(self, val):
        self.val = val

ob1 = ClaseMuestra(0)
ob2 = ClaseMuestra(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2) #False
print(ob2 is ob3) #False
print(ob3 is ob1) #True. No se copia el objeto, sólo su identificador, por tanto, es el mismo objeto (alojado en la memoria) con otra etiqueta
print(ob1.val, ob2.val, ob3.val) #1, porque se suma el objeto 3 que es lo mismo que el obj 1. #2. #1

str1 = "Mary tenía un "
str2 = "Mary tenía un corderito"
str1 += "corderito"
#Ojo acá:
#estos textos se almacenan en diferentes objetos.
print(str1 == str2, str1 is str2) #True y False

#Existe una clase muy simple equipada con un constructor simple, que crea una sola propiedad. La clase se usa para instanciar dos objetos. 
#El primero se asigna a otra variable, y su propiedad val se incrementa en uno.
#Luego, el operador is se aplica tres veces para verificar todos los pares de objetos posibles, 
#y todos los valores de la propiedad val son mostrados en pantalla.
#La última parte del código lleva a cabo otro experimento. Después de tres tareas, 
#ambas cadenas contienen los mismos textos, pero estos textos se almacenan en diferentes objetos.
#El código imprime:

#False
#False
#True
#1 2 1
#True False

#Conclusión:
#Los resultados prueban que ob1 y ob3 son en realidad los mismos objetos, mientras que str1 y str2 no lo son, 
#a pesar de que su contenido sea el mismo.


print("---2---")

#Cómo Python encuentra propiedades y métodos
#Ahora veremos cómo Python trata con los métodos de herencia.

#Echa un vistazo al ejemplo en el editor. Vamos a analizarlo:
class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self): #permite que la clase pueda presentar su identidad en forma de texto.
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre) #Así se heredan los atributos y métodos de una súper clase


obj = Sub("Andy")

print(obj)

#Salida:
#Mi nombre es Andy.

#Existe una clase llamada Super, que define su propio constructor utilizado para asignar la propiedad del objeto, llamada nombre.
#La clase también define el método __str__(), lo que permite que la clase pueda presentar su identidad en forma de texto 
# y no de espacio de memoria
#La clase se usa luego como base para crear una subclase llamadaSub. La clase Sub define su propio constructor, que invoca el de la superclase. 
#Toma nota de cómo lo hemos hecho: Super.__init__(self, nombre).
#Hemos nombrado explícitamente la superclase y hemos apuntado al método para invocar a __init__(), 
#proporcionando todos los argumentos necesarios.
#Hemos instanciado un objeto de la clase Sub y lo hemos impreso.
#El código da como salida:

#Mi nombre es Andy.

#IMPORTANTE:
#Nota: Como no existe el método __str__() dentro de la clase Sub, la cadena a imprimir se producirá dentro de la clase Super.
#Esto significa que el método __str__() ha sido heredado por la clase Sub.

print("---3---")

#Cómo Python encuentra propiedades y métodos: continuación
#Mira el código en el editor. Lo hemos modificado para mostrarte otro método de acceso a cualquier entidad definida dentro de la superclase.
class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        super().__init__(nombre)


obj = Sub("Andy")

print(obj)

#En el ejemplo anterior, nombramos explícitamente la superclase. En este ejemplo, hacemos uso de la función super(),
#la cual accede a la superclase sin necesidad de conocer su nombre:

#super().__init__(nombre)

#La función super() crea un contexto en el que no tiene que (además, no debe) pasar el argumento propio al método que se invoca;
#es por eso que es posible activar el constructor de la superclase utilizando solo un argumento.

#Nota: puedes usar este mecanismo no solo para invocar al constructor de la superclase, 
#pero también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.

print("---4---")

#Cómo Python encuentra propiedades y métodos: continuación
#Intentemos hacer algo similar, pero con propiedades (más precisamente con: variables de clase).

#Observa el ejemplo en el editor.
# Probando propiedades: variables de clase
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)
print(obj.supVar) #Se puede obtener las variables de clase sin constructor 

#Como puedes observar, la clase Super define una variable de clase llamada supVar, y la clase Sub define una variable llamada subVar.

#Ambas variables son visibles dentro del objeto de clase Sub - es por ello que el código da como salida:

#2
#1


print("---5---")

#Cómo Python encuentra propiedades y métodos: continuación
#El mismo efecto se puede observar con variables de instancia - observa el segundo ejemplo en el editor.
# Probando propiedades: variables de instancia
class Super:
    def __init__(self):
        self.supVar = 11 #Variable de instancia

class Sub(Super):
    def __init__(self):
        super().__init__() #Si quito esto, generaría error al llamar al atributo .supVar
        self.subVar = 12 #Variable de instancia

obj = Sub()

print(obj.subVar)
print(obj.supVar)

#El constructor de la clase Sub crea una variable de instancia llamada subVar, 
#mientras que el constructor de Super hace lo mismo con una variable de nombre supVar. 
#Al igual que el ejemplo anterior, ambas variables son accesibles desde el objeto de clase Sub.

#La salida del programa es:

#12
#11

#Nota: La existencia de la variable supVar obviamente está condicionada por la invocación del constructor de la clase Super. 
#Omitirlo daría como resultado la ausencia de la variable en el objeto creado (pruébalo tu mismo).

print("---6---")


#Cómo Python encuentra propiedades y métodos: continuación
#Ahora es posible formular una declaración general que describa el comportamiento de Python.

#Cuando intentes acceder a una entidad de cualquier objeto, Python intentará (en este orden): IMPORTANTE

#Encontrarla dentro del objeto mismo.
#Encontrarla en todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
#Si ambos intentos fallan, una excepción (AttributeError) será lanzada.


#La primera condición puede necesitar atención adicional. Como sabes, todos los objetos derivados 
#de una clase en particular pueden tener diferentes conjuntos de atributos, y algunos de los atributos 
#pueden agregarse al objeto mucho tiempo después de la creación del objeto.

#El ejemplo en el editor resume esto en una línea de herencia de tres niveles. Analízalo cuidadosamente.
class Nivel1:
    varia1 = 100
    def __init__(self):
        self.var1 = 101

    def fun1(self):
        return 102


class Nivel2(Nivel1):
    varia2 = 200
    def __init__(self):
        super().__init__()
        self.var2 = 201
    
    def fun2(self):
        return 202


class Nivel3(Nivel2):
    varia3 = 300
    def __init__(self):
        super().__init__()
        self.var3 = 301

    def fun3(self):
        return 302


obj = Nivel3()

print(obj.varia1, obj.var1, obj.fun1())
print(obj.varia2, obj.var2, obj.fun2())
print(obj.varia3, obj.var3, obj.fun3())

#Todos los comentarios que hemos hecho hasta ahora están relacionados con casos de herencia única, cuando una subclase 
#tiene exactamente una superclase. Esta es la situación más común (y también la recomendada).

#Python, sin embargo, ofrece mucho más aquí. En las próximas lecciones te mostraremos algunos ejemplos de herencia múltiple.




