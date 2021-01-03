print("Historia clinica")
##if op==1:
while True:
    try:
        def datos():
            hce=[]
            for i in range(1):
                    nom=str(input("Nombre y apellido"))
                    eps=str(input("EPS"))
                    ide=int(input("ingrese identificaciÃ³n"))
                    eda=int(input("ingresa edad"))
                    a=(nom,eps,ide,eda)
                    hce.append(a)
                    print(type(hce))
                    print(hce)
        datos()
        op=int(input("1 para continuar, 2 para salir"))
        if op==1:
            def datos():
                hce=[]
                for i in range(2):
                        nom=input("Nombre y apellido")
                        eps=str(input("EPS"))
                        ide=int(input("ingrese identificaciÃ³n"))
                        eda=int(input("ingresa edad"))
                        a=(nom,eps,ide,eda)
                        hce.append(a)
                        print(type(hce))
                        print(hce)
        
        elif op==2:
            break
        
    except ValueError:
        print("Repita el dato")
        
    except TypeError:
        print("una funcion es llamada")
    except SyntaxError:
        print("el codigono puede ser analizado")
    except NameError:
        print("una variable desconocida")
    except IndexError:
        print("falla de importacion")
    except ImportError:
        print("error de importacion")




