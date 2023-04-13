# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:51:36 2023

@author: Toshiba
"""

#Al pulsar el botón de resultados, se deben listar los nombres de usuarios
# con el número de aciertos realizados en el formato “aciertos/5” junto con la fecha y hora de inicio de la partida.

import datetime

opciones_elegidas = []
aciertos=[]

nombre= input("ingrese su nombre: ")
archivo_nuevo = open('registro1.txt','a')

#prueba
valor= input("ingrese el puntaje de prueba ")
aciertos.append(valor)

## representacion de fecha y hora
for aciert in aciertos:
    hora3 = str(datetime.datetime.now())
    linea3 = nombre + '= La cantidad de aciertos es : '+ aciert + ', la fecha es' + hora3 +'\n'
    opciones_elegidas.append(linea3)
    archivo_nuevo.write(linea3)
    print(linea3)

x=input("para borrar el historial ingrese 1: ")
while x==1:
    #borrar el historial      
    hora4 = str(datetime.datetime.now())
    linea4 = nombre+'borro el registro en la fecha:' + hora4 +'\n'
    opciones_elegidas.append(linea4)
    archivo_nuevo.write(linea4)
    archivo_nuevo.truncate(0)
    print(linea4)
