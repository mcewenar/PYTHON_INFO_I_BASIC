import mysql.connector
servidor='localhost'
usuario='root'
contrasena=''
bd='hce'
cnx=mysql.connector.connect(user=usuario,password=contrasena,host=servidor,database=bd)
cursor=cnx.cursor()
######consultar_id=input('ingrese el id que va a consultar:')
######sql="SELECT * FROM pacientes ORDER BY id ASC" """PUNTO DOS """"
##########sql="SELECT*FROM pacientes WHERE id = '%s'" %consultar_id
######"""PUNTO DOS"""
########sql="SELECT*FROM pacientes"
######cursor.execute(sql)
######
######pacientes=cursor.fetchall()
######for pacientes in pacientes:
######    print("{0}{1}{2}{3}{4}".format(pacientes[0],pacientes[1],pacientes[2],pacientes[3],pacientes[4]))
######"""este es el pedazo de codigo para consultar paciente apartir del documento"""    
##########INGRESAR DATOS EN LA BASE DE DATOS
id1=input("ingrese id")
nom=input("ingrese nombre")
apel=input("ingrese apellido")
edad=input("ingrese edad")
gen=input("ingrese genero")
ingdatos="INSERT INTO pacientes (id,nombre,apellido,edad,genero)VALUES(%s,%s,%s,%s,%s)"
cursor.execute(ingdatos,(id1,nom,apel,edad,gen))
cnx.commit()
