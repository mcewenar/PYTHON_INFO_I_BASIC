print("Éste es un programa para recolectar la información de aquellos participantes cuyo número elegido al azar sea primo")
lista1=[]
lista2=[]
while True:
    while True:
        x=int(input("escribir un número"))
        if not(x%2==0) and not(x%5==0)and not(x%11==0)and not(x%4==0)and not(x%9==0)and not(x%7==0)and not(x%3==0)and(x%x==0)and not(x%8==0):
            print("el número es primo")
            break
        elif x==2:
            print("es primo")
            break
        elif x==3:
            print("es primo")
            break
        elif x==5:
            print("es primo")
            break
        elif x==7:
            print("es primo")
            break
        elif x==11:
            print("es primo")
            break
        else:       
            continue
    
    ce=float(input("por favor ingrese la cédula"))
    nom=str(input("por favor ingresar nombre completo"))
    ps=float(input("ingresar peso"))
    dire=input("ingrese su dirección")
    lista1=[ce,nom,ps,dire]
    print(lista1)
    mod1=int(input("si desea modificar su peso y dirección, por favor elija la opción 1; de lo contrario, se tomará como una negación"))
    if mod1==1:
        qs=int(input("por favor escriba nuevamente su peso"))
        barr=input("por favor escriba nuevamente la dirección")
        lista1[3]=barr
        lista1[2]=qs
    else:
        print("entendido")
        
    
    lista2.append(lista1)
    sal=int(input("si desea continuar ingresar 1, cualquier otro número se tomará como salir"))
    if sal==1:
        continue
    else:
        print(lista2)
        print("usted ha finalizado sesión. Nos vemos pronto")
        break
    


