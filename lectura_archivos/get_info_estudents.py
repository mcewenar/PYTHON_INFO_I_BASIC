import os
files = os.listdir('C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos')
print(files) #IMPORT OS te permite manipular todos los archivos txt que hay en la carpeta cuya ruta ha sido traída
#for i in files:
    #archivo = open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos'+i, 'r')
    #f3=archivo.readlines()
    #print (f3)


file = open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\estudiantes.txt","r+")
w=input("Ingrese numero ID estudiante")
content = file.readlines() #Pass to list
print(content)

for i in content:
    if i.startswith(w):
        student_unit=i.split('#') #método to split the list
        print('\n Student code: #{0}'.format(student_unit[0]))
        print('complet name: {0} {1}'.format(student_unit[1],student_unit[2]))
        print('See semestre {0}'.format(student_unit[3]))
        print('Edad: {0}'.format(student_unit[4]))
        print('Career {0}'.format(student_unit[5]))
file.close()
