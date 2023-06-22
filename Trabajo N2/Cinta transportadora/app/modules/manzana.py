
from fruta import Fruta

e=2.71828
class Manzana(Fruta):
    def __init__(self,p_masa):
        super().__init__(p_masa) #invocar el init de la clase base 
        self.nombre = "Manzana"
      
    def aw_prom_manzana(self,p_masa):
        act= 0.97*((15*p_masa)^2)/(1+(15*p_masa)^2)
        return act
        

if __name__ == "__main__":
    m = Manzana(10)
    print(m.aw_prom_manzana())