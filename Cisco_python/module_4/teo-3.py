#IMPORTANTE

#Funciones con parámetros
#El potencial completo de una función se revela cuando puede ser equipada con una interface que es capaz de aceptar datos provenientes 
#de la invocación. Dichos datos pueden modificar el comportamiento de la función,
#haciéndola mas flexible y adaptable a condiciones cambiantes.


 #Puede pensar en el parámetro como un espacio de estacionamiento y el argumento como un automóvil. Del mismo modo 
 #que los diferentes automóviles pueden detenerse en un espacio de estacionamiento en momentos diferentes, 
 #el código de llamada puede pasar un argumento diferente al mismo parámetro cada vez que llama al procedimiento.

#Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

#1. Los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único lugar donde un parámetro puede ser definido es entre los 
#paréntesis después del nombre de la función, donde se encuentra la palabra reservada def.
#2. La asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca, 
#especificando el argumento correspondiente.
def funcion(parametro):
    pass
    ###





#IMPORTANTE:
#ARGUMENTO ES DIFERENTE A PARÁMETRO. EL ARGUMENTO ES LO QUE VA POR DENTRO DE LOS PARÉNTESIS DE LA FUNCIÓN QUE SE INVOCA. PARÁMETRO ES
#LO QUE VA ADENTRO DE LA FUNCIÓN (DEF)

#Recuerda que:

#Los parámetros solo existen dentro de las funciones (este es su entorno natural).
#Los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.
piso="l"
def casa(puerta): #esto es parámetro
    print("hola")

casa(piso) #Lo que va dentro de la invocación se llama argumento

#Esta definición especifica que nuestra función opera con un solo parámetro con el nombre de numero. 
# Se puede utilizar como una variable normal, 
# pero solo dentro de la función - no es visible en otro lugar.


print("------3------")

def mensaje(numero):
     print("Ingresa el número:", numero)

#Se ha hecho buen uso del parámetro. Nota: No se le ha asignado al parámetro algún valor. ¿Es correcto?
#Si, lo es.
#Un valor para el parámetro llegará del entorno de la función.

    
#Recuerda: especificar uno o mas parámetros en la definición de la función es un requerimiento, y se debe de cumplir durante la 
#invocación de la misma. SE DEBE PROVEER EL MISMO NÚMERO DE ARGUMENTOS COMO HAYA PARÁMETROS DEFINIDOS.


#El no hacerlo provocará un error.




#Funciones con parámetros: continuación
#Intenta ejecutar el código en el editor.

#Esto es lo que aparecerá en consola:

#def mensaje(numero):
#    print("Ingresa un número:", numero)

#mensaje() #Genera error porque el argumento es vacío
#TypeError: mensaje() missing 1 required positional argument: 'numero'

#Esto significa que se esta invocando la función pero esta faltando el argumento.



#FORMA CORRECTA
def mensaje(numero):
    print("Ingresa un número:", numero)

mensaje(1) 
#De esta manera ya esta correcto. El código producirá la siguiente salida:

#Ingresa un número: 1

#¿Puedes ver como funciona? El valor del argumento utilizado durante la invocación (1) ha sido pasado a la función, 
#dándole un valor inicial al parámetro con el nombre de numero.

#Existe una circunstancia importante que se debe mencionar.
#Es posible tener una variable con el mismo nombre del parámetro de la función.
#El siguiente código muestra un ejemplo de esto:
print("-----4-----")
def mensaje(numero):
    print("Ingresa un número:", numero)

numero = 1234
mensaje(1)
print(numero)

#Una situación como la anterior, activa un mecanismo denominado sombreado:
#El parámetro x sombrea cualquier variable con el mismo nombre, pero...
#... solo dentro de la función que define el parámetro.

#El parámetro llamado numero es una entidad completamente diferente de la variable llamada numero.

#Esto significa que el código anterior producirá la siguiente salida:

#Ingresa un número: 1
#1234


#Funciones con parámetros: continuación

#Una función puede tener tantos parámetros como se desee, pero entre más parámetros, es más difícil memorizar su rol y propósito.

#Modifiquemos la función- ahora tiene dos parámetros:
def mensaje(que, numero):
    print("Ingresa", que, "número", numero)
mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "número")
#mensaje("l") ERROR

#Esto significa que para invocar la función, se necesitan dos argumentos.
#El primer valor va a contener el nombre del valor deseado.

#Output:
#Ingresa teléfono número 11
#Ingresa precio número 5
#Ingresa número número número 
