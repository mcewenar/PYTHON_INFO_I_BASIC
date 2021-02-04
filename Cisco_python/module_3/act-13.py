#Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.

#Tu tarea es:

#Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado 
# por el usuario (paso 1).
#Escribir una línea de código que elimine el último elemento de la lista (paso 2).
#Escribir una línea de código que imprima la longitud de la lista existente (paso 3).
#¿Listo para este desafío?

listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
num = int(input("Ingrese un número entero: "))
# para reemplazar el número de en medio con un número entero ingresado por el usuario.
listaSombrero[2] = num
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del listaSombrero[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud es ",len(listaSombrero))


print(listaSombrero)