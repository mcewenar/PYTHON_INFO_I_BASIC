#Esta programa realizará la matrícula de un estudiante a la UdeA
#Con 4 materias obligatorias, pero las introducciones varian segun la carrera

lista=[]
programas=[]
i=0
d=0
credtot=0
archivo=open("matricula.txt", "a+")
carreras = {1: "Bioingeniería", 2: "Ingeniería de Sistemas", 3: "Ingeniería Industrial"}
materiasbio = {111: ["Cálculo", 4, "MJ8-10"], 222: ["Física", 6, "WV8-10"], 333: ["Geometría", 4, "MJ10-12"],
            444: ["Expresión Gráfica", 4, "MJ18-20"], 000: ["ingles",0, "WV12-14"], 1555: ["Introducción a la Bioingeniería", 2, "S8-12"]}
materiassis = {111: ["Cálculo", 4, "MJ8-10"], 222: ["Física", 6, "WV8-10"], 333: ["Geometría", 4, "MJ10-12"],
            444: ["Expresión Gráfica", 4, "MJ18-20"], 000: ["ingles",0, "WV12-14"], 2555: ["Introducción a los sistemas", 2, "MJ6-8"]}
materiasind = {111: ["Cálculo", 4, "MJ8-10"], 222: ["Física", 6, "WV8-10"], 333: ["Geometría", 4, "MJ10-12"],
            444: ["Expresión Gráfica", 4, "MJ18-20"], 000: ["ingles",0, "WV12-14"], 3555: ["Introducción a Industrial", 2, "WV6-8"]}

nmatri={1:"si", 2:"no"}
busqueda={1:"si", 2:"no"}
print("A continuación realizará su proceso de matrícula")
while True:
    usuario=input("Por favor ingrese su nombre y apellido ")
    while usuario.isdigit():
        print("ingresaste una invalidacion")
        usuario=input("Por favor ingrese su nombre y apellido ")
    lista.append(usuario)
    X= lista[0]
    ID=input("Por favor ingrese su cédula ")
    while not ID.isdigit():
        print("ingresaste una invalidacion")
        ID=input("Por favor ingrese su cédula ")
    lista.append(ID)
    Y=lista[1]
    archivo.write("\n"+usuario+":"+ID)
    while True:
        try:
            print("Ingrese la carrera a la cual pertece ")
            print(carreras)
            carrera=int(input())
            lista.append(carreras[carrera])
            break
        except KeyError:
            print("Ingrese un dato válido ")
    Z=lista[2]            
    if carrera==1:
        for i in range(4):
            print("Ingrese la materia # "+str(i+1)+" que desea matricular: ")
            print(materiasbio)
            materia=int(input())
            lista.append(materiasbio[materia])
            
        A=lista[3][1]
        B=lista[4][1]
        C=lista[5][1]
        D=lista[6][1]
        cred=int(A+B+C+D)
        P=lista[3][0]
        Q=lista[4][0]
        S=lista[5][0]
        T=lista[6][0]
        R=lista[3][2]
        O=lista[4][2]
        U=lista[5][2]
        V=lista[6][2]
        print("Su número total de créditos es: "+str(cred))
        print("Nombre y apellidos: "+str(X))
        print("Cédula: "+str(Y))
        print("Programa: "+str(Z))
        print("Materias: "+str(P+", "+Q+", "+S+", "+T))
        print("Horario: "+str(R+", "+O+", "+U+", "+V))
       
    if carrera==2:
        for i in range(4):
            print("Ingrese la materia # "+str(i+1)+" que desea matricular: ")
            print(materiassis)
            materia=int(input())
            lista.append(materiassis[materia])
        A=lista[3][1]
        B=lista[4][1]
        C=lista[5][1]
        D=lista[6][1]
        cred=int(A+B+C+D)
        P=lista[3][0]
        Q=lista[4][0]
        S=lista[5][0]
        T=lista[6][0]
        R=lista[3][2]
        O=lista[4][2]
        U=lista[5][2]
        V=lista[6][2]
        print("Su número total de créditos es: "+str(cred))
        print("Nombre y apellidos: "+str(X))
        print("Cédula: "+str(Y))
        print("Programa: "+str(Z))
        print("Materias: "+str(P+", "+Q+", "+S+", "+T))
        print("Horario: "+str(R+", "+O+", "+U+", "+V))
        
    if carrera==3:
        for i in range(4):
            print("Ingrese la materia # "+str(i+1)+" que desea matricular: ")
            print(materiasind)
            materia=int(input())
            lista.append(materiasind[materia])
        A=lista[3][1]
        B=lista[4][1]
        C=lista[5][1]
        D=lista[6][1]
        cred=int(A+B+C+D)
        P=lista[3][0]
        Q=lista[4][0]
        S=lista[5][0]
        T=lista[6][0]
        R=lista[3][2]
        O=lista[4][2]
        U=lista[5][2]
        V=lista[6][2]
        print("Su número total de créditos es: "+str(cred))
        print("Nombre y apellidos: "+str(X))
        print("Cédula: "+str(Y))
        print("Programa: "+str(Z))
        print("Materias: "+str(P+", "+Q+", "+S+", "+T))
        print("Horario: "+str(R+", "+O+", "+U+", "+V))
        break
    print("Desea realizar un nuevo proceso de matricula? ")
    print(nmatri)
    nuevamatri=int(input())
    if nuevamatri==1:
        lista=[]
        continue    
    elif nuevamatri>=2:
        print("Ha finalizado su proceso de matricula. Hasta luego")
        break
archivo.close()





