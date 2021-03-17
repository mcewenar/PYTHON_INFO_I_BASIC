#Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código que te mostramos recientemente.

#El cifrado César original cambia cada caracter por otro a se convierte en b, z se convierte en a, y así sucesivamente. 
#Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga del rango 1 al 25.

#Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas) 
#y todos los caracteres no alfabéticos deben permanecer intactos.

#Tu tarea es escribir un programa el cual:

#Le pida al usuario una línea de texto para encriptar.
#Le pida al usuario un valor de cambio (un número entero del rango 1 al 25, nota: debes obligar al usuario a ingresar un valor de cambio válido 
#(¡no te rindas y no dejes que los datos incorrectos te engañen!).
#Imprime el texto codificado.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada Muestra:

#abcxyzABCxyz 123
#2

#Salida Muestra:

#cdezabCDEzab 123

#Entrada Muestra:

#The die is cast
#25

#Salida Muestra:

#Sgd chd hr bzrs
#Forma de Internet (https://www.youtube.com/watch?v=Ws5E2gCW4Hc) con mejoras en mi código

#Ecuación general c=(x-n)%26
def encripted(string,shift):
    pair=[]
    ciper=""
    pair.append(string)
    
    
    if shift < 1 or shift > 25:
        pair.append("Out range")
        return pair
    else:
        for char in string:
            if char==" ":
                ciper=ciper+char
            elif ord(char) >= ord("1") and ord(char) <= ord("9"):
                ciper=ciper+char
            elif char.isupper():
                ciper=ciper+chr((ord(char)+shift-65)%26+65) #No entiendo
            else:
                ciper=ciper+chr((ord(char)+shift-97)%26+97) #No entiendo
        pair.append(ciper)
        
        return pair            
while True:
    try:
        text = input("Enter the text: ")
        s=int(input("Enter the shift key: "))
        en=encripted(text,s)
        print("The original text is:",en[0])
        print("The encripted string is:",en[1])
    except ValueError:
        print("Don't allow it characters")





#forma mala:
#def cifrado_cesar(texto,num):
#    cifrado = ''
#    if num > 25 or num <1:
#        print("número fuera de rango")
#    else:
#        for char in texto:
#            if ord(char) >= ord("1") and ord(char) <= ord("9"):
#                char=ord(char)
#            elif ord(char)==32:
#                continue
#            code = ord(char) + num
#            if code > ord('z'):
#               resi = ord(char)%num
#                code = ord('a')+resi
#            elif code > ord("Z"):
#                resi = ord(char)%num
#                code = ord('A')+resi
#            cifrado += chr(code)
#        print(cifrado)

#while True:
#    try:
#        text = input("Ingresa tu mensaje: ")
#        numcam=int(input("Ingrese el valor de cambio de cifrado de 1-25: "))
#        cifrado_cesar(text,numcam)
#    except ValueError:
#        print("No se permiten valores alfanuméricos")