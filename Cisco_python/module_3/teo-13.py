
#¿Cómo cambias el valor de un elemento elegido en la lista?

#Vamos a asignar un nuevo valor de 111 al primer elemento en la lista. Lo hacemos de esta manera:

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprime el contenido de la lista original

numeros[0] = 111 
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.



print("-----------------------------")

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original.

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.



#El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice,
#mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.

#Vamos a utilizar la función print() para imprimir el contenido de la lista cada vez que realicemos los cambios.
#Esto nos ayudará a seguir cada paso con más cuidado y ver que sucede después de una modificación de la lista en particular.

#Nota: todos los índices utilizados hasta ahora son literales. Sus valores se fijan en el tiempo de ejecución,
#pero cualquier expresión también puede ser un índice. Esto abre muchas posibilidades.

print(numeros[0]) # accediendo al primer elemento de la lista.
print(numeros) # imprimiendo la lista completa.

#Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).





#Eliminando elementos de una lista
#Cualquier elemento de la lista puede ser eliminado en cualquier momento, esto se hace con una instrucción llamada del (eliminar).
#Nota: es una instrucción, no una función.

#Tienes que apuntar al elemento que quieres eliminar, desaparecerá de la lista y la longitud de la lista se reducirá en uno.

#Mira el fragmento de abajo. ¿Puedes adivinar qué salida producirá? Ejecuta el programa en el editor y comprueba.

#del numeros[1]
print(len(numeros))
print(numeros) 

#No puedes acceder a un elemento que no existe , no puedes obtener su valor ni asignarle un valor.
#Ambas instrucciones causarán ahora errores de tiempo de ejecución:

print(numeros[4])
numeros[4] = 1 

#Agrega el fragmento de código anterior después de la última línea de código en el editor, ejecute el programa y verifique que sucede.

#Nota: hemos eliminado uno de los elementos de la lista; ahora solo hay cuatro elementos en la lista.
#Esto significa que el elemento número cuatro no existe.




numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros[1] = numeros[4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print ("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista anterior

###

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual