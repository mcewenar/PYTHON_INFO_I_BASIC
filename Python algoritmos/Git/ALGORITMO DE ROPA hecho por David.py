x=1
while (x):
    arti=[]
    datos=[]
    nomb=input("ingrese el nombre")
    datos.append(nomb)
    iden=input("ingrese cédula")
    datos.append(nomb)
    tel=int(input("ingrese el telefono"))
    datos.append(tel)
    print(datos)

    camisetas={1: ["Polo", "Blanca", 15], 2:["Polo", "Azul", 15], 3: ["Polo", "Roja", 15], 4:
    ["Polo", "Amarilla", 15], 5: ["Cuello redondo", "Gris", 12], 6: ["Cuello redondo", "Negro",
    12], 7: ["Cuello redondo", "Verde", 12]}
    c=int(input("camisetas 1= polo..."))

    if c==1:
        arti.append(camisetas[1])
    if c==2:
        arti.append(camisetas[2])
    if c==3:
        arti.append(camisetas[3])
    if c==4:
        arti.append(camisetas[4])
#Lo mismo para jeans y zapatos.
    print("los datos se mostrarán a continuación")
    print(datos)
    print("los articulos se mostrarán a continuación")
    print(arti)

    a=arti[0]
    a=a[2]
    a=int(a)
    b=arti[1]
    b=a[1]
    b=int(b)
    c=arti[2]
    c=c[2]
    c=int(0)
    print("el valor de los artículos son")
    v=a+b
    print(v)

    x=int(input("desea continuar con otra compra: sí=1, no=2"))
    if x==1:
        x==True
    else:
        x=False



        
    
        
    
