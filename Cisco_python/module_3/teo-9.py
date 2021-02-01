#La rama else del ciclo siempre se ejecuta una vez, independientemente de si el ciclo ha entrado o no en su cuerpo .


i = 1
while i < 5:
    print (i)
    i += 1
else:
    print("else:", i)



print("-------------------------")


#No ejecuta el while y directamente se va al else (while sirve como IF)
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)



print("------------------------------------")
#CON LOS FOR

#Los ciclos for se comportan de manera un poco diferente: echa un vistazo al fragmento en el editor y ejecútalo.
#La salida puede ser un poco sorprendente.
#La variable i conserva su último valor.

i = 111
for i in range(2, 1): #No se ejecuta (no es vádido rangos decrecientes)
    print(i)
else:
    print("else:", i) 

print("------------------------------------")

for i in range(5):
    print(i)
else:
    print("else:", i)