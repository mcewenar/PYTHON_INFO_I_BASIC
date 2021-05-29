# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:23:13 2021

@author: Manuel
"""
"A,B,C,D"
"""500,200,100,50"""




def calcular_cambio(cambio:int)->None:
 
    A = cambio//500
    cambio = cambio%500
    B = cambio//200
    cambio = cambio%200
    C = cambio//100 
    cambio = cambio%100
    D = cambio//50
    print("Devuelve {0} monedas de 500".format(A))
    print("Devuelve {0} monedas de 200".format(B))
    print("Devuelve {0} monedas de 100".format(C))
    print("Devuelve {0} monedas de 50".format(D))
    
    
    
    
    
calcular_cambio(32250)


def calcularCambio(valor:int):
    monedas = [500, 200, 100, 50] # LISTA VALORES TIPO INT
    devuelta = {500: 0, 200:0, 100:0, 50:0} # DICCIONARIO 
    for mon in monedas: # RECORRE LA LISTA 
        if valor//mon >= 1:
            devuelta[mon] = valor//mon # INGRESA AL VALOR DEL DICCIONARIO Y LE AGREGA UN ELEMENTO
            
            valor -= (valor//mon)*mon
        
    for llave, valores in devuelta.items():
        if devuelta[llave] != 0:
            print("Monedas de", llave, ":", valores)

calcularCambio(17100)





def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):
    segundos =  (segundo_salida + duracion_segundos)
    minutos = (minuto_salida + duracion_minutos) + segundos//60
    hora = (hora_salida + duracion_horas) + minutos//60
    segundos = segundos%60
    minutos = minutos%60
    hora = hora%24
    return str(hora)+":"+str(minutos)+":"+str(segundos)


    
print(calcular_horario_llegada(23, 32, 4, 7, 30, 15))





def reflejo_reloj(hora:int,minutos:int)->str:
    # horas 1-12
    # minutos de 0-59
    if minutos == 0:
        hora = hora  if hora == 12 else 12-hora
    else:
        minutos = 60-minutos
        if hora==11:
            hora = 12
        elif hora == 12 :
            hora = 11
        else:
            
            hora = 11-hora
    
    
    return  str(hora)+":"+str(minutos)



print(reflejo_reloj(11,30)) 
print(reflejo_reloj(8,5)) 
print(reflejo_reloj(6,0)) 
 
    






