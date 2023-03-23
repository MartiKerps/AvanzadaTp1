# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:25:59 2023

@author: alumno
"""


# MODULO ENCARGADO DE LEER EL ARCHIVO Y DEVOLVER UNA LISTA DE LAS FECHAS Y LOS VALORES

def escala_precios (NombreArchivo):
    
    defi = []
    alt=[]


    with open(NombreArchivo, "r") as archi:
        prueba=archi.readlines()
    del prueba[0]
    
    for i in range(len(prueba)):
        
        
        defi.append(prueba[i].split(","))
        
        defi[i][1]=defi[i][1].rstrip()
    

    
    return(defi)
        
        
        
        
        
"""    for i in range(len(defi)):
        
        
        x=defi[i][0].replace(" 16:00","")

        
        alt.append([x,defi[i][1]])
        

"""  

   

            
            
    


        
    