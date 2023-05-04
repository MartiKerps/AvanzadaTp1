# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:30:12 2023

@author: Toshiba
"""


import random
import datetime

def historial():
    with open('./data/registro.txt', "r") as archi:
        xd=archi.readlines()
    
    retorno=[]
    
    for i in range(len(xd)):
        nombre, fecha, bien, mal=xd[i].split(";")
        retorno.append("NOMBRE: "+nombre+"    FECHA: "+fecha+"    ACIERTOS: "+bien+"/5")
    
    return(retorno)

def vaciarRegistrop(Nombre):
    with open('./data/'+Nombre, "w") as archi:
        archi.truncate(0)


def historico():
    with open('./data/Registrop.txt', "r") as archi:
        xd=archi.readlines()
    x="Hecho"

    nombre, fecha, bien, mal=xd[0].split(";")

    with open('./data/registro.txt', "a") as archi:
        archi.write(nombre+";"+fecha+";"+bien+";"+str(mal)+"\n")
    return(x)


def contador():
    with open('./data/Registrop.txt', "r") as archi:
        xd=archi.readlines()
    
    nombre, fecha, bien, mal=xd[0].split(";")

    total=int(bien)+int(mal)

    return(total)



def cargarRegistroP():
    with open('./data/Registrop.txt', "r") as archi:
        xd=archi.readlines()
    
    nombre, fecha, bien, mal=xd[0].split(";")

    bien=int(bien)+1

    with open('./data/Registrop.txt', "w") as archi:
        archi.write(nombre+";"+fecha+";"+str(bien)+";"+str(mal))
    




def cargarRegistroN():
    with open('./data/Registrop.txt', "r") as archi:
        xd=archi.readlines()
    
    nombre, fecha, bien, mal=xd[0].split(";")

    mal=int(mal)+1

    with open('./data/Registrop.txt', "w") as archi:
        archi.write(nombre+";"+fecha+";"+str(bien)+";"+str(mal))
    

    


def guardar_lista_en_archivo(nombre_archivo, nombres):  
    with open(nombre_archivo, "w", encoding="utf-8") as archi:                
        for libro in nombres:
            nombre=libro[0]
            fecha=libro[1]

            archi.write(nombre + ";" + fecha + ";" + "0" + ";" + "0")   


def pregunta_1(pelis_y_frases):
    lista = []
    for linea in pelis_y_frases:
        index, peli, frase = linea.split("/")
        linea1 = index + " - " + peli
        #linea1 = linea.lstrip()
        lista.append(linea1)
    return lista


    

def pregunta_2(lista_peliculas):
    random.shuffle(lista_peliculas)
    pelis=[]
    frases=[]
    for pelicula in lista_peliculas:
        index, peli, frase = pelicula.split('/')
        pelis.append(peli)
        frases.append(frase)
    
    correcta=pelis[0]

    opciones = [pelis[0],pelis[1],pelis[2]]
    random.shuffle(opciones)
    frase=frases[0]
    
    return(frase, opciones, correcta)

def preguntar(numeroopcion):
    numero=0
        
    print("\n","\n","#######################################")
    print("#  Películas: Preguntas y respuestas  #")
    print("#######################################")
    print("\n","Elige una opción: ")
    print("1 - Mostrar lista de películas.")
    print("2 - ¡Trivia de película!")
    print("3 - Mostrar secuencia de opciones seleccionadas previamente.")
    print("4 - Borrar historial de opciones.")
    print("5 - Salir")
    numeroopcion=int(input("Quiere elegir otra opcion? (ingrese 1,2,3,4,5): "))
    if numeroopcion==2:
        numero=2
    elif numeroopcion==3:
        numero=3 
    elif numeroopcion==4:
        numero=4
    elif numeroopcion==5:
        numero=5 
    else :
       print("el numero ingresado no es correcto ")

    return numero

def corrector(op, correcta):
    if op == correcta:
        return "Correcto"
    else:
        return "incorrecto"
    
def cargarReg(texto):
    with open('./data/Registro1.txt', "a") as archi:
        archi.write(texto)

def leerArchivo(Nombre):
    with open(('./data/'+Nombre), "r") as archi:
        texto=archi.read()
        
    return(texto)


    
    




    
