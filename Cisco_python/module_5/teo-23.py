#El Cifrado César: encriptando un mensaje
#Te mostraremos cuatro programas simples para presentar algunos aspectos del procesamiento de cadenas en Python. Son intencionalmente simples, 
#pero los problemas de laboratorio serán significativamente más complicados.

#El primer problema que queremos mostrarte se llama Cifrado César - más detalles aquí: https://en.wikipedia.org/wiki/Caesar_cipher.

#Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César y sus tropas durante las Guerras Galas. 
#La idea es bastante simple: cada letra del mensaje se reemplaza por su consecuente más cercano 
#(A se convierte en B, B se convierte en C, y así sucesivamente). La única excepción es Z, la cual se convierte en A.

#El programa en el editor es una implementación muy simple (pero funcional) del algoritmo.

#Se ha escrito utilizando los siguientes supuestos:

#Solo acepta letras latinas (nota: los romanos no usaban espacios en blanco ni dígitos).
#Todas las letras del mensaje están en mayúsculas (nota: los romanos solo conocían las mayúsculas).
#Veamos el código:
# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)

#La línea 02: pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
#La línea 03: prepara una cadena para el mensaje cifrado (esta vacía por ahora).
#La línea 04: inicia la iteración a través del mensaje.
#La línea 05: si el caracter actual no es alfabético...
#La línea 06: ...ignoralo.
#La línea 07: convierta la letra a mayúsculas (es preferible hacerlo a ciegas, en lugar de verificar si es necesario o no).
#La línea 08: obtén el código de la letra e increméntalo en uno.
#La línea 09: si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
#La línea 10: ... cámbialo al código de la A.
#La línea 11: agrega el carácter recibido al final del mensaje cifrado.
#La línea 13: imprime el cifrado.
#El código, alimentado con este mensaje:

#AVE CAESAR

#Da como salida:

#BWFDBFTBS

#Haz tus propias pruebas.

print("---2---")

#El cifrado César: descifrando un mensaje
#La operación inversa ahora debería ser clara para ti: solo presentamos el código tal como está, sin ninguna explicación.

#Observa el código en el editor. Comprueba cuidadosamente si funciona. Usa el criptograma del programa anterior.

# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

print("---3---")

#El Procesador de Números
#El tercer programa muestra un método simple que permite ingresar una línea llena de números y sumarlos fácilmente. 
#Nota: la función input(), combinada junto con las funciones int() o float(), no es lo adecuado para este propósito.

#El procesamiento será extremadamente fácil: queremos que se sumen los números.

#Observa el código en el editor. Analicémoslo.

#Procesador de números

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
if linea !="":

    strings = linea.split() #De forma predeterminada se toman los espacios y se reemplazan con comas
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("El total es:", total)
    except:
        print(substr, "no es un numero.")
else:
    print("Campo vacío")

#Emplear listas puede hacer que el código sea más pequeño. Puedes hacerlo si quieres.

#Presentemos nuestra versión:

#La línea 03: pide al usuario que ingrese una línea llena de cualquiser cantidad de números (los números pueden ser flotantes).
#La línea 04: divide la línea en una lista con subcadenas.
#La línea 05: se inicializa la suma total a cero.
#La línea 06: como la conversión de cadena a flotante puede generar una excepción, es mejor continuar con la protección del bloque try-except.
#La línea 07: itera a través de la lista...
#La línea 08: ...e intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
#La línea 09: todo está bien hasta ahora, así que imprime la suma.
#La línea 10: el programa termina aquí en caso de error.
#La línea 11: imprime un mensaje de diagnóstico que muestra al usuario el motivo del error.
#El código tiene una debilidad importante: muestra un resultado falso cuando el usuario ingresa una línea vacía. ¿Puedes arreglarlo?


#Forma másinteresante:
#def sumaNum(enteros):
#    if enteros != "":
#        listado = list(enteros)
#        total = 0
#        for substr in listado:
#            total += int(substr)
#        return total
#    else:
#        print("No has ingresado valor\nVuelve a intentarlo\n")
#        return "vacío"
            
    

#while True:
#    try:
#        linea = input("Ingresa una línea de números enteros: ")
#        print(linea)
        #print(type(linea))
#        substr=sumaNum(linea)
#        print("El total es:", substr)
#        print()
        
#    except:
#        print(linea, "no es un numero entero")
