#COMPRENSIÓN DE LISTAS (IMPORTANTE)



#El mismo efecto se puede lograr mediante una comprensión de lista, la sintaxis especial utilizada por Python para completar o 
#llenar listas masivas.

#Una comprensión de lista es en realidad una lista, pero se creó sobre la marcha durante la ejecución del programa, y no se 
#describe de forma estática.

#Echa un vistazo al fragmento:

#fila = [PEON_BLANCO for i in range(8)]

#La parte del código colocada dentro de los paréntesis especifica:

#Los datos que se utilizarán para completar la lista (PEON_BLANCO)
#La cláusula que especifica cuántas veces se producen los datos dentro de la lista (for i in range(8))



#ermítenos mostrarte otros ejemplos de comprensión de lista:

#Ejemplo # 1:

cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)

#El fragmento de código genera una lista de diez elementos y rellena con cuadrados de diez números enteros que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

#Ejemplo # 2:

dos = [2 ** i for i in range(8)]
print(dos)
#El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos (1, 2, 4, 8, 16, 32, 64, 128)

#Ejemplo # 3:
print("----------------------")
probabilidades = [x for x in cuadrados if x % 2 != 0] #Usa los valores del anteanterior ejemplo
print(probabilidades)

#El fragmento hace una lista con solo los elementos impares de la lista cuadrados.





#Listas dentro de listas: arreglos bidimensionales (IMPORTANTE):

#Supongamos también que un símbolo predefinido denominado EMPTY designa un campo vacío en el tablero de ajedrez.
#Entonces, si queremos crear una lista de listas que representan todo el tablero de ajedrez, se puede hacer de la siguiente manera:

#tablero  = []

#for i in range(8):
#    fila = [EMPTY for i in range(8)]
#    tablero.append(fila)

#Nota:
#La parte interior del bucle crea una fila que consta de ocho elementos(cada uno de ellos es igual a EMPTY) y lo agrega a la lista del tablero.
#La parte exterior se repite ocho veces.
#En total, la lista tablero consta de 64 elementos (todos iguales a EMPTY).


#Este modelo imita perfectamente el tablero de ajedrez real, que en realidad es una lista de elementos de ocho elementos,
#todos ellos en filas individuales. Resumamos nuestras observaciones:

#Los elementos de las filas son campos, ocho de ellos por fila.
#Los elementos del tablero de ajedrez son filas, ocho de ellos por tablero de ajedrez.
#La variable tablero ahora es un arreglo bidimensional. También se le llama, por analogía a los términos algebraicos, una MATRIZ.


#Como las listas de comprensión puede ser anidadas, podemos acortar la creación del tablero de la siguiente manera:
#FORMA RESUMIDA
#tablero = [[EMPTY for i in range(8)] for j in range(8)]

#La parte interna crea una fila, y la parte externa crea una lista de filas.



#Listas dentro de listas: arreglos bidimensionales - continuación


#El acceso al campo seleccionado del tablero requiere dos índices: el primero selecciona la fila; 
#el segundo: el número del campo dentro de la fila, el cual es un número de columna.

#Echa un vistazo al tablero de ajedrez. Cada campo contiene un par de índices que se deben dar para acceder al contenido del campo:
#ARMAR UN TABLERO DE AJEDREZ (ARREGLO BIDIMENSIONAL)
EMPTY = "-"
TORRE = "TORRE"
CABALLO = "CABALLO"
PEON = "PEÓN"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE #Torre blancas y negras
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
#Si deseas agregar un caballo a C4, hazlo de la siguiente manera:
tablero[4][2] = CABALLO
#Y ahora un peón a E5:
tablero[3][4] = PEON

print(tablero)