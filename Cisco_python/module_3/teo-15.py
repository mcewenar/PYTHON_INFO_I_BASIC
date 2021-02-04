#Funciones vs. métodos (IMPORTANTE)
#Un método es un tipo específico de función: se comporta como una función y se parece a una función,
#pero difiere en la forma en que actúa y en su estilo de invocación.

#Una función no pertenece a ningún dato: obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.
#Un método hace todas estas cosas, pero también puede cambiar el estado de una entidad seleccionada.
#Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.


#Esto también significa que invocar un método requiere alguna especificación de los datos a partir de los cuales se invoca el método.
#Puede parecer desconcertante aquí, pero lo trataremos en profundidad cuando profundicemos en la programación orientada a objetos.
#En general, una invocación de función típica puede tener este aspecto:

#resultado =  funcion(argumento)

#La función toma un argumento, hace algo y devuelve un resultado.


#Una invocación de un método típico usualmente se ve así:

#resultado =  data.method(arg)  

#Nota: el nombre del método está precedido por el nombre de los datos que posee el método. A continuación, se agrega un punto,
# seguido del nombre del método y un par de paréntesis que encierran los argumentos.

#El método se comportará como una función, pero puede hacer algo más: puede cambiar el estado interno de los datos a partir de los 
#cuales se ha invocado.



#Puedes preguntar: ¿por qué estamos hablando de métodos, y no de listas?

#Este es un tema esencial en este momento, ya que le mostraremos como agregar nuevos elementos a una lista existente. 
# Esto se puede hacer con métodos propios de las listas, no por funciones.





#MÉTODOS PROPIOS DE LISTAS: (IMPORTANTE) Agregar elementos a una lista: append() e insert()
#Un nuevo elemento puede ser añadido al final de la lista existente:

#lista.append(valor)

#Dicha operación se realiza mediante un método llamado append(). 
#Toma el valor de su argumento y lo coloca al final de la lista que posee el método.


#El método insert() es un poco más inteligente: puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.

#lista.insert(ubicación,valor)  

#Toma dos argumentos:

#El primero muestra la ubicación requerida del elemento a insertar. Nota: todos los elementos existentes que ocupan ubicaciones a 
#la derecha del nuevo elemento (incluido el que está en la posición indicada) se desplazan a la derecha, para hacer espacio para el nuevo 
#elemento.
#El segundo es el elemento a insertar.
#Observa el código en el editor. Ve como usamos los métodos append() e insert(). Presta atención a lo que sucede después de usar insert(): 
#el primer elemento anterior ahora es el segundo, el segundo el tercero, y así sucesivamente.


#Agrega el siguiente fragmento después de la última línea de código en el editor:

#numeros.insert(1,333)

#Imprime el contenido de la lista final en la pantalla y ve que sucede. 
#El fragmento de código sobre el fragmento de código inserta 333 en la lista, por lo que es el segundo elemento.
#El segundo elemento anterior se convierte en el tercero, el tercero en el cuarto, y así sucesivamente.




numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
numeros.insert(1,333) #Se remodifican las posiciones
print(len(numeros))
print(numeros)



print("-----------------2--------------------------")


miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)


print("--------------------3-----------------------")

#Deberías obtener la misma secuencia, pero en orden inverso (este es el mérito de usar el método insert()

miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1) #Empieza con 1. Se asigna 1 a la posición 0, se asigna 2 a la posición 0,...

print(miLista)





print("---------------------4---------------------")
#El bucle for tiene una variante muy especial que puede procesar las listas de manera muy efectiva. Echemos un vistazo a eso.

#Supongamos que desea calcular la suma de todos los valores almacenados en la lista miLista.

#Necesitas una variable cuya suma se almacenará y se le asignará inicialmente un valor de 0 - su nombre es suma. 
#Luego agrega todos los elementos de la lista usando el bucle for. 
#Echa un vistazo al fragmento en el editor.


#El bucle for tiene una variante muy especial que puede procesar las listas de manera muy efectiva. Echemos un vistazo a eso.
#Supongamos que desea calcular la suma de todos los valores almacenados en la lista miLista.
#Necesitas una variable cuya suma se almacenará y se le asignará inicialmente un valor de 0 - su nombre es suma.
#Luego agrega todos los elementos de la lista usando el bucle for. Echa un vistazo al fragmento en el editor.

#FORMA DE SUMAR LOS ELEMENTOS ENTEROS DE UNA LISTA
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)): #El número de elementos: 5
    suma += miLista[i] #ELEMENTO 0 (10)+ ELEMENTO 1 (1) + ELEMENTO 2 (8)...

print(suma)



#FORMA EFICIENTE:
print("---------------5---------------")

miLista = [10, 1, 8, 3, 5]
suma = 0

for i in miLista:
    suma += i

print(suma) 


