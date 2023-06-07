from fruta import Fruta

e=2.71828

class Kiwi (Fruta):
    def __init__(self,p_masa):
        super().__init__(p_masa) #invocar el init de la clase base 
        self.nombre = "Kiwi"
   
    def aw_prom_kiwi(self,p_masa):
        act= 0.96*((1-e^(-18*p_masa))/(1+e^(-18*p_masa)))
        return act

        

if __name__ == "__main__":
    k = Kiwi(10)
    print(k.aw_prom_kiwi())