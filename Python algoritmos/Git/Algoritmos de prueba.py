print("Calculadora sencilla")
a=int(input("escoger una operacion aritmética elemental: suma=1, resta=2, multiplicación=3, 4=división, 5=salir"))
while True:
     try:
        if a==1:
            x=int(input("elija un número a sumar"))
            y=int(input("elija otro número a sumar"))
            print(x+y)
            break
        elif a==2:
            x=int(input("elija un número a restar"))
            y=int(input("elija otro número a restar"))
            print(x-y)
            break
        elif a==3:
            x=int(input("elija un número a multiplicar"))
            y=int(input("elija otro número a multiplicar"))
            print(x*y)
            break
        elif a==4:
            x=int(input("elija el numerador"))
            y=int(input("elija el denominador"))
            print(x/y)
            break
        elif a==5:
            print("gracias por utilizar la calculadora")
            break
     except ValueError:
            print("¡Error! Sumaste datos incompatibles, vuelve a ingresar los números:")
     except ZeroDivisionError:
            print("¡ERROR!Dividiste entre 0, vuelve a ingresar los números")

