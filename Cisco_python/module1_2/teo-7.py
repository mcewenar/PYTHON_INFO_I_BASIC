#Operadores: +, -, *, /, //, %, ** (menor a mayor jerarquía)

"""Recuerda: Es posible formular las siguientes reglas con base en los resultados:

Cuando ambos ** argumentos son enteros, el resultado es entero también.
Cuando al menos un ** argumento es flotante, el resultado también es flotante.
Esta es una distinción importante que se debe recordar."""

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3)


print(6 // 4)
print(6. // 4)

#Esto es muy importante: el redondeo siempre va hacia abajo.
e="Esto es muy importante: el redondeo siempre va hacia abajo."
for i in range(0,15):
    print(e)



print(-6 // 4)
print(6. // -4)

"""Nota: Algunos de los valores son negativos. Esto obviamente afectara el resultado. ¿Pero cómo?

El resultado es un par de dos negativos. El resultado real (no redondeado) es -1.5 en ambo casos.
Sin embargo, los resultados se redondean. 
El redondeo se hace hacia el valor inferior entero, dicho valor es -2, por lo tanto los resultados son: -2 y -2.0."""



a = 6
b = 3
a /= 2 * b
print(a) #2 * b = 6
#a = 6 → 6 / 6 = 1.0