#En contraste con el operador aritmético,
#el operador de concatenación no es conmutativo, por ejemplo, "ab" + "ba" no es lo mismo que "ba" + "ab".
#Contatenador != sumador.
#Para concatenar, ambos términos tienen que ser strings

nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

#Replicación
#El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena)
# se convierte en un operador de replicación.

#cadena * número
#número * cadena

#Replica la cadena el numero de veces indicado por el número.

#Por ejemplo:

#"James" * 3 nos da "JamesJamesJames".
#3 * "an" nos da "ananan".
#5 * "2" (o "2" * 5) da como resultado "22222" (no 10).

#Un número menor o igual que cero produce una cadena vacía.


#Este sencillo programa "dibuja" un rectángulo, haciendo uso del operador (+), pero en un nuevo rol:

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Nota como se ha utilizado el paréntesis en la segunda línea de código.