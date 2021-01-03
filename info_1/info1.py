##info1=open("base.txt")
##conte=info1.read()
##print(conte)
##info1.close()
##info1=open("base.txt")
##conte=info1.readlines ()
##print(conte)
##info1.close()


##info1=open("base.txt")
##conte=info1.readlines()
##d=input("ingrese código de paciente")
##for i in conte:
##    if i.startswith(d):
##        var_pacientes=i.split('|')
##        print("Código del paciente: "+var_pacientes[0])
##        print("Nombre completo: "+var_pacientes[1]+" "+var_pacientes[2])
##        print("EPS: "+var_pacientes[3])
##        print("Edad: "+var_pacientes[4])
##        print("")
##
##info1.close()


##archivo.write('Historia electrónica.\n')
##archivo.write('estudiantes de bio.\n') #Se añaden texto al archivo
##archivo=open("prueba.txt","w+")
##for i in range(1,5):
##
##    nombre=input('ingrese su nombre:')
##    apellido=input('ingrese apellido')
##    edad=input("ingrese edad")
##    carrera=input("ingrese la carrera")
##    credito=input("ingrese los créditos")
##    archivo.write(str(i+1)+'|'+nombre+'|'+apellido+'|'+edad+'|'+'|'+carrera+'|'+'|'+credito+'\n')
##
##archivo.close()

        
##archivo.close()
import os
files=os.listdir("‪C:\Users\dmcew\proy_programacion\Info_I\info_1\base.tx")
for file in files:
    print(file)
    archivo=open("‪C:\Users\dmcew\proy_programacion\Info_I\info_1\base.tx"+file)
    contenido=archivo.readlines()

    for i in contenido:
        if i.startswith("\x021H"):
            datosequipo=i.split("|")
            nomequipo=datosequipo[4]
            nombre=nomequipo.split("^")
            serialequipo=datosequipo[7]
            print("nombre del equipo: "+nombre[0])
            print("serial del equipo: "+serialequipo)
    archivo.close()
