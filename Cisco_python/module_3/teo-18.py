#Ordenamiento Burbuja (IMPORTANTE)
#Ahora que puedes hacer malabarismos con los elementos de las listas, 
#es hora de aprender como ordenarlos. Se han inventado muchos algoritmos de clasificación, 
#que difieren mucho en velocidad, así como en complejidad. Vamos a mostrar un algoritmo muy simple, 
#fácil de entender, pero desafortunadamente, tampoco es muy eficiente. Se usa muy raramente, y ciertamente 
#no para listas extensas.

#Digamos que una lista se puede ordenar de dos maneras:

#Ascendente (o más precisamente, no descendente): si en cada par de elementos adyacentes, 
#el primer elemento no es mayor que el segundo.
#Descendente (o más precisamente, no ascendente): si en cada par de elementos adyacentes, 
#el primer elemento no es menor que el segundo.
#En las siguientes secciones, ordenaremos la lista en orden ascendente, de modo que los números se ordenen 
#de menor a mayor.


#Aquí está la lista:
[8,10],6,2,4

#1. Intentaremos utilizar el siguiente enfoque: tomaremos el primer y el segundo elemento y los compararemos; 
#si determinamos que están en el orden incorrecto (es decir, el primero es mayor que el segundo), los intercambiaremos; 
#Si su orden es válido, no haremos nada. 
#Un vistazo a nuestra lista confirma lo último: los elementos 01 y 02 están en el orden correcto, así como 8<10.

#2. Ahora observa el segundo y el tercer elemento. Están en las posiciones equivocadas. Tenemos que intercambiarlos:
8,[6,10],2,4
#.
#.
#.
#Observa - El 10 está en la parte superior. Podríamos decir que flotó desde el fondo hasta la superficie, 
#al igual que las burbujas en una copa de champán.
#El método de clasificación deriva su nombre de la misma observación: se denomina ordenamiento de burbuja.




#ALGORITMO DE BURBUJA PARA ORDENAR UNA LISTA:

#Ordenando una lista
#¿Cuántos pases necesitamos para ordenar la lista completa?

#Resolvamos este problema de la siguiente manera: introducimos otra variable, 
#su tarea es observar si se ha realizado algún intercambio durante el pase o no. Si no hay intercambio, 
#entonces la lista ya está ordenada, y no hay que hacer nada más. Creamos una variable llamada swapped, 
#y le asignamos un valor de False para indicar que no hay intercambios. De lo contrario, se le asignará True.
miLista = [8, 10, 6, 2, 4] # lista para ordenar

for i in range(len(miLista) - 1): # necesitamos (5 - 1) comparaciones
    if miLista[i] > miLista[i + 1]: # compara elementos adyacentes
        miLista[i], miLista [i + 1] = miLista[i + 1], miLista[i] # si terminamos aquí significa que tenemos que intercambiar los elementos.



print("------------")

miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)




print("-------2--------")
#Forma interactiva
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)




#Python, sin embargo, tiene sus propios mecanismos de clasificación. Nadie necesita escribir sus propias clases, 
# ya que hay un número suficiente de herramientas listas para usar.

#Te explicamos este sistema de clasificación porque es importante aprender como procesar los contenidos de una lista y mostrarte 
# como puede funcionar la clasificación real.

#Si quieres que Python ordene tu lista, puedes hacerlo de la siguiente manera:

miLista = [8, 10, 6, 2, 4]
miLista.sort() 
print(miLista) 

#Como puedes ver, todas las listas tienen un método denominado sort(), que las ordena lo más rápido posible. 
#Ya has aprendido acerca de algunos de los métodos de lista anteriormente, y pronto aprenderás más sobre otros.


#2.También hay un método de lista llamado reverse(), que puedes usar para invertir la lista, por ejemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
    
lst.reverse()
print (lst) # salida: [4, 2, 1, 3, 5]



#¿Cuál es la salida del siguiente fragmento de código?

lst = ["D", "F", "A", "Z"]
lst.sort ()

print(lst)


#¿Cuál es la salida del siguiente fragmento de código?

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort ()

print(lst)


#¿Cuál es la salida del siguiente fragmento de código?

a = "A"
b = "B"
c = "C"
d = ""

lst = [a, b, c, d]
lst.reverse ()

print(lst)