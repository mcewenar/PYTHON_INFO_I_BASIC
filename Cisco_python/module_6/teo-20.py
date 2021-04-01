#Procesamiento de archivos de texto
#En esta lección vamos a preparar un archivo de texto simple con contenido breve y simple.

#Te mostraremos algunas técnicas básicas que puedes utilizar para leer el contenido del archivo para poder procesarlo.

#El procesamiento será muy simple: vas a copiar el contenido del archivo a la consola y contarás todos los caracteres que el programa ha leído.

#Pero recuerda: nuestra comprensión de un archivo de texto es muy estricta. Es un archivo de texto sin formato: puede contener solo texto, 
#sin decoraciones adicionales (formato, diferentes fuentes, etc.).

#EJEMPLO:
#stream = open("tzop.txt", "rt", encoding = "utf-8") # se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto de archivo
#print(stream.read()) # se imprime el contenido del archivo

#Es por eso que debes evitar crear el archivo utilizando un procesador de texto avanzado como MS Word, LibreOffice Writer o algo así.
#Utiliza los conceptos básicos que ofrece tu sistema operativo: Bloc de notas, vim, gedit, etc.

#Si tus archivos de texto contienen algunos caracteres nacionales no cubiertos por el juego de caracteres ASCII estándar,
# es posible que necesites un paso adicional. La invocación de tu función open() puede requerir un argumento que denote 
# una codificación específica del texto.

#Por ejemplo, si estás utilizando un sistema operativo Unix/Linux configurado para usar UTF-8 como una configuración de todo el sistema,
# la función open() puede verse de la siguiente manera:

#stream = open('file.txt', 'rt', encoding='utf-8')

#Donde el argumento de codificación debe establecerse en un valor dentro de una cadena que representa
# la codificación de texto adecuada (UTF-8, en este caso).

#Consulta la documentación de tu sistema operativo para encontrar el nombre de codificación adecuado para tu entorno.


#INFORMACIÓN:

#A los fines de nuestros experimentos con el procesamiento de archivos que se llevan a cabo en esta sección,
# vamos a utilizar un conjunto de archivos precargados (p. Ej., los archivos tzop.txt, o text.txt) con los cuales podrás trabajar.
#  Si deseas trabajar con tus propios archivos localmente en tu máquina,
#   te recomendamos que lo hagas y que utilices un Entorno de Desarrollo para llevar a cabo tus propias pruebas.




#INFORMACIÓN IMPORTANTE:
#The Zen of Python
#=================

#::

#    Beautiful is better than ugly.
#    Explicit is better than implicit.
#    Simple is better than complex.
#    Complex is better than complicated.
#    Flat is better than nested.
#    Sparse is better than dense.
#    Readability counts.
#    Special cases aren't special enough to break the rules.
#    Although practicality beats purity.
#    Errors should never pass silently.
#    Unless explicitly silenced.
#    In the face of ambiguity, refuse the temptation to guess.
#    There should be one-- and preferably only one --obvious way to do it.
#    Although that way may not be obvious at first unless you're Dutch.
#    Now is better than never.
#    Although never is often better than *right* now.
#    If the implementation is hard to explain, it's a bad idea.
#    If the implementation is easy to explain, it may be a good idea.
#    Namespaces are one honking great idea -- let's do more of those!



#----------------
#source: https://github.com/python/peps/blob/master/pep-0020.txt


print("---2---")

#Procesamiento de archivos de texto: continuación
#La lectura del contenido de un archivo de texto se puede realizar utilizando diferentes métodos; ninguno de ellos es mejor o peor que otro.
# Depende de ti cuál de ellos prefieres y te gusta.

#Algunos de ellos serán a veces más prácticos y otros más problemáticos. Se flexible. No tengas miedo de cambiar tus preferencias.

#El más básico de estos métodos es el que ofrece la función read(), la cual pudiste ver en acción en la lección anterior.

#Si se aplica a un archivo de texto, la función es capaz de:

#Leer un número determinado de caracteres (incluso solo uno) del archivo y devolverlos como una cadena.
#Leer todo el contenido del archivo y devolverlo como una cadena.
#Si no hay nada más que leer (el cabezal de lectura virtual llega al final del archivo), la función devuelve una cadena vacía.

#Comenzaremos con la variante más simple y usaremos un archivo llamado text.txt. El archivo contiene lo siguiente:

#Lo hermoso es mejor que lo feo.
#Explícito es mejor que implícito.
#Simple es mejor que complejo.
#Complejo es mejor que complicado.

#Ahora observa el código en el editor y analicémoslo.
from os import strerror

try:
    cnt = 0
    #s = open('text.txt', "rt") FORMA DEL CURSO
    s = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\text.txt', "rt")
    ch = s.read(1) #LEE EL PRIMER CARACTER
    while ch != '': #Si no es caracter vacío, se ejecuta
        print(ch, end='')
        cnt += 1 #SE ACTUALIZA PARA LEER EL SIGUIENTE
        ch = s.read(1) #Nuevamente se lee y repite el ciclo hasta finalizar
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt) #HACE EL CONTEO
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#La rutina es bastante simple:

#Se usa el mecanismo try-except y se abre el archivo con el nombre (text.txt en este caso).
#Intenta leer el primer caracter del archivo (ch = s.read(1)).
#Si tienes éxito (esto se demuestra por el resultado positivo de la condición while), se muestra el caracter (nota el argumento end=,
#¡es importante! ¡No querrás saltar a una nueva línea después de cada caracter!).
#Se actualiza el contador (cnt).
#Intenta leer el siguiente carácter y el proceso se repite.

print("---3---")

#Procesamiento de archivos de texto: continuación
#Si estás absolutamente seguro de que la longitud del archivo es segura y puedes leer todo el archivo en la memoria de una vez,
#puedes hacerlo: la función read(), invocada sin ningún argumento o con un argumento que se evalúa a None, hará el trabajo por ti.

#IMPORTANTE:
#Recuerda - el leer un archivo muy grande (en terabytes) usando este método puede dañar tu sistema operativo.

#No esperes milagros: la memoria de la computadora no se puede extender.

#Observa el código en el editor. ¿Que piensas de el?
from os import strerror

try:
    cnt = 0
    #s = open('text.txt', "rt") FORMA DEL CURSO
    s = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\text.txt', "rt")
    content = s.read() #Se guarda todo el archivo en la variable content
    print("Este es la cadena: ", content) #SE MUESTRA TODO EL ARCHIVO
    for ch in content: #Se recorre toda la cadena
        print(ch, end='') #SIN EL END, ESTO SE VERÍA COMO UNA ITERACIÓN DE LETRAS (IMPORTANTE)
        cnt += 1 #Para contar el número de carácteres que hay en el archivo.
        ch = s.read(1) #LEE SÓLO 1 CARACTER
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))


#Vamos a analizarlo:

#Abre el archivo, como anteriormente se hizo.
#Lee el contenido mediante una invocación de la función read().
#Despues, se procesa el texto, iterando con un bucle for su contenido, y se actualiza el valor del contador en cada vuelta del bucle.
#El resultado será exactamente el mismo que en el ejemplo anterior.


print("---4---")
#Procesando archivos de texto: readline()
#Si deseas manejar el contenido del archivo como un conjunto de líneas, no como un montón de caracteres,
#el método readline() te ayudará con eso.

#OJO:
#El método intenta leer una línea completa de texto del archivo, y la devuelve como una cadena en caso de éxito.
#De lo contrario, devuelve una cadena vacía.

#Esto abre nuevas oportunidades: ahora también puedes contar líneas fácilmente, no solo caracteres.

#Hagámos uso de ello. Observa el código en el editor.
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\text.txt', "rt")
    #s = open('text.txt', 'rt') FORMA DEL CURSO
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Como puedes ver, la idea general es exactamente la misma que en los dos ejemplos anteriores.


print("---5---")
#OJO:
#readline != readlines

#Procesando archivos de texto: readlines()
#Otro método, que maneja el archivo de texto como un conjunto de líneas, no como caracteres, es readlines().

#Cuando el método readlines(), se invoca sin argumentos, intenta leer todo el contenido del archivo y devuelve una lista de cadenas, 
#un elemento por línea del archivo.

#Si no estás seguro de si el tamaño del archivo es lo suficientemente pequeño y no deseas probar el sistema operativo, 
#puedes convencer al método readlines() 
#de leer no más de un número especificado de bytes a la vez (el valor de retorno sigue siendo el mismo, es una lista de una cadena).

#Siéntete libre de experimentar con este código de ejemplo para entender cómo funciona el método readlines().
s = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\text.txt', "rt")
#s = open("text.txt") FORMA DEL CURSO
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20)) #ESTO ESTÁ EN BYTES
print(s.readlines(20))
s.close()

#El tamaño máximo del búfer de entrada aceptado se pasa al método como argumento.

#Puedes esperar que readlines() procese el contenido del archivo de manera más efectiva que readline(), ya que puede ser invocado menos veces.

#Nota: cuando no hay nada que leer del archivo, el método devuelve una lista vacía. Úsalo para detectar el final del archivo.

#Puedes esperar que al aumentar el tamaño del búfer mejore el rendimiento de entrada, pero no hay una regla de oro para ello: 
#intenta encontrar los valores óptimos por ti mismo.


#Observa el código en el editor. Lo hemos modificado para mostrarte cómo usar readlines().
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\text.txt', "rt")
    #s = open('text.txt', 'rt') FORMA DEL CURSO
    lines = s.readlines(20)
    print(lines) #AÑADIDO POR MÍ
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Hemos decidido usar un búfer de 15 bytes de longitud. No pienses que es una recomendación.

#Hemos utilizado ese valor para evitar la situación en la que la primera invocación de readlines() consuma todo el archivo.

#Queremos que el método se vea obligado a trabajar más duro y que demuestre sus capacidades.

#Existen dos bucles anidados en el código: el exterior emplea el resultado de readlines() para iterar a través de él, 
#mientras que el interno imprime las líneas carácter por carácter.