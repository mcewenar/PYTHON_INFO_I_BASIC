#IMPORTANTE




#La vida al interior de las listas
#Ahora queremos mostrarte una característica importante y muy sorprendente de las listas, que las distingue de las variables ordinarias.

#Queremos que lo memorices, ya que puede afectar tus programas futuros y causar graves problemas si se olvida o se pasa por alto.

#Echa un vistazo al fragmento en el editor.

#El programa:

#Crea una lista de un elemento llamada lista1.
#La asigna a una nueva lista llamada lista2.
#Cambia el único elemento de lista1.
#Imprime la lista2.
#La parte sorprendente es el hecho de que el programa mostrará como resultado: [2], no [1], que parece ser la solución obvia.


#Las listas (y muchas otras entidades complejas de Python) se almacenan de diferentes maneras que las variables ordinarias (escalares).

#Se podría decir que:

#El nombre de una variable ordinaria es el nombre de su contenido.
#El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.
#Lee estas dos líneas una vez más, la diferencia es esencial para comprender de que vamos a hablar a continuación.

#La asignación: lista2 = lista1copia el nombre de la matriz, no su contenido. En efecto, los dos nombres (lista1 y lista2) 
#identifican la misma ubicación en la memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa.

#¿Cómo te las arreglas con eso?

lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)

print("---------------------------------------")
#FORMA DE EVITAR ESTO:
#Rodajas Poderosas
#Afortunadamente, la solución está al alcance de su mano: su nombre es rodaja.

#Una rodaja es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.

#En realidad, copia el contenido de la lista, no el nombre de la lista.

#Esto es exactamente lo que necesitas. Echa un vistazo al fragmento de código a continuación:

lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

#Su salida es [1].

#Esta parte no visible del código descrito como [:] puede producir una lista completamente nueva.

#Una de las formas más generales de la rodaja es la siguiente:

#miLista[inicio:fin]

#Como puedes ver, se asemeja a la indexación, pero los dos puntos en el interior hacen una gran diferencia.

#Una rodaja de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen: los elementos de los índices 
#desde el principio hasta el fin-1.

#Nota: no hasta el fin, sino hasta fin-1. Un elemento con un índice igual a fin es el primer elemento el cual no participa en la segmentación.

#Es posible utilizar valores negativos tanto para el inicio como para el fin(al igual que en la indexación).

#Echa un vistazo al fragmento:

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:3]
print(nuevaLista)

#La lista nuevaLista contendrá inicio-fin (3-1=2) elementos, los que tienen índices iguales a 1 y 2 (pero no 3)

#La salida del fragmento es: [8, 6]


# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)


#Usando : dentro de la indexación de una lista a la que se le asigna a otra, es que se puede compiar listas. IMPORTANTE







#RODAJAS CON ÍNDICES NEGATIVOS:

#Observa el fragmento de código a continuación:

#miLista[inicio:fin]

#Para repetir:

#inicio es el índice del primer elemento incluido en la rodaja.
#fin es el índice del primer elemento no incluido en la rodaja.


#Así es como los índices negativos funcionan con la rodaja:
print("----------2------------")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:-1]
print(nuevaLista) #[8,6,4]

#Si elinicio especifica un elemento que se encuentra más allá del descrito por fin (desde el punto de vista inicial de la lista), 
#la rodaja estará vacía:

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [-1:1]
print(nuevaLista)

#La salida del fragmento es: [].



#Si omites inicio en tu rodaja, se supone que deseas obtener un segmento que comienza en el elemento con índice 0.

#En otras palabras, la rodaja sería de esta forma:

#miLista[:fin]
#Es un equivalente más compacto:
#miLista[0:fin]

#Observa el fragmento de código a continuación:
print("--------------3--------------")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [:3]
print(nuevaLista)

#Es por esto que su salida es: [10, 8, 6].

#Del mismo modo, si omites el fin en tu rodaja, se supone que deseas que el segmento termine en el elemento con el índice len(miLista).

#En otras palabras, la rodaja sería de esta forma:

#miLista[inicio:]

#Es un equivalente más compacto:

#miLista[inicio:len(miLista)]

#Observa el siguiente fragmento de código:
print("----------4-----------")
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[3:]
print(nuevaLista)

#Por lo tanto, la salida es: [4, 2].




#RODAJAS CONTINUACIÓN:
#Como hemos dicho antes, el omitir inicio y fin hace una copia de toda la lista:
print("--------5--------")
miLista = [10, 8, 6, 4, 2]
nuevLista = miLista[:] 
print(nuevLista)

#El resultado del fragmento es: [10, 8, 6, 4, 2]



#TAMBIÉN SE PUEDEN ELMINAR RODAJAS CON DEL:
#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez, también puede eliminar rodajas:
print("---------6-----------")
miLista = [10, 8, 6, 4, 2]
del miLista[1:3] 
print(miLista)
#Nota: En este caso, la rodaja ¡no produce ninguna lista nueva!
#La salida del fragmento es:[10, 4, 2].
print("---------7----------")
#También es posible eliminar todos los elementos a la vez:

miLista = [10, 8, 6, 4, 2]
del miLista[:] 
print(miLista)

#La lista se queda vacía y la salida es: []



print("-----------8----------------")

#Al eliminar la rodaja del código, su significado cambia dramáticamente.

#Echa un vistazo:

miLista = [10, 8, 6, 4, 2]
del miLista
print(miLista) #Aparece subraya porque el intérprete ya detectó que se va a borrar

#La instrucción del eliminará la lista, no su contenido.
#La función print() de la última línea del código provocará un error de ejecución.