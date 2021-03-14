#El método replace()

#IMPORTANTE:
#El método replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer 

#argumento han sido reemplazadas por el segundo argumento.

#Analiza el código en el editor y ejecútalo.
# Demostración del método replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

#Para eliminar cadenas:
#El segundo argumento puede ser una cadena vacía (lo que hace es eliminar en lugar de reemplazar), 
#pero el primer argumento no puede estar vacío.

#La salida del ejemplo es:
#www.pyhoninstitute.org
#Thare are it!
#Apple


#La variante del métdodo replace() con tres parámetros emplea un tercer argumento (un número) para limitar el número de reemplazos.

#Observa el código modificado a continuación:

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

#¿Puedes adivinar su salida? Ejecuta el código y verifica tus conjeturas.
#Salida:
#Thare are it!
#Thare is it!

print("---3---")

#El método rfind()
#Los métodos de uno, dos y tres parámetros denominados rfind() hacen casi lo mismo que sus contrapartes 
#(las que carecen del prefijo r), pero comienzan sus búsquedas desde el final de la cadena, no el principio (de ahí el prefijo r, de reversa).

#Echa un vistazo al código en el editor e intenta predecir su salida. Ejecuta el código para verificar si tenías razón.

# Demostración del método rfind()
print("tau tau tau".rfind("ta")) #De derecha a izquierda
print("tau tau tau".rfind("ta", 9)) #No encontrado
print("tau tau tau".rfind("ta", 3, 9))

#Salida:
#8
#-1
#4

print("---4---")
#El método rstrip()
#Dos variantes del método rstrip() (remueve espacio derecho) hacen casi lo mismo que el método lstrip (remueve espacio izquierdo), 
# pero afecta el lado opuesto de la cadena.

#Mira el ejemplo en el editor. ¿Puedes adivinar su salida? Ejecuta el código para verificar tus conjeturas.
# Demostración del método rstrip()
print("[" + " upsilon ".rstrip() + "]") #se remueven los espacios de la derecha
print("cisco.com".rstrip(".com")) #Remueve .com, quedando sólo cis
print("cisco.com".lstrip(".com"))
print("cisco.com".strip(".com"))

#Como de costumbre, te recomendamos experimentar con tus propios ejemplos.
#[ upsilon]
#cis
#isco.com
#is

print("----5----")
#El método split()
#El método split() divide la cadena y crea una lista de todas las subcadenas detectadas.

#El método asume que las subcadenas están delimitadas por espacios en blanco - los espacios no participan en la operación 
#y no se copian en la lista resultante.

#Si la cadena está vacía, la lista resultante también está vacía.

#Observa el código en el editor. El ejemplo produce el siguiente resultado:
# Demostración del método split()
print("phi       chi\npsi".split())

#['phi', 'chi', 'psi']

#Nota: la operación inversa se puede realizar por el método join().

print("----6----")

#El método startswith()
#El método startswith() es un espejo del método endswith() - comprueba si una cadena dada comienza con la subcadena especificada.

#Mira el ejemplo en el editor. Este es el resultado:
# Demostración del método startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

#False
#True

#El método strip()
#El método strip() combina los efectos causados por rstrip() y lstrip() - 
#crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.

#Observa el segundo ejemplo en el editor. Este es el resultado que devuelve:
# Demostración del método strip() 
print("[" + "   aleph   ".strip() + "]")

#[aleph]

#Ahora realiza tus propios experimentos con los dos métodos.