# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:16:02 2021

@author: dmcew
"""
import numpy as np
import matplotlib.pyplot as plt


x=np.arange(0,100)
plt.plot(x,[xi*2 for xi in x])
plt.plot(x,[xi/2 for xi in x])
plt.plot([25,50,75,100,125])
plt.show()
