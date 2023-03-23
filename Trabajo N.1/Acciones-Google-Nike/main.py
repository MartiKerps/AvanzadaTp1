# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:25:32 2023

@author: alumno
"""

from module import module1 as r

from module import module2 as s

from module import module_precios as t

from module import ExtraerDatos as q


Normalizado=[]


x=input("Ingrese nombre del archivo: ")

y=r.escala_precios(x)


Normalizado=t.precios(y)

Porcentual=s.porcentual(y)


x2=input("Ingrese nombre del otro archivo: ")

y2=r.escala_precios(x2)


Normalizado2=t.precios(y2)

Porcentual2=s.porcentual(y2)

Norm=q.ExtraerDatos(Normalizado)
Norm2=q.ExtraerDatos(Normalizado2)
Por=q.ExtraerDatos(Porcentual)
Por2=q.ExtraerDatos(Porcentual2)

import matplotlib.pyplot as plt
import math as m

plt.subplot(2, 1, 1)
plt.plot(Norm, label="Google")
plt.grid()
plt.title('Normalizado')

plt.plot(Norm2, label="Nike")
plt.title('Normalizado')

plt.grid()
plt.legend()
plt.show()


plt.subplot(2, 1, 2)
plt.plot(Por, label="Google")
plt.grid()
plt.title('Porcentual')

plt.plot(Por2, label="Nike")
plt.title('Porcentual')

plt.grid()
plt.legend()
plt.show()

    





