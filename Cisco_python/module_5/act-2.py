
#Ya sabes como funiona el método split(). Ahora queremos que lo pruebes.

#Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

#Debe aceptar únicamente un argumento: una cadena.
#Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
#Si la cadena está vacía, la función debería devolver una lista vacía.
#Su nombre debe ser misplit().
#Usa la plantilla en el editor. Prueba tu código con cuidado.

#Salida esperada
#['Ser', 'o', 'no', 'ser', 'esa', 'es,', 'la', 'pregunta']
#['Ser', 'o', 'no', 'ser,esa', 'es', 'la', 'pregunta']
#[]
#['abc']
#[]

def misplit(strng):
    return strng.split()
    #if strng == " ":
    #    print([])
    #else:
    #    c=strng.replace(" ",",")

    #    print(c)
print("-----")
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))