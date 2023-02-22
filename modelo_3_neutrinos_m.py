# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:20:25 2022

@author: User
"""

#MODELO DE OSCILACIÓN EN MATERIA DE 3 NEUTRINOS 

#IMPORTACIONES

import numpy as np
from scipy.linalg import expm
from constantes import *



#MATRIZ DE MEZCLA

U_12 = np.array([[np.cos(t12), np.sin(t12), 0], [-np.sin(t12), np.cos(t12), 0], [0, 0, 1]])
U_23 = np.array([[1, 0, 0], [0, np.cos(t23), np.sin(t23)], [0, -np.sin(t23), np.cos(t23)]])
U_13 = np.array([[np.cos(t13), 0, f13*np.sin(t13)], [0, 1, 0], [-np.conjugate(f13)*np.sin(t13), 0, np.cos(t13)]])


Um = U_23.dot(U_13.dot(U_12))
Umt = np.conjugate(Um.T)

#MATRIZ DE DIFERENCIAS DE MASAS AL CUADRADO

M3 = np.matrix([[0, 0, 0], [0, m21, 0], [0, 0, m31]])

#HAMILTONIANO

Hm = Um.dot(M3.dot(Umt))
Hp = np.matrix([[vcc, 0, 0], [0, 0, 0], [0, 0, 0]])

#FUNCIONES

def Ht(en):
    return (Hm + 2*en*Hp)


def mex(e):
    return expm(np.complex(0, -1)*(Ht(e)*l)/(2*e*hb*c))


#BRA Y KET

km = np.matrix([[0], [1], [0]])
bm = np.matrix([[0, 1, 0]])

be = np.matrix([[1, 0, 0]])

def puu3m(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = abs(bm.dot(mex(i*(1e9)).dot(km)))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R



def pue3m(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = abs(be.dot(mex(i*(1e9)).dot(km)))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R



