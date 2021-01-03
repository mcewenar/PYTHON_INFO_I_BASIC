#clase 26 de nov

import mysql.connector
##servidor="localhost"
##usuario="root"
##contrasena=""
##BD="informatica1"
###realiza la conexión con el servidor MySQL
##cnx=mysql.connector.connect(user=usuario,password=contrasena,host=servidor,database=BD)
##conexion=cnx.cursor()
##sql="SELECT*FROM informatica1"
##conexion.execute(sql)
##resultado=conexion.fetchall()
##for registro in resultado:
##    print(str(registro[0])+"|"+str(regristro[1]))


###Clase 28 de nov
##import mysql.connector
##servidor="localhost"
##usuario="root"
##contrasena=""
##BD="informatica1"
##realiza la conexión con el servidor MySQL
##cnx=mysql.connector.connect(user=usuario,password=contrasena,host=servidor,database=BD)
=##conexion=cnx.cursor()
##sql="SELECT*FROM informatica1 ORDER BY nombre ASC"
##conexion.execute(sql)
##resultado=conexion.fetchall()
##for registro in resultado:
##    print(str(registro[0])+"|"+str(registro[1]))
##
##
##
########
##sql= "SELECT * FROM laboratorio WHERE id="+b
##sql="SELECT*FROM informatica1 ORDER BY nombre ASC"
##conexion.execute(sql)
##resultado=conexion.fetchall()
##for registro in resultado:
##    print(str(registro[0])+"|"+str(regristro[1]))
##
########
##sql="SELECT * FROM eps WHERE codigoeps="str(registro[6])
##sql="SELECT*FROM informatica1 ORDER BY nombre ASC"
##conexion.execute(sql)
##resultado=conexion.fetchall()
##for registro in resultado:
##    print(str(registro[0])+"|"+str(regristro[1]))
##
####30 de noviembre:
##sql="SELECT pacientes.nombre, pacientes.apellido, laboratorio.ctotal, laboratorio.trig, laboratorio.hdl, laboratorio.ldl "+ "FROM pacientes, laboratorio WHERE pacientes.id=1012999001 and laboratorio.id=1012999001"
##
##conexion.execute(sql)
##resultado=conexion.fetchall()
##for registro in resultado:
####    print("| {0} | {1}| {2} | {3} | {4} | {5}".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5])
##      print("col total: "+str(registro[2]))
##      print("nombre completo: "+registro[0]+" "+registro[1])
##      print("trig: "+registro[4])
##      print("hdl: "+registr[5])
##      print("ldl: "+registro[6])
##      eps=registro[2]
##sql="SELECT * FROM eps WHERE codigoeps= "+eps
##conexion.execute(sql)
##resultado=conexion.fetchall()
##for  registro in resultado:
##    print("EPS: "+registro[0])
##    
##PARA INDEXAR A LA BASE DE DATOS:
servidor="localhost"
usuario="root"
contrasena=""
bd="info1"

cnx=mysql.connector.connect(user=usuario,password=contraseña, host=servidor, database=bd)
conexion=cnx.cursor()
#estos llevan input
codigo=16
cc=111111
nomb="maria"
edad=23
genero=2
eps=4

sql="INSERT INTO pacientes (codec,id,nombre,apellido,edad,genero,eps) VALUES(%s,%s,%s,%s,%s,%s,%s"
datos=(codigo,cc,nom,ape,edad,genero,eps)
conexion.execute(sql,datos)

##Eliminar información
eliminar=input("ingrese el id del paciente a eliminar")
sql="DELETE FROM pacientes WHERE id="+eliminar
conexion.execute(sql) #ejecuta el comando SQL
cnx.commit() #confirma los cambios en la base de datos
cnx.close()
##Update actualizar un registro
idact=input("ingrese el id del paciente que desea actualizar")
nombre=input("ingrese el nombre")
sql="UPDATE pacientes SET apellido="martinez" WHERE id=776655"
conexion.execute(sql) #ejecuta el comando SQL
cnx.commit() #confirma los cambios en la base de datos
