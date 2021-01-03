#Historia clinica
lista=[]
i=1
d=0
HCE=0000
archivo=open("HCE_FINAL.txt","a+")
hce={}
EPS={1:"Coomeva", 2:"Sura", 3:"Sanitas", 4:"IPS UdeA", 5:"Sisben"}

nuevoing={1:"Si", 2:"No"}
print("A continuación se creará una histroria clínica electrónica")
while True:
    for i in range(1000):
        HCE=HCE+i
        usuario=input("Ingrese nombres y apellido ")
        while usuario.isdigit():
            print("ingresaste una invalidacion")
            usuario=input("Por favor ingrese su nombre y apellido ")
        lista.append(usuario)
        archivo.write("\n"+"Paciente: "+usuario)
        while True:
            try:
                pw=int(input("Ingrese su cédula "))
                lista.append(pw)
                break
            except ValueError:
                print("Solo se admiten valores numéricos. Intente nuevamente ")
        archivo.write("\n"+"cedula: "+str(pw))
        while True:
            try:
                print("Ingrese su edad ")
                edad=int(input())
                lista.append(edad)
                break
            except ValueError:
                print("Solo se admiten valores numéricos. Intente nuevamente ")
            archivo.write("\n"+" Edad: "+str(edad))
        while True:
            try:
                print("Indique a qué EPS pertenece o si pertenece al Sisben ")
                print(EPS)
                eps=int(input())
                lista.append(EPS[eps])
                X=lista[3]
                break
            except KeyError:
                print("Ingrese un dato válido ")
        if eps==5:
            regimen="EPS-S"
        if 1<=eps<=4:
            regimen="EPS"
        archivo.write("\n"+"Regimen: "+str(X))
        clave="HCE-"+regimen+"-"+str(HCE)

        hce[clave]=[lista]
        print(hce)
        print("Desea ingresar un nuevo paciente? ")
        print(nuevoing)
        nuevoing=int(input())
        if nuevoing==1:
            lista=[]
            continue    
        elif nuevoing>=2:
##            print("nombre: "+usuario)
##            print("cedula: "+str(pw))
##            print("Edad: "+str(edad))
##            print("Regimen: "+str(X))
            contenido=archivo.readlines()
            print(contenido)
            print("Ha finalizado su proceso. Hasta luego")
            break
        break
    break
archivo.close()

 
