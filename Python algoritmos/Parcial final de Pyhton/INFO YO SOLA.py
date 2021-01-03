lista=[]
ubicación={1:"ICU", 2:"UCE", 3:"Cirugía", 4:"Hospitalización", 5:"Ingeniería"}
área={1:"Área biomédica", 2:"Área de sistemas", 3:"Área de infraestructura", 4:"Otra área"}
activo={1:"Si", 2:"No"}
opcion={1:"Si", 2:"No"}
for i in range (3):
    print ("Ingrese la marca del equipo: ")
    marca=input()
    lista.append(marca)
    while True:
        try:
            print("Ingrese el número de serie del equipo: ")
            serial=int(input())
            lista.append(serial)
            break
        except ValueError:
            print("Este campo permite solo números, intentelo de nuevo")
    print("Ingrese la ubicación a la cual pertenece el equipo")
    print(ubicación)
    ubicacion=int(input())
    lista.append(ubicación[ubicacion])
    print("Ingrese el área al cual pertenece el equipo")
    print(área)
    Area=int(input())
    lista.append(área[Area])
    print("¿Está su equipo activo?: ")
    print(activo)
    estado=int(input())
    lista.append(estado)
for d in range (2):
    print("¿Desea hacer la búsqueda de un equipo?: ")
    print(opcion)
    respuesta=int(input())
    if respuesta==1:
        print("Ingrese el número del serial del equipo que desea buscar: ")
        serial1=int(input())
        if serial1 in lista:
            Y=lista.index(serial1)
            M=Y-1
            P=Y+1
            L=Y+2
            W=Y+3
            print("La marca del equipo es: ",lista[M])
            print("El número del serial de equipo es: ",lista[Y])
            print("La ubicación del equipo es: ",lista[P])
            print("El área del equipo es: ",lista[L])
            print("El estado del equipo es: ",lista[W])
        else:
            print("Éste número de serial no se encuentra en la base de datos")
            break
    else:
        print("Hasta luego")
        break 
    


    
          
