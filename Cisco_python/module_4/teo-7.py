#Efectos y resultados: listas y funciones

#Hay dos preguntas adicionales que deben responderse aquí.

#El primero es: ¿Se puede enviar una lista a una función como un argumento?


#¡Por supuesto que se puede! Cualquier entidad reconocible por Python puede desempeñar el papel de un argumento de función,
#aunque debes asegurarte de que la función sea capaz de hacer uso de él.

#Entonces, si pasas una lista a una función, la función tiene que manejarla como una lista.

#Una función como la siguiente:

def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum

#y se invoca así:

print(sumaDeLista([5, 4, 3])) 

#Regresará 12 como resultado, pero habrá problemas si la invocas de esta manera riesgosa:

#print(sumaDeLista(5)) TypeError: 'int' object is not iterable

#La respuesta de Python será la siguiente:
#TypeError: 'int' object is not iterable 

#Esto se debe al hecho de que el bucle for no puede iterar un solo valor entero.



#Efectos y resultados: listas y funciones - continuación
#La segunda pregunta es: ¿Puede una lista ser el resultado de una función?

#¡Si, por supuesto! Cualquier entidad reconocible por Python puede ser un resultado de función.

print("------2-------")
def strangeListFunction(n,m):
    strangeList = []
    
    for i in range(0, n):
       d = strangeList.insert(0, i) #Con el insert se hace regresivo a diferencia del append.
    
    for i in range(0, m):
      c = strangeList.append(i+1) #Aumenta

    return strangeList

print(strangeListFunction(5,4))

print("-----3-----")

def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))

#Observa el código en el editor. La salida del programa será así:
#SALIDA: [4, 3, 2, 1, 0] 

#Ahora puedes escribir funciones con y sin resultados.

#Vamos a profundizar un poco más en los problemas relacionados con las variables en las funciones. 
# Esto es esencial para crear funciones efectivas y seguras.



