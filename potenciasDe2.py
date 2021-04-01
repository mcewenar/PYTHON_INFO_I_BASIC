#Cómo construir tu propio generador
#¿Qué pasa si necesitas un generador para producir las primeras n potencias de 2 ?

#Nada difícil. Solo mira el código en el editor.
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

for v in potenciasDe2(8):
    print(v)
#2ala0
#2ala1
#2ala2
#2ala3
#2ala4
#2ala5
#. 
#.
#.

#¿Puedes adivinar la salida? Ejecuta el código para verificar tus conjeturas.

#Los generadores también pueden usarse dentro de listas de comprensión, como aqui:

def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = [x for x in potenciasDe2(5)]

print(t)

#Ejecuta el ejemplo y verifica la salida.

#La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista real:

def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = list(potenciasDe2(3))

print(t)

#Nuevamente, intenta predecir el resultado y ejecuta el código para verificar tus predicciones.

#Además, el contexto creado por el operador in también te permite usar un generador.

#El ejemplo muestra cómo hacerlo:

def potenciasDe2(n):
    potencia= 1
    for i in range(n):
        yield potencia
        potencia*= 2

for i in range(20):
    if i in potenciasDe2(4):
        print(i)

#¿Cuál es la salida del código? Ejecuta el programa y verifica.

#Ahora veamos un Generador de números de la serie Fibonacci implementando lo anterior.

#Aquí está:

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)

#Adivina la salida (una lista) producida por el generador y ejecuta el código para verificar si tenías razón.





#FORMA 2, MÁS SENCILLA:
    
    
def potencia(n):
    for i in range(n):
        print(pow(2, i))
        
        
potencia(8)