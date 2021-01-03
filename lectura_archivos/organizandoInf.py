mi_archivo=open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\pacientes.txt','r+')



mi_archivo=open('C:\\Users\\dmcew\\proy_programacion\\Info_I\\lectura_archivos\\pacientes.txt','r+')
contenido1 = mi_archivo.readlines()
print(contenido1)
contenido2 = mi_archivo.read()
print(contenido2)


w=input('Ingrese el código de paciente que desea consultar: ')


contenido = mi_archivo.readlines()

for paciente in contenido:
    if paciente.startswith(w):
        var_paciente=paciente.split('|')
        print('\nCódigo del paciente: #{0}'.format(var_paciente[0]))
        print('Nombre completo: {0} {1}'.format(var_paciente[1],var_paciente[2]))
        print('Documento de identidad: {0}'.format(var_paciente[3]))
        print('career: {0}'.format(var_paciente[4]))
        print('age: {0}'.format(var_paciente[5]))
mi_archivo.close()

#linea1 = mi_archivo.readlines()
#for i in linea1:
    #lista_linea1 = i.split('|')
    ##mi_archivo.close()