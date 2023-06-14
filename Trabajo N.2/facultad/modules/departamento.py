# -*- coding: utf-8 -*-

from modules.profesor import Profesor

#departamento tiene un nombre 
#composicion con facultad 
# hereda de profesor 

#departamentos tiene profesores y directores 

class Departamento:
    
    def __init__(self,pNombre):
        # self es una referencia al objeto que invoca al metodo
        self.__nombre = pNombre
        self.__profesores = []# lista de profesores 
        self.__director = None
        

    def agregar_profesor(self, pProfesor):
         if isinstance(pProfesor, Profesor): 
             self.miembros.append(pProfesor)
         else:
             raise TypeError("Los miembros de un departamento deben ser profesores")
         
    def agregar_director(self, pDirector):
         if pDirector in self.miembros: 
                 self.director = pDirector
         else:
             self.agregar_miembro(pDirector)
             self.director = pDirector
             raise ValueError("El director debe ser miembro del departamento")
        
       
    def eliminar_miembro(self, pMiembro):
        for i in range(len(self.miembros)-1):
            if self.miembros[i] == pMiembro:
                self.miembros.pop(i)
            else:
                raise TypeError("El miembro"+ pMiembro +" no pertenece al departamento")
                
    def get_director(self):
        if self.director != None:
            direc = self.director 
        else:
            raise ValueError("No hay ningun director")
        return direc
    
    #def __str__(self):  #pasa el nombre del departamento  
     #   departamentos = self._nombre 
      #  return departamentos
    
   
