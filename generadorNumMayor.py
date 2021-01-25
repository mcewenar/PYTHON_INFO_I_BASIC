#lee tres números
# lee tres números
list1=[]
while True:
    a=int(input("Ingresa 1 para agregar número"))
    if a==1:
        numero1=int(input("Ingresa cualquier número"))
        list1.append(numero1)
    else:
        print("El número más grande es: " + str(max(list1)))
        break

    


