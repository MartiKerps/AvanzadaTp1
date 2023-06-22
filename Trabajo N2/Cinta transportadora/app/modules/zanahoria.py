from verdura import Verdura

e=2.71828
class Zanahoria (Verdura):
    def __init__(self,p_masa):
        super().__init__(p_masa) #invocar el init de la clase base 
        self.nombre = "Zanahoria"
       
    
    def aw_prom_zanahoria(self,m):
        act= 0.96*(1-e^(-10*m))
        return act

    
if __name__ == "__main__":
    m = Zanahoria (10)
    print(m.aw_prom_zanahoria())