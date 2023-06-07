
from abc import ABC, abstractmethod
import detectorAlimento as d #import detectar_alimento

class Alimento (ABC):
    def __init__(self,p_masa):
        self.nombre = "Alimentos"
        self.set_masa(p_masa)
        
    def set_masa(self,p_masa):
        if p_masa > 0.0:
             self.__masa=p_masa
        else: 
            raise ValueError("La masa debe ser mayor a cero")
            
    def get_masa(self):
        return self.__masa
    
    
    def __str__(self):
        return f'{self.nombre} de masa {self.__masa} gr'
        
         
    @abstractmethod
    def aw_prom_alimento (self):
        pass

    def aw_prom_total (self,f1,f2,v1,v2):
        dato=(f1+f2+v1+v2)/100
        return(dato)

    def eliminarAlimento (self,p_aw):
        while p_aw >= 0.95:
            aliment=Alimento()
            masa,peso=d.detectar_alimento()
            pass