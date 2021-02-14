#Las funciones y sus alcances (scopes): (IMPORTANTÍSIMO)


#Comencemos con una definición:
#El alcance de un nombre (por ejemplo, el nombre de una variable) es la parte del código donde el nombre es reconocido correctamente.

#Por ejemplo, el alcance del parámetro de una función es la función en si misma. El parámetro es inaccesible fuera de la función.

#Vamos a revisarlo. Observa el código en el editor. ¿Que ocurrirá cuando se ejecute?

#El programa no correrá. El mensaje de error dirá:
#NameError: name 'x' is not defined

#Esto era de esperarse.

#Vamos a conducir algunos experimentos para mostrar como es que Python define los alcances y como los puedes utilizar para tu beneficio.

#La variable debe definirse por fuera de la función.
def scopeTest():
    x = 123
scopeTest()
#print(x)
#SALIDA: NameError: name 'x' is not defined


#Las funciones y sus alcances (scopes): continuación (IMPORTANTE IGUAL)

print("-------2--------")
#Comencemos revisando si una variable creada fuera de una función es visible dentro de una función. En otras palabras, 
#¿El nombre de la variable se propaga dentro del cuerpo de la función?
def miFuncion():
    print("¿Conozco a la variable?", var)

var = 1
miFuncion()
print(var)

#Observa el código en el editor. Ahí esta nuestro conejillo de indias.

#El resultado de la prueba es positivo, el código da como salida:

#SALIDA:
#¿Conozco a la variable? 1
#1

#LA RESPUESTA ES: UNA VARIABLE QUE EXISTE FUERA DE UNA FUNCIÓN TIENE ALCANCE DENTRO DEL CUERPO DE LA FUNCIÓN

#Esta regla tiene una excepción muy importante. Intentemos encontrarla.

#Hagamos un pequeño cambio al código:

def miFuncion():
    var = 2
    print("¿Conozco a la variable?", var)

var = 1
miFuncion()
print(var)

#El resultado ha cambiado también el código arroja una salida con una ligera diferencia:
#SALIDA:
#¿Conozco a la variable? 2
#1

#¿Qué es lo que ocurrió? (IMPORTANTE)

#La variable var creada dentro de la función no es la misma que la que se definió fuera de ella, parece ser que hay dos variables 
#diferentes con el mismo nombre.
#La variable de la función es una sombra de la variable fuera de la función.
#La regla anterior se puede definir de una manera mas precisa y adecuada:


#(HIPERIMPORTANTE):

#1. UNA VARIABLE QUE EXISTE FUERA DE UNA FUNCIÓN TIENE UN ALCANCE DENTRO DEL CUERPO DE LA FUNCIÓN, EXCLUYENDO A AQUELLAS 
#QUE TIENEN EL MISMO NOMBRE
#2. TAMBIÉN SIGNIFICA QUE EL ALCANCE DE UNA VARIABLE EXISTENTE FUERA DE UNA FUNCIÓN SOLO SE PUEDE IMPLEMENTAR DENTRO DE UNA FUNCIÓN
#CUANDO SU VALOR ES LEÍDO. EL ASIGNAR UN VALOR HACE QUE LA FUNCIÓN CREE SU PROPIA VARIABLE 

#Asegúrate bien de entender esto correctamente y de realizar tus propios experimentos.




print("---------3---------")

#Las funciones y sus alcances (scopes): la palabra reservada global
#Al llegar a este punto, debemos hacernos la siguiente pregunta: ¿Una función es capaz de modificar una variable que fue definida fuera de ella?
#Esto sería muy incomodo.

#Afortunadamente, la respuesta es no.

#Existe un método especial en Python el cual puede extender el alcance de una variable incluyendo el cuerpo de las funciones para poder 
#no solo leer los valores de las variables sino también modificarlos.

#Este efecto es causado por la palabra reservada llamada global:

global name
global name1, name2 #...

#El utilizar la palabra reservada dentro de una función con el nombre o nombres de las variables separados por comas, obliga a Python a 
#abstenerse de crear una nueva variable dentro de la función; se empleará la que se puede acceder desde el exterior.

#En otras palabras, este nombre se convierte en global (tiene un alcance global, y no importa si se esta leyendo o asignando un valor).

#Observa el código en el editor:
def miFuncion():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)

var = 1
miFuncion()
print(var)
#Se ha agregado la palabra global a la función.

#El código ahora da como salida:

#¿Conozco a aquella variable? 2
#2

#Esto debe de ser suficiente evidencia para mostrar lo que la palabra reservada global puede hacer.