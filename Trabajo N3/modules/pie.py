import matplotlib.pyplot as plt
import os

class Grafico:
    def __init__(self):
        self.imagen_guardada = None

    def crear_grafico_pie(self, datos):
        fig, ax = plt.subplots()
        etiquetas = ["Resueltos","En Progreso"]
        ax.pie(datos, labels=etiquetas, autopct='%1.1f%%')
        ax.axis('equal')  # Asegurar que el gráfico sea un círculo

        # Guardar el gráfico en carpeta llamada "images"
        self.imagen_guardada = "static/images/grafico_pie.png"
        plt.savefig(self.imagen_guardada)
        plt.close()

    def eliminar_grafico_guardado(self):
            os.remove("static/images/grafico_pie.png")
