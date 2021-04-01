#Cómo leer bytes de un stream: continuación
#Si el método read() se invoca con un argumento, se especifica el número máximo de bytes a leer.

#El método intenta leer la cantidad deseada de bytes del archivo, y la longitud del objeto devuelto puede usarse para determinar 
#la cantidad de bytes realmente leídos.

#Puedes usar el método como aquí:
from os import strerror
try:

    bf = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\file.bin', 'rb')
    #bf = open('file.bin', 'rb') FORMA DEL CURSO
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

#Nota: los primeros cinco bytes del archivo han sido leídos por el código; los siguientes cinco todavía están esperando ser procesados.


from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\file2.bin', 'wb')
    #bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))



# ingresa aquí el código que lee los bytes del stream


print("---2---")
#Copiando archivos: una herramienta simple y funcional
#Ahora vas a juntar todo este nuevo conocimiento, agregarle algunos elementos nuevos y usarlo para escribir 
#un código real que pueda copiar el contenido de un archivo.

#Por supuesto, el propósito no es crear un reemplazo para los comandos como copy de (MS Windows) o cp de (Unix/Linux) 
#pero para ver una forma posible de crear una herramienta de trabajo, incluso si nadie quiere usarla.

#Observa el código en el editor. Analicémoslo:
from os import strerror

srcname = input("¿Nombre del archivo fuente?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	
dstname = input("¿Nombre del archivo de destino?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()

#Las líneas 3 a la 8: solicitan al usuario el nombre del archivo a copiar e intentan abrirlo para leerlo; se termina la ejecución 
#del programa si falla la apertura; nota: emplea la función exit() para detener la ejecución del programa y pasar 
#el código de finalización al sistema operativo; cualquier código de finalización que no sea 0 significa que el 
#programa ha encontrado algunos problemas; se debe utilizar el valor errno para especificar la naturaleza del problema.
#Las líneas 9 a la 15: repiten casi la misma acción, pero esta vez para el archivo de salida.
#La línea 17: prepara una parte de memoria para transferir datos del archivo fuente al destino; Tal área de transferencia a menudo 
#se llama un búfer, de ahí el nombre de la variable; el tamaño del búfer es arbitrario; en este caso, decidimos usar 64 kilobytes; 
#técnicamente, un búfer más grande es más rápido al copiar elementos, ya que un búfer más grande significa menos operaciones de E/S; 
#en realidad, siempre hay un límite, cuyo cruce no genera más ventajas; pruébalo tú mismo si quieres.
#Línea 18: cuenta los bytes copiados: este es el contador y su valor inicial.
#Línea 20: intenta llenar el búfer por primera vez.
#Línea 21: mientras se obtenga un número de bytes distinto de cero, repite las mismas acciones.
#Línea 22: escribe el contenido del búfer en el archivo de salida (nota: hemos usado un segmento para limitar la cantidad de bytes 
#que se escriben, ya que write() siempre prefiero escribir todo el búfer).
#Línea 23: actualiza el contador.
#Línea 24: lee el siguiente fragmento de archivo.
#Las líneas 29 a la 31: limpieza final: el trabajo está hecho.