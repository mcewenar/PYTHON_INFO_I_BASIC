listaUno = []
for ex in range(6):
    listaUno.append(10 ** ex)

#esto es igual a:
listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)