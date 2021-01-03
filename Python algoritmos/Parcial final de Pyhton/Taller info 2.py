lista=[]
i=0
ubicacion={1:"ICU", 2:"UCE", 3:"Cirugía", 4:"Hospitalización", 5:"Ingeniería"}
area={1:"Área biomédica", 2:"Área de sistemas", 3:"Área de infraestructura", 4:"Otra área"}
activo={1:"Si", 2:"No"}
opcion={1:"Si", 2:"No"}

for i in range (3):
    print ("Ingrese la marca del equipo: ")
    marca=input()
    lista.append(marca)
    try:
        print("Ingrese el número de serial del equipo: ")
        serial=int(input())
        lista.append(serial)
    except ValueError:
        print("Éste campo acepta solo números, intentelo de nuevo")
        print ("Ingrese el número de serial del equipo: ")
        serial=int(input())
        lista.append(serial)
    print("Ingrese la ubicación del equipo en la IPS: ")
    print(ubicacion)
    ubicación=int(input())
    lista.append(ubicacion[ubicación])
    print("Ingrese el área al que pertenece el equipo: ")
    print(area)
    área=int(input())
    lista.append(area[área])
    print("Ingrese el estado del equipo: ")
    print(activo)
    estado=int(input())
    lista.append(activo[estado])
for d in range (3):
    print("Desea buscar algún activo?: ")
    print(opcion)
    respuesta=int(input())
    if respuesta==1:
        print("Ingrese el número del serial del activo que quiere buscar: ")
        serial1=int(input())
        if serial1 in lista:
            Y=lista.index(serial1)
            X= Y-1
            Z= Y+1
            W= Y+2
            L= Y+3
            print("La marca del activo es ",lista[X])
            print("La ubicación del activo es ",lista[Z])
            print("El área del activo es ", lista[W])
            print("El estado del activo es", lista[L])
        else:
            print("El serial no se encuentra ingresado en la base de datos")        
    else:
        print ("Hasta luego")
        break 

        
    
      
    
    
    
   
    
        
    
