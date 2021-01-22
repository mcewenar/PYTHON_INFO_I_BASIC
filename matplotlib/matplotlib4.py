# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:25:34 2021

@author: dmcew
"""

#Subplots

import numpy as np
import matplotlib.pyplot as plt

x=np.radians(np.arange(0,360))
sin=np.sin(x)
cos=np.cos(x)
fun=np.cos(2*x)-3*np.sin(x/2)
fig=plt.figure()
ax1=fig.add_subplot(3,1,1) #alto,ancho,número de subplots
ax1.plot(x,sin)
plt.title("Funciones trigonométricas")
ax1.set_ylabel("sen(x)")
ax1.set_xbound(x[1],x[-1])
ax2=fig.add_subplot(3,1,2)
ax2.plot(x,cos)
ax2.set_ylabel("cos(x)")
ax2.set_xbound(x[1],x[-1])
ax3=fig.add_subplot(3,1,3)
ax3.plot(x,fun)
ax3.set_xlabel("x(rad)")
ax3.set_ylabel("fun(x)")
ax3.set_xbound(x[1],x[-1])
plt.show()


#fig= plt.figure()
#fig1=fig.add_subplot(filas,columnas,posicion)
#fig1.set_xlabel("Nombre")
#fig1.set_ylabel("Nombre")
#fig1.plot(datos)
