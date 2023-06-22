from modules.alimento import Alimento


e=2.71828
class Fruta(Alimento):
    def __init__(self,p_masa1):
        super().__init__(p_masa1) #invocar el init de la clase base 
        self.nombre = "Frutas"
      
    def calcular_aw(self):
        pass
    
    #def calcular_aw (self,listaM,listaK):
    #def aw_prom_frutas (self,listaM,listaK):
        #x=range(listaK)+range(listaM)
        #dato=(sum(listaM)+ sum(listaK))/x
        #return(dato)
        

if __name__ == "__main__":
    
    f = Fruta(0.85)
    #lista1=[0.96,0.85,0.96]
    #print(f.calcular_aw(lista1,lista1))