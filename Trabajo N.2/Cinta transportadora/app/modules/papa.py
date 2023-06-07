from verdura import Verdura

e=2.71828
class Papa (Verdura):
    def __init__(self,p_masa):
        super().__init__(p_masa) #invocar el init de la clase base 
        self.nombre = "Papa"
    
    def aw_prom_papa(self,):
        act= 0.66*(18*m)
        return act
        

if __name__ == "__main__":
    m = Papa(10)
    print(m.aw_prom_papa())