#True (cuando su valor no sea cero) y False (cuando sea igual a cero). # != 0: TRUE, #==0 FALSE

#1. No debes usar else sin un if precedente.
#2. Else siempre es la última rama de la cascada , independientemente de si has usado elif o no.
#3. Else es una parte opcional de la cascada, y puede omitirse.
#4. Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas.
#5. Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.

#Nota: si alguna de las ramas de if-elif-else contiene una sola instrucción, puedes codificarla de forma más completa (no es necesario que aparezca una línea con sangría después de la palabra clave),
#pero solo continúa la línea después de los dos puntos).
#Sin embargo, este estilo puede ser engañoso,
#y no lo vamos a usar en nuestros programas futuros, pero definitivamente 
#vale la pena saber si quieres leer y entender los programas de otra persona.
#No hay otras diferencias en el código.
numero1,numero2=1,2

if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

print(numero1,numero2)
print(type(numero1))



