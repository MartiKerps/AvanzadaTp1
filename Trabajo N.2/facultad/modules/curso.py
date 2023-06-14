# -*- coding: utf-8 -*-

#herencia de profesor a curso 
#herencia de estudiantes a curso 


from modules.profesor import Profesor
from modules.estudiante import Estudiante

class Curso:
    
    def __init__(self, pNombre):
        self.__nombre = pNombre
        self.__profesores = []
        self.__estudiantes = []
        
    def set_profesor(self, pProf):
        if isinstance(pProf, Profesor) and pProf not in self.__profesores:
            self.__profesores.append (pProf) 
        else:
            raise Exception ("El profesor no es un Profesor o ya esta en la lista")
                               
    def get_profesor(self):
        return self.__profesores
    
    def set_estudiantes(self, pEst):
        if isinstance(pEst, Estudiante):
            self.__estudiantes.append(pEst)
        else:
            raise TypeError("Estudiante no es de tipo Estudiante")
    
    def get_estudiantes(self):
        return self.__estudiantes
    