
from abc import ABC, abstractmethod
from modules.detectoralimento import DetectorAlimento as d

class Alimento (ABC):   #clase abstracta
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
        
         
    #@abstractmethod
    #def calcular_aw (self):
     #   pass
    
    #def calcular_aw (self,listaM,listaK,listaP,listaZ):
    #def aw_prom_total (self,listaM,listaK,listaP,listaZ):
        #x=range(listaK)+range(listaM)+range(listaP)+range(listaZ)
        #dato=(sum(listaM)+ sum(listaK)+sum(listaP)+ sum(listaZ))/x
        #return(dato)

    def eliminarAlimento (self,p_aw):
        while p_aw >= 0.95:
            aliment=Alimento()
            masa,peso=d.detectar_alimento()
            pass