
from modules import cintaTransportadora

class CalcularAgua:
    
    def __init__(self):
        pass
    
    def analizar(self, pListFrutas):
        contAgua = 0.0
        for fruta in pListFrutas:
            contAgua += fruta.calcular_agua()
        return contAgua