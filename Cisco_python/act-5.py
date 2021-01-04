"""Es claro que la separación hace que sea más fácil de leer, especialmente cuando el número tiene demasiados dígitos. Sin embargo, Python no acepta estas cosas. Esta prohibido. ¿Qué es lo que 
Python permite? El uso de guion bajo en los literales numéricos.*
Por lo tanto, el número se puede escribir ya sea así: 11111111, o como sigue: 11_111_111.
NOTA   *Python 3.6 ha introducido el guion bajo en los literales numéricos, permitiendo colocar un 
guion bajo entre dígitos y después de especificadores de base para mejorar la legibilidad. Esta característica no está disponible en versiones anteriores de Python.
¿Cómo se codifican los números negativos en Python? Como normalmente se hace, agregando un signo de menos. Se puede escribir: -11111111, o -11_111_111.
Los números positivos no requieren un signo positivo antepuesto, pero es permitido, si se desea hacer. Las siguientes líneas describen el mismo número: +11111111 y 11111111."""


11111111
11_111_111
-11111111
-11_111_111
+11_111_111 #All allowed


"""Enteros: números octales y hexadecimales
Existen dos convenciones adicionales en Python que no son conocidas en el mundo de las matemáticas. 
El primero nos permite utilizar un número en su representación octal.
Si un numero entero esta precedido por un código 0O o 0o (cero-o), el numero será tratado como un valor octal. 
Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.
0o123 es un número octal con un valor (decimal) igual a 83.
La función print() realiza la conversión automáticamente. Intenta esto:

print(0o123)

La segunda convención nos permite utilizar números en hexadecimal. 
Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x).
0x123 es un número hexadecimal con un valor (decimal) igual a 291. 
La función print() puede manejar estos valores también. Intenta esto:
print(0x123)"""

print(0o123)
print(0x123)
print("\n")
print(0.4==.4 and 4.0 == 4.) #True
print(3E8==300000000) #True. E ó e == Exponente
print(6.62607E-34==0.000000000000000000000000000000000000662607)
print(0.0000000000000000000001)
print("Me gusta \"Monty Python\"") #o
print("Me gusta 'Monty Python'")
print('Me gusta "Monty Python"')
print('I\'m Monty Python.')
print("I'm Monty Python")

print("\n")

#Verdadero y Falso, denotados como 1 y 0. BOOLEANOS
print(True > False) #1>0 == True
print(True < False) #0<1 == False

