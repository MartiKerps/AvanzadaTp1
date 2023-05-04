# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:25:32 2023

@author: alumno
"""

from module import lista_archivo as r

from module import porcentual as s

from module import module_precios as t

from module import ExtraerDatos as q


Normalizado=[]

x="google.csv"
#x=input("Ingrese nombre del archivo: ")

y=r.escala_precios(x)


Normalizado=t.precios(y)

Porcentual=s.porcentual(y)

#print (" Datos de ",x)
#print("La escala de precios normalizando")

x2="nike.csv"
#x2=input("Ingrese nombre del otro archivo: ")

y2=r.escala_precios(x2)


Normalizado2=t.precios(y2)

Porcentual2=s.porcentual(y2)

Norm=q.ExtraerDatos(Normalizado)
Norm2=q.ExtraerDatos(Normalizado2)
Por=q.ExtraerDatos(Porcentual)
Por2=q.ExtraerDatos(Porcentual2)


if x== "google.csv":
    
    
    #max_val = max(y)
    #min_val = min(y)
    precios = q.ExtraerDatos(y)
   
    max_val = max(precios[25:40])
    min_val = min(precios[45:60])
    

    
    #caida porcentual 
    porc= ((max_val-min_val)/max_val)*100
    porc=round(porc,3)    
    
    print ("\n")
    print ("La caida en porciento del precio de google fue: ", porc, "%")
    print ("\n")
    print ("La relacion entre la caida del precio",porc ,"% y la caida porecentual de google son aproximadas")

    #porcentaje de repunte 
    min_anual = min(precios)
    
    ult_valor = precios[-1]
    
    
    repun= ((ult_valor-min_anual) /min_anual)*100
    repun= round(repun,3)
    
    print ("\n")
    print("El porcentaje de “repunte” (crecimiento) entre el soporte o mínimo anual y el último valor de la serie es: ", repun, "%")
    
    print ("\n")
    #¿Se corresponde aproximadamente el valor calculado en el punto anterior con el repunte para Google en el gráfico de la derecha? Justificar.
    print ("Corresponden aproximadamente el valor de crecimiento",repun ,"% con el repunte de Google" ) 

# para  cuando vos cargas los archivos 
'''    
elif x2=="google.csv":
    #max_val = max(y2)
    #min_val = min(y2)
    
    #max_val = y2[31]
    #min_val = y2[56]
    
    precios = q.ExtraerDatos(y2)
   
    max_val = max(precios[25:40])
    min_val = min(precios[45:60])
    
    #caida porcentual 
    porc= ((max_val-min_val)/max_val)*100
    porc=round(porc,3)    
    
    print ("\n")
    print ("La caida en porciento del precio de google fue: ", porc, "%")
    print ("\n")
    print ("La relacion entre la caida del precio",porc ,"% y la caida porecentual de google son aproximadas")

    #porcentaje de repunte 
    min_anual = min(precios)
    
    ult_valor = precios[-1]
    
    
    repun= ((ult_valor-min_anual) /min_anual)*100
    repun= round(repun,3)
    
    print ("\n")
    print("El porcentaje de “repunte” (crecimiento) entre el soporte o mínimo anual y el último valor de la serie es: ", repun, "%")
    
    print ("\n")
    #¿Se corresponde aproximadamente el valor calculado en el punto anterior con el repunte para Google en el gráfico de la derecha? Justificar.
    print ("Corresponden aproximadamente el valor de crecimiento",repun ,"% con el repunte de Google" ) 

'''   

import matplotlib.pyplot as plt
import math as m

plt.subplot(2, 1, 1)
plt.plot(Norm, label="Google")
plt.grid()
plt.title('Normalizado')

plt.plot(Norm2, label="Nike")
plt.title('Normalizado')

plt.grid()
plt.legend()
plt.show()


plt.subplot(2, 1, 2)
plt.plot(Por, label="Google")
plt.grid()
plt.title('Porcentual')

plt.plot(Por2, label="Nike")
plt.title('Porcentual')

plt.grid()
plt.legend()
plt.show()

    





