x=1
while x:
    while True:
        try:
            nomb=(input("ingrese su nombre y apellido"))
            break
        except ValueError:
            print("vuelva a ingresar su nombre")
        except SyntaxError:
            print("asdsad")
        except NameError:
            print("error nombre")
        except TypeError:
            print("error tipo")
        except NameError:
            print("nombre malo")
    while True:
        try:
            ID=input("ingrese identificación")
            break
        except ValueError:
            print("no")
            
        
    datos=[ID,nomb]
    car=[]
    carreras={1:"BIOING", 2:"ING. DE SISTEMAS", 3:"Ing. industrial"}

    c=int(input("ingrese la carrera a la que pertenezcas 1: Bioing., 2:ing. sistemas, 3: indufácil"))

    if c==1:
        car.append(carreras[1])
    if c==2:
        car.append(carreras[2])
    if c==3:
        car.append(carreras[3])

    mat=[]
    materias={111: ["Cálculo", 4, "MJ8-10"], 222: ["Física", 6, "WV8-10"], 333: ["Geometría", 4, "MJ10-12"], 444: ["Expresión Gráfica", 4, "MJ18-20"], 000: ["Inglés",0, "WV12-14"], 1555: ["Introducción a la Bioingeniería", 2, "S8-12"], 2555: ["Introducción a los sistemas", 2, "MJ6-8"], 3555: ["Introducción a Industrial", 2, "WV6-8"] }
    print("seleccione las cuatro materias que desea ingresar")
    if c==1:
        for i in range(4):
            m=int(input("1-cálculo, 2-..."))
            if m==1:
                mat.append(materias[111])
            elif m==2:
                mat.append(materias[222])
            elif m==3:
                mat.append(materias[333])
            elif m==4:
                mat.append(materias[444])
            elif m==5:
                mat.append(materias[000])
            elif m==6:
                mat.append(materias[1555])
    elif c==2:
        for i in range(4):
            m=int(input("1-calculo, 2-sistemas"))
            if m==1:
                mat.append(materias[111])
            elif m==2:
                mat.append(materias[222])
            elif m==3:
                mat.append(materias[333])
            elif m==4:
                mat.append(materias[444])
            elif m==5:
                mat.append(materias[000])
            elif m==6:
                mat.append(materias[1555])
    elif c==3:
        for i in range(4):
            m=int(input("1-calculo, 2-sistemas"))
            if m==1:
                mat.append(materias[111])
            elif m==2:
                mat.append(materias[222])
            elif m==3:
                mat.append(materias[333])
            elif m==4:
                mat.append(materias[444])
            elif m==5:
                mat.append(materias[000])
            elif m==6:
                mat.append(materias[1555])
    print("los datos del estudiante son")
    print(datos[0])
    print(datos[1])
    print("la carrera")
    print(car)
    print("materias elegidas:")
    print(mat[0])
    print(mat[1])
    print(mat[2])
    print(mat[3])


    a=mat[1]
    a=a[1]
    a=int(a)

    b=mat[1]
    b=b[1]
    b=int(b)

    c=mat[1]
    c=c[1]
    c=int(c)

    d=mat[1]
    d=d[1]
    d=int(d)
    print("el número total de créditos")
    cred=a+b+c+d
    print(cred)

    x=input("desea matricular otra materia? Sí=1, no=2")
if x==1:
    x=True

else:
    x=False
