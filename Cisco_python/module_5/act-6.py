#Escenario
#¿Sabes qué es un palíndromo?

#Es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. Por ejemplo, "kayak" es un palíndromo, 
#mientras que "leal" no lo es.

#Tu tarea es escribir un programa que:

#Le pida al usuario algún texto.
#Compruebe si el texto introducido es un palíndromo e imprima el resultado.
#Nota:

#Supón que una cadena vacía no es un palíndromo.
#Trata las letras mayúsculas y minúsculas como iguales.
#Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
#Existe más de una solución correcta: intenta encontrar más de una.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada Muestra:

#Ten animals I slam in a net

#Salida Muestra:

#Es un palíndromo

#Entrada Muestra:

#Eleven animals I slam in a net

#Salida Muestra:

#No es un palíndromo

def palindromo(cadena):
    cadenaLow=cadena.lower()
    cadenaEspa=cadenaLow.replace(" ","")
    cadeInv = cadenaEspa[::-1]
    if cadena == "":
        print("No es palíndromo")
    elif cadeInv == cadenaEspa:
        print("Es palíndromo")
    else:
        print("No es palíndromo")
while True:
    letra=input("Ingresa una palabra: ")
    palindromo(letra)