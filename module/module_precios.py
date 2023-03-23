# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:03:04 2023

@author: User
"""

# MODULO QUE NORMALIZA LOS VALORES ENTRE 0 Y 1

def precios(lista):
    menor=5000.0
    mayor=0.0
    dato=[]
    for i in range(len(lista)):
        if float(lista[i][1]) < menor:
            menor=float(lista[i][1])
        if float(lista[i][1]) > mayor:
            mayor= float(lista[i][1])
    for y in range(len(lista)):
        
        x=(float(lista[y][1])-menor)/(mayor-menor)
        dato.append([lista[y][0],round(x,3)])
    return(dato)