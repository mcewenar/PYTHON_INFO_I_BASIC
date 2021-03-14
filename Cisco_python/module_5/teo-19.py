#El método isalnum()
#El método sin parámetros llamado isalnum() comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) 
#y devuelve True (verdadero) o False (falso) de acuerdo al resultado.

#Observa el ejemplo en el editor y ejecútalo.
# Demostración del método the isalnum()
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#Nota: cualquier elemento de cadena que no sea un dígito o una letra hace que el método regrese False (falso). 
#Una cadena vacía también lo hace.

#El resultado de ejemplo es:

#True
#True
#True
#False
#False
#False
print("jeje")
#Hay tres más ejemplos aquí:

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ' #Sigue siendo alfabeto
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#Ejecútalos y verifica su salida.
#False
#True
#True
#Nota: la causa del primer resultado es un espacio, no es ni un dígito ni una letra.


print("--2--")

#El método isalpha()
#El método isalpha() es más especializado, se interesa en letras solamente.

#Observa el Ejemplo 1, su salida es:
# Ejemplo 1: Demostración del método isapha()
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit()
    
print('2018'.isdigit())
print("Año2019".isdigit())

#True
#False

#El método isdigit()
#Al contrario, el método isdigit() busca sólo dígitos - cualquier otra cosa produce False (falso) como resultado.

#Observa el Ejemplo 2, su salida es:

#True
#False

#Realiza más experimentos.

print("--3--")

#El método islower()
#El método islower() es una variante de isalpha() - solo acepta letras minúsculas.

#Observa el Ejemplo 1 en el editor, genera:

#False
#True


#El método isspace()
#El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro caracter (el resultado es entonces False).

#Observa el Ejemplo 2 en el editor, genera:

#True
#True
#False


#El método isupper()
#El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.

#De nuevo, observa el Ejemplo 3 en el editor, genera:

#False
#False
#True

print("--3--")

#El método islower()
#El método islower() es una variante de isalpha() - solo acepta letras minúsculas.

#Observa el Ejemplo 1 en el editor, genera:

# Ejemplo 1: Demostración del método islower()
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper() 
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

#False
#True


#El método isspace()
#El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro caracter (el resultado es entonces False).

#Observa el Ejemplo 2 en el editor, genera:
# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

#True
#True
#False


#El método isupper()
#El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.

#De nuevo, observa el Ejemplo 3 en el editor, genera:
# Ejemplo 3: Demostración del método isupper() 
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
#False
#False
#True

print("--4--")

#El método join()
#El método join() es algo complicado, así que déjanos guiarte paso a paso:

#Como su nombre lo indica, el método realiza una unión y espera un argumento del tipo lista; 
#se debe asegurar que todos los elementos de la lista sean cadenas: de lo contrario, el método generará una excepción TypeError.
#Todos los elementos de la lista serán unidos en una sola cadena pero...
#...la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
#La cadena recién creada se devuelve como resultado.
#Echa un vistazo al ejemplo en el editor. Vamos a analizarlo:
# Demostración del método join()
print(",".join(["omicron", "pi", "rho"]))

#El método join() se invoca desde una cadena que contiene una coma (la cadena puede ser larga o puede estar vacía).
#El argumento del join es una lista que contiene tres cadenas.
#El método devuelve una nueva cadena.
#Aquí está:

#omicron,pi,rh

#El método lower()
#El método lower() genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas, 
#y devuelve la cadena como resultado. Nuevamente, la cadena original permanece intacta.

#Si la cadena no contiene caracteres en mayúscula, el método devuelve la cadena original.

#Nota: El método lower() no toma ningún parámetro.
# Demostración del método lower()
print("SiGmA=60".lower())

#La salida del ejemplo del editor es:

#sigma=60

#Como ya sabes, realiza tus propios experimentos.
print("---5---")
#El método lstrip()
#El método sin parámetros lstrip() devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios 
#en blanco iniciales.

#Analiza el ejemplo en el editor.
# Demostración del método the lstrip()
print("[" + " tau ".lstrip() + "]")

#Los corchetes no son parte del resultado, solo muestran los límites del resultado.

#Las salida del ejemplo es:

#[tau ]


#El método con un parámetro lstrip() hace lo mismo que su versión sin parámetros, pero elimina todos los caracteres incluidos 
#en el argumento (una cadena), no solo espacios en blanco:

print("www.cisco.com".lstrip("w."))

#Aquí no se necesitan corchetes, ya que el resultado es el siguiente:

#cisco.com

#¿Puedes adivinar la salida del fragmento a continuación? Piensa cuidadosamente. Ejecuta el código y verifica tus predicciones.

print("pythoninstitute.org".lstrip(".org"))
#SALIDA:
#pythoninstitute
#¿Sorprendido? Nuevamente, experimenta con tus propios ejemplos.



