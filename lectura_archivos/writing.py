archivo = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\caneca.txt","w")
archivo.write("Contenido nuevo \n jaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssd \n jdjdjdjdjdjdjjd")
archivo.close()

archivo = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\caneca.txt","r")
print(archivo.read())
archivo.close()



archivo = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\caneca.txt","r")
print (archivo.read())
archivo.close()
archivo = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\caneca.txt","a") #No sobreescribe
archivo.write("\nContenido nuevo del archivo")
archivo.close()