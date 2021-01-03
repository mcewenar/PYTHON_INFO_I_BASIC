"""Recorrer un diccionario


p = {"py": [1,3,4,5,5], "pt": "qkramacha", "ert": {2:4,4:"rer"}}
for i in p:
    print (p, ":", p[i] )


Existen diversas formas de recorrer un diccionario. Es posible recorrer sus claves y usar esas
claves para acceder a los valores.
for dia in materias:
print dia, ":", materias[dia]
Es posible, también, obtener los valores como tuplas donde el primer elemento es la clave
y el segundo el valor.
for dia, codigos in materias.items():
print dia, ":", codigos
9.3. Algunos usos de diccionarios 97
Para verificar si una clave se encuentra en el diccionario, es posible utilizar la función
has_key o la palabra reservada in.
d = {’x’: 12, ’y’: 7}
if d.has_key(’x’):
print d[’x’] # Imprime 12
if d.has_key(’z’):
print d[’z’] # No se ejecuta
if ’y’ in d:
print d[’y’] # Imprime 7"""




#LAS CLAVES DE LOS DICCIONARIOS SON INMUTABLES. LOS VALORES NO.