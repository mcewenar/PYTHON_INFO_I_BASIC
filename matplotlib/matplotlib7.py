# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:24:17 2021

@author: dmcew
"""

import matplotlib.pyplot as plt
import numpy as np

X=np.asarray(list(range(50)))
y1=np.asarra([1/(x+5) for x in X])
y2 = np.asarray(x**2 for x in X)