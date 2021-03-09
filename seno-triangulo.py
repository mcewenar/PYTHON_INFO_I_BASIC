import math as n

def lado_triangulo(a,b,c):
    if user==1:
        c=n.sin(c)
        angulo = (a*c)/b
        angulo= n.degrees(n.asin(angulo))
        #print(type(angulo))
        print(angulo,"°")
    elif user == 2:
        b=n.degrees(n.sin(b))
        c=n.degrees(n.sin(c))
        lado = (a*b)/c
        #print(type(lado))
        print(lado,"cm")
while True:
    try:
        user = int(input("Elija 1 si desea hallar ángulo;\n elija 2 si desea hallar el lado;\nelija 3 para salir: "))
        print()
        if user == 1:
            lado_a = float(input("Ingrese lado a: "))
            lado_b = float(input("Ingrese lado b: "))
            angulo_alfa=float(input("Ingrese el ángulo alfa (en grados): "))
            lado_triangulo(lado_a,lado_b,angulo_alfa)
        elif user == 2:
            a=float(input("Ingrese el lado a: "))
            angulo_alfa=float(input("Ingrese el ángulo alfa (en grados): ")) #B
            angulo_beta=float(input("Ingrese el ángulo beta (en grados): ")) #C
            lado_triangulo(a,angulo_alfa,angulo_beta)
        elif user == 3:
            print("Feliz tarde")
            break
        else:
            print()
            print("No se admiten más opciones. Reintenta de nuevo")
            continue
    except ValueError:
        print()
        print("No se admiten carácteres")


