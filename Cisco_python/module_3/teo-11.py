#AND (Y)
#Un operador de conjunción lógica en Python es la palabra y. Es un operador binario con una prioridad inferior a 
# la expresada por los operadores de comparación.
#Nos permite codificar condiciones complejas sin el uso de paréntesis como este:
#contador > 0 and valor == 100 

#El resultado proporcionado por el operador and se puede determinar
#sobre la base de la tabla de verdad.

#Si consideramos la conjunción de A and B,
#el conjunto de valores posibles de argumentos y los valores correspondientes 
#de conjunción se ve de la siguiente manera:


#Argumento A 	Argumento B 	A y B 
#False	         False	        False
#False	         True	        False
#True	         False	        False
#True	         True	        True

#OR (O)

#or
#Un operador de disyunción es la palabra or. Es un operador binario con una prioridad más baja que and 
#(al igual que + en comparación con *). Su tabla de verdad es la siguiente:

#Argumento A 	Argumento B 	A or B 
#False	           False	    False
#False	           True	        True
#True	           False	    True
#True	           True	        True



#NOT 
#not
#Además, hay otro operador que se puede aplicar para condiciones de construcción.
#Es un operador unario que realiza una negación lógica. Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad.

#Este operador se escribe como la palabra not, y su prioridad es muy alta: igual que el unario + y -.
#Su tabla de verdad es simple:

#Argumento	not(Argumento)
#False	    True
#True	    False


#IMPORTANTEEEEEEEEEEEEEEEEEEEE

#Puedes estar familiarizado con las leyes de De Morgan. Dicen que:
#La negación de una conjunción es la separación(disyunción) de las negaciones.
#La negación de una disyunción es la conjunción de las negaciones.


#Escribamos lo mismo usando Python:

#not(p and q) == (not p) or (not q) 
#not(p or q) == (not p) and (not q)

#Deberíamos agregar que ninguno de estos operadores de dos argumentos se puede usar en la forma 
#abreviada conocida como op=. Vale la pena recordar esta excepción.


#Valores lógicos vs. bits individuales
#Los operadores lógicos toman sus argumentos como un todo, independientemente de cuántos bits contengan.
#Los operadores solo conocen el valor: cero (cuando todos los bits se restablecen) significa False; no cero 
#(cuando se establece al menos un bit) significa True.

#El resultado de sus operaciones es uno de estos valores: False o True. 
#Esto significa que este fragmento de código asignará el valor True a la variable j si i no es cero; de lo contrario, 
#será False.

i = 1
j = not not i

