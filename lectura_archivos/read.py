archivo = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\prueba.txt','r')
contenido1= archivo.readlines() #Lee todas las líneas y las pasa alista

#contenido1=archivo.read()
contenido2=archivo.read()
for linea in archivo:
    print (linea)
print (contenido1)
print ('Re-leyendo')
print (contenido2) #Como ya leyó todo el archivo, sale en espacio en blanco
print ('Fin de programa')
archivo.close()



#lengu = ('C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\prueba.txt','r')
#cadena = lengu.read()
#print(len(cadena))
#archivo.close()