#Los operadores in y not
#Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro 
#de la lista o no.

#Estos operadores son:

#elem in miLista
#elem not in miLista 

#El primero de ellos (in) verifica si un elemento dado(su argumento izquierdo) está actualmente almacenado en algún lugar dentro de la 
#lista(el argumento derecho) - 
#el operador devuelve True en este caso.

#El segundo (not in) comprueba si un elemento dado (su argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso.

#Observa el código en el editor. El fragmento muestra ambos operadores en acción. ¿Puedes adivinar su salida? Ejecuta el programa 
#para comprobar si tenías razón.


miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)



print("------2-------")

#Ahora queremos mostrarte algunos programas simples que utilizan listas.
#El primero de ellos intenta encontrar el mayor valor en la lista. Mira el código en el editor.
#El concepto es bastante simple: asumimos temporalmente que el primer elemento es el más grande y comparamos la hipótesis 
#con todos los elementos restantes de la lista.
#El código da como resultado el17(como se espera).

miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0] #FORMA LARGA

for i in range(1, len(miLista)):
   if miLista[i]> mayor:
        mayor = miLista[i]

print(mayor)


print("----3----") #Mejor forma de hacerlo

#El código puede ser reescrito para hacer uso de la forma recién introducida del ciclo for:

miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista:
    if i > mayor:
        mayor = i

print(mayor)


print("-----4------")


#El programa anterior realiza una comparación innecesaria, cuando el primer elemento se compara consigo mismo, 
#pero esto no es un problema en absoluto.
#El código da como resultado el 17 también (nada inusual).
#Si necesitas ahorrar energía de la computadora, puedes usar una rodaja:

miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista [1:]:
   if i > mayor:
        mayor = i

print(mayor)




print("--------5----------")

#Ahora encontremos la ubicación de un elemento dado dentro de una lista:

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

#Nota:
#El valor buscado se almacena en la variable Encontrar.
#El estado actual de la búsqueda se almacena en la variable Encontrado (True/False).
#Cuando Encontrado se convierte en True, se sale del bucle for.


print("---------6-----------")
#Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.
#Los números que han salido sorteados son: 5, 11, 9, 42, 3, 49.
#La pregunta es: ¿A cuántos números le has atinado?
#El programa te dará la respuesta:

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados: #Cada vez que dé True, se suma
        aciertos += 1

print(aciertos)

#Nota:

#La lista sorteados almacena todos los números ganadores.
#La lista de seleccionados almacena con números con que se juega.
#La variable aciertos cuenta tus aciertos.
#La salida del programa es: 4.

#Or:
print("--------7-----------")
sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in sorteados:
    if numeros in seleccionados: #Cada vez que dé True, se suma
        aciertos += 1

print(aciertos)



