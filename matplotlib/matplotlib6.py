# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:17:08 2021

@author: dmcew
"""

import numpy as np
import matplotlib.pyplot as plt
labels="Biosenales","Bioinstrumentación","Bioinformática","Biomateriales","Otras áreas"
colors=["Vellowgreen","pink","coral","lightskyblue","blue"]
sizes=[25,27,22,23,3]
plt.pie(sizes,labels=labels,colors=colors,autopct="%1.1f%%")
plt.show()