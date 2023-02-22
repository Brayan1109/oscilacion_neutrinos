# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:30:15 2022

@author: User
"""

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
graphFrame = ttk.Frame(frm, width=100).grid(column=0, row=2)
ttk.Button(graphFrame, text="Ingresa nombre", command=print("Hola")).grid(column=1, row=1)

frm.grid()
ttk.Label(frm, text="Hello word!").grid(column=0, row=0)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
