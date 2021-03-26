#Herencia: ¿por qué y cómo?
#Antes de comenzar a hablar sobre la herencia, queremos presentar un nuevo y práctico mecanismo utilizado por las clases y los objetos
# de Python: es la forma en que el objeto puede presentarse a si mismo.

#Comencemos con un ejemplo. Observa el código en el editor.
class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre #self.cualquier nombre = parámetro
        self.galaxia = galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)

#El programa imprime solo una línea de texto, que en nuestro caso es:

#<__main__.Estrella object at 0x7f377e552160>

#Si ejecutas el mismo código en tu computadora, verás algo muy similar, aunque el número hexadecimal (la subcadena que comienza con 0x) 
#será diferente, ya que es solo un identificador de objeto interno utilizado por Python, 
#y es poco probable que aparezca igual cuando se ejecuta el mismo código en un entorno diferente.

#Como puedes ver, la impresión aquí no es realmente útil, y algo más específico, es preferible.

#Afortunadamente, Python ofrece tal función.

print("---2---")

#Herencia: ¿por qué y cómo?
#Cuando Python necesita que alguna clase u objeto deba ser presentado como una cadena 
#(es recomendable colocar el objeto como argumento en la invocación de la función print()), 
#intenta invocar un método llamado __str__() del objeto y emplear la cadena que devuelve.

#El método por default __str__() devuelve la cadena anterior: fea y poco informativa. Puedes cambiarlo definiendo tu propio método del nombre.

#Lo acabamos de hacer: observa el código en el editor.

class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)

#Salida:
#Sol en la Vía Láctea

#Forma sin el método __str__ dentro de la clase:
class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    #def __str__(self):
    #    return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)

#Salida:
#<__main__.Estrella object at 0x000001FE3325D190> :$ GUACALAAAA

#El método nuevo __str__() genera una cadena que consiste en los nombres de la estrella y la galaxia, 
#nada especial, pero los resultados de impresión se ven mejor ahora, ¿no?

#¿Puedes adivinar la salida? Ejecuta el código para verificar si tenías razón.

print("---3---")

#Herencia: ¿por qué y cómo?
#El término herencia es más antiguo que la programación de computadoras, y describe la práctica común de pasar diferentes bienes 
#de una persona a otra después de la muerte de esa persona. El término, cuando se relaciona con la programación de computadoras, 
#tiene un significado completamente diferente.

#Definamos el término para nuestros propósitos:

#La herencia es una práctica común (en la programación de objetos) de pasar atributos y métodos de la superclase (definida y existente) 
#a una clase recién creada, llamada subclase.

#En otras palabras, la herencia es una forma de construir una nueva clase, no desde cero, sino utilizando un repertorio de rasgos ya definido. 
#La nueva clase hereda (y esta es la clave) todo el equipamiento ya existente, pero puedes agregar algo nuevo si es necesario.

#Gracias a eso, es posible construir clases más especializadas (más concretas) utilizando algunos conjuntos de reglas y 
#comportamientos generales predefinidos.


#El factor más importante del proceso es la relación entre la superclase y todas sus subclases (nota: si B es una subclase de A y C es 
#una subclase de B, esto también significa que C es una subclase de A, ya que la relación es totalmente transitiva).
#TRANSITIVIDAD
#Aquí se presenta un ejemplo muy simple de herencia de dos niveles:

class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass

#Todas las clases presentadas están vacías por ahora, ya que te mostraremos cómo funcionan las relaciones mutuas entre las superclases 
#y las subclases. Las llenaremos con contenido pronto.

#Podemos decir que:

#La clase Vehiculo es la superclase para clases VehiculoTerrestre y VehiculoOruga.
#La clase VehiculoTerrestre es una subclase de Vehiculo y la superclase de VehiculoOruga al mismo tiempo.
#La clase VehiculoOruga es una subclase tanto de Vehiculo y VehiculoTerrestre.
#El conocimiento anterior proviene de la lectura del código (en otras palabras, lo sabemos porque podemos verlo).

#¿Python sabe lo mismo? ¿Es posible preguntarle a Python al respecto? Sí lo es.


print("---4---")
#Herencia: issubclass()

#Python ofrece una función que es capaz de identificar una relación entre dos clases, y aunque su diagnóstico no es complejo, 
#puede verificar si una clase particular es una subclase de cualquier otra clase.

#Así es como se ve:

#issubclass(ClaseUno, ClaseDos) True si ClaseUno es subclase de ClaseDos

#La función devuelve True si ClaseUno es una subclase de ClaseDos, y False de lo contrario.

#Vamos a verlo en acción, puede sorprenderte. Mira el código en el editor. Léelo cuidadosamente.
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]: #Si son la misma clase, se toma True.
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]: #Mete cada clase en listas para así recorrerlas
        print(issubclass(cls1, cls2), end="\t") #end="\t" organiza como tablas
    print()

#Hay dos bucles anidados. Su propósito es verificar todos los pares de clases ordenadas posibles y que imprima los resultados de la 
#verificación para determinar si el par coincide con la relación subclase-superclase.

#Ejecuta el código. El programa produce el siguiente resultado:

#True	False	False	
#True	True	False	
#True	True	True	

#Hagamos que el resultado sea más legible:

#↓ es una subclase de →	Vehiculo	VehiculoTerrestre	VehiculoOruga
#Vehiculo	              True	       False	           False
#VehiculoTerrestre	      True	       True	               False
#VehiculoOruga	          True	       True	               True

#IMPORTANTE:
#Existe una observación importante que hacer: cada clase se considera una subclase de sí misma.


print("---5---")

#Herencia: isinstance()
#Como ya sabes, un objeto es la encarnación de una clase. Esto significa que el objeto es como un pastel horneado usando 
#una receta que se incluye dentro de la clase.

#Esto puede generar algunos problemas.

#Supongamos que tienes un pastel (por ejemplo, resultado de un argumento pasado a tu función). 
#Deseas saber qué receta se ha utilizado para prepararlo. ¿Por qué? Porque deseas saber qué esperar de él, 
#por ejemplo, si contiene nueces o no, lo cual es información crucial para ciertas personas.

#Del mismo modo, puede ser crucial si el objeto tiene (o no tiene) ciertas características. En otras palabras, 
#si es un objeto de cierta clase o no.

#Tal hecho podría ser detectado por la función llamada isinstance():

#isinstance(nombreObjeto, nombreClase) si el objeto es una instancia de la clase, develve True

#La función devuelve True si el objeto es una instancia de la clase, o False de lo contrario.

#Ser una instancia de una clase significa que el objeto (el pastel) se ha preparado utilizando una receta 
#contenida en la clase o en una de sus superclases.

#IMPORTANTE:
#No lo olvides: si una subclase contiene al menos las mismas caracteristicas que cualquiera de sus superclases, 
#significa que los objetos de la subclase pueden hacer lo mismo que los objetos derivados de la superclase, 
#por lo tanto, es una instancia de su clase de inicio y cualquiera de sus superclases.

#Probémoslo. Analiza el código en el editor.

#Hemos creado tres objetos, uno para cada una de las clases. Luego, usando dos bucles anidados, 
#verificamos todos los pares posibles de clase de objeto para averiguar si los objetos son instancias de las clases.

#Ejecuta el código.
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()

#Esto es lo que obtenemos:

#True	False	False	
#True	True	False	
#True	True	True	

#Hagamos que el resultado sea más legible:

#↓ es una instancia de →	Vehiculo	miVehiculoTerrestre	VehiculoOruga
#miVehiculo	              True	          False	           False
#miVehiculoTerrestre	  True	          True	           False
#VehiculoOruga	          True	          True	           True

#¿La tabla confirma nuestras expectativas?







