#Algunas funciones simples: continuación
#Ahora trabajaremos con triángulos. Comenzaremos con una función que verifique si tres lados de ciertas longitudes pueden formar un triángulo.

#IMPORTANTE
#En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.

#No será algo difícil. La función tendrá tres parámetros - uno para cada lado.

#Regresará True si todos los lados pueden formar un triángulo, y False de lo contrario. En este caso, esUnTringulo es un buen nombre 
#para dicha función.

#Observa el código en el editor. Ahí se encuentra la función. Ejecuta el programa.

def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))


#Parece que funciona perfectamente: estos son los resultados:

#True
#False

#¿Se podrá hacer más compacta?. Parece tener demasiadas palabras.

#Esta es la versión mas compacta:

def esUnTriangulo(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(esUnTriangulo(1, 1, 1))
print(esUnTriangulo(1, 1, 3))

#¿Se puede compactar aun mas?

#Por supuesto, observa:

def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

#Se ha negado la condición (se invirtieron los operadores relacionales y se reemplazaron los ors con ands, obteniendo una expresión 
# universal para probar triángulos).

#Coloquemos la función en un programa más grande. Se le pedirá al usuario los tres valores y se hará uso de la función.

print("-----2-----")
#Algunas funciones simples: triángulos y el teorema de Pitágoras
#Observa el código en el editor. Le pide al usuario tres valores. 

#Después hace uso de la función esUnTriangulo. El código esta listo para correrse.

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b #Viene implícito el True or False

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")

#En el segundo paso, intentaremos verificar si un triángulo es un triángulo rectángulo.

#Para ello haremos uso del Teorema de Pitágoras:

#c2 = a2 + b2

#¿Cómo saber cual de los tres lados es la hipotenusa?

#La hipotenusa es el lado mas largo.

#Aquí esta el código:

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo(a, b, c): #Si es false, se vuelte true y se ejecuta
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(esUnTrianguloRectangulo(5, 3, 4))
print(esUnTrianguloRectangulo(1, 3, 4))
#Observa como se establece la relación entre la hipotenusa y los dos catetos. Se eligió el lado mas largo y 
#se aplico el Teorema de Pitágoras para verificar que todo estuviese en orden. Esto requiere tres revisiones en total.


print("----3----")

#Algunas funciones simples: evaluando el campo de un triángulo
#También es posible evaluar el campo de un triángulo. La Formula de Heron será útil aquí:
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")


#Vamos a emplear el operador de exponenciación para calcular la raíz cuadrada - puede ser extraño, pero funciona.

#Este es el código resultante:

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(1., 1., 2. ** .5))


#Lo probaremos con un triángulo rectángulo la mitad de un cuadrado y con un lado igual a 1. Esto significa que su campo debe ser igual a 0.5.

#Es extraño pero el código produce la siguiente salida:

#0.49999999999999983

#Es muy cercano a 0.5, pero no es exactamente 0.5,¿Que significa?, ¿Es un error?

#No, no lo es. Son solo los cálculos de valores punto flotantes. Pronto se discutirá el tema.

