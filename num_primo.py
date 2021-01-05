def parimpar(x):
    if x%2 == 0:
        return "es par"
    else:
        return "es impar"

x=int(input("Ingrese un número"))
print(parimpar(x))
