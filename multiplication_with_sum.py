suma = 0
def imprimir_suma(x,y,suma):
    for i in range(x):
        suma=suma+y
    print(suma)
x = int(input("Ingrese el #1: " ))
y = int(input("Ingrese el #2: " ))
imprimir_suma(x,y,suma)


