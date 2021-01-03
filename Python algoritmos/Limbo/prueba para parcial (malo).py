#Historia clínica
lista=[]
hce={}
i=1
d=0
HCE=0000
##hce = {"HCE-EPS-0001":["ID", "Nombre", "edad", "EPS", "edad"]}
EPS= {1: "Coomeva", 2: "Sura", 3: "Sanitas", 4: "IPS UdeA", 5: "SISBEN"}
nuvo={1:"sí", 2:"no"}
print("a continuación se crerá una historia clínica")
while True:
    for i in range(2):
        while True:
            try:
                HCE=HCE+i
                nom=str(input("escriba nombre y apellido"))
                lista.append(nom)
                break
            except ValueError:
                print("por favor no ingrese números")
                print("escriba nombre y apellido")
                
        while True:
            try:
                ID=input("Ingrese número ID")
                lista.append(ID)
                break
            except ValueError:
                print("has ingresado valores incorrectos")
                
        while True:
            try:
                ed=int(input("ingresa la edad"))
                lista.append(ed)
                break
            except ValueError:
                print("solo se admiten números")
                
        while True:
            try:
                print("indique a qué EPS pertenece, o si pertenece al SISBEN")
                print(EPS)
                eps=int(input())
                lista.append(EPS[eps])
                X=lista[3]
                break
            except KeyError:
                print("ingrese un dato valido")
        if eps==5:
            regimen="EPS-S"
        elif 1<=eps<=4:
            regimen="EPS"
        clave="HCE-"+regimen+"-"+str(HCE)

        hce[clave]=[lista]
    try:
        print(hce)
        print("desea agregar un nuevo paciente? Escribe 1 si si; 2 si no")
        print(nuvo)
        nuvo=int(input())
        if nuvo==1:
            lista=[]
            continue
        elif nuvo>=2:
            print("ha finalizado su proceso")
        break
    except KeyError:
        print(hce)
        continue
    break
