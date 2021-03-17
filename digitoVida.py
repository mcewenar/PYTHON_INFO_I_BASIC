#Escenario
#Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. 
#Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, 
#se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

#1 Enero 2017 = 2017 01 01
#2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#1 + 2 = 3
#3 es el dígito que buscamos y encontramos.

#Tu tarea es escribir un programa que:

#Le pregunta al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, el orden de los dígitos no importa).
#Da como salida El Dígito de la Vida para la fecha ingresada.
#Prueba tu código utilizando los datos que te proporcionamos.

#Datos de Prueba
#Entrada de Ejemplo:

#19991229

#Salida del Ejemplo:

#6

#Entrada de Ejemplo:

#20000101

#Salida del Ejemplo:

#4

def digitoVida(edad):
    j=0
    for i in edad:
        j+=int(i)
        if j>9:
            j=j%10 + j//10
    return j
while True:
    try:
        a=input("Ingrese la fecha de nacimiento (puede ser en formato AAAAMMDD, AAAADMM o MMDDAAAA): ")
        b=a.replace(" ","")
        vida=digitoVida(b)
        print("El dígito de la vida es",vida)
    except ValueError:
        print("No se permite ingresar carácteres o decimales")


#res = 0
#for num in test_str: 
#    res += int(num) 
      
    # modulation in case of 2 digit number 
#    if res > 9: 
#        res = res % 10 + res // 10
  
# printing result 
#print("Life Path Number  : " + str(res)) 