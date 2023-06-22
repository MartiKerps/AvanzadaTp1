# -*- coding: utf-8 -*-

#estudiante tiene de atributos un nombre, pertenece a un curso 
#tiene agregacion con facultadd (los estudiantes son parte de facultad )
# hereda de persona 

from modules.persona import Persona


class Estudiante(Persona):
    
    def __init__(self, pNombre):
        from modules.curso import Curso 
        self.__nombre = pNombre
        self._curso = list ()
        self._curso.append(Curso("Lengua"))
        
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, pCurso):
        self._curso = pCurso
        
    def get_nombre(self):
        return self.__nombre
    
    def datos(self):
        print("Soy", type(self).__name__)

        