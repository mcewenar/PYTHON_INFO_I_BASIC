#Recursión ImportError: falla de importación.
#IndexError: un lista es indexada con un número fuera de rango.
#NameError: una variable desconocida es utilizada.
#SyntaxError: el código no puede ser analizado correctamente.
#TypeError: una función es llamada con un valor de un tipo inapropiado.
#ValueError: una función es llamada con un valor de tipo correcto pero con un valor incorrecto.


def Misterio(a,b):
    if (a<=0 and b<=0): #caso base. Importante para no generar bucle de recursión
        return 1
    if (a%2==0):
        return a + Misterio(b,b-1)
    else: 
        return b + Misterio(a+1,b)

print(Misterio(6,2))