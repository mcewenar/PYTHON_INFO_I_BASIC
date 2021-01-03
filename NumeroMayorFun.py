


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

#z = maximo(int(input("#1: ")),int(input("#2: ")))
#print (z)



#Return boolean
def prueba (x,y):
    if (x<y):
        return True
    else:
        return False
a = int(input('#1: '))
b = int(input('#2: '))
r = prueba(a,b)
print(r)
#Other:

def prueba (x,y):
    if (x<y):
        return "{0} es menor que {1}".format(x,y)
    else:
        return "{0} es mayor o igual que {1}".format(x,y)
a = int(input("#1: "))
b = int(input("#2: "))
r = prueba(a,b)
print(r)






