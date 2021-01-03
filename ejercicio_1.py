print("Programa para calificar tareas")

notas = int(input("desea ingresar el número de notas? Sí = 1, No=2"))
if notas == 1:
    while True:
        n = int(len(input("Ingrese las notas a promediar")))
        n = n + 1
        d = int(input("desea continuar agregar más notas?"))
        if d == 1:
            continue
        else: 
            print(n*len(n)/)
            

else: 
    print("chao")
