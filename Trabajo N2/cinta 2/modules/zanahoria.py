from modules.verdura import Verdura

e=2.71828
class Zanahoria (Verdura):
    def __init__(self,p_masa):
        super().__init__(p_masa) #invocar el init de la clase base 
        self.nombre = "Zanahoria"
       
    def calcular_aw(self):
    #def aw_zanahoria(self):
        p_masa=self.get_masa()
        
        act= 0.96*(1-e**(-10*p_masa))
        return act

    
if __name__ == "__main__":
    
    m = Zanahoria (10)
    print(m.calcular_aw())