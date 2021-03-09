from sys import path
path.append("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_5\\extra\\iota.py")
#path.append('..\\packages')

import extra.iota
print(extra.iota.funI())

#otra forma:

#from sys import path
#path.append("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_5\\extra\\iota.py")
#from extra.iota import funI
#print(funI())

print("---2---")

from sys import path
path.append("C:\\Users\\dmcew\\proy_programacion\\Info_I\\Cisco_python\\module_5\\extra\\good\\best\\sigma.py")
#path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())

#otra forma:
# main2.py

from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())

print("---3---")
from sys import path

path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())
