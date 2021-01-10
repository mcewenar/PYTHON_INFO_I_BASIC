#print("Dime algo...")
#algo = input()
#print("Mmm...", algo, "...¿en serio?")
#cualquierNumero = int(input("Inserta un número: "))
#algo = cualquierNumero ** 2.0
#print(cualquierNumero, "al cuadrado es", algo)

while 1==1:
    cateto_a = float(input("Inserta la longitud del primer cateto: "))
    cateto_b = float(input("Inserta la longitud del segundo cateto "))
    if (cateto_a < 0) or (cateto_b < 0):
        print("ingreso incorrecto")
    else:
        hipo = (cateto_a**2 + cateto_b**2) ** .5 #sqrt(5)== 0.5
        print("La longitud de la hipotenusa es: ", round(hipo,2), "cm")
        #print("La longitud de la hipotenusa es: " + str(cateto_a**2 + cateto_b**2) **.5+"cm")
        print("See you later")
        