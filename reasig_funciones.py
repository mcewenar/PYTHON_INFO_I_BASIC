
#Reasignación de nombres de funciones

def multiply(x,y):
    return x*y
a=4
b=7
operacion = multiply
print(operacion(a,b))


#Las funciones también pueden ser utilizadas como
#argumentos de otras funciones.
def suma(x,y):
    return x + y
def otra_func(func,x,y):
    return func(func(x,y),func(x,y))
a=5
b=10

print(otra_func(suma,a,b))



def funcion2(func,arg):
    return func(func(arg))
def suma5(x):
    return x+5
print(funcion2(suma5,10))

def test(func,arg):
    return func(func(arg))
def mult(x):
    return x*x

print (test(mult,2))