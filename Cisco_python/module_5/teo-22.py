#Comparando cadenas
#Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.

#Eche un vistazo a estos operadores: también pueden comparar cadenas:

#==
#!=
#>
#>=
#<
#<=
#Existe un "pero": los resultados de tales comparaciones a veces pueden ser un poco sorprendentes. 
#No olvides que Python no es consciente (no puede ser de ninguna manera) de problemas lingüísticos sutiles, 
#simplemente compara valores de puntos de código, caracter por caracter. PUNTOS DE CÓDIGO

#Los resultados que obtienen de una operación de este tipo a veces son sorprendentes. Comencemos con los casos más simples.


#Dos cadenas son iguales cuando consisten en los mismos caracteres en el mismo orden. Del mismo modo, 
#dos cadenas no son iguales cuando no consisten en los mismos caracteres en el mismo orden.

#Ambas comparaciones dan True (verdadero) como resultado:

print('alfa' == 'alfa')
print('alfa' != 'Alfa')


#La relación final entre cadenas está determinada por comparar el primer caracter diferente en ambas cadenas 
#(ten en cuenta los puntos de código ASCII / UNICODE en todo momento).

#Cuando se comparan dos cadenas de diferentes longitudes y la más corta es idéntica a la más larga, 
#la cadena más larga se considera mayor.

#Justo como aquí:

print('alfa' < 'alfabeto')

#La relación es True (verdadera).

#La comparación de cadenas siempre distingue entre mayúsculas y minúsculas 
#(las letras mayúsculas se consideran menores en comparación con las minúsculas).

#La expresión es True (verdadera):

print('beta' > 'Beta')


print("---2---")

#Comparando cadenas: continuación
#Aún si una cadena contiene solo dígitos, todavía no es un número. Se interpreta como lo que es, 
#como cualquier otra cadena regular, y su aspecto numérico (potencial) no se toma en cuenta, en ninguna manera.

#Mira los ejemplos:

'10' == '010'
'10' > '010'
'10' > '8'
'20' < '8'
'20' < '80'

#Producen los siguientes resultados:

#alse
#True
#False
#True
#True

#Comparar cadenas contra números generalmente es una mala idea.

#Las únicas comparaciones que puede realizar con impunidad son aquellas simbolizadas por los operadores == y !=. 
#El primero siempre devuelve False, mientras que el segundo siempre devuelve True.

#El uso de cualquiera de los operadores de comparación restantes generará una excepción TypeError.

#Vamos a verlo:

'10' == 10
'10' != 10
'10' == 1
'10' != 1
'10' > 10

#Los resultados en este caso son:

#False
#True
#False
#True
#TypeError exception

#Ejecuta todos los ejemplos y realiza más experimentos.

print("---3---")

#Ordenamiento
#La comparación está estrechamente relacionada con el ordenamiento (o más bien, el ordenamiento es, de hecho, 
#un caso muy sofisticado de comparación).

#Esta es una buena oportunidad para mostrar dos formas posibles de ordenar listas que contienen cadenas. 
#Dicha operación es muy común en el mundo real: cada vez que ves una lista de nombres, productos, títulos o ciudades, 
#esperas que este ordenada.

#Supongamos que deseas ordenar la siguiente lista:

greek = ['omega', 'alfa', 'pi', 'gama']

#En general, Python ofrece dos formas diferentes de ordenar las listas.

#El primero se implementa con una función llamada sorted().

#La función toma un argumento (una lista) y devuelve una nueva lista, con los elementos ordenados del argumento. 
#(Nota: esta descripción está un poco simplificada en comparación con la implementación real; lo discutiremos más adelante).

#La lista original permanece intacta.

#Mira el código en el editor y ejecútalo. El fragmento produce el siguiente resultado:
# Demostración de la función sorted()
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

print()

# Demostración del método sort()
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)

['omega', 'alfa', 'pi', 'gama']
['alfa', 'gama', 'omega', 'pi']


#El segundo método afecta a la lista misma - no se crea una nueva lista. 
#El ordenamiento se realiza por el método denominado sort().

#El resultado no ha cambiado:

['omega', 'alfa', 'pi', 'gama']
['alfa', 'gama', 'omega', 'pi']

#Si necesitas un orden que no sea descendente, debes convencer a la función o método de cambiar su comportamiento predeterminado. 
#Lo discutiremos pronto.

print("---4---")

#Cadenas contra números
#Hay dos cuestiones adicionales que deberían discutirse aquí: cómo convertir un número (un entero o un flotante) en una cadena, 
#y viceversa. Puede ser necesario realizar tal transformación. Además, es una forma rutinaria de procesar datos de entrada o salida.

#La conversión de cadena a número es simple, ya que siempre es posible. Se realiza mediante una función llamada str().

#Justo como aquí:

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

#La salida del código es:

#13 1.3

##La transformación inversa solo es posible cuando la cadena representa un número válido. Si no se cumple la condición, 
#espera una excepción ValueError.

#Emplea la función int() si deseas obtener un entero, y float() si necesitas un valor punto flotante.

#Justo como aquí:

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

#Esto es lo que verás en la consola:

#14.3

#En la siguiente sección, te mostraremos algunos programas simples que procesan cadenas.

#  Prueba el código aquí

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print("---")
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)


