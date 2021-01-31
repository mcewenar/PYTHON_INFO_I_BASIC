#La instrucción break se usa para salir/terminar un ciclo.

#Diseña un programa que use un ciclo while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese
#"chupacabra" como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el ciclo con éxito".
#Debe imprimirse en la pantalla y el ciclo debe terminar.

#No imprimas ninguna de las palabras ingresadas por el usuario.
#Utiliza el concepto de ejecución condicional y la declaración break.

#Break: Sale del ciclo inmediatamente, e incondicionalmente termina la operación del ciclo; el programa comienza a
#  ejecutar la instrucción más cercana después del cuerpo del ciclo.
#Continue: Se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se 
# inicia y la expresión de condición se prueba de inmediato.
while True:
    palabra = input("Ingresa una palabra: ")
    if palabra == "Chupacabra" or palabra == "chupacabra" or palabra == "CHUPACABRA":
        print("¡Has dejado el ciclo con éxito")
        break
