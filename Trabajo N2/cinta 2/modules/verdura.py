from modules.alimento import Alimento

e=2.71828
class Verdura(Alimento): # Verdura
    def __init__(self,p_masa1):
        super().__init__(p_masa1) #invocar el init de la clase base 
        self.nombre = "Frutas"

    def calcular_aw(self):
        pass 
   
    #def calcular_aw (self,listaP,listaZ):  
    #def aw_prom_verduras (self,listaP,listaZ):
        #x=range(listaP)+range(listaZ)
        #dato=(sum(listaP)+ sum(listaZ))/x
        #return(dato)
        
if __name__ == "__main__":
    verdura=Verdura(0.3)
    #v1 =[10,11]
    #print(verdura.calcular_aw(v1,v1))
    