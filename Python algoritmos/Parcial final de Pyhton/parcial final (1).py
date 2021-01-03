
def NUMHCE(dic,eps):
    actual=0
    if eps=="SISBEN":
        key="HCE-EPS-S-"
    else:
        key="HCE-EPS-"
        
    for k,v in dic.items():
        modKey=k.replace("HCE-EPS-S-","").replace("HCE-EPS-","")
        actual=int(modKey)

    actual+=1
    numZeros=(4-len(str(actual)))*"0"
    key=key + numZeros + str(actual)
    return key

def validarID():
    while True:
        try:
            ID=int(input("ingrese la identificacion de el paciente: "))
        except ValueError:
              print("ingresó letras en vez de numeros")
              continue
        return ID
            
        
            
def validarEDAD():
    while True:
        try:
            edad=int(input("ingrese la edad de el paciente: "))
        except ValueError:
            print("ingresó letras en vez de numeros")
            continue   
        return edad
    
        
x=True
EPS={1: "Coomeva", 2: "Sura", 3: "Sanitas", 4: "IPS UdeA", 5: "SISBEN" }
hce={}
while(x):
        
        datos=[]
        nom=input("ingrese el nombre y los apellidos del paciente: ")
        ID=validarID()
        edad=validarEDAD()
        epsValidas=int(input("ingrese numero de la eps a la cual pertenece:\n\t1 - coomeva\n\t2 - sura\n\t3 - sanitas\n\t4 - ips udea\n\t5 - sisben\n "))
        eps=EPS[epsValidas]

        key=NUMHCE(hce,eps)    
        
        datos=[nom,ID,edad,eps]

        hce[key]=datos

        a=input("ingrese 1 si desea ingresar otro paciente, sino oprima cualquier otra tecla para salir: ")
        if a!="1":
            x=False
            

for k,v in hce.items():
    print("numero de historia clinica: "+k)
    
    print ("\tnombre y apellidos del paciente: " +v[0])
 
    
    print("\tidentificacion:"+str(v[1]))
    
   
    print ("\tedad:"+str(v[2]))
    
    
    print("\teps:"+v[3])

    print ("")
