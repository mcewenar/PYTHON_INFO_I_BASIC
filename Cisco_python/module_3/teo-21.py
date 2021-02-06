#1. Si tienes una lista l1, la siguiente asignación: l2 = l1 no hace una copia de la lista l1, 
#pero hace que las variables l1 y l2 apunten a la misma lista en la memoria . Por ejemplo:

vehiculosUno = ['carro', 'bicicleta', 'moto']
print(vehiculosUno) # salida: ['carro', 'bicicleta', 'moto']

vehiculosDos = vehiculosUno
del vehiculosUno[0] # borra 'carro'
print(vehiculosDos) # salida: ['bicicleta', 'moto']
#COMPARTEN LA MISMA MEMORIA, PERO DIFERENTE NOMBRE



#2. Si deseas copiar una lista o parte de la lista, puede hacerlo haciendo uso de rodajas(slicing):

colores = ['rojo', 'verde', 'naranja']

copiaTodosColores = colores[:] # copia la lista completa
copiaParteColores = colores[0:2] # copia parte de la lista


#3. También puede utilizar índices negativos para hacer uso de rodajas. Por ejemplo:

listaMuestra = ["A", "B", "C", "D", "E"]
nuevaLista = listaMuestra[2:-1]
print(nuevaLista) # salida: ['C', 'D']


#4. Los parámetros inicio y finson opcionales al partir en rodajas una lista: lista[inicio:fin], por ejemplo:

miLista = [1, 2, 3, 4, 5]
rodajaUno = miLista [2:]
rodajaDos = miLista [:2]
rodajaTres = miLista [-2:]

print(rodajaUno) # salidas: [3, 4, 5]
print(rodajaDos) # salidas: [1, 2]
print(rodajaTres) # salidas: [4, 5]

#5. Puedes eliminar rodajas utilizando la instrucción del:

miLista = [1, 2, 3, 4, 5]
del miLista [0:2]
print(miLista) # salida: [3, 4, 5]

del miLista[:]
print(miLista) # elimina el contenido de la lista, genera: []

print("-------------------")
#6. Puedes probar si algunos elementos existen en una lista o no utilizando las palabras clave in y not in, por ejemplo:

miLista = ["A", "B", 1, 2]

print("A" in miLista) # salida: True
print("D" not in miLista) # salida: True
print("C" in miLista) # salida: False
print(2 not in miLista) # salidas: False



l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[0]

print(l3) #["C"] porque todas las listas comparten el mismo espacio de memoria. Se comporta diferente a una variable corriente


print("-------3----------")
#¿Cuál es la salida del siguiente fragmento de código?

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2
#print(l2)
print(l3)


l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[:]

print(l3)




l1 = ["A", "B", "C"]
l2 = l1[:]
l3 = l2[:]

del l1[0]
del l2[0] #Elimina las copias

print(l3) 


#Inserte in o not in en lugar de ??? para que el código genere el resultado esperado.

miLista = [1, 2, "in", True, "ABC"]

print(1 in miLista) # salida True
print("A" not in miLista) # salida True
print(3 not in miLista) # salida True
print(False in miLista) # salida False