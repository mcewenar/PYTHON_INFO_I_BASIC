#El Procesador de Números
#El tercer programa muestra un método simple que permite ingresar una línea llena de números y sumarlos fácilmente. 
#Nota: la función input(), combinada junto con las funciones int() o float(), no es lo adecuado para este propósito.

#Procesador de números


#Forma másinteresante:
def sumaNum(enteros):
    if enteros != "":
        listado = list(enteros)
        total = 0
        for substr in listado:
            total += int(substr)
        return total
    else:
        print("No has ingresado valor\nVuelve a intentarlo\n")
        return "vacío"
            
    

while True:
    try:
        linea = input("Ingresa una línea de números enteros: ")
        print(linea)
        #print(type(linea))
        substr=sumaNum(linea)
        print("El total es:", substr)
        print()
        
    except:
        print(linea, "no es un numero entero")

#Forma predeterminada (con flotantes):
#linea = input("Ingresa una línea de números, sepáralos con espacios: ")
#strings = linea.split()
#total = 0
#try:
#    for substr in strings:
#        total += float(substr)
#    print("El total es:", total)
#except:
#    print(substr, "no es un numero.")
