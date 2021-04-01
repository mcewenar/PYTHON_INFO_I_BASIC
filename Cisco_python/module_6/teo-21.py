#Procesando archivos de texto: continuación
#El último ejemplo que queremos presentar muestra un rasgo muy interesante del objeto devuelto por la función open() en modo de texto.

#Creemos que puede sorprenderte - el objeto es una instancia de la clase iterable.

#¿Extraño? De ningúna manera. ¿Usable? Si, por supuesto.

#El protocolo de iteración definido para el objeto del archivo es muy simple: su método __next__ solo devuelve la siguiente línea 
#leída del archivo.

#Además, puedes esperar que el objeto invoque automáticamente a close() cuando cualquiera de las lecturas del archivo lleguen al 
#final del archivo.

#Mira el editor y ve cuán simple y claro se ha vuelto el código.
from os import strerror

try:
    ccnt = lcnt = 0
    for line in open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\text.txt', "rt"):
	#for line in open('text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))


print("---2---")

#Manejando archivos de texto: write()
#Escribir archivos de texto parece ser más simple, ya que hay un método que puede usarse para realizar dicha tarea.

#El método se llama write() y espera solo un argumento: una cadena que se transferirá a un archivo abierto (no lo olvides), 
#el modo de apertura debe reflejar la forma en que se transfieren los datos - escribir en un archivo abierto en modo de lectura no tendrá éxito).

#No se agrega carácter de nueva línea al argumento de write(), por lo que debes agregarlo tu mismo si 
#deseas que el archivo se complete con varias líneas.

#El ejemplo en el editor muestra un código muy simple que crea un archivo llamado newtext.txt 
#(nota: el modo de apertura w asegura que el archivo se creará desde cero, incluso si existe y contiene datos) y luego pone diez líneas en él.

#La cadena que se grabará consta de la palabra línea, seguida del número de línea. 
#Hemos decidido escribir el contenido de la cadena carácter por carácter (esto lo hace el bucle interno for) pero no estás obligado
# a hacerlo de esta manera.

#Solo queríamos mostrarte que write() puede operar con caracteres individuales.

#El código crea un archivo con el siguiente texto:

#línea #1
#línea #2
#línea #3
#línea #4
#línea #5
#línea #6
#línea #7
#línea #8
#línea #9
#línea #10

#¿Puedes imprimir el contenido del archivo en la consola?
from os import strerror

try:
    #fo = open('newtext.txt', 'wt') #un nuevo archivo (newtext.txt) es creado FORMA DEL CURSO
	fo = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\newtext.txt', 'wt') #un nuevo archivo (newtext.txt) es creado
	for i in range(10): #EL NÚM. DE LÍNEAS SE DEFINE EN EL RANGE
		s = "línea #" + str(i+1) + "\n"
		for ch in s: #aquí se copia al archivo creado newtext
			fo.write(ch)
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
#Te alentamos a que pruebes el comportamiento del método write() localmente en tu máquina.

print("---3---")

#Manejando archivos de texto: continuación
#Mira el ejemplo en el editor. Hemos modificado el código anterior para escribir líneas enteras en el archivo de texto.
from os import strerror

try:
    
    fo = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\newtext.txt', 'wt')
	#fo = open('newtext.txt', 'wt') FORMA DEL CURSO
    fo.write("Prueba 2")
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))

#El contenido del archivo recién creado es el mismo.

#Nota: puedes usar el mismo método para escribir en el stream stderr, pero no intentes abrirlo, ya que siempre está abierto implícitamente.

#Por ejemplo, si deseas enviar un mensaje de tipo cadena a stderr para distinguirlo de la salida normal del programa, puede verse así:

import sys
sys.stderr.write("Mensaje de Error")

print("---4---")

#¿Qué es un bytearray?
#Antes de comenzar a hablar sobre archivos binarios, tenemos que informarte sobre una de las clases especializadas que 
#Python usa para almacenar datos amorfos.

#Los datos amorfos son datos que no tienen forma específica - son solo una serie de bytes.

#Esto no significa que estos bytes no puedan tener su propio significado o que no puedan representar ningún objeto útil, por ejemplo, 
#gráficos de mapa de bits.

#Los datos amorfos no pueden almacenarse utilizando ninguno de los medios presentados anteriormente: no son cadenas ni listas.

#Debe haber un contenedor especial capaz de manejar dichos datos.

#Python tiene más de un contenedor, uno de ellos es una clase especializada llamada bytearray - como su nombre indica,
#es un arreglo que contiene bytes (amorfos).

#Si deseas tener dicho contenedor, por ejemplo, para leer una imagen de mapa de bits y procesarla de alguna manera,
# debes crearlo explícitamente, utilizando uno de los constructores disponibles.

#Observa:

#data = bytearray(100)

#Tal invocación crea un objeto bytearray capaz de almacenar diez bytes.

#Nota: dicho constructor llena todo el arreglo con ceros.

print("---5---")

#Bytearrays: continuación
#Bytearrays se asemejan a listas en muchos aspectos. Por ejemplo, son mutables, son suceptibles a la función len(),
# y puedes acceder a cualquiera de sus elementos usando indexación convencional.

#Existe una limitación importante - no debes establecer ningún elemento del arreglo de bytes con un valor que no sea un entero
#(violar esta regla causará una excepción TypeError) 
#y tampoco está permitido asignar un valor fuera del rango de 0 a 255 (a menos que quieras provocar una excepción ValueError).

#Puedes tratar cualquier elemento del arreglo de bytes como un valor entero - al igual que en el ejemplo en el editor.
data = bytearray(10)
print(data)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

#Nota: hemos utilizado dos métodos para iterar el arreglo de bytes, y hemos utilizado la función hex()
# para ver los elementos impresos como valores hexadecimales.

#Ahora te vamos a mostrar cómo escribir un arreglo de bytes en un archivo binario, como no queremos guardar su representación legible,
# queremos escribir una copia uno a uno del contenido de la memoria física, byte a byte.

print("---6---")

#Bytearrays: continuación
#Entonces, ¿cómo escribimos un arreglo de bytes en un archivo binario?

#Observa el código en el editor. Analicémoslo:
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))



# ingresa aquí el código que lee los bytes del stream

#Primero, inicializamos bytearray con valores a partir de 10; si deseas que el contenido del archivo sea claramente legible, 
#reemplaza el 10con algo como ord('a'), esto producirá bytes que contienen valores correspondientes a 
#la parte alfabética del código ASCII (no pienses que harás que el archivo sea un archivo de texto; sigue siendo binario, 
#ya que se creó con un indicador - bandera wb).
#Después, creamos el archivo usando la función open(), la única diferencia en comparación con las variantes anteriores 
#es que el modo de apertura contiene el indicador b.
#El método write() toma su argumento (bytearray) y lo envía (como un todo) al archivo.
#El stream se cierra de forma rutinaria.
#El método write() devuelve la cantidad de bytes escritos correctamente.

#Si los valores difieren de la longitud de los argumentos del método, puede significar que hay algunos errores de escritura.

#En este caso, no hemos utilizado el resultado; esto puede no ser apropiado en todos los casos.

#Intenta ejecutar el código y analiza el contenido del archivo recién creado.

#Lo vas a usar en el siguiente paso.


#Cómo leer bytes de un stream
#La lectura de un archivo binario requiere el uso de un método especializado llamado readinto(), 
#ya que el método no crea un nuevo objeto del arreglo de bytes, sino que llena uno creado previamente 
#con los valores tomados del archivo binario.

#Nota:

#El método devuelve el número de bytes leídos con éxito.
#El método intenta llenar todo el espacio disponible dentro de su argumento; si existen más datos en el archivo que espacio en el argumento, 
#la operación de lectura se detendrá antes del final del archivo; el resultado del método puede indicar que el arreglo de 
#bytes solo se ha llenado de manera fragmentaria (el resultado también lo mostrará y la parte del arreglo que no está siendo utilizada 
#por los contenidos recién leídos permanece intacta).
#Mira el código completo a continuación:

from os import strerror

data = bytearray(10)
print("prueba")
try:
    bf = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Analicémoslo:

#Primero, abrimos el archivo (el que se creó usando el código anterior) con el modo descrito como rb.
#Luego, leemos su contenido en el arreglo de bytes llamado data, con un tamaño de diez bytes.
#Finalmente, imprimimos el contenido del arreglo de bytes: ¿Son los mismos que esperabas?
#Ejecuta el código y verifica si funciona.


print("---7---")

#Cómo leer bytes de un stream
#Se ofrece una forma alternativa de leer el contenido de un archivo binario mediante el método denominado read().
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))



# ingresa aquí el código que lee los bytes del stream

#Invocado sin argumentos, intenta leer todo el contenido del archivo en la memoria, haciéndolo parte de un objeto recién
# creado de la clase bytes.

#Esta clase tiene algunas similitudes con bytearray, con la excepción de una diferencia significativa: es immutable.

#Afortunadamente, no hay obstáculos para crear un arreglo de bytes tomando su valor inicial directamente del objeto de bytes, como aquí:

from os import strerror

try:
    bf = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Ten cuidado - no utilices este tipo de lectura si no estás seguro de que el contenido del archivo se ajuste a la memoria disponible.