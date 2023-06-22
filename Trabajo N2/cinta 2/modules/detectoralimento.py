import numpy as np
import random
import matplotlib.pyplot as plt

e=2.71828

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
        self.alimentos = ["kiwi", "manzana", "papa", "zanahoria"]#, "undefined"]
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
       # return {alimento_detectado,peso_detectado}
   
    def alimento_aceptable (self,lista):
        for aw_alimento in lista:
            if aw_alimento>0.95:
                #el alimento no es aceptable
                alimento="Revisar Cajon (contiene alimentos con aw mayor a 0.95)"
            elif aw_alimento <0.95:
                alimento="Alimentos Aceptables "
            return alimento

            
    def calcularAgua (lista_alimento,tipo):
        
        contador=0
        aw_alimento=0
        for alimento in lista_alimento:
            if isinstance(alimento,tipo):
                aw=alimento.calcular_aw()
                aw_alimento = aw + aw_alimento
                i=i+1
                resultado=aw_alimento/i

                return resultado

            
if __name__ == "__main__":
    
    random.seed(1)
    sensor = DetectorAlimento()
   
    for i in range(10):
        lista= sensor.detectar_alimento()
        print(lista)
    
    aw=[0.94,0.80,0.87]
    alimento=sensor.alimento_aceptable(aw)
    print(alimento)