# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:57:08 2022

@author: User
"""

import numpy as np
from scipy.linalg import expm
from constantes import *

vcc1 = 0.0

#definición de las matrices de mezcla

U_12 = np.array([[np.cos(t12), np.sin(t12), 0], [-np.sin(t12), np.cos(t12), 0], [0, 0, 1]], dtype=np.complex128)
U_23 = np.array([[1, 0, 0], [0, np.cos(t23), np.sin(t23)], [0, -np.sin(t23), np.cos(t23)]], dtype=np.complex128)
U_13 = np.array([[np.cos(t13), 0, f13*np.sin(t13)], [0, 1, 0], [-np.conjugate(f13)*np.sin(t13), 0, np.cos(t13)]], dtype=np.complex128)


#se halla la matriz de mezcla 
Um = U_23.dot(U_13.dot(U_12))
Umt = np.conjugate(Um.T)

#prueba de que esta correcto
#print(Um.dot(Umt))

#se define la matriz de diferencias de masas
M3 = np.matrix([[0, 0, 0], [0, m21, 0], [0, 0, m31]])

#se define el hamiltoniano 

Hm = Um.dot(M3.dot(Umt))
Hp = np.matrix([[vcc1, 0, 0], [0, 0, 0], [0, 0, 0]])

def Ht(en):
    return (Hm + 2*en*Hp)

def mex(e):
    return expm((0 - 1j)*(Ht(e)*l)/(2*e*hb*c))


#se definen los vectores brak kets

ku = np.matrix([[0], [1], [0]])
bu = np.matrix([[0, 1, 0]])

ke = np.matrix([[1], [0], [0]])
be = np.matrix([[1, 0, 0]])

kt = np.matrix([[0], [0], [1]])
bt = np.matrix([[0, 0, 1]])

def puu3(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = abs(bu.dot(mex(i*(1e9)).dot(ku)))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R

def pue3(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = abs(be.dot(mex(i*(1e9)).dot(ku)))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R

def put3(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = abs(bt.dot(mex(i*(1e9)).dot(ku)))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R

def pee3(ei, ef, p):
    R = np.ones((p, 2))
    j = 0
    for i in np.linspace(ei, ef, p):
        r = abs(be.dot(mex(i*(1e9)).dot(ke)))**2
        R[j, 0] = i
        R[j, 1] = r
        j = j + 1
    return R









