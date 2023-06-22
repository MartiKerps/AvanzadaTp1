# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:05:04 2023

@author: alumno
"""

def ExtraerDatos(lista):
    
    columna=1
    nuevo=[]
    
    for i in range(len(lista)):
        nuevo.append(float(lista[i][columna]))
        
    return(nuevo)