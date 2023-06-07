from flask import Flask, render_template, request 

import detectorAlimento as d
import fruta as  f
import kiwi as ki
from modules import manzana as ma
from modules import papa as pa
from modules import verdura as v
from modules import zanahoria as za
from modules import alimento as a
import random

class Cinta_Transportadora():
 
    def Cajon_alimentos(cantidad):
        i=0
        lista_alimento=[]
        aw_manzana_total=0
        aw_kiwi_total=0
        aw_papa_total=0
        aw_zanahoria_total=0

        while i==cantidad:
            cad_alimento,peso=d.detectorAlimento.detectar_alimento()
            nose=d.detectorAlimento.__softmax(i)
            alimento = None

            if cad_alimento == "kiwi":
                alimento = ki.Kiwi(peso)
            elif cad_alimento == "manzana":
                alimento = ma.Manzana(peso)
            elif cad_alimento == "papa":
                alimento = pa.Papa(peso)
            elif cad_alimento == "zanahoria":
                alimento = za.Zanahoria(peso)

            lista_alimento.append(alimento,peso)


            for alimento in lista_alimento:
                if isinstance(alimento, ki.Kiwi):
                    aw_kiwi=alimento.aw_prom_kiwi
                    aw_kiwi_total=aw_kiwi_total+aw_kiwi

                elif isinstance(alimento, ma.Manzana):
                    aw_manzana=alimento.aw_prom_manzana
                    aw_manzana_total=aw_manzana_total+aw_manzana

                elif isinstance(alimento, pa.Papa):
                    aw_papa=alimento.aw_prom_papa
                    aw_papa_total=aw_papa_total+aw_papa

                elif isinstance(alimento, za.Zanahoria):
                    aw_zanahoria=alimento.aw_prom_zanahoria
                    aw_zanahoria_total=aw_zanahoria_total+aw_zanahoria

            
        if isinstance(alimento, f.Fruta):
            aw_fruta=alimento.aw_prom_frutas(aw_kiwi_total,aw_manzana_total)

        if isinstance(alimento, v.Verdura):
            aw_verdura=alimento.aw_prom_verduras(aw_papa_total,aw_zanahoria_total)

        if isinstance(alimento, v.Verdura):
            aw_alimento=alimento.aw_prom_total(aw_kiwi_total,aw_manzana_total,aw_papa_total,aw_zanahoria_total)

        return(aw_manzana_total,aw_kiwi_total,aw_papa_total,aw_zanahoria_total,aw_fruta,aw_verdura,aw_alimento)