#Ciertas expresiones se pueden simplificar sin cambiar el comportamiento del programa.
#Intenta recordar cómo Python interpreta la verdad de una condición y ten en cuenta que 
# estas dos formas son equivalentes:

#while numero != 0: y while numero:
#La condición que verifica si un número es impar también puede codificarse en estas formas equivalentes:
#if numero % 2 == 1: e if numero % 2:


#Este código está destinado a imprimir la cadena "Dentro del ciclo" y el valor almacenado en la variable contador 
#durante un ciclo dado exactamente cinco veces. Una vez que la condición se haya cumplido (la variable contador 
#ha alcanzado 0), se sale del ciclo y aparece el mensaje "Fuera del ciclo". así como el valor almacenado 
#en contador se imprime.

#Pero hay una cosa que se puede escribir de forma más compacta: la condición del ciclo while.

contador = 5
while contador != 0:
    print("Dentro del ciclo: ", contador)
    contador -= 1
print("Fuera del ciclo", contador)

print("------------------------1----------------------------")
#Son iguales
contador=5
while contador:
    print("Dentro del ciclo.", contador)
    contador -= 1
print("Fuera del ciclo", contador)
