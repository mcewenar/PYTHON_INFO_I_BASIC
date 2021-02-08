#Paso de parámetros posicionales (IMPORTANTE)

#La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, 
#los argumentos pasados de esta manera son llamados argumentos posicionales.

#Ya se ha utilizado, pero Python ofrece mucho más. Se abordará este tema a continuación.

def miFuncion(a, b, c):
    print(a, b, c)

miFuncion(1, 2, 3)

#Nota: el paso de parámetros posicionales es usado de manera intuitiva por las personas en muchas situaciones. 
#Por ejemplo, es generalmente aceptado que cuando nos presentamos mencionamos primero nuestro nombre(s) y después nuestro apellido, 
#por ejemplo, "Me llamo Juan Pérez."

#Sin embargo, En Hungría se hace al revés.

#Implementemos esa costumbre en Python. La siguiente función es utilizada para presentar a alguien:

def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")

#¿Puedes predecir la salida? Ejecuta el código y verifícalo por ti mismo.


#Ahora imaginemos que la función esta siendo utilizada en Hungría. En este caso, el código sería de la siguiente manera:

def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Skywalker" ,"Luke" )
presentar("Quick", "Jesse")
presentar("Kent", "Clark")
#La salida será diferente. ¿La puedes predecir?
print("-----2-----")

#Mirar la variación; se cambia la posición de los parámetros
def presentar(segundoNombre,primerNombre): #PARÁMETROS
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Skywalker" ,"Luke" ) #ARGUMENTOS
presentar("Quick", "Jesse")
presentar("Kent", "Clark")



#Paso de argumentos con palabras clave (IMPORTANTE):

#Python ofrece otra manera de pasar argumentos, donde el significado del argumento esta definido por su nombre, no su posición, 
#a esto se le denomina paso de argumentos con palabras clave.
print("---------3----------")
#Observa el siguiente código:

def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar(primerNombre = "James", segundoNombre = "Bond")
presentar(segundoNombre = "Skywalker", primerNombre = "Luke") #Reconoce el nombre del argumento que se pasa al parámetro, mas no la posición



#El concepto es claro: los valores pasados a los parámetros son precedidos por el nombre del parámetro al que se le va a pasar el valor, 
#seguido por el signo de =.

#La posición no es relevante aquí, cada argumento conoce su destino con base en el nombre utilizado.

#Debes de poder predecir la salida. Ejecuta el código y verifica tu respuesta.

#Por supuesto que no se debe de utilizar el nombre de un parámetro que no existe.

#El siguiente código provocará un error de ejecución:
print("-------4--------")

def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es ", primerNombre, segundoNombre)

#presentar(apellido="Skywalker", primerNombre="Luke")  ERRORRRRR

#Esto es lo que Python arrojará:
#TypeError: presentar() got an unexpected keyword argument 'apellido'





#El combinar argumentos posicionales y de palabras clave (IMPORTANTE)


#Es posible combinar ambos tipos si se desea, solo hay una regla inquebrantable: SE DEBEN COLOCAR PRIMERO LOS ARGUMENTOS POSICIONALES Y 
#DESPUÉS LOS DE PALABRA CLAVE

#Piénsalo por un momento y entenderás el porque.

#Para mostrarte como funciona, se utilizara la siguiente función de tres parámetros:
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

#Su propósito es el de evaluar y presentar la suma de todos sus argumentos.
#La función, al ser invocada de la siguiente manera:
suma(1, 2, 3)

#Hasta ahorita es un ejemplo puro de un argumento posicional.
#También, se puede reemplazar la invocación actual por una con palabras clave, como la siguiente:
suma(c = 1, a = 2, b = 3)

#Ten presente el orden de los valores.
#Ahora intentemos mezclar ambas.
#Observa la siguiente invocación de la función:
#FORMA CON ARGUMENTOS POSICIONALES Y CON PALABRAS CLAVES (MIXTO)
suma(3, c = 1, b = 2)

#Vamos a analizarla:

#El argumento (3) para el parametro a es pasado utilizando la manera posicional.
#Los argumentos para c y b son especificados con palabras clave.

#Esto es lo que se verá en la consola:
#3 + 2 + 1 = 6

#Se cuidadoso, ten cuidado de no cometer errores. Si se intenta pasar mas de un valor a un argumento, 
#ocurrirá un error y se mostrará lo siguiente:

#Observa la siguiente invocación, se le esta asignando dos veces un valor al parámetro a:

#suma(3, a = 1, b = 2) el valor 3 entra en el parámetro a de la función, entonces es redundante. ERRORRRRRRRR
#La respuesta de Python es:
#TypeError: suma() got multiple values for argument 'a'


#Observa el siguiente código. Es un código completamente correcto y funcional, pero no tiene mucho sentido:
suma(4, 3, c = 2)
#Todo es correcto, pero el dejar solo un argumento con palabras clave es algo extraño - ¿Qué es lo que opinas?



#Funciones con parámetros: mas detalles (IMPORTANTE):
#En ocasiones ocurre que algunos valores de ciertos argumentos son mas utilizados que otros. 
#Dichos argumentos tienen valores predefinidos los cuales pueden ser considerados cuando los argumentos correspondientes han sido omitidos.

#Uno de los apellidos más comunes en Latinoamérica es González. Tomémoslo para el ejemplo.


#El valor por default para el parámetro se asigna de la siguiente manera:
print("---------5----------")
def presentar(primerNombre, segundoNombre="González"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

# mandar llamar la función aquí (invocarla)
#Solo se tiene que colocar el nombre del parámetro seguido del signo de = y el valor por default.

#Invoquemos la función de manera normal:
presentar("Jorge", "Pérez")
#¿Puedes predecir la salida del programa? Ejecútalo y revisa si era lo esperado.


#OJO AQUÍ
#¿Y? No parece haber cambiado algo, pero cuando se invoca la función de una manera inusual, como esta:

presentar("Enrique")

#o así:
presentar (primerNombre="Guillermo")
#no habrá errores, ambas invocaciones funcionarán, la consola mostrará los siguientes resultados:
#Output:
#Hola, mi nombre es Enrique González
#Hola, mi nombre es Guillermo González 


#Puedes hacerlo con mas parámetros, si te resulta útil. Ambos parámetros tendrán sus valores por default, observa el siguiente código:

def presentar(primerNombre="Juan", segundoNombre="González"):
    print("Hola, mi nombre es ", primerNombre, segundoNombre)


#Esto hace que la siguiente invocación sea completamente valida:
presentar() #Se hace válido por los parámetros por default

#Y esta es la salida esperada:
# Hola, mi nombre es Juan González


#Si solo se especifica un argumento de palabra clave, el restante tomará el valor por default:

presentar(segundoNombre="Rodríguez")
presentar("Rodríguez") #SE TOMA POR ARGUMENTO POSICIONAL Y, CONFUSAMENTE, SE TOMA COMO UN NOMBRE, CUANDO, CLARAMENTE, ES UN APELLIDO

#La salida es:
#Hola, mi nombre es Juan Rodríguez 

#Pruébalo.


#Felicidades, has aprendido las maneras básicas de comunicación con funciones.



print("-----6-----")

#Se puede pasar información a las funciones utilizando parámetros. Las funciones pueden tener tantos parámetros como sean necesarios.
#Un ejemplo de una función con un parámetro:

def hola(nombre):
    print("Hola,", nombre)

hola("Greg")

#Un ejemplo de una función de dos parámetros:

def holaTodos(nombre1, nombre2):
    print("Hola,", nombre2)
    print("Hola,", nombre1)

holaTodos("Sebastián", "Felipe")



#Un ejemplo de una función de tres parámetros y que, además, es interactivo:

def direccion(calle, ciudad, codigoPostal):
    print("Tu dirección es:", calle, ciudad, codigoPostal)

c = input("Calle: ")
cp = input("Código Postal: ")
cd = input("Ciudad: ")

direccion(c, cd, cp)


#2. Puedes pasar argumentos a una función utilizando las siguientes técnicas:

#Paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1).
#Paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2).
#Una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).

#Ejemplo 1
def resta(a, b):
    print(a - b)

resta(5, 2)    # salida: 3
resta(2, 5)    # salida: -3


#Ejemplo 2
def resta(a, b):
    print(a - b)

resta(a=5, b=2)    # salida: 3
resta(b=2, a=5)    # salida: 3

#Ejemplo 3
def resta(a, b):
    print(a - b)

resta(5, b=2)    # salida: 3
resta(5, 2)    # salida: 3

#Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave.
#Es por esa razón que si se intenta ejecutar el siguiente código:

def resta(a, b):
    print(a - b)

resta(5, b=2)    # salida: 3
#resta(a=5, 2)   Syntax Error. ARGUMENTOS POSICIONALES PRIMERO PARA NO GENERAR ERROR

#Python no lo ejecutará y marcará un error de sintaxis SyntaxError


#3. Se puede utilizar la técnica de argumentos con palabras clave para asignar valores predefinidos a los argumentos:

def nombre(nombre, apellido="Pérez"):
    print(nombre, apellido)

nombre("Andy")    # salida: Andy Pérez
nombre("Bety", "Rodríguez")    # salida: Bety Johnson (el argumento de palabra clave es reemplazado por " Rodríguez ")
#nombre(apellido="Pizarro") ERROR



#¿Cuál es la salida del siguiente código?

def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro() #Mi nombre es Bond. James Bond.


print("-------7---------")

#¿Cuál es la salida del siguiente código?

def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sergio López")
#Salida: Mi nombre es Sergio López. James Bond.


#¿Cuál es la salida del siguiente fragmento de código?

def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro("Susan")
#Salida: Mi nombre es Bond. Susan.




#IMPORTANTEEEEEEEE
#¿Cuál es la salida del siguiente código?

#def suma(a, b=2, c): Paso de argumentos por default primero que un parámetro de palabras clave.
def suma(a,c,b=2): #LOS ARGUMENTOS POR DEFAULT TIENEN QUE IR DE ÚLTIMO
    print(a + b + c)

suma(a=1, c=3)
#Salida: SyntaxError - a non-default argument (c) follows a default argument (b=2)