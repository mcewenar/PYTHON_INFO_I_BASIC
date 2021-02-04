#1. La lista es un tipo de dato en Python que se utiliza para almacenar múltiples objetos.
#Es una colección ordenada y mutable de elementos separados por comas entre corchetes, por ejemplo:

miLista = [1, None, True, "Soy una cadena", 256, 0]

#2. Las listas se pueden indexar y actualizar , por ejemplo:

miLista  = [1, 1, None, True, 'Soy una cadena', 256, 0]
print(miLista [3]) # salida: soy una cadena
print(miLista  [-1]) # salida: 0


#3. Las listas pueden estar anidadas, por ejemplo: 

miLista = [1, 'a', ["lista", 64, [0, 1], False]]
print(miLista[2][2][0])


#4. Los elementos de la lista y las listas se pueden eliminar, por ejemplo:

miLista = [1, 2, 3, 4]
del miLista[2]
print(miLista) # salida: [1, 2, 4]

del miLista  # borra toda la lista 


#5.Las listas pueden ser iteradas mediante el uso del bucle for, por ejemplo:

miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in miLista :
    print(color) 

#6.La función len() se puede usar para verificar la longitud de la lista, por ejemplo:

miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(miLista)) # la salidas es 5

del miLista[2]
print (len(miLista)) # la salidas es 4 


#7. Una invocación típica de función tiene el siguiente aspecto: resultado = funcion(argumento),
#mientras que una invocación típica de un método se ve así: resultado = data.method(arg).

print("-----")
lst = [1, 2, 3, 4, 5]
lst2 = []
agregar = 0

for number in lst:
    agregar += number
    lst2.append (agregar)

print(lst2) 



#¿Qué sucede cuando ejecutas el siguiente fragmento de código?

#lst = []
#del lst
#print(lst) (NO EXISTE) 





