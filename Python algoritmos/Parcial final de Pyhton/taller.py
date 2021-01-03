while True:
    hce={}
    lista=[]
    ##eps={1:"coomeva",2:"sura",3:"sanitas",4:"ips udea",5:"sisben"}
    a=str(input("historia clinica"))
    b=str(input("nombbre"))
    c=str(input("ingrese algo"))
    lista.append(a)
    lista.append(b)
    lista.append(c)

    ##hce.add(lista)
    ##print (hce)
    hce[a]=lista
    print(hce)
    print(hce[a])

    op=int(input("1 seguir,2 salir"))
    if op==1:
        hce={}
        lista=[]
        ##eps={1:"coomeva",2:"sura",3:"sanitas",4:"ips udea",5:"sisben"}
        a=str(input("historia clinica"))
        b=str(input("nombbre"))
        c=str(input("ingrese algo"))
        lista.append(a)
        lista.append(b)
        lista.append(c)

        ##hce.add(lista)
        ##print (hce)
        hce[a]=lista
        print(hce)
        print(hce[a])
    else:
         break
    
