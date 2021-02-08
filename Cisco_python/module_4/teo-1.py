#Un buen desarrollador divide el código (o mejor dicho: el problema) en piezas aisladas, y codifica cada una de ellas 
#en la forma de una función.

#Esto simplifica considerablemente el trabajo del programa, debido a que cada pieza se codifica por separado y 
#consecuentemente se prueba por separado. A este proceso se le llama comúnmente descomposición.


#Existe una segunda condición: si un fragmento de código se hace tan extenso que leerlo o entenderlo se hace complicado, 
#considera dividirlo pequeños problemas por separado e implementa cada uno de ellos como una función independiente.

#Esta descomposición continua hasta que se obtiene un conjunto de funciones cortas, fáciles de comprender y probar.

li = [0,1,2,3]
x=1
for elem in li:
    x *= elem 
print(x)

#Descomposición
#Es muy común que un programa sea tan largo y complejo que no puede ser asignado a un solo desarrollador, 
#y en su lugar un equipo de desarrolladores trabajarán en el. El problema, debe ser dividido entre varios desarrolladores 
#de una manera en que se pueda asegurar su eficiencia y cooperación.
#Es inconcebible que más de un programador deba escribir el mismo código al mismo tiempo, por lo tanto, 
#el trabajo debe de ser dividido entre todos los miembros del equipo.

#Este tipo de descomposición tiene diferentes propósitos, no solo se trata de compartir el trabajo, 
#sino también de compartir la responsabilidad entre varios desarrolladores.

#Cada uno debe escribir un conjunto bien definido y claro de funciones, las cuales al ser 
#combinadas dentro de un módulo (esto se clarificara un poco mas adelante) nos dará como resultado el producto final.

#Esto nos lleva directamente a la tercera condición: si se va a dividir el trabajo entre varios programadores, 
#se debe descomponer el problema para permitir que el producto 
#sea implementado como un conjunto de funciones escritas por separado empacadas juntas en diferentes módulos.

#¿De dónde provienen las funciones?
#En general, las funciones provienen de al menos tres lugares:

#De Python mismo: varias funciones (como print()) son una parte integral de Python, y siempre están disponibles sin algún esfuerzo 
#adicional del programador; se les llama a estas funciones funciones integradas.
#De los módulos preinstalados de Python: muchas de las funciones, las cuales comúnmente son menos utilizadas que las integradas, 

#Existe una posibilidad más, pero se relaciona con clases, se omitirá por ahora.