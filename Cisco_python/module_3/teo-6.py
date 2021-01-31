#FOR
#La palabra reservada for abre el ciclo for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, 
#ya que se verifican internamente, sin ninguna intervención.
#Cualquier variable después de la palabra reservada for es la VARIABLE DE CONTROL del ciclo; cuenta los giros del ciclo y lo hace 
#automáticamente.
#La palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.
#La función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en 
#nuestro ejemplo, la función creará (incluso podemos decir que alimentará el ciclo con) valores subsiguientes del 
#siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un 
#paso (un número entero) antes del valor de su argumento.
#Nota la palabra clave pass dentro del cuerpo del ciclo - no hace nada en absoluto; es una instrucción vacía : 
#la colocamos aquí porque la sintaxis del ciclo for exige al menos una instrucción dentro del cuerpo (por cierto, if, elif, else y while 
#expresan lo mismo).


#NOTA: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.
l=0
for i in range(0,11):
    l+=1
    if i ==0:
        pass
    elif i>0:
        print("El valor de i es actualmente", i)
    
print(l)

#La función range() también puede aceptar tres argumentos: Echa un vistazo al código del editor.
#El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada giro del ciclo 
# (como puedes sospechar, el valor predeterminado del incremento es 1

for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)
    #3 y 5
#¿Sabes por qué? El primer argumento pasado a la función range() nos dice cual es el número de inicio de la secuencia (por lo tanto, 2 en la salida). El segundo argumento le dice a la función dónde detener la secuencia
#(la función genera números hasta el número indicado por el segundo argumento, pero no lo incluye). Finalmente, el tercer argumento indica el paso, que en realidad significa la diferencia entre cada número en la secuencia de números generados por la función.

#2(número inicial) → 5 (2 incremento por 3 es igual a 5 - el número está dentro del rango de 2 a 8) → 8 (5 incremento por 3 es igual a 8 - el número no está dentro del rango de 2 a 8, 
#porque el parámetro de parada no está incluido en la secuencia de números generados por la función).

#Nota: si el conjunto generado por la función range() está vacío, el ciclo no ejecutará su cuerpo en absoluto.
for i in range(1, 1):
    print("El valor de i es actualmente", i)


#Nota: el conjunto generado por range() debe ordenarse en un orden ascendente. No hay forma de forzar el range() 
#para crear un conjunto en una forma diferente.
#Esto significa que el segundo argumento de range() debe ser mayor que el primero.
for i in range(2, 1):
    print ("El valor de i es actualmente", i)

#Potencias de 2

pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 #pow=pow*2