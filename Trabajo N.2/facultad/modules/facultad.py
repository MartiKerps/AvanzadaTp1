# -*- coding: utf-8 -*-


from modules.estudiante import Estudiante
from modules.departamento import Departamento

# clase FACULTAD

 #agregacion con estudiantes 
 #composicion con departamento 
class Facultad:
    
    def __init__(self):
        self._estudiantes =[]
        self._departamentos = list() #tengo una lista de departamento 
        self._departamentos.append(Departamento("Matematica"))
        
        
    def get_estudiantes (self):
        return self._estudiantes
    
    def set_estudiantes (self, pEstudiante):
        if isinstance(pEstudiante, Estudiante):
            self._estudiantes.append(pEstudiante)
        else:
            raise TypeError("Si quiere agregar un estudiante a la facultad debe ser de tipo Estudiante")
       
    def agregar_departamento(self,pDep): #crear_departamento
        if isinstance(pDep, Departamento):
            self._departamentos.append(pDep)
        else: 
            raise TypeError("El parametro pasado no es de tipo Departamento")
            
    def get_departamentos(self):
        return self._departamentos
    
    def set_departamento(self, pDpto):
        if isinstance(pDpto, Departamento):
            pass
            self._departamentos.append(pDpto)
        else:
            raise TypeError("El departamento de la facultad debe ser de tipo Departamento")
     
    
                
    
    
        

    
            