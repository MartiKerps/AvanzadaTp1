# -*- coding: utf-8 -*-


class Persona:
    
    def __init__(self, pNombre, pEdad, pDni):
        self.__nombre = pNombre
        self.__edad = pEdad
        self.__DNI = pDni
        
    def get_nombre(self):
        return self.__nombre
    
        