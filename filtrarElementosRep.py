#Interactivo
miLista =  []
ap=int(input("Ingrese el número de elementos que quieras agregar a la lista: "))
for i in range(ap):
    elem=int(input("Ingrese un número: "))
    miLista.append(elem)
#
# coloca tu código aquí
miLista2 = []
for i in miLista:
     if i not in miLista2:
         miLista2.append(i)


print("La lista solo con elementos únicos:")
print(miLista2)


#Con lista definida

#miLista =  [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#miLista2 = []
#for i in miLista:
#     if i not in miLista2:
#         miLista2.append(i)


#print("La lista solo con elementos únicos:")
#print(miLista2)