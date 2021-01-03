#Práctica de preparcial
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
    x=int(input("escriba 1 si desea ingresar un activo \n2 si desea buscar un activo \n3 si desea salir"))
    if x==1:
        while True:
            cont=1+cont
            y=input("Ahora ingrese el área al cual pertenece (con tilde). Si no desea continuar, eliga cualquier otro caracter")
            if y=="biomédica" or y=="BIOMÉDICA" or y=="Biomédica":
                
                nom=input("ingrese el nombre")
                marc=input("ingrese la marca")
                vari=ser()
                mant=input("ingrese cada cuánto se hace mantenimiento")
                cali=input("ingrese cada cuánto se hace calibración")
                conta=act()
                list1=[nom,marc,vari,mant,cali,conta]
                print(list1)
                break
            elif y=="sistemas" or y=="SISTEMAS" or y=="Sistemas":
                nom=input("ingrese el nombre")
                marc=input("ingrese la marca")
                vari=ser()
                mant=input("ingrese cada cuánto se hace mantenimiento")
                conta=act()
                list1=[nom,marc,vari,mant,conta]
                print(list1)
            elif y=="infraestructura" or y=="Infraestructura" or y=="INFRAESTRUCTURA":
                nom=input("ingrese el nombre")
                marc=input("ingrese la marca")
                vari=ser()
                mant=input("ingrese cada cuánto se hace mantenimiento")
                conta=act()
                list1=[nom,marc,vari,mant,conta]
                print(list1)
            else:
                break
            
                



    elif x==2:
        if len(list1)>0:
            c=int(input("ingrese el número del serial del equipo que desea buscar"))
            if c==list1[2]:
                print("nombre: "+list1[0])
                print("marca: "+list1[1])
                print("serial: "+str(list1[2]))
                print("mantenimiento: "+list1[3])
                print("calibración: "+list1[4])
            elif c!=list1[2]:
                print("El activo no existe")
                continue
        else:
            print("primero hay que rellenar un activo")
            continue

    elif x==3:
        print("feliz día")
        break
    list2.append(list1)
    print(list2)
