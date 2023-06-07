from alimento import Alimento

e=2.71828
class Fruta(Alimento):
    def __init__(self,p_masa1,p_masa2):
        super().__init__(p_masa1,p_masa2) #invocar el init de la clase base 
        self.nombre = "Frutas"
      
    def aw_prom_frutas (self,f1,f2):
        dato=(f1+f2)/100
        return(dato)
        

if __name__ == "__main__":
    f = Fruta(10,11)
    print(f.aw_prom_frutas())