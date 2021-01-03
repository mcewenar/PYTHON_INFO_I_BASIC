list1=[]
print("esto es un programa para ingresar una matriz nxm")
def mat():
    while True:
        try:
            m=int(input("ingrese el número de filas"))
            n=int(input("ingrese el número de columnas"))
            break
        except ValueError:
            print("señor usuario, recuerde que solo se permiten números naturales")
    list1=[0]*m
    for x in range(m):
        list1[x]=[0]*n
    for x in range(m):
        for y in range(n):
            while True:
                try:
                    list1[x][y]=float(input("ingrese un número"))
                    break
                except ValueError:
                    print("recuerde que solo se permiten números")
                    
    return list1   
        
def giro90horario(list1):
    filas=len(list1)
    colu=len(list1[0])
    matrizho=[0]*colu
    for x in range(colu):
        matrizho[x]=[0]*filas

    for y in range(colu):
        a=0
        for z in range(filas-1,-1,-1):
            matrizho[y][a]=list1[z][y]
            a=a+1
    return matrizho
def antihorario(list1):
    filas=len(list1)
    colu=len(list1[0])
    antih=[0]*colu
    for x in range(colu):
        antih[x]=[0]*filas
    for y in range(filas):
        a=filas
        for z in range(colu):
            antih[a][y]=list1[y][z]
            a=a-1
    return antih



matriz=mat()
print(matriz)
horario=giro90horario(matriz)
print(horario)
antihor=antihorario(matriz)
print(antihor)
