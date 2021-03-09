# main.py

from sys import path

path.append('C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_5\\prueba_modules2\\modulex') #DOBLE \
#path.append('..\\modulex') Hemos utilizado el nombre relativo de la carpeta

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes)) #APLICANDO LAS FUNCIONES CREADAS EN EL OTRO MÓDULO
print(module.prodl(ones))