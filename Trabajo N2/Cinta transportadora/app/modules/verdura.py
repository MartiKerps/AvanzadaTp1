from alimento import Alimento

e=2.71828
class Verdura(Alimento): # Verdura
    def __init__(self,p_masa1,p_masa2):
        super().__init__(p_masa1,p_masa2) #invocar el init de la clase base 
        self.nombre = "Frutas"
      
    def aw_prom_verduras (self,v1,v2):
        dato=(v1+v2)/100
        return(dato)
        
if __name__ == "__main__":
    v = Verdura(10,11)
    print(v.aw_prom_verduras())