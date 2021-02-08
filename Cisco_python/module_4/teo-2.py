#Así es como se ve la definición más simple de una función:

#def nombreFuncion():
#    cuerpoFuncion


#1.Siempre comienza con la palabra reservada def (que significa definir)
#2.Después de def va el nombre de la función (las reglas para darle nombre a las funciones son las mismas que para las variables).
#3.Después del nombre de la función, hay un espacio para un par de paréntesis (ahorita no contienen algo, pero eso cambiará pronto).
#4.La línea debe de terminar con dos puntos.
#5.La línea inmediatamente después de def marca el comienzo del cuerpo de la función - donde varias o (al menos una). instrucción anidada, 
#será ejecutada cada vez que la función sea invocada; nota: la función termina donde el anidamiento termina, se debe ser cauteloso.

def mensaje():
    print("Ingresa un valor: ")

print("Se comienza aquí.")
mensaje()
print("Se termina aquí.")

#La salida ahora se ve diferente.
#Output:

#Se comienza aquí.
#Ingresa un valor: 
#Se termina aquí.

#Cuando se invoca una función, Python recuerda el lugar donde esto ocurre y salta hacia dentro de la función invocada.
#El cuerpo de la función es entonces ejecutado.
#Al llegar al final de la función, Python regresa al lugar inmediato después de donde ocurrió la invocación.

#Existen dos consideraciones muy importantes, la PRIMERA de ella es:

#No se debe invocar una función antes de que se haya definido.

#Recuerda: Python lee el código de arriba hacia abajo. No va a adelantarse en el código para determinar 
#si la función invocada esta definida mas adelante, el lugar correcto para definirla es antes de ser invocada.

#print("Se comienza aquí.")
#mensaje2()
#print("Se termina aquí.")

#def mensaje2():
#    print("Ingresa un valor: ")
#ERROR
#NameError: name 'mensaje2' is not defined

#SEGUNDA CONSIDERACIÓN:
#La segunda consideración es mas sencilla:


#Una función y una variable no pueden compartir el mismo nombre.
#UNA FUNCIÓN Y UNA VARIABLE NO PUEDEN COMPARTIR EL MISMO NOMBRE
#El siguiente fragmento de código es erróneo:

def mensaje():
    print("Ingresa un valor: ")

mensaje = 1
#El asignar un valor al nombre "mensaje" causa que Python olvide su rol anterior. La función con el nombre de mensaje ya no estará disponible.
print(mensaje)
#mensaje() ==> error



#Afortunadamente, es posible combinar o mezclar el código con las funciones - no es forzoso colocar todas las funciones al inicio 
#del archivo fuente.

#Observa el siguiente código:

print("Se comienza aquí.")

def mensaje():
    print("Ingresa un valor: ")

mensaje()
print("Se termina aquí.")


print("---------------")
def mensaje():
    print("Ingresa un valor: ")

mensaje()
a = int(input())
mensaje()
b = int(input())
mensaje()
c = int(input())
#"El modificar el mensaje de entrada es ahora sencillo: 
#se puede hacer con solo modificar el código una única vez - dentro del cuerpo de la función.


#FORMA INEFICIENTE:
#print("Ingresa un valor: ")
#a = int(input())

#print("Ingresa un valor: ")
#b = int(input())

#print("Ingresa un valor: ")
#c = int(input())

#1. Una función es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada). 
#Las funciones son útiles para hacer que el código sea reutilizable, que este mejor organizado y más legible.
#Las funciones contienen parámetros y pueden regresar valores.

#2. Existen al menos cuatro tipos de funciones básicas en Python:

#Funciones integradas las cuales son partes importantes de Python (como lo es la función print()). 
#Puedes ver una lista completa de las funciones integradas de Python en la siguiente liga: https://docs.python.org/3/library/functions.html.
#También están las que se encuentran en módulos pre-instalados (se hablará acerca de ellas en el Módulo 5 de este curso).
#Funciones definidas por el usuario las cuales son escritas por los programadores para los programadores, 
#puedes escribir tus propias funciones y utilizarlas libremente en tu código.
#Las funciones lambda (aprenderás acerca de ellas en el Módulo 6 del curso).

#Se puede definir una función sin que haga uso de argumentos, por ejemplo:

def mensaje():    # definiendo una función
    print("Hola")    # cuerpo de la función

mensaje()    # invocación de la función 

#También es posible definir funciones con argumentos, como la siguiente que contiene un solo parámetro:

def hola(casa):    # definiendo una función
    print("Hola,", casa)    # cuerpo de la función


nombre = input("Ingresa tu nombre: ")

hola(nombre)    # invocación de la función

print("------2------")
#¿Qué es lo que ocurrirá cuando se ejecute el siguiente código?

def hola():
    print("hola")

#hola(5) #Se genera una excepción (la excepción TypeError) - la función hola() no toma argumentos.






#LO QUE ESTÁ DENTRO DE LA FUNCIÓN SE LLAMA CUERPO DE LA FUNCIÓN
