#ImportError
#Ubicación:

#BaseException ← Exception ← StandardError ← ImportError

#Descripción:

#Se produce una excepción concreta cuando falla una operación de importación.

#Código:

# una de estas importaciones fallará, ¿cuál será?

#try:
#    import math
#    import time
#    import abracadabra

#except:
#    print('Una de sus importaciones ha fallado.')

#KeyError
#Ubicación:

#BaseException ← Exception ← LookupError ← KeyError

#Descripción:

#Una excepción concreta que surge cuando intentas acceder al elemento inexistente de una colección (por ejemplo, el elemento de un diccionario).

#Código:

# como abusar del diccionario
# y cómo lidiar con ello

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)

#Hemos terminado con excepciones por ahora, pero volverán cuando discutamos la programación orientada a objetos en Python. 
#Puedes usarlos para proteger tu código de accidentes graves, pero también tienes que aprender a sumergirte en ellos, 
#explorando la información que llevan.

#De hecho, las excepciones son objetos; sin embargo, no podemos decirle nada sobre este aspecto hasta que te presentemos clases, 
#objetos y similares.

#Por el momento, si deseas obtener más información sobre las excepciones por tu cuenta, consulta la Biblioteca estándar de Python en 
#IMPORTANTE REVISAR: https://docs.python.org/3.6/library/exceptions.html.