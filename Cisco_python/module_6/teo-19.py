#Manejo de archivos: continuación
#Dado que los problemas de portabilidad eran (y siguen siendo) muy graves, se tomó la decisión de resolver definitivamente 
#el problema de una manera que no atraiga mucho la atención del desarrollador.

#Se realizó a nivel de clases, que son responsables de leer y escribir caracteres hacia y desde el stream. Funciona de la siguiente manera:

#Cuando el stream está abierto y se recomienda que los datos en el archivo asociado se procesen como texto (o no existe tal aviso), 
#se cambia al modo texto.

#Durante la lectura y escritura de líneas desde y hacia el archivo asociado, no ocurre nada especial en el entorno Unix, 
#pero cuando se realizan las mismas operaciones en el entorno Windows, un proceso llamado traducción de caracteres de nueva línea ocurre: 
#cuando lees una línea del archivo, cada par de caracteres \r\n se reemplaza con un solo caracter \n, y viceversa; 
#durante las operaciones de escritura, cada caracter \n se reemplaza con un par de caracteres \r\n.

#El mecanismo es completamente transparente para el programa, el cual puede escribirse como si estuviera destinado a procesar 
#archivos de texto Unix/Linux solamente; el código fuente ejecutado en un entorno Windows también funcionará correctamente.

#Cuando el stream está abierto, su contenido se toma tal cual es, sin ninguna conversión - no se agregan, ni se omiten bytes.

#Abriendo los streams

#OJO:
#El abrir un stream se realiza mediante una función que se puede invocar de la siguiente manera:

#stream = open(file, mode = 'r', encoding = None)

#HAY OTRA FORMA:
#file = open(file,”mode")
#Hacer algo con el archivo
#file.close()

#Vamos a analizarlo:
#PASOS:
#El nombre de la función (open) habla por si mismo; si la apertura es exitosa, la función devuelve un objeto stream; de lo contrario, 
#se genera una excepción (por ejemplo, FileNotFoundError si el archivo que vas a leer no existe).
#El primer parámetro de la función (file) especifica el nombre del archivo que se asociará al stream.
#El segundo parámetro (mode) especifica el modo de apertura utilizado para el stream; es una cadena llena de una secuencia de caracteres, 
#y cada uno de ellos tiene su propio significado especial (más detalles pronto).
#El tercer parámetro (encoding) especifica el tipo de codificación (por ejemplo, UTF-8 cuando se trabaja con archivos de texto).
#La apertura debe ser la primera operación realizada en el stream.
#Nota: el modo y los argumentos de codificación pueden omitirse; en dado caso, se tomarán sus valores predeterminados. 
#El modo de apertura predeterminado es leer en modo de texto, mientras que la codificación predeterminada depende de la plataforma utilizada.

#Permítenos ahora presentarte los modos de apertura más importantes y útiles. ¿Listo?


print("---2---")

#Abriendo los streams: modos
#Modo de apertura r: lectura

#El stream será abierto en modo lectura.
#El archivo asociado con el stream debe existir y tiene que ser legible, de lo contrario la función open() lanzará una excepción.
#Modo de apertura w: escritura

#El stream será abierto en modo escritura.
#El archivo asociado con el stream no necesita existir. Si no existe, se creará; si existe, se truncará a la longitud de cero (se borrá); 
#si la creación no es posible (por ejemplo, debido a los permisos del sistema) la función open() lanzará una excepción.
#Modo de apertura a: adjuntar

#El stream será abierto en modo adjuntar.
#El archivo asociado con el stream no necesita existir; si no existe, se creará; si existe, el cabezal de grabación virtual se 
#establecerá al final del archivo (el contenido anterior del archivo permanece intacto).
#Modo de apertura r+: leer y actualizar

#El stream será abierto en modo leer y actualizar.
#El archivo asociado con el stream debe existir y tiene que ser escribible, de lo contrario la función open() lanzará una excepción.
#Se permiten operaciones de lectura y escritura en el stream.
#Modo de apertura w+: escribir y actualizar

#El stream será abierto en modo escribir y actualizar.
#El archivo asociado con el stream no necesita existir; si no existe, se creará; el contenido anterior del archivo permanece intacto.
#Se permiten operaciones de lectura y escritura en el stream.

#Seleccionando modo de texto y modo binario
#Si hay una letra b al final de la cadena del modo significa que el stream se debe abrir en el modo binario.

#Si la cadena del modo termina con una letra t el stream es abierto en modo texto.

#El modo texto es el comportamiento predeterminado que se utiliza cuando no se especifica ya sea modo binario o texto.

#Finalmente, la apertura exitosa del archivo establecerá la posición actual del archivo (el cabezal virtual de lectura/escritura)
# antes del primer byte del archivo si el modo no es a y después del último 
#byte del archivo si el modo es a.


#  Modo texto	Modo binario	Descripción
#     rt	        rb	          lectura
#     wt	        wb	         escritura
#     at	        ab	         adjuntar
#     r+t	        r+b	       leer y actualizar
#     w+t	        w+b	     escribir y actualizar

#EXTRA:
#También puedes abrir un archivo para su creación exclusiva. Puedes hacer esto usando el modo de apertura x. 
#Si el archivo ya existe, la función open() lanzará una excepción.

print("---3---")

#Abriendo el stream por primera vez
#Imagina que queremos desarrollar un programa que lea el contenido del archivo de texto llamado: C:\Users\User\Desktop\file.txt.

#¿Cómo abrir ese archivo para leerlo? Aquí está el fragmento del código:

try:
    stream = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\pruebaManejoArchivo.txt", "w") #VA A GENERAR ERROR DEBIDO A QUE NO ES LINUX O UNIX
    #stream = open("C:\Users\User\Desktop\file.txt", "rt") #VA A GENERAR ERROR DEBIDO A QUE NO ES LINUX O UNIX
    # aqui se procesa el archivo
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)

#¿Que está pasando aqui?

#Hemos abierto el bloque try-except ya que queremos manejar los errores de tiempo de ejecución suavemente.
#Se emplea la función open() para intentar abrir el archivo especificado 
#(ten en cuenta la forma en que hemos especificado el nombre del archivo).
#El modo de apertura se define como texto para leer (como texto es la configuración predeterminada, podemos omitir la t en la cadena de modo).
#En caso de éxito obtenemos un objeto de la función open() y lo asignamos a la variable del stream.
#Si open() falla, manejamos la excepción imprimiendo la información completa del error (es bueno saber qué sucedió exactamente).
#Streams pre-abiertos
#Dijimos anteriormente que cualquier operación del stream debe estar precedida por la invocación de la función open(). 
#Hay tres excepciones bien definidas a esta regla.

#Cuando comienza nuestro programa, los tres streams ya están abiertos y no requieren ninguna preparación adicional. 
#Además, tu programa puede usar estos streams explícitamente si tienes cuidado de importar el módulo sys:

import sys

#Porque ahí es donde se coloca la declaración de estos streams.


#Los nombres de los streams son: sys.stdin, sys.stdout y sys.stderr.

#Vamos a analizarlos:

sys.stdin
#stdin (significa entrada estándar).
#El stream stdin normalmente se asocia con el teclado, se abre previamente para la lectura 
#y se considera como la fuente de datos principal para los programas en ejecución.
#La función bien conocida input() lee datos de stdin por default.

sys.stdout
#stdout (significa salida estándar).
#El stream stdout normalmente está asociado con la pantalla, preabierta para escritura, considerada como el objetivo principal 
#para la salida de datos por el programa en ejecución.
#La función bien conocida print() envía los datos al stream stdout.

sys.stderr
#stderr (significa salida de error estándar).
#El stream stderr normalmente está asociado con la pantalla, preabierta para escribir, considerada como el lugar principal 
#donde el programa en ejecución debe enviar información sobre los errores encontrados durante su trabajo.
#No hemos presentado ningún método para enviar datos a este stream (lo haremos pronto, lo prometemos).
#La separación de stdout (resultados útiles producidos por el programa) de stderr (mensajes de error, 
#indudablemente útiles pero no proporcionan resultados) ofrece la posibilidad de redirigir estos dos tipos de información 
#a los diferentes objetivos. Una discusión más extensa sobre este tema está más allá del alcance de nuestro curso. 
#El manual del sistema operativo proporcionará más información sobre estos temas.

print("---4---")

#Cerrando streams
#La última operación realizada en un stream (esto no incluye a los streams stdin, stdout, y stderr pues no lo requieren) debe ser cerrarlo.

#Esa acción se realiza mediante un método invocado desde dentro del objeto del stream: stream.close().

#El nombre de la función es fácil de entender close(), es decir cerrar.
#La función no espera argumentos; el stream no necesita estar abierto.
#La función no devuelve nada pero lanza una excepción IOError en caso de un error.
#La mayoría de los desarrolladores creen que la función close() siempre tiene éxito y, por lo tanto, 
#no hay necesidad de verificar si ha realizado su tarea correctamente.

#Esta creencia está solo parcialmente justificada. Si el stream se abrió para escribir y luego se realizó una serie de operaciones de escritura, 
#puede ocurrir que los datos enviados al stream aún no se hayan transferido al dispositivo físico (debido a los mecanismos de cache o buffer). 
#Dado que el cierre del stream obliga a los búferes a descargarse, es posible que dichas descargas fallen y, por lo tanto, close() falle también.
#Ya hemos mencionado fallas causadas por funciones que operan con los streams, pero no mencionamos nada 
#sobre cómo podemos identificar exactamente la causa de la falla.

#La posibilidad de hacer un diagnóstico existe y es proporcionada por uno de los componentes de excepción de los streams.

#Diagnosticando problemas con los streams
#El objeto IOError está equipado con una propiedad llamada errno (el nombre viene de la frase error number, número de error) 
#y puedes accederla de la siguiente manera:

#try:
    # operaciones con streams
#except IOError as exc:
#    print(exc.errno)

#El valor del atributo errno se puede comparar con una de las constantes simbólicas predefinidas en módulo errno.

#Echemos un vistazo a algunas constantes seleccionadas útiles para detectar errores de flujo:

#errno.EACCES → Permiso denegado

#El error se produce cuando intentas, por ejemplo, abrir un archivo con atributos de solo lectura para abrirlo.


#errno.EBADF → Número de archivo incorrecto

#El error se produce cuando intentas, por ejemplo, operar un stream sin abrirlo.

#errno.EEXIST → Archivo existente

#El error se produce cuando intentas, por ejemplo, cambiar el nombre de un archivo con su nombre anterior.


#errno.EFBIG → Archivo demasiado grande

#El error ocurre cuando intentas crear un archivo que es más grande que el máximo permitido por el sistema operativo.


#errno.EISDIR → Es un directorio

#El error se produce cuando intentas tratar un nombre de directorio como el nombre de un archivo ordinario.


#errno.EMFILE → Demasiados archivos abiertos

#El error se produce cuando intentas abrir simultáneamente más streams de los aceptables para el sistema operativo.


#errno.ENOENT → El archivo o directorio no existe

#El error se produce cuando intentas acceder a un archivo o directorio inexistente.


#errno.ENOSPC → no queda espacio en el dispositivo

#El error ocurre cuando no hay espacio libre en el dispositivo.


#La lista completa es mucho más larga (incluye también algunos códigos de error no relacionados con el procesamiento del stream).

print("---5---")

#Diagnosticando problemas con los streams: continuación

#Si eres un programador muy cuidadoso, puedes sentir la necesidad de usar una secuencia de sentencias similar 
#a la que se presenta a continuación:

import errno
#try:
    #s = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\pruebaManejoArchivo3.txt", "rt") CON ARCHIVO DE DAVID
    #s = open("c:/users/user/Desktop/file.txt", "rt")
    # el procesamiento va aquí
    #s.close()
#except Exception as exc:
#    if exc.errno == errno.ENOENT:
#        print("El archivo no existe.")
#    elif exc.errno == errno.EMFILE:
#        print("Has abierto demasiados archivos.")
#    else:
#        print("El número de error es:", exc.errno)

#Afortunadamente, existe una función que puede simplificar el código de manejo de errores. Su nombre es strerror(), 
#y proviene del módulo os y espera solo un argumento: un número de error.

#Su función es simple: proporciona un número de error y una cadena que describe el significado del error.

#Nota: Si pasas un código de error inexistente (un número que no está vinculado a ningún error real), 
#la función lanzará una excepción ValueError.

#Ahora podemos simplificar nuestro código de la siguiente manera:

#FORMA CORTA Y SIMPLIFICADA:
from os import strerror
try:
    s = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_6\\pruebaManejoArchivo2.txt", "wt")
    #s = open("c:/users/user/Desktop/file.txt", "rt") FORMA EN QUE APARECE EN EL CURSO
    # el procesamiento va aquí
    s.close()
except Exception as exc:
    print("El archivo no se pudo abrir:", strerror(exc.errno));

#Bueno. Ahora es el momento de tratar con archivos de texto y familiarizarse con algunas técnicas básicas que puedes utilizar para procesarlos.