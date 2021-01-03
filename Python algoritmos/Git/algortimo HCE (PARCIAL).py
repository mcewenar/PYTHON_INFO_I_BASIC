print("esto es un programa para guardar listas de pacientes")
hce=[]
p=[]
for i in range(1000):
    nom=input("ingrese el nombre")
    iden=int(input("ingrese número de identificación"))
    ed=int(input("ingrese edad"))
    eps=input("ingrese EPS")
    p=[nom,iden,ed,eps]
    hce.append(p)
    s=int(input("¿Desea ingresar otro paciente? Sí-1 o No-2"))
    if s==1:
        continue
    else:
        break
print(hce)
print(i)

print("finalizado")
    
    
