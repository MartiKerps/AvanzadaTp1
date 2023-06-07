
'''import numpy as np
import random
import matplotlib.pyplot as plt

e=2.71828

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
        self.alimentos = ["kiwi", "manzana", "papa", "zanahoria", "undefined"]
        self.peso_alimentos = np.round(np.linspace(0.05, 0.6, 12),2)
        self.prob_pesos = np.round(self.__softmax(self.peso_alimentos)[::-1], 2)

    def __softmax(self, x):
        """función softmax para crear vector de probabilidades 
        que sumen 1 en total
        """
        return (np.exp(x - np.max(x)) / np.exp(x - np.max(x)).sum())

    def detectar_alimento(self):
        """método que simula la detección del alimento y devuelve un diccionario
        con la información del tipo y el peso del alimento.
        """
        n_alimentos = len(self.alimentos)
        alimento_detectado = self.alimentos[random.randint(0, n_alimentos-1)]
        peso_detectado = random.choices(self.peso_alimentos, self.prob_pesos)[0]
        return {"alimento": alimento_detectado, "peso": peso_detectado}

    def aw_prom_kiwi(self,m):
        act= 0.96*((1-e^(-18*m))/(1+e^(-18*m)))
        return act
    
    def aw_prom_manzana(self,m):
        act= 0.97*((15*m)^2)/(1+(15*m)^2)
        return act
    
    def aw_prom_papa(self,m):
        act= 0.66*(18*m)
        return act
    
    def aw_prom_zanahoria(self,m):
        act= 0.96*(1-e^(-10*m))
        return act

    def aw_prom_frutas (self,f1,f2):
        dato=(f1+f2)/100
        return(dato)
    
    def aw_prom_verduras (self,v1,v2):
        dato=(v1+v2)/100
        return(dato)
    
    def aw_prom_total (self,f1,f2,v1,v2):
        dato=(f1+f2+v1+v2)/100
        return(dato)

if __name__ == "__main__":
    
    random.seed(1)
    sensor = DetectorAlimento()
    lista_pesos = []
    for _ in range(200):
        lista_pesos.append(sensor.detectar_alimento()["peso"])

    plt.hist(lista_pesos, bins=12)
    plt.show()
    '''