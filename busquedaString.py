#Tiempo Estimado
#15-20 minutos

#Nivel de Dificultad
#Medio

#Objetivos
#Mejorar las habilidades del alumno para trabajar con cadenas.
#Emplear el método find() para realizar busquedas dentro de las cadenas.
#Escenario
#Vamos a jugar un juego. Le daremos dos cadenas: una es una palabra (por ejemplo, "dog") y la segunda es una combinación de un 
#grupo de caracteres.

#Tu tarea es escribir un programa que responda la siguiente pregunta: ¿Los caracteres que comprenden la primera cadena están ocultos 
#dentro de la segunda cadena?

#Por ejemplo:

#Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si.
#Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no (ya que no están las letras "d", "o", "g", ni en ese orden).
#Consejos:

#Debes usar las variantes de dos argumentos de las funciones pos() dentro de tu código.
#No te preocupes por mayúsculas y minúsculas.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada de Ejemplo:

#donor
#Nabucodonosor

#Salida del Ejemplo:

#Si

#Entrada de Ejemplo:

#donut
#Nabucodonosor

#Salida del Ejemplo:

#No

#Escribe un string que se busca en otro string, así esté en desorden
def finder(string1,string2):
    for i in string1:
        fnd = string2.find(i)
        if fnd!= -1:
            encontrado="Sí"
        else:
            encontrado="No"
            break
    return encontrado
    
while True:
    first=input("Ingresa cadena uno: ")
    second=input("Ingresa segunda cadena: ")
    p=finder(first,second)
    print(p)