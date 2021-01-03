
def imprimir_algo(palabra):
    print (palabra + "!!!!")
imprimir_algo("Hola")
imprimir_algo("Bioingenieros")
var = str( input("Ingrese algo: " ) )
imprimir_algo(var)



def imprimir_mult():
    print(2*2)
imprimir_mult()

def imp_mult(x):
    print(2*x)
var= int(input("ingrese un número"))
imp_mult(var)



def imprimir_suma(a,b):
    print (a+b)
x = int(input("Ingrese el #1: " ))
y = int(input("Ingrese el #2: " ))
imprimir_suma(x,y)



def mi_func(x=0): #Cuando se llama a la función, no hay argumento, este toma el valor por defecto.
    print (x * x)
mi_func()
mi_func(5)
mi_func(10)


def otra_func(x="No tiene argumento"):
    print (x)
otra_func()
otra_func(5)



#Valor mayor:
def maximo(x,y):
    if x > y:
        print ("El número mayor es: ")
        return x
    elif y > x:
        print ("El número mayor es: ")
        return y
    else:
        print ("Los números ingresados son iguales")
        return x,y
x = int(input("Ingrese un número"))
y = int(input("ingrese otro número"))
print(maximo(x,y))


