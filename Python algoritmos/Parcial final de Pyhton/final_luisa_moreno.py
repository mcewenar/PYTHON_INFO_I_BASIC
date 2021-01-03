lista=[]
inventario={}
i=0
equipo=0
ubicacion = {1: "ICU", 2:"UCE", 3: "Cirugía", 4: "Hospitalización", 5: "Ingeniería"}
area = {1: "Área Biomédica", 2:"Área de Sistemas", 3: "Área de infraestructura", 4: "Otra área"}
activo = {1: "SI", 2:"No"}
archivo=open("inventario.txt","r+")
print("A continuación se realizará un inventario de los equipos de la IPS")
while True:
    for i in range(3):
        equipo=equipo+i
        marca=input("Ingrese por favor la marca del equipo ")
        while marca.isdigit():
            print("Este campo solo permite letras. Ingrese un dato válido")
            marca=input("Ingrese por favor la marca del equipo ")
        lista.append(marca)
        archivo.write("Marca: "+marca)
        A=lista[0]
        while True:
            try:
                print("Ingrese por favor el número del serial ")
                serial=int(input())
                lista.append(str(serial))
                break
            except ValueError:
                print("Este campo solo permite números. Ingrese un dato válido ")
        archivo.write("\n"+"Serial: "+str(serial))
        B=lista[1]
        while True:
            try:
                print("Seleccione la ubicación donde se encuentr el equipo ")
                print(ubicacion)
                ub=int(input())
                lista.append(ubicacion[ub])
                break
            except KeyError:
                print("Ingreso invalido. Seleccione una de las opciones que se encuentran en el menú")
            except ValueError:
                print("Ingreso invalido. Seleccione una de las opciones que se encuentran en el menú")
        X=lista[2]
        archivo.write("\n"+"Ubicacion: "+X)
        while True:
            try:
                print("Seleccione el área donde al que pertece el equipo ")
                print(area)
                ar=int(input())
                lista.append(area[ar])
                break
            except KeyError:
                print("Ingreso invalido. Seleccione una de las opciones que se encuentran en el menú")
            except ValueError:
                print("Ingreso invalido. Seleccione una de las opciones que se encuentran en el menú")
        Y=lista[3]
        archivo.write("\n"+"Area: "+Y)
        while True:
            try:
                print("El equipo se encuentra activo? ")
                print(activo)
                ac=int(input())
                lista.append(activo[ac])
                break
            except KeyError:
                print("Ingreso invalido. Seleccione una de las opciones que se encuentran en el menú")
            except ValueError:
                print("Ingreso invalido. Seleccione una de las opciones que se encuentran en el menú")
        Z=lista[4]
        archivo.write("\n"+"Activo: "+Z)
        print("Marca: "+str(A))
        print("Serial: "+str(B))
        print("Ubicacion: "+str(X))
        print("Area: "+str(Y))
        print("Activo: "+str(Z))
    
    print("Qué desea hacer? Marque:\n 1-Ingresar un nuevo equipo\n 2. Mostrar su información.\n 3. salir del programa")
    op=int(input())
    if op==1:
        lista=[]
        continue
    if op==2:
        lista=[]
        print("Ingrese el serial del equipo que desea verificar")
        serial1=int(input())
        a=open("inventario.txt")
        contenido=archivo.readlines()
        print(contenido)
      
    if op==3:
        print("Ha finalizado su proceso ")
    break
archivo.close()




            
