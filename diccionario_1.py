pares = { 1: "manzana",
"naranja": [2,3,4],
None: "True"
}
print (pares.get("naranja"))
print (pares.get(7))
print (pares.get(12345,"No está en el diccionario")) #Opcional, para mostrar un mensaje si no se encuentra la clave en el diccionario




#2
fib = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8}
print (fib.get(4,"Hello, this is optional") + fib.get(7,5)) #Si la clave del diccionario se encuentra, este no oasigna el valor opcional
#Por eso da 8