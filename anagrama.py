#Escenario
#Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, usando todas las letras originales exactamente una vez. 
#Por ejemplo, las frases "rail safety" y "fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.

#Tu tarea es escribir un programa que:

#Le pida al usuario dos textos por separado.
#Compruebe si los textos ingresados son anagramas e imprima el resultado.
#Nota:

#Supongamos que dos cadenas vacías no son anagramas.
#Tratar las letras mayúsculas y minúsculas como iguales.
#Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada de Ejemplo:

#Listen
#Silent

#Salida del Ejemplo:

#Anagramas

#Entrada de Ejemplo:

#modern
#norman

#Salida del Ejemplo:

#No son Anagramas
#https://www.youtube.com/watch?v=Pb7pmvifBf4


def anagrama(ana,grama):
    n=0
    m=0
    anaSin=ana.replace(" ","").lower()
    gramaSin=grama.replace(" ","").lower()
    list(anaSin)
    list(gramaSin)
    
    for i in anaSin:
        n+=ord(i)
    for j in gramaSin:
        m+=ord(j)
    if ana == "" or grama == "" or ana==" " or grama==" ":
        print("No es anagrama")
    elif n == m:
        print("Es anagrama")
    else:
        print("No es anagrama")
while True:
    text1=input("Ingresa cadena 1: ")
    text2=input("Ingresa cadena 2: ")
    anagrama(text1,text2)