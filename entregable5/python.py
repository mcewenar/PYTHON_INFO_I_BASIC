##ERROR1
##archivo=open("entregable5.txt","w")
##n=20
##
##for i in range(n+1):
##    esp=n-i
##    archivo.write(" "*esp+"* "*i+"\n")
##    
##
##
##
##
##archivo.close()

##FORMAPOCOPRÁCTICA
##archivo=open("entregable5.txt","w")
##n=1
##d=" "
##x="*"
##
##for i in range(20):
##    
##    archivo.write((d*(20-n))+x+"\n")
##    n=n+1
##    x="**"+x
##archivo.close()


archivo=open("C:\\Users\\dmcew\\proy_programacion\\Info_I\\entregable5\\entregable5.txt","w")
x=20
for i in range(1,41,2):
    archivo.write(" "*x+i*"*"+"\n")
    x=x-1


    

archivo.close()
