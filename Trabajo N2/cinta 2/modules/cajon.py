#from flask import Flask, render_template, request 

from modules.detectoralimento import DetectorAlimento
#from fruta import Fruta 
from modules.kiwi import Kiwi 
from modules.manzana import Manzana 
from modules.papa import Papa 
#from verdura import Verdura
from modules.zanahoria import Zanahoria 
#from alimento import Alimento 


#import random

class Cajon:
    #atributos 

    #inicializo la clase 
    def __init__(self, p_cantidad) -> None:
        self.cantidad=p_cantidad


    #metodos 
    def calcular_cajon(self):
        cantidad=self.cantidad

        lista_alimento=[]
        
        lista_kiwi=[]
        lista_Manzana=[]
        lista_papa=[]
        lista_zanahoria=[]

        aw_manzana_total=0
        aw_kiwi_total=0
        aw_papa_total=0
        aw_zanahoria_total=0


        detectar=DetectorAlimento()
        for i in range(cantidad):
            # detecta el alimento ], lo instancia y lo guarda en una lista 
            cad_alimento=detectar.detectar_alimento()["alimento"]
            peso=float(detectar.detectar_alimento()["peso"])
            alimento = None

            if cad_alimento == "kiwi":
                alimento = Kiwi(peso)
            elif cad_alimento == "manzana":
                alimento = Manzana(peso)
            elif cad_alimento == "papa":
                alimento = Papa(peso)
            elif cad_alimento == "zanahoria":
               alimento = Zanahoria(peso)
               
            lista_alimento.append(alimento)

            if isinstance(alimento, Kiwi):
                aw_kiwi=alimento.calcular_aw()
                aw_kiwi_total=aw_kiwi_total+aw_kiwi
                lista_kiwi.append(aw_kiwi)
            elif isinstance(alimento,Manzana):
                aw_manzana=alimento.calcular_aw()
                aw_manzana_total=aw_manzana_total+aw_manzana
                lista_Manzana.append(aw_manzana)
                

            elif isinstance(alimento, Papa):
                #####aw_papa=detectar.CalcularAgua(alimento)
                aw_papa=alimento.calcular_aw()
                aw_papa_total=aw_papa_total+aw_papa
                lista_papa.append(aw_papa)

            elif isinstance(alimento, Zanahoria):
                aw_zanahoria=alimento.calcular_aw()
                aw_zanahoria_total=aw_zanahoria_total+aw_zanahoria
                lista_zanahoria.append(aw_zanahoria)
            
       #calculo los promedios de la actividad aw

        if len(lista_Manzana)==0:
            aw_manzana_total=0
        else:
            aw_manzana_total=aw_manzana_total/len(lista_Manzana)
            aw_manzana_total=round(aw_manzana_total,2) 
        if len(lista_kiwi)==0:
            aw_kiwi_total=0
        else: 
            aw_kiwi_total=aw_kiwi_total/len(lista_kiwi)
            aw_kiwi_total=round(aw_kiwi_total,2)
        if len(lista_papa)==0:
            aw_papa_total=0
        else:
            aw_papa_total=aw_papa_total/len(lista_papa)
            aw_papa_total=round(aw_papa_total,2)
        if len(lista_zanahoria)==0:
            aw_zanahoria_total=0
        else:
            aw_zanahoria_total=aw_zanahoria_total/len(lista_zanahoria)
            aw_zanahoria_total=round(aw_zanahoria_total,2)


        #calcular los promedios 
        
        manz=sum(lista_Manzana)/len(lista_Manzana)
        kiw=sum(lista_kiwi)/len(lista_kiwi)
        aw_fruta=(manz+kiw)/2
        aw_fruta=round(aw_fruta,2)

        papa=sum(lista_papa)/len(lista_papa)
        zana=sum(lista_zanahoria)/len(lista_zanahoria)
        aw_verdura=(papa+zana)/2
        aw_verdura=round(aw_verdura,2)

        aw_alimento=(papa+zana+manz+kiw)/4
        aw_alimento=round(aw_alimento,2)

        #funcion responsable de informar si se debe revisar el cajon 
        resp_k=detectar.alimento_aceptable(lista_kiwi)
        resp_m=detectar.alimento_aceptable(lista_Manzana)
        resp_p=detectar.alimento_aceptable(lista_papa)
        resp_z=detectar.alimento_aceptable(lista_zanahoria)

        return(aw_manzana_total,aw_kiwi_total,aw_papa_total,aw_zanahoria_total,aw_fruta,aw_verdura,aw_alimento,resp_k,resp_m,resp_p,resp_z)
        #return aw_fruta
    


    
if __name__ == "__main__":
    cantidad=10
    c = Cajon(12)
    aw_manzana_total,aw_kiwi_total,aw_papa_total,aw_zanahoria_total,aw_fruta,aw_verdura,aw_alimento,resp_k,resp_m,resp_p,resp_z=c.calcular_cajon()
    print(aw_manzana_total,aw_kiwi_total,aw_papa_total,aw_zanahoria_total,aw_fruta,aw_verdura,aw_alimento,resp_k,resp_m,resp_p,resp_z)
    #lista= c.calcular_cajon()
    #print(lista)