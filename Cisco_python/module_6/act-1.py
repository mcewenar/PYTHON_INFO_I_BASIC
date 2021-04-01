#Escenario
#Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos saber con qué frecuencia aparece cada letra en el texto. 
#Tal análisis puede ser útil en criptografía, por lo que queremos poder hacerlo en referencia al alfabeto latino.

#Tu tarea es escribir un programa que:

#Pida al usuario el nombre del archivo de entrada.
#Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan como iguales).
#Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).
#Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.

#Suponiendo que el archivo de prueba contiene solo una línea con:

#aBc

#el resultado esperado debería verse de la siguiente manera:
#a -> 1
#b -> 1
#c -> 1

#Tip:

#Creemos que un diccionario es un medio perfecto de recopilación de datos para almacenar los recuentos. 
#Las letras pueden ser las claves mientras que los contadores pueden ser los valores.