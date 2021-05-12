# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:53:43 2021

@author: USUARIO
"""

from math import pi
x = (1.602*(10**-19))**2
epsi = 8.85*(10**-12)
while True:
   
    menu = int(input("Ingrese:\n1. Hallar fuerza de atracción.\n2. Hallar radio iónico.\n3. Salir.\nOpción ingresada: "))

    if menu == 1:
        
        z1 = int(input("Ingrese la carga de valencia 1: "))
        z2 = int(input("Ingrese la carga de valencia 2: "))
        r1 = float(input("Ingrese el valor del radio iónico 1 en nanómetros: "))
        r2 = float(input("Ingrese el valor del radio iónico 2 en nanómetros: "))
        a = r1 + r2
        a = a * (10**-9)
        c = a**2
        FA = (-(z1 * z2 * x))/(4 * pi * epsi * c)
        
        print("\nLa fuerza de atracción es: " + str(FA) + " N")
        
    elif menu == 2:
        
        FA = float(input("Ingrese la fuerza de atracción sin exponente: "))
        exponente = int(input("Ingrese el exponente: "))
        FA = FA*(10**exponente)
        r1 = float(input("Ingrese el radio iónico 1: "))
        z1 = int(input("Ingrese la carga de valencia 1: "))
        z2 = int(input("Ingrese la carga de valencia 2: "))
        a = (-(x * z1* z2) / (4 * pi * epsi * FA))**(1/2)
        a = a * (10**9)
        r2 = a - r1
        
        print("\nEl radio iónico 2 es: " + str(r2) + " nm")
        
    elif menu == 3:
        print("\nPrograma finalizado.")
        break
        