# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:33:42 2022

@author: User
"""

#SCRIP PARA GRAFICAR 

#SE IMPORTAN LAS FUNCIONES QUE GENERAN LOS DATOS 


import matplotlib.pyplot as plt

from modelo_3_neutrinos import *
from modelo_4_neutrinos import *
from modelo_3_neutrinos_m import *
from modelo_4_neutrinos_vacio import *

#sol3_1 = pue3(1e8, 4e9, 2000)
#sol3_2 = puu3m(1e8, 4e9, 2000)
#sol3_3 = put3(1e8, 10e9, 2000)
#sol4_4 = pue4(1e8, 4e9, 2000)
#sol4_5 = pus4(1e8, 4e9, 2000)

#res2 = sol3_1/sol4_4

#res = sol3_1/sol3_2
#print(res)

#sol4 = pue4(1e8, 10e9, 2000)
#sol3m = pue3m(1e8, 10e9, 2000)
#print(sol3_1[100, 1] + sol3_2[100, 1] + sol3_3[100, 1])

#Vacío siempre azul m3 verde m4
#Materia naranja m3 rojo m4

#GRAFICOS SESIÓN 4.1.1: PROBABILIDAD DE SUPERVIVENCIA DE NEUTRINOS MUONICOS 3 Y 3+1
sol_m3_v_uu = puu3(0.8, 8, 2000)
sol_m4_v_uu = puu4_v(0.8, 8, 2000)
sol_m4_v_us = pus4_v(0.8, 8, 2000)

sol_m4_v_ue = pue4_v(0.8, 8, 2000)
sol_m4_v_ut = put4_v(0.8, 8, 2000)

#sol_m3_m_uu = puu3m(0.8, 8, 2000) #verificar los potenciales en materia
sol_m4_m_us = pus4(0.8, 8, 2000)

#sol_m4_m_uu = puu4(0.8, 8, 2000)
sol_m4_v_us = pus4_v(0.8, 8, 2000)

#Probabilidad de oscilación de neutrinos muonicos a neutrinos electronicos

#sol_m3_m_ue = pue3m(0.8, 8, 2000)

#Probabilidad de oscilación de neutrinos muonicos a esteriles


#Diferencias entre las probabilidades de oscilación
#sol_dif_m3 = sol_m3_m_uu - sol_m3_v_uu
#sol_div_m3 = ((sol_m3_m_uu -  sol_m3_v_uu)/sol_m3_v_uu) *100

sol_dif_m4 = sol_m4_m_us - sol_m4_v_us
#sol_div_m4 = ((sol_m4_m_uu -  sol_m4_v_uu)/sol_m4_v_uu) *100

   
"""
fig, axes = plt.subplots()
axes.plot(sol_m3_v_uu[:, 0], sol_m3_v_uu[:, 1], 'blue')
plt.title('Probabilidad de supervivencia de ' r'$\nu_{\mu}$'' modelo 3 vacío')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.show()
"""

"""
fig, axes = plt.subplots()
axes.plot(sol_m3_m_uu[:, 0], sol_m3_m_uu[:, 1])
plt.title('Probabilidad de supervivencia de ' r'$\nu_{\mu}$'' modelo 3 materia')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.show()
"""

"""
fig, axes = plt.subplots()
axes.plot(sol_m4_v_uu[:, 0], sol_m4_v_uu[:, 1], 'green')
plt.title('Probabilidad de supervivencia de ' r'$\nu_{\mu}$'' modelo 4')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.show()
"""

"""
fig, axes = plt.subplots()
axes.plot(sol_m4_v_uu[:, 0], sol_m4_v_uu[:, 1], 'green', label='Modelo 3 + 1')
axes.plot(sol_m3_v_uu[:,0], sol_m3_v_uu[:, 1], 'blue', label='modelo 3')
plt.title('Probabilidad de supervivencia de ' r'$\nu_{\mu}$'' modelo 3 y 3+1')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.legend()
plt.show()
"""
"""
fig, axes = plt.subplots()
axes.plot(sol_m4_v_us[:, 0], sol_m4_v_us[:, 1], 'green', label=' ' r'$\nu_{\mu} \rightarrow \nu_{s}  $'' ')
axes.plot(sol_m4_v_ue[:,0], sol_m4_v_ue[:, 1], 'blue', label=' ' r'$\nu_{\mu} \rightarrow \nu_{e}  $'' ')
axes.plot(sol_m4_v_ut[:,0], sol_m4_v_ut[:, 1], 'orange', label=' ' r'$\nu_{\mu} \rightarrow \nu_{\tau}  $'' ')
plt.title('Probabilidad de oscilación de ' r'$\nu_{\mu} \rightarrow \nu_{s,e,\tau}  $'' modelo 3+1')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.legend()
plt.show()
"""

"""
fig, axes = plt.subplots()
axes.plot(sol_m4_v_us[:, 0], sol_m4_v_us[:, 1], 'green')
plt.title('Probabilidad de oscilación de ' r'$\nu_{\mu} \rightarrow \nu_{s}  $'' modelo 3+1')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.show()
"""

#MATERIA

"""
fig, axes = plt.subplots()
axes.plot(sol_m3_m_uu[:, 0], sol_m3_m_uu[:, 1], label= 'Modelo materia')
axes.plot(sol_m3_v_uu[:, 0], sol_m3_v_uu[:, 1],'--',label= 'Modelo vacío')
plt.title('Probabilidad de supervivencia de ' r'$\nu_{\mu}$'' modelo 3')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.legend()
plt.show()
"""


fig, axes = plt.subplots()
axes.plot(sol_m4_m_uu[:, 0], sol_dif_m4[:,1])
plt.title('Dif. en probabilidad de osc. de ' r'$\nu_{\mu} \rightarrow \nu_{s}$'' modelo 4 vac. y mat.')
plt.xlabel("Energía [GeV]")
plt.ylabel(' ' r'$\nu_{\mu m} - \nu_{\mu v}$''')
plt.show()


"""
fig, axes = plt.subplots()
axes.plot(sol_m4_v_uu[:, 0], sol_div_m4[:,1])
plt.title('Dif. en probabilidad de sup. de ' r'$\nu_{\mu}$'' modelo 4 vac y mat.')
plt.xlabel("Energía [GeV]")
plt.ylabel(' % ')
plt.show()
"""

"""
fig, axes = plt.subplots()
axes.plot(sol_m4_v_uu[:, 0], sol_m4_v_uu[:,1], label = 'Vacío')
axes.plot(sol_m4_m_uu[:, 0], sol_m4_m_uu[:,1], label='Materia')
plt.title('Probabilidad de sup. de ' r'$\nu_{\mu}$'' modelo 3 y 3+1 vac. y mat.')
plt.xlabel("Energía [GeV]")
plt.ylabel('Probabilidad')
plt.legend()
plt.show()
"""


"""
fig, axes = plt.subplots()
axes.plot(sol_m4_m_us[:, 0], sol_m4_m_us[:, 1])
plt.title('Probabilidad de oscilación de ' r'$\nu_{\mu} \rightarrow \nu_{s}  $'' modelo 3+1 materia  ')
plt.xlabel("Energía [GeV]")
plt.ylabel("Probabilidad")
plt.show()
"""



