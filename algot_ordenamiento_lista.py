#Con base en el planteamiento anterior,
#diseñe un algoritmo de ordenamiento (burbuja)

lista = [54,26,93,17,77,31,44,55,20]
numPasada=len(lista)-1
#for numPasada in range(len(lista)-1,0,-1):
for i in range(numPasada):
    if lista[i]>lista[i+1]:
        temp = lista[i]
        lista[i+1]=temp 
    print(lista)
print("{0} - ok".format(lista))



#O TAMBIÉN (distintas formas):


#miLista = [8, 10, 6, 2, 4] # lista para ordenar

#for i in range(len(miLista) - 1): # necesitamos (5 - 1) comparaciones
#    if miLista[i] > miLista[i + 1]: # compara elementos adyacentes
#        miLista[i], miLista [i + 1] = miLista[i + 1], miLista[i] # si terminamos aquí significa que tenemos que intercambiar los elementos.



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




#FORMA INTERACTIVA


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





#NOTA:
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





