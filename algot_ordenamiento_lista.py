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
