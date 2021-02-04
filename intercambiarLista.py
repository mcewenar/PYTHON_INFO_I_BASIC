#Intercambiar elementos de una lista

miLista = []
while True:
    ingre = int(input("Ingresa cualquier otro número si quieres ingresar un elemento de lista. Ingresa -1 si no quieres continuar: "))
    if ingre == -1:
        longitud = len(miLista)
        for i in range (longitud // 2): #Esto intercambia cualquier tamaño de lista
            miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]
        print("Elementos intercambiados",miLista)
        break
    
    else:
        ele=int(input("Ingresa un número"))
        miLista.append(ele)
        print(miLista)
        continue