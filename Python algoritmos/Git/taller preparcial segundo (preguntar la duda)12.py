list1=[]
list2=[]
cont=0
def act():
    if y=="biomédica" or y=="BIOMÉDICA" or y=="Biomédica":
        act="B-2018-"+str(cont)
        return act
    elif y=="sistemas" or y=="Sistemas" or y=="SISTEMAS":
        act="S-2018-"+str(cont)
        return act
    elif y=="infraestructura" or y=="Infraestructura" or y=="INFRAESTRUCTURA":
        act="I-2018-"+str(cont)
        return act
def ser():
    
    while True:
        try:
            ser=int(input("ingrese el serial"))
            return ser
        except ValueError:
            print("sólo se permiten números")
        
        
        
while True:
    x=int(input("Escriba 1 si desea ingresar un activo\n 2 si desea buscar un activo\n 3 si desea salir"))
    if x==1:
        while True:
            cont=1+cont
            y=input("Ahora ingrese el área al cual pertenece (con tilde)")
            if y=="biomédica" or y=="BIOMÉDICA" or y=="Biomédica":
                
                nom=input("ingrese el nombre")
                marc=input("ingrese la marca")
                ser=ser()
                mant=input("ingrese cada cuánto se hace mantenimiento")
                cali=input("ingrese cada cuánto se hace calibración")
                act=act()
                list1=[nom,marc,ser,mant,cali,act]
                print(list1)
                break

            elif y=="sistemas" or y=="Sistemas" or y=="SISTEMAS":
                
                nom=input("ingrese el nombre")
                marc=input("ingrese la marca")
                ser=ser()
                mant=input("ingrese cada cuánto se hace mantenimiento")
                cali=input("ingrese cada cuánto se hace calibración")
                act=act()
                list1=[nom,marc,ser,mant,cali,act]
                print(list1)
                break

            elif y=="infraestructura" or y=="Infraestructura" or y=="INFRAESTRUCTURA":
                nom=input("ingrese el nombre")
                marc=input("ingrese la marca")
                ser=ser()
                mant=input("ingrese cada cuánto se hace mantenimiento")
                cali=input("ingrese cada cuánto se hace calibración")
                act=act()
                list1=[nom,marc,ser,mant,cali,act]
                print(list1)
                break
            
            list2.append(list1)
            print(list2)
    elif x==2:
        c=int(input("ingrese el número del serial del equipo que desea buscar"))
        if c==list1[2]:
            print("nombre: "+list1[0])
            print("marca: "+list1[1])
            print("serial: "+str(list1[2]))
            print("mantenimiento: "+list1[3])
            print("calibración: "+list1[4])
            print("Número de activo: "+list1[5])
            continue
        elif c!=list1[2]:
            print("El activo no existe")
            continue
    elif x==3:
        print("Feliz día")
        break
    
       
