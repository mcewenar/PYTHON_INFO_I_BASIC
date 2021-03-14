#Escenario
#Seguramente has visto un display de siete segmentos.

#Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un 
#subconjunto de siete segmentos. Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia artículo.

#Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar 
#LEDs individuales en lugar de segmentos.

#Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

#Nota: el número 8 muestra todas las luces LED encendidas.

#Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.

#Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.

#Datos de prueba
#Entrada de muestra:

#123

#Salida de muestra:

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

#Entrada de muestra:

#9081726354

#Salida de muestra:

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 


def led(num):
    lista = [["###","# #","# #","# #","###"], #0
            ["#","#","#","#","#"], #1
            ["###","  #","###","#  ","###"], #2
            ["###","  #","###","  #","###"], #3
            ["# #","# #","###","  #","  #"], #4
            ["###","#  ","###","  #","###"], #5
            ["###","#  ","###","# #","###"], #6
            ["###","  #","  #","  #","  #"], #7
            ["###","# #","###","# #","###"], #8
            ["###","# #","###","  #","###"] #9
    ]
    if num < 0:
        print("No se permiten números negativos")
    elif num >= 0:
        
        for row in range(5):
          lista2=[]
          for i in str(num): 
            i=int(i)
            lista2.append(lista[i][row])
          print(' '.join(lista2))
        
      

while True:
    try:
        c=int(input("Ingresa un número mayor o igual a 0: "))
        led(c)
    except ValueError:
        print("No se permiten carácteres")

#Forma inefectiva:
#print(lista[num])
        #b=list(str(num))
        #for i in b:
        #  ind=int(i)
        #  lista2.append(lista[ind])
        #print(' '.join(lista2))


#[["###","# #","# #","# #","###"], #0
#            ["#","#","#","#","#"], #1
#            ["###","  #","###","#","###"], #2
#            ["###","  #","###","  #","###"], #3
#            ["# #","# #","###","  #","  #"], #4
#            ["###","#","###","  #","###"], #5
#            ["###","#","###","# #","###"], #6
#            ["###","  #","  #","  #","  #"], #7
#            ["###","# #","###","# #","###"], #8
#            ["###","# #","###","  #","###"] #9