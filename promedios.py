while True:
    print('Este programa le calculará la nota final de una materia, luego de\n ingresar las 5 notas del semestre')
    n1 = float(input("Ingrese la nota 1 (30%): "))
    if n1<0 or n1>5:
        print("Recuerde que las notas deben estar entre 0 y 5. Intente de nuevo por favor")
        n1 = float(input("Ingrese la nota 1 (30%): "))
    n2 = float(input("Ingrese la nota 2 (15%): "))
    if n2<0 or n2>5:
        print("Recuerde que las notas deben estar entre 0 y 5. Intente de nuevo por favor")
        n2 = float(input("Ingrese la nota 2 (15%): "))
    n3 = float(input("Ingrese la nota 3 (15%): "))
    if n3<0 or n3>5:
        print("Recuerde que las notas deben estar entre 0 y 5. Intente de nuevo por favor")
        n3 = float(input("Ingrese la nota 3 (15%): "))
    n4 = float(input("Ingrese la nota 4 (20%): "))
    if n4<0 or n4>5:
        print("Recuerde que las notas deben estar entre 0 y 5. Intente de nuevo por favor")
        n4 = float(input("Ingrese la nota 4 (20%): "))
    n5 = float(input("Ingrese la nota 5 (20%): "))
    if n5<0 or n5>5:
        print("Recuerde que las notas deben estar entre 0 y 5. Intente de nuevo por favor")

        n5 = float(input("Ingrese la nota 5 (20%): "))
    notaf = (n1*0.3 + n2*0.15 + n3*0.15 + n4*0.2 + n5*0.2)
    if notaf >= 3:
        print ("Su nota final fue: {0} - APROBADO".format(notaf))
    else:
        print ("Su nota final fue: {0} – REPROBADO".format(notaf))
    print ("--------------------------")
    op = int(input("Desea evaluar otro estudiantes. 1- Si o 2-No: "))
    if op == 1:
        continue
    else:
        break
print("Fin de programa.")