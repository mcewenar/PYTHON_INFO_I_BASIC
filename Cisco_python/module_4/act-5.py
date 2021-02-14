#El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, 
#se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

#En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

#Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(millas por galón), y viceversa.

#Las funciones:

#Se llaman l100kmampg y mpgal100km respectivamente.
#Toman un argumento (el valor correspondiente a sus nombres).
#Complementa el código en el editor.

#Ejecuta tu código y verifica si tu salida es la misma que la nuestra.

#Aquí hay información para ayudarte:

#1 milla = 1609.344 metros.
#1 galón = 3.785411784 litros.


def l100kmtompg(liters): #EL PARÁMETRO DICE QUE ESTÁ INGRESANDO (truquito)
    g=(liters/3.785411784)
    mile=100*1000*(1/1609.344)
    return mile/g
 
def mpgtol100km(miles): #USAR EN MILLAS
    km=(miles*1609.344)*(1/1000)*(1/100)
    li=3.785411784
    return li/km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))