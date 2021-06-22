#Escenario
#¿Sabes qué es un palíndromo?

#Es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. Por ejemplo, "kayak" es un palíndromo, 
#mientras que "leal" no lo es.

#Tu tarea es escribir un programa que:

#Le pida al usuario algún texto.
#Compruebe si el texto introducido es un palíndromo e imprima el resultado.
#Nota:

#Supón que una cadena vacía no es un palíndromo.
#Trata las letras mayúsculas y minúsculas como iguales.
#Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
#Existe más de una solución correcta: intenta encontrar más de una.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada Muestra:

#Ten animals I slam in a net

#Salida Muestra:

#Es un palíndromo

#Entrada Muestra:

#Eleven animals I slam in a net

#Salida Muestra:

#No es un palíndromo

def palindromo(cadena):
    cadenaLow=cadena.lower()
    cadenaEspa=cadenaLow.replace(" ","")
    cadeInv = cadenaEspa[::-1]
    if cadena == "":
        print("No es palíndromo")
    elif cadeInv == cadenaEspa:
        print("Es palíndromo")
    else:
        print("No es palíndromo")
while True:
    letra=input("Ingresa una palabra: ")
    palindromo(letra)


#a=input("Enter word")
#def Convert(string): 
#    li = list(string.split("-")) 
#    return li 
#a1=a.reverse()
#if a==a1:
#    print("Es palíndroma")
#else: 
#    print("No es palíndroma")

from math import ceil
def esPalindrome(palabra):
   NN = len(palabra)   
   long2 = NN // 2     # 
   izq = palabra[0:long2] #slice o rebanada, exclueye la pos [long2]
   der1 = palabra[long2:NN] if NN % 2 == 0 else palabra[long2+1:NN]
   der = der1[::-1] # reversa el lado derecho
   res:bool = der == izq  #compara ambas en orden lexicografico
   return res 
#print(math.ceil(3.2))
lista=["amor a roma","anita atina","al sur de Colombia","anula las alas a la luna", \
"anulal a sala sal aluna","la tele letal"]
for frase in lista: #frase es una cadena
  res=esPalindrome(frase)
  print(frase,'\t',res)


  #parte2: palindrome de frase, donde mayusculas se consideran igual a minusculas
# se ignoran signos de puntuacion (. : ; , ? ! ), y espacios, aun falta quitar tildes
def esPalindrome(palabra):
   NN = len(palabra)   
   long2=NN//2   
   izq = palabra[0:long2] #slice o rebanada, excluye la pos [long2]
   der1 = palabra[long2:NN] if (NN % 2 == 0) else palabra[long2+1:NN]  #ani l ina
   der = der1[::-1] # reversa el lado derecho
   res= der == izq  #compara ambas en orden lexicografico
   return res
lista=['Anula las alas a la luna  ',".... Dabale arroz a la zorra el abad .?!;:,", \
       'La tela letal?', '!Arriba la birra', 'Isaac no ronca asi...','Anita la latina']
for frase in lista:
   frase=frase.strip() #quito espacios a izq y derecha
   frase=frase.strip('.,?;!:') #quita estos simbolos a la izq y a la derecha, pero no internas
   frase=frase.upper() #convierto a mayusculas
   NN=len(frase) #Vamos a quitarle los espacios intermedios, uno a la vez
   conta=frase.count(' ')
   for i in range(conta): #genero una coleccion 0, 1,2, sirve para controlar cuantos espacios voy a quitar
     pos= frase.find(' ') #detecto la posicion del primer espacio
     izq=frase[0:pos] #Como las cadenas son inmutables, no puedo cambiar sus caracteres
     der=frase[pos+1:NN] #genero dos subcadenas, izq y der, elimino el espacio intermedio
     print(izq, der) #subcadenas con funcion slice, notacion de range, [ini:fin:incr]
     frase = izq + der #Junto las 2 subcadenas, omito el espacio
   print(esPalindrome(frase)) #solucion