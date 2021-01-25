
#Se ejecutan todas las que cumplan la condición
x = 10

if x > 5: # condición uno
    print("x es mayor que 5") # ejecutado si la condición uno es verdadera

if x <10: # condición dos
    print("x es menor que 10") # ejecutado si la condición dos es verdadera

if x == 10: # condición tres
     print("x es igual a 10") # ejecutado si la condición tres es verdadera

print("-------------------------1----------------------------")
#Se ejecuta la primera que cumpla
#Como el intérprete lee de arriba a abajo, sólo imprime la primera con la que se topa
x = 10

if x > 5: # condición uno
    print("x es mayor que 5") # ejecutado si la condición uno es verdadera

elif x <10: # condición dos
    print("x es menor que 10") # ejecutado si la condición dos es verdadera

elif x == 10: # condición tres
     print("x es igual a 10") # ejecutado si la condición tres es verdadera




print("-----------------------2-----------------------------")

#Como el ÚLTIMO if es falso, se ejecuta automáticamente el Else contiguo
x = 10

if x > 5: # Verdadero
    print("x > 5")

if x > 8: # Verdadero
    print("x > 8")

if x > 10: # Falso
    print("x > 10")

else:
    print("Se ejecutará el else")


print("-----------------------3------------------------")

#Si la condición para if es False, el programa verifica las condiciones de los bloques elif posteriores: 
#el primer elif que sea True es el que se ejecuta. Si todas las condiciones son False, se ejecutará el bloque else.
x = 10

if  x == 10: # Verdadero
    print("x == 10")

if x > 15: # Falso
    print("x > 15")

elif x > 10: # Falso
    print("x > 10")

elif x > 5: # Verdadero
    print("x > 5")

else:
    print("No se ejecutará el else")



print("------------------------4---------------------------")

x = 10

if x > 5: # Verdadero
    if x == 6: # Falso
        print("anidado: x == 6")
    elif x == 10: # Verdadero
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")


print("-----------------------------5------------------------------")

x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int (z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro") 



#x = 10

#if x > 5: # Verdadero
    #print("x > 5")

#if x > 8: # Verdadero
    #print("x > 8")

#if x > 10: # Falso
    #print("x > 10")

#else:
    #print("Se ejecutará el else")