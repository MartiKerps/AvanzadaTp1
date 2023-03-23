# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:34:12 2023

@author: alumno
"""

# MODULO ENCARGADO DE CREAR LA LISTA CON LA FECHA Y LA VARIACION PORCENTUAL


def porcentual(lista):
    inicial=float(lista[0][1])
    
    lista2=[]
    
    for i in range(len(lista)):
        porc=((float(lista[i][1])-inicial)/inicial)*100
        lista2.append([lista[i][0],porc])
        


    return(lista2)
            
        
    
    
        
            
