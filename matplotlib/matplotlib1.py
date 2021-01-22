# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:38:43 2021

@author: dmcew
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'gs')
plt.show()

#datos = np.arange(100)
#plt.plot(datos) #Arange 0--100
#plt.plot([1,2,3,4],[1,4,9,16],'ro') #Puntos
#plt.axis([0,6,0,20]) #X2=LIMITE SUPERIOR EJE X
#x1LÍMITE INFERIOR EJE X
#Y1 LÍMITE INFERIOR EJE Y
#Y2 LÍMITE SUPERIOR EJE Y
#plt.show()
