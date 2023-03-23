# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:02:38 2023

@author: Toshiba
"""

""" Películas: Preguntas y respuestas  #
#######################################
Elige una opción
1 - Mostrar lista de películas.
2 - ¡Trivia de película!
3 - Mostrar secuencia de opciones seleccionadas previamente.
4 - Borrar historial de opciones.
5 - Salir
"""

import random
import module
import datetime

# abro el archivo
archi=open('frases_de_peliculas.txt', 'r')
info=archi.readlines()

#listas 
frases=[]
peliculas=[]
frases_y_peliculas=[]

for linea in info:
    linea = linea.rstrip('\n')
    frase, pelicula = linea.split(';')
    frases.append(frase)
    peliculas.append(pelicula)
    lineanueva = pelicula + '/' + frase
    frases_y_peliculas.append(lineanueva)
    
print("#######################################")
print("#  Películas: Preguntas y respuestas  #")
print("#######################################")
print("Elige una opción")
print("1 - Mostrar lista de películas.")
print("2 - ¡Trivia de película!")
print("3 - Mostrar secuencia de opciones seleccionadas previamente.")
print("4 - Borrar historial de opciones.")
print("5 - Salir")


opcion = int(input("Ingrese una opcion: "))

ordenado_alf = sorted(frases_y_peliculas)

pelis_aux = []
pelis_final = []

for n in range(len(ordenado_alf)):
    num=str(n+1)
    linea= num + '/' +ordenado_alf[n]
    pelis_final.append(linea)
    pelis_aux.append(linea)

opciones_elegidas = []

archivo_nuevo = open('registro.txt','a')

while 0<opcion<6:
    
    if opcion == 1:
        pelis_1 = module.pregunta_1(pelis_aux)
        print("eligio opcion 1: ")
        for n in pelis_1:
            print(n)
        hora = str(datetime.datetime.now())
        linea = 'Se eligio opcion 1 a la hora:' + hora +'\n'
        opciones_elegidas.append(linea)
        archivo_nuevo.write(linea)
        
        
    if opcion == 2:
        print("eligio opcion 2: ")
        pelis_2 = module.pregunta_2(pelis_aux)
        hora2 = str(datetime.datetime.now())
        linea2 = 'Se eligio opcion 2 a la hora:' + hora2 +'\n'
        opciones_elegidas.append(linea2)
        archivo_nuevo.write(linea2)
    
    if opcion == 3:
        print("eligio opcion 3: ")
        hora3 = str(datetime.datetime.now())
        linea3 = 'Se eligio opcion 3 a la hora:' + hora3 +'\n'
        opciones_elegidas.append(linea3)
        archivo_nuevo.write(linea3)
        
        for a in opciones_elegidas:
            print(a)
            
    if opcion == 4:
        print("eligio opcion 4: ")
        hora4 = str(datetime.datetime.now())
        linea4 = 'Se borro el registro a las:' + hora4 +'\n'
        opciones_elegidas.append(linea4)
        archivo_nuevo.write(linea4)
        archivo_nuevo.truncate(0)
        
    if opcion == 5:
        print("eligio opcion 5: ")
        print('Gracias, vuelva prontos (diria apu)')
        break
        
    opcion = module.preguntar(True)

archivo_nuevo.close()
