# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:43:59 2022

@author: User
"""

#SE ESTUDIA LA OSCILACIÓN DE 4 NEUTRINOS EN VACIO

#IMPORTACIONES
import numpy as np
from scipy.linalg import expm
from constantes import *

#MATRIZ DE MEZCLA 

U124 = np.array([[np.cos(t12), np.sin(t12), 0, 0], [-np.sin(t12), np.cos(t12), 0, 0],
                  [0, 0, 1, 0], [0, 0, 0, 1]])
U134 = np.array([[np.cos(t13), 0, f13*np.sin(t13), 0], [0, 1, 0, 0], [-np.conjugate(f13)*np.sin(t13), 0, np.cos(t13), 0],
                  [0, 0, 0, 1]])
U234 = np.array([[1, 0, 0, 0], [0, np.cos(t23), np.sin(t23), 0], [0, -np.sin(t23), np.cos(t23), 0],
                  [0, 0, 0, 1]])
U144 = np.array([[np.cos(t14), 0, 0, f14*np.sin(t14)], [0, 1, 0, 0], [0, 0, 1, 0],
                  [-np.conjugate(f14)*np.sin(t14), 0, 0, np.cos(t14)]])
U244 = np.array([[1, 0, 0, 0], [0, np.cos(t24), 0, np.sin(t24)], [0, 0, 1, 0],
                  [0, -np.sin(t24), 0, np.cos(t24)]])
U344 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(t34), f34*np.sin(t34)],
                  [0, 0, -np.conjugate(f34)*np.sin(t34), np.cos(t34)]])


Um4 = U234.dot(U344.dot(U144.dot(U244.dot(U134.dot(U124)))))
Umt4 = np.conjugate(Um4.T)

#MATRIZ DE DIFERENCIA DE MASAS Y HAMILTONIANO

M4 = np.matrix([[0, 0, 0, 0], [0, m21, 0, 0], [0, 0, m31, 0], [0, 0, 0, m41]])

Hv = Um4.dot(M4.dot(Umt4))

Hm = np.matrix([[vcc, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -vnc]])

#HAMILTONIANO EN FUNCIÓN DEL TIEMPO

def Ht4(en):
    return Hv + 2*en*Hm

def mexp4r(e):
    Ht = Hv + (2 * e * Hm)
    return expm(np.complex(0, 1)*(Ht*l)/(2*e*hb*c))

def mexp4(e):
    return expm(np.complex(0, 1)*(Ht4(e)*l)/(2*e*hb*c))


#BRA Y KET

km = np.matrix([[0], [1], [0], [0]])
bm = np.matrix([[0, 1, 0, 0]])

ks = np.matrix([[0], [0], [0], [1]])
bs = np.matrix([[0, 0, 0, 1]])

be = np.matrix([[1, 0, 0, 0]])


#FUNCIONES DE PROBABILIDAD

def puu4(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = (abs(bm.dot(mexp4(i*(1e9)).dot(km))))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R


def pus4(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = float(abs(bs.dot(mexp4(i*(1e9)).dot(km)))**2)
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R

def pue4(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = float(abs(be.dot(mexp4(i*(1e9)).dot(km)))**2)
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R

