from modules.verdura import Verdura
import math

e=2.71828
class Papa (Verdura):
    def __init__(self,p_masa):
        super().__init__(p_masa) #invocar el init de la clase base 
        self.nombre = "Papa"
    
    def calcular_aw(self):
    #def aw_papa(self):
        p_masa=self.get_masa()
        act= 0.66* math.atan(18*p_masa)
        return act
        

if __name__ == "__main__":
    m = Papa(0.3)
    print(m.calcular_aw())