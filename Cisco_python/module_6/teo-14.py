#Anatomía detallada de las excepciones
#Echemos un vistazo más de cerca al objeto de la excepción, ya que hay algunos elementos realmente interesantes aquí 
#(volveremos al tema pronto cuando consideremos las técnicas base de entrada y salida de Python, ya que su subsistema de excepción extiende 
#un poco estos objetos).

#La clase BaseException introduce una propiedad llamada args. Es una tupla diseñada para reunir todos los 
#argumentos pasados al constructor de la clase. Está vacío si la construcción se ha invocado sin ningún argumento, 
#o solo contiene un elemento cuando el constructor recibe un argumento (no se considera el argumento self aquí), y así sucesivamente.

#Hemos preparado una función simple para imprimir la propiedad args de una manera elegante, puedes ver la función en el editor.
def printargs(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))

try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=' : ' ,end=' : ')
	printargs(e.args)

try:
	raise Exception("mi excepción") #Levanta el tipo de excepción que deseas, con tus propias condiciones
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

try:
	raise Exception("mi", "excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

#Hemos utilizado la función para imprimir el contenido de la propiedad args en tres casos diferentes, 
#donde la excepción de la clase Exception es lanzada de tres maneras distintas. Para hacerlo más espectacular, 
#también hemos impreso el objeto en sí, junto con el resultado de la invocación __str__().

#El primer caso parece de rutina, solo hay el nombre Exception despues de la palabra clave reservada raise. 
#Esto significa que el objeto de esta clase se ha creado de la manera más rutinaria.

#El segundo y el tercer caso pueden parecer un poco extraños a primera vista, pero no hay nada extraño, 
#son solo las invocaciones del constructor. En la segunda sentencia raise, el constructor se invoca con un argumento, 
#y en el tercero, con dos.

#Como puedes ver, la salida del programa refleja esto, mostrando los contenidos apropiados de la propiedad args:

# :  :
#mi excepción : mi excepción : mi excepción
#('mi', 'excepción') : ('mi', 'excepción') : ('mi', 'excepción')


print("---2---")

#Cómo crear tu propia excepción
#La jerarquía de excepciones no está cerrada ni terminada, y siempre puedes ampliarla si deseas o necesitas crear 
#tu propio mundo poblado con tus propias excepciones.

#Puede ser útil cuando se crea un módulo complejo que detecta errores y genera excepciones, y deseas que las excepciones 
#se distingan fácilmente de cualquier otra de Python.

#Esto se puede hacer al definir tus propias excepciones como subclases derivadas de las predefinidas.

#Nota: si deseas crear una excepción que se utilizará como un caso especializado de cualquier excepción incorporada, 
#derivala solo de esta. Si deseas construir tu propia jerarquía, y no quieres que esté estrechamente conectada 
#al árbol de excepciones de Python, derivala de cualquiera de las clases de excepción principales, tal como: Exception.

#Imagina que has creado una aritmética completamente nueva, regida por sus propias leyes y teoremas. 
#Está claro que la división también se ha redefinido, y tiene que comportarse de una manera diferente a la división de rutina. 
#También está claro que esta nueva división debería plantear su propia excepción, diferente de la incorporada ZeroDivisionError,
# pero es razonable suponer que, en algunas circunstancias, tu (o el usuario de tu aritmética) pueden tratar todas 
# las divisiones entre cero de la misma manera.

#Demandas como estas pueden cumplirse en la forma presentada en el editor. Mira el código y analicémoslo:
class MyZeroDivisionError(ZeroDivisionError):	
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("peores noticias")
	else:		
		raise ZeroDivisionError("malas noticias")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('División entre cero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('Mi división entre cero')
	except ZeroDivisionError:
		print('División entre cero original')

#Hemos definido nuestra propia excepción, llamada MyZeroDivisionError, derivada de la incorporada ZeroDivisionError.
# Como puedes ver, hemos decidido no agregar ningún componente nuevo a la clase.

#En efecto, una excepción de esta clase puede ser, dependiendo del punto de vista deseado, tratada como una simple excepción ZeroDivisionError, 
#o puede ser considerada por separado.

#La función doTheDivision() lanza una excepción MyZeroDivisionError o ZeroDivisionError, dependiendo del valor del argumento.

#La función se invoca cuatro veces en total, mientras que las dos primeras invocaciones se manejan utilizando solo una rama except 
#(la más general), las dos últimas invocan dos ramas diferentes, capaces de distinguir las excepciones 
#(no lo olvides: el orden de las ramas hace una diferencia fundamental).

print("---3---")
#Cómo crear tu propia excepción: continuación
#Cuando vas a construir un universo completamente nuevo lleno de criaturas completamente nuevas que no 
#tienen nada en común con todas las cosas familiares, es posible que desees construir tu propia estructura de excepciones.

#Por ejemplo, si trabajas en un gran sistema de simulación destinado a modelar las actividades de un restaurante de pizza,
#puede ser conveniente formar una jerarquía de excepciones por separado.

#Puedes comenzar a construirla definiendo una excepción general como una nueva clase base para cualquier otra excepción especializada. 
#Lo hemos hecho de la siguiente manera:

class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(mensaje)
        self.pizza = pizza

#Nota: vamos a recopilar más información específica aquí de lo que recopila una Excepción regular, 
#entonces nuestro constructor tomará dos argumentos:

#Uno que especifica una pizza como tema del proceso.
#Otro que contiene una descripción más o menos precisa del problema.
#Como puedes ver, pasamos el segundo parámetro al constructor de la superclase y guardamos el primero dentro de nuestra propiedad.

#Un problema más específico (como un exceso de queso) puede requerir una excepción más específica. 
#Es posible derivar la nueva clase de la ya definida PizzaError, como hemos hecho aquí:

class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError._init__(self, pizza, mensaje)
        self.queso = queso

#La excepción DemasiadoQuesoError necesita más información que la excepción regular PizzaError, así que lo agregamos al constructor, 
#el nombre queso es entonces almacenado para su posterior procesamiento.

#Ejemplo:
class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(mensaje)
        self.pizza = pizza	


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError._init__(self, pizza, mensaje)
        self.queso = queso

print("---4---")

#Cómo crear tu propia excepción: continuación
#Mira el código en el editor. Combinamos las dos excepciones previamente definidas y las aprovechamos para que funcionen en un pequeño ejemplo.
class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def makePizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no hay tal pizza en el menú")
	if queso > 100:
		raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
	print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)

#Salida:
#¡Pizza lista!
#demasiado queso : 110
#no hay tal pizza en el menú : mafia

#Una de ellas es lanzada dentro de la función hacerPizza() cuando ocurra cualquiera de estas dos situaciones erróneas: 
#una solicitud de pizza incorrecta o una solicitud de una pizza con demasiado queso.

#Nota:

#El remover la rama que comienza con except DemasiadoQuesoError hará que todas las excepciones que aparecen se clasifiquen como PizzaError.
#El remover la rama que comienza con except PizzaError provocará que la excepción DemasiadoQuesoError no pueda ser manejada, 
#y hará que el programa finalice.

#La solución anterior, aunque elegante y eficiente, tiene una debilidad importante. 
#Debido a la manera algo fácil de declarar los constructores, las nuevas excepciones no se pueden usar tal cual,
# sin una lista completa de los argumentos requeridos.

#Eliminaremos esta debilidad estableciendo valores predeterminados para todos los parámetros del constructor. Observa:

class PizzaError(Exception):
    def __init__(self, pizza='desconocida', mensaje=''):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza='desconocida', queso='>100', mensaje=''):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def hacerPizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError
	if queso > 100:
		raise DemasiadoQuesoError
	print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		hacerPizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)

#Ahora, si las circunstancias lo permiten, es posible usar unicamente los nombres de clase.




