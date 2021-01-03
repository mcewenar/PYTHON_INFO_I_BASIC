#Diccionarios
list1=[]
camisetas = {1: ['Polo', 'Blanca', 15], 2:['Polo', 'Azul', 15], 3: ['Polo', 'Roja', 15], 4: ['Polo', 'Amarilla', 15], 5: ['Cuello redondo', 'Gris', 12], 6: ['Cuello redondo', 'Negro', 12], 7: ['Cuello redondo', 'Verde', 12]}
jean = {1: ["Azul", 20], 2:["Verde", 20], 3:["Café", 20], 4: ["Negro", 20], 5: ["Gris", 20]}
zapatos = {1:['Botas', 'Café', 25], 2: ['Tenis', 'Azul', 20], 3:['Botas', 'Negro', 25], 4: ['Tenis', 'Blanco', 20]}
while True:
    nom=input("escriba su nombre por favor")
    iden=input("escriba su cédula")
    dir=input("escriba la direccción")
    tel=input("escriba el número de teléfono")

    print(camisetas)
    cami=int(input("señor usuario, elija la camiseta que más le gusta\n Si desea una polo blanca, elija 1\n polo azul a 15, 2\n polo roja a 15, 3\n polo amarilla a 15, 4\n cuello redondo gris a 12, 5\n cuello redondo gris, 6\n cuello redondo verde a 12, 7"))
    
    if cami==1:
        a=(camisetas[1])
    elif cami==2:
        a=(camisetas[2])
    elif cami==3:
        a=(camisetas[3])
    elif cami==4:
        a=(camisetas[4])
    elif cami==5:
        a=(camisetas[5])
    elif cami==6:
        a=(camisetas[6])
    elif cami==7:
        a=(camisetas[7])
    list1.append(a)
    print(list1)


    je=int(input("señor usuario, elija el jean que más le gusta\n Si desea un jean azul a 20, elija 1\n jean verde a 20, 2\n jean café a 20, 3\n jean negro a 20, 4\n jean gris a 20"))

    if je==1:
        b=(jean[1])
    elif je==2:
        b=(jean[2])
    elif je==3:
        b=(jean[3])
    elif je==4:
        b=(jean[4])
    elif je==5:
        b=(jean[5])

    list1.append(b)
    print(list1)
    zapa=int(input("señor usuario, elija las botas que más le gusta\n Si desea botas café a 25, elija 1\n tenis azules a 20, 2\n botas negras a 25, 3\n tenis blancos a 20, 4."))
    if zapa==1:
        c=(zapatos[1])
    elif zapa==2:
        c=(zapatos[2])
    elif zapa==3:
        c=(zapatos[3])
    elif zapa==4:
        c=(zapatos[4])
    list1.append(c)
    print(list1)
    print(list1[0][2]+list1[1][1]+list1[2][2])

    x=int(input("desea continuar, escriba 1, 2 para salir"))
    if x==1:
        continue
    elif x==2:
        print("chao")
        break
