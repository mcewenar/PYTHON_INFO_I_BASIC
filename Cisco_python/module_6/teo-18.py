#Accediendo a archivos desde el código en Python
#Uno de los problemas más comunes en el trabajo del desarrollador es procesar datos almacenados en archivos que generalmente se almacenan 
#físicamente utilizando dispositivos de almacenamiento: 
#discos duros, ópticos, de red o de estado sólido.

#Es fácil imaginar un programa que clasifique 20 números, y es igualmente fácil imaginar que el usuario de este programa 
#ingrese estos veinte números directamente desde el teclado.

#Es mucho más difícil imaginar la misma tarea cuando hay 20,000 números para ordenar, y no existe un solo usuario que pueda 
#ingresar estos números sin cometer un error.

#Es mucho más fácil imaginar que estos números se almacenan en el archivo que lee el programa. El programa clasifica los 
#números y no los envía a la pantalla, sino que crea un nuevo archivo y guarda la secuencia ordenada de números allí.

#Si queremos implementar una base de datos simple, la única forma de almacenar la información entre ejecuciones del programa 
#es guardarla en un archivo (o archivos si tu base de datos es más compleja).


#Es un principio que cualquier problema de programación no simple se basa en el uso de archivos, ya sea que procese imágenes 
#(almacenadas en archivos), multiplique matrices (almacenadas en archivos) 
#o calcule salarios e impuestos (lectura de datos almacenados en archivos).

#Puedes preguntarte por qué hemos esperado hasta ahora para mostrarte esto.

#La respuesta es muy simple: la forma en que Python accede y procesa los archivos se implementa utilizando un conjunto consistente de objetos. 
#No hay mejor momento para hablar de esto.


print("---2---")
#IMPORTANTÍSIMO:
#Nombres de archivos
#Los diferentes sistemas operativos pueden tratar a los archivos de diferentes maneras. Por ejemplo, 
#Windows usa una convención de nomenclatura diferente a la adoptada en los sistemas Unix/Linux.

#Si utilizamos la noción de un nombre de archivo canónico (un nombre que define de forma exclusiva la ubicación del archivo, 
#independientemente de su nivel en el árbol de directorios), podemos darnos cuenta de que estos nombres se ven diferentes 
#en Windows y en Unix/Linux:

#Como puedes ver, los sistemas derivados de Unix/Linux no usan la letra de la unidad de disco (p. Ejemplo, C:) 
#y todos los directorios crecen desde un directorio raíz llamado /, 
#mientras que los sistemas Windows reconocen el directorio raíz como \.

#IMPORTANTE:
#Además, los nombres de archivo de sistemas Unix/Linux distinguen entre mayúsculas y minúsculas. 
#Los sistemas Windows almacenan mayúsculas y minúsculas en el nombre del archivo, pero no distinguen entre ellas.

#Esto significa que estas dos cadenas:

#EsteEsElNombreDelArchivo

#y

#esteeselnombredelarchivo


#describen dos archivos diferentes en sistemas Unix/Linux, pero tienen el mismo nombre para un solo archivo en sistemas Windows.

#ULTRAMEGAIMPORTANTE:
#La diferencia principal y más llamativa es que debes usar dos separadores diferentes para los nombres de directorio:
# \ en Windows y / en Unix/Linux.

#Esta diferencia no es muy importante para el usuario normal, pero es muy importante al escribir programas en Python.

#Para entender por qué, intenta recordar el papel muy específico que desempeña \ dentro de las cadenas en Python.

#Linux: /
#Windows: \


print("---3---")
#Nombres de Archivo: continuación
#Supongamos que estás interesado en un archivo en particular ubicado en el directorio dir, y con el nombre de archivo.

#Supongamos también que deseas asignar a una cadena el nombre del archivo.

#En sistemas Unix/Linux, se ve de la siguiente manera:

#nombre = "/dir/archivo"

#Pero si intentas codificarlo para el sistema Windows:

#nombre = "\dir\archivo"

#obtendrás una sorpresa desagradable: Python generará un error o la ejecución del programa se comportará de manera extraña,
#como si el nombre del archivo se hubiera distorsionado de alguna manera.

#IMPORTANTÍSIMO:
#De hecho, no es extraño en lo absoluto, pero es bastante obvio y natural. Python usa la \ como un caracter de escape (como \n).
#Esto significa que los nombres de archivo de Windows deben escribirse de la siguiente manera:

#nombre = "\\dir\\archivo"

#Afortunadamente, también hay una solución más. Python es lo suficientemente
#inteligente como para poder convertir diagonales en diagonales invertidas cada vez que descubre que el sistema operativo lo requiere.

#Esto significa que cualquiera de las siguientes asignaciones:
#nombre = "/dir/archivo"
#nombre = "c:/dir/archivo"

#funcionará también con Windows.

#Cualquier programa escrito en Python (y no solo en Python, porque esa convención se aplica a prácticamente todos 
#los lenguajes de programación) no se comunica con los archivos directamente, sino a través de algunas entidades 
#abstractas que se nombran de manera diferente en los distintos lenguajes o entornos, los términos más utilizados 
#son handles (un tipo de puntero inteligente) o streams (una especie de canal) (los usaremos como sinónimos aquí).

#El programador, que tiene un conjunto de funciones y métodos, puede realizar ciertas operaciones en el stream, 
#que afectan los archivos reales utilizando mecanismos contenidos en el núcleo del sistema operativo.

#De esta forma, puedes implementar el proceso de acceso a cualquier archivo, incluso cuando el nombre del 
#archivo es desconocido al momento de escribir el programa.


print("---4---")

#Streams para Archivos
#La apertura del stream no solo está asociada con el archivo, sino que también se debe declarar la manera en que se procesará el stream.
#Esta declaración se llama un open mode (modo abierto).

#Si la apertura es exitosa, el programa solo podrá realizar las operaciones que sean consistentes con el modo abierto declarado.

#Hay dos operaciones básicas a realizar con el stream:

#Lectura del stream: las porciones de los datos se recuperan del archivo y se colocan en un área de memoria administrada por el programa
#(por ejemplo, una variable).
#Escritura del stream: Las porciones de los datos de la memoria (por ejemplo, una variable) se transfieren al archivo.
#Hay tres modos básicos utilizados para abrir un stream:

#Modo Lectura: un stream abierto en este modo permite solo operaciones de lectura; intentar escribir en la transmisión provocará una excepción
#(la excepción se llama UnsupportedOperation, la cual hereda el OSError y el ValueError, y proviene del módulo io).
#Modo Escritura: un stream abierto en este modo permite solo operaciones de escritura;
#intentar leer el stream provocará la excepción mencionada anteriormente.
#Modo Actualizar: un stream abierto en este modo permite tanto lectura como escritura.

#Antes de discutir cómo manipular los streams, te debemos una explicación. El stream se comporta casi como una grabadora.

#Cuando lees algo de un stream, un cabezal virtual se mueve sobre la transmisión de acuerdo con el número de bytes transferidos desde el stream.

#Cuando escribes algo en el stream el mismo cabezal se mueve a lo largo del stream registrando los datos de la memoria.

#Siempre que hablemos de leer y escribir en el stream, trata de imaginar esta analogía.
#Los libros de programación se refieren a este mecanismo como la posición actual del archivo, aquí también usaremos este término.


#Ahora es necesario mostrarte el objeto responsable de representar los streams en los programas.


print("---5---")
#Manejo de Archivos
#Python supone que cada archivo está oculto detrás de un objeto de una clase adecuada.

#Por supuesto, es difícil no preguntar cómo interpretar la palabra adecuada.

#Los archivos se pueden procesar de muchas maneras diferentes: algunos dependen del contenido del archivo, otros de las intenciones del 
#programador.

#En cualquier caso, diferentes archivos pueden requerir diferentes conjuntos de operaciones y comportarse de diferentes maneras.

#Un objeto de una clase adecuada es creado cuando abres el archivo y lo aniquilas al momento de cerrarlo.

#Entre estos dos eventos, puedes usar el objeto para especificar qué operaciones se deben realizar en un stream en particular.
#Las operaciones que puedes usar están impuestas por la forma en que abriste el archivo.

#En general, el objeto proviene de una de las clases que se muestran aquí:

#Nota: nunca se utiliza el constructor para dar vida a estos objetos. La unica forma de obtenerlos es invocar la función llamada open().

#La función analiza los argumentos proporcionados y crea automáticamente el objeto requerido.

#Si deseas deshacerte del objeto, invoca el método denominado close().

#La invocación cortará la conexión con el objeto y el archivo, y eliminará el objeto.

#Para nuestros propósitos, solo nos ocuparemos de los streams representados por los objetos BufferIOBase y TextIOBase.
#Entenderás por qué pronto.

print("---6---")

#Manejo de Archivos: continuación
#Debido al tipo de contenido de los streams, todos se dividen en tipo texto y binario.

#Los streams de texto están estructurados en líneas; es decir, contienen caracteres tipográficos 
#(letras, dígitos, signos de puntuación, etc.) dispuestos en filas (líneas), como se ve a simple vista cuando se mira 
#el contenido del archivo en el editor.

#Este tipo de archivo es escrito (o leído) principalmente carácter por carácter, o línea por línea.

#Los streams binarios no contienen texto, sino una secuencia de bytes de cualquier valor. Esta secuencia puede ser,
# por ejemplo, un programa ejecutable, una imagen, un audio o un videoclip, un archivo de base de datos, etc.

#Debido a que estos archivos no contienen líneas, las lecturas y escrituras se relacionan con porciones de datos de cualquier tamaño.
# Por lo tanto, los datos se leen y escriben byte a byte, o bloque a bloque, donde el tamaño del bloque generalmente varía de uno a 
# un valor elegido arbitrariamente.

#Ahora viene un problema pequeño. En los sistemas Unix/Linux, los extremos de la línea están marcados 
#por un solo carácter llamado LF (código ASCII 10) designado en los programas de Python como \n.

#Otros sistemas operativos, especialmente los derivados del sistema prehistórico CP/M 
#(que también aplica a los sistemas de la familia Windows) utilizan una convención diferente: 
#el final de la línea está marcada por un par de caracteres, CR y LF (códigos ASCII 13 y 10) los cuales se puede codificar como \r\n.

#Esta ambigüedad puede causar varias consecuencias desagradables.

#Si creas un programa responsable de procesar un archivo de texto y está escrito para Windows, puedes reconocer los extremos 
#de las líneas al encontrar 
#los caracteres \r\n, pero si el mismo programa se ejecuta en un entorno Unix/Linux será completamente inútil, y viceversa: el programa escrito para sistemas Unix/Linux podría ser inútil en Windows.

#Ojo:
#Estas características indeseables del programa, que impiden o dificultan el uso del programa en diferentes entornos, se denomina 
#falta de portabilidad.

#Del mismo modo, el rasgo del programa que permite la ejecución en diferentes entornos se llama portabilidad.
# Un programa dotado de tal rasgo se llama programa portable.





