# -*- coding: utf-8 -*-

#profesor asignado a un deppartamento 
#profesor director de departamento 

#profesor ensena en un curso

#el profesor va  a  tener atributos = nombre, curso , departamento 

from modules.persona import Persona

class Profesor(Persona):
    
    def __init__(self, pNombre, pCurso):
        self.__nombre = pNombre
        self.__curso = pCurso
        self.__departamento = None
        pCurso.set_profesor(self)
        # self es una referencia al objeto que invoca al metodo
    

    def status(self):
        return self.__curso
