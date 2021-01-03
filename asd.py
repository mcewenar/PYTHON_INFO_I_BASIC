while True:
    resultado = "No hay resultado disponible"
    print ("Seleccione una de las siguientes opciones\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
    op = int(input())
    print("\n")
    if op == 1:
        num1 = int(input("Ingrese el 1er número: "))
        num2 = int(input("Ingrese el 2do número: "))
        resultado = num1 + num2
    elif op == 2:
        num1 = int(input("Ingrese el 1er número: "))
        num2 = int(input("Ingrese el 2do número: "))
        resultado = num1 - num2
    elif op == 3:
        num1 = int(input("Ingrese el 1er número: "))
        num2 = int(input("Ingrese el 2do número: "))
        resultado = num1 * num2
    elif op == 4:
        num1 = float(input("Ingrese el numerador: "))
        num2 = float(input("Ingrese el denominador: "))
        if num2 == 0:
            print("La operación no se puede realizar. La división por cero no existe")
        else:
            resultado = num1 / num2
    elif op == 5:
        break
    else:
        print("Seleccionó una opción no válida. Intente de nuevo")
        continue
    print(resultado)