# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:50:14 2022

@author: User
"""

import numpy as np

hb, c = 6.5821e-16, 2.88e8
l = 810e3

#DIFERENCIAS DE MASAS
m21, m31, m41 = 7.41e-5, 2.51e-3, 0.1


#ÁNGULOS DE MEZCLA
t12 = np.radians(33.41)
t13 = np.radians(8.54)
t23 = np.radians(49.1)
t14 = np.radians(20) #20
t24 = np.radians(10) #10
t34 = np.radians(10) #10

#POTENCIALES
#vcc = 0.0
#vnc = 0.0

#MATERIA

vcc = 1.102e-13 #fración de electrones de 0.5
vnc = -0.7714e-13 #para una densidad de 2.9 y fración de neutrones de 0.7

#ANGULOS DE FASES

s13 = np.radians(197)
s34 = np.radians(0)
s14 = np.radians(0)
f13 = np.exp(complex(0, -s13))
f34 = np.exp(complex(0, -s34))
f14 = np.exp(complex(0, -s14))