#Como seguramente sabrás, debido a algunas razones astronómicas, el año pueden ser bisiesto o común.
#Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

#Desde la introducción del calendario gregoriano (en 1582),
#se utiliza la siguiente regla para determinar el tipo de año:

#Si el número del año no es divisible entre cuatro, es un año común.
#De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
#De lo contrario, si el número del año no es divisible entre 400, es un año común.
#De lo contrario, es un año bisiesto.

#Observa el código en el editor: solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que 
#acabamos de describir.

#El código debe mostrar uno de los dos mensajes posibles, que son Año bisiesto o Año común, 
#según el valor ingresado.

#Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario:
#No dentro del período del calendario gregoriano. Consejo: utiliza los operadores != y %.
while True:
    año = int(input("Introduzca un año: "))

    if año>=1582:
        if año%4!=0:
            print("Año común")
        elif año%100!=0:
            print("Años bisiesto")
        elif año%400!=0:
            print("Año común")
        else: 
            print("Año bisiesto")
    else:
        print("No dentro del período del calendario gregoriano")