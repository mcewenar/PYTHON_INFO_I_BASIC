while True:
    try:
        num1 = int(input("Ingrese el numerador"))
        num2 = int(input("Ingrese el denominador"))
        print(num1/num2)
        print("División correcta")
        break
    except ZeroDivisionError:
        print("División por cero, error")
    except ValueError:
        print("Dato incorrecto")