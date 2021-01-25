
#Si deseas ejecutar más de una declaración dentro de un while, debes (como con if) poner sangría a todas las 
#instrucciones de la misma manera.
#Una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del ciclo.
#Si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, el cuerpo no se 
#ejecuta ni una sola vez
#(ten en cuenta la analogía de no tener que hacer nada si no hay nada que hacer).
#El cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al principio,
#el cuerpo podría funcionar continuamente hasta el infinito. Observa que hacer una cosa generalmente disminuye 
#la cantidad de cosas por hacer.


# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int(input("Introduce un número o escribe -1 para detener:"))

#Imprimir el número más grande
print("El número más grande es:", numeroMayor)