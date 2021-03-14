#El método capitalize()
#Veamos algunos métodos estándar de cadenas en Python. Vamos a analizarlos en orden alfabético, 
#cualquier orden tiene tanto desventajas como ventajas, por lo que la elección puede ser aleatoria.

#El método capitalize() hace exactamente lo que dice - crea una nueva cadena con los caracteres tomados de la cadena fuente, 
#pero intenta modificarlos de la siguiente manera:

#IMPORTANTE:
#Si el primer caracter dentro de la cadena es una letra (nota: el primer carácter es el elemento con un índice igual a 0, 
#no es el primer caracter visible), se convertirá a mayúsculas.
#Todas las letras restantes de la cadena se convertirán a minúsculas.
#No olvides que:

#La cadena original (desde la cual se invoca el método) no se cambia de ninguna manera 
#(la inmutabilidad de una cadena debe obedecerse sin reservas).
#La cadena modificada (en mayúscula en este caso) se devuelve como resultado; si no se usa de alguna manera 
#(asígnala a una variable o pásala a una función / método) desaparecerá sin dejar rastro.
#Nota: los métodos no tienen que invocarse solo dentro de las variables. 
#Se pueden invocar directamente desde dentro de literales de cadena. Usaremos esa convención regularmente: 
#simplificará los ejemplos, ya que los aspectos más importantes no desaparecerán entre asignaciones innecesarias.

#Echa un vistazo al ejemplo en el editor. Ejecutalo.
# Demostración del método capitalize()
print('aBcD'.capitalize())
#o
print("o...")
c='aBcD'
print(c.capitalize())

#Esto es lo que imprime:

#Abcd

#Prueba algunos ejemplos más avanzados y prueba su salida:

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize()) #ANALIZAR ESTE
print('123'.capitalize())
print("αβγδ".capitalize())

#Salida:
#Alpha
# alpha
#123
#Αβγδ

print("---2---")

#El método center()

#La variante de un parámetro del método center() genera una copia de la cadena original,
#tratando de centrarla dentro de un campo de un ancho especificado.

#El centrado se realiza realmente al agregar algunos espacios antes y después de la cadena.

#No esperes que este método demuestre habilidades sofisticadas. Es bastante simple.
#string.center(length, character)

#El ejemplo en el editor usa corchetes para mostrar claramente dónde comienza y termina realmente la cadena centrada.
# Demostración del método center()
print('[' + 'alfa'.center(10) + ']')

#Su salida se ve de la siguiente manera:

#[  alfa   ]

#Si la longitud del campo de destino es demasiado pequeña para ajustarse a la cadena, se devuelve la cadena original.

#Puedes ver el método center() en más ejemplos aquí:

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

#Ejecuta el código anterior y verifica qué salidas produce.

#La variante de dos parámetros de center() hace uso del caracter del segundo argumento, en lugar de un espacio. Analiza el siguiente ejemplo:
print('[' + 'gamma'.center(20, '*') + ']')
txt = "banana"
x = txt.center(15, "O")
print(x)

#Es por eso que la salida ahora se ve así:

#[*******gamma********]

#Realiza más experimentos.

print("---3---")

#El método endswith()
#El método endswith() comprueba si la cadena dada termina con el argumento especificado y devuelve True (verdadero) o False (falso), 
#dependiendo del resultado.

#Nota: la subcadena debe adherirse al último carácter de la cadena; no se puede ubicar en algún lugar cerca del final de la cadena.

#Observa el ejemplo en el editor, analizalo y ejecútalo. Produce:
# Demostración del método endswith()
if "epsilon".endswith("on"): #True, por tanto se ejecuta
    print("si")
else:
    print("no")

#si

#Ahora deberías poder predecir la salida del fragmento de código a continuación:

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#Ejecuta el código para verificar tus predicciones.
#Salida:

#True
#False
#False
#True

print("---4---")

#El método find()

#TENER EN CUENTA
#El método find() es similar al método index(), el cual ya conoces - busca una subcadena y devuelve el índice de la primera aparición 
#de esta subcadena, pero:

#Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
#Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.
#Analiza el código en el editor. Así es como puedes usarlo.
# Demostración del método find()
print("Eta".find("ta"))
print("Eta".find("mma"))

#El ejemplo imprime:

#1
#-1

#Nota: no se debe de emplear find() si deseas verificar si un solo carácter aparece dentro de una cadena 
#- el operador in será significativamente más rápido.

#Aquí hay otro ejemplo:

t = 'teta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('te'))
print(t.find('ha'))
#Salida:

#¿Puedes predecir la salida? Ejecútalo y verifica tus predicciones.
#1
#1
#0
#-1

#Si deseas realizar la búsqueda, no desde el principio de la cadena, sino desde cualquier posición,
#puedes usar una variante de dos parámetros del método find(). Mira el ejemplo:

print('kappa'.find('a', 2))

#El segundo argumento especifica el índice en el que se iniciará la búsqueda.

#De las dos letras a, solo se encontrará la segunda. Ejecuta el código y verifica.
#Salida: 4

#Se puede emplear el método find() para buscar todas las ocurrencias de la subcadena, como aquí:

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

#El código imprime los índices de todas las ocurrencias del artículo the, y su salida se ve así:

#15
#80
#198
#221
#238

#Existe también una mutación de tres parámetros del método find() - el tercer argumento apunta al primer índice que no se tendrá 
#en cuenta durante la búsqueda (en realidad es el límite superior de la búsqueda).

#Observa el ejemplo a continuación:

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que caber dentro de la cadena).

#Por lo tanto, las salidas de ejemplo son:

#1
#-1

#a no se puede encontrar dentro de los límites de búsqueda dados en el segundo print().
