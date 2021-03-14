#Operaciones con cadenas: ord()
#Si deseas saber el valor del punto de código ASCII/UNICODE de un caracter específico,
#puedes usar la función ord() (proveniente de ordinal).

#La función necesita una cadena de un caracter como argumento - incumplir este requisito provoca una excepción TypeError, 
#y devuelve un número que representa el punto de código del argumento.

#Observa el código en el editor y ejecútalo. Las salida del fragmento de código es:
# Demostrando la función ord ()

ch1 = 'a' 
ch2 = ' ' # espacio
ch3 = "α"
ch4 = "ę"

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))
print(ord(ch4))
#Salidas:
#97
#32
#945
#281
#Ahora asigna diferentes valores a ch1 y ch2, por ejemplo, α (letra griega alfa), y ę (una letra en el alfabeto polaco); 
#luego ejecuta el código y ve qué resultado produce. Realiza tus propios experimentos.

print("--2--")

#Operaciones con cadenas: chr()
#Si conoces el punto de código (número) y deseas obtener el carácter correspondiente, puedes usar la función llamada chr().

#La función toma un punto de código y devuelve su carácter.

#Invocándolo con un argumento inválido (por ejemplo, un punto de código negativo o inválido) provoca las excepciones ValueError o TypeError.

#Ejecuta el código en el editor, su salida es la siguiente:

# Demostrando la función chr()
print(chr(97))
print(chr(945))

#a
#α

#Nota:

#chr(ord(x)) == x
#ord(chr(x)) == x
#De nuevo, realiza tus propios experimentos.

print("--3--")

#IMPORTANTE:
#Cadenas como secuencias: indexación
#Ya dijimos antes que las cadenas de Python son secuencias. Es hora de mostrarte lo que significa realmente.

#Las cadenas no son listas, pero pueden ser tratadas como tal en muchos casos.

#Por ejemplo, si deseas acceder a cualquiera de los caracteres de una cadena, puedes hacerlo usando indexación, 
#al igual que en el ejemplo en el editor. Ejecuta el programa.
# Indexando cadenas

exampleString = 'silly walks'
print(len(exampleString))
for ix in range(len(exampleString)):  #INDEXACIÓN
    #print(exampleString[ix]) #Se muestra por línea en la consola
    print(exampleString[ix], end=' ') #Se salta los saltos de línea implícitos
    #print(exampleString[-ix])
print("fin")
#Ten cuidado, no intentes pasar los límites de la cadena, ya que provocará una excepción.

#El resultado de ejemplo es:
#s i l l y   w a l k s

#Por cierto, los índices negativos también se comportan como se esperaba. Comprueba esto tú mismo.

#Cadenas como secuencias: iterando
#Iterar a través de las cadenas funciona también. Observa el siguiente ejemplo:

# Iterando a través de una cadena

#ITERACIÓN
exampleString = 'silly walks'
for ch in exampleString:
    print(ch, end=' ')
    #print(-ch) MALOOOOOOOOO
print("hi")
print(exampleString[-1],exampleString[-3],"Hola") #No se permiten cortes de lista
print()

#La salida es la misma que el ejemplo anterior, revisalo.