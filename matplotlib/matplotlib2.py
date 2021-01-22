# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:04:55 2021

@author: dmcew
"""
import numpy as np
import matplotlib.pyplot as plt



plt.plot([1,-1,0,3,-1])
datos=np.arange(0,360)
datos=np.radians(datos)
datos=np.sin(datos)
plt.plot(datos,label="Función seno")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
