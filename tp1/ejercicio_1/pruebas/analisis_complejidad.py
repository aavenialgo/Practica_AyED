# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:43:16 2022

@author: Andres Venialgo

Este programa se encarga de analizar el el algorimo de ordenamiento 
para el TAD ListaDobleEnlazada. Se grafican las cantidad de elementos en
el TAD en funcion del tiempo.
"""

from modulos.LDE import ListaDobleEnlazada
import random as rd
from matplotlib import pyplot as plt
from timeit import Timer
import time

numeroElementos = [i for i in range(1, 1002, 100)]
vectorTiempos = [0.0 for i in range(len(numeroElementos))]
vectorIteraciones = [0.0 for i in range(len(numeroElementos))]
indice = 0
for n in numeroElementos:
    lista = ListaDobleEnlazada()

    for i in range(n):
        lista.agregar(rd.randint(0, n))
    
    #mido el tiempo
    tic = time.perf_counter()
    cantidad_iteraciones= lista.ordenar()
    toc = time.perf_counter()
    vectorIteraciones[indice] = cantidad_iteraciones
    vectorTiempos[indice] = toc - tic
    
    indice +=1
plt.title('Curva Temporal del Algoritmo de Ordenamiento\n')
plt.xlabel('n - Cantidad de elementos en la LDE')
plt.ylabel('t(n) - Tiempo de ejecución [s]')
plt.plot(numeroElementos, vectorTiempos, 'r')
plt.show()
 # Grafica para las iteracciones en funcion del tiempo
 
plt.title('Curva de Cantidad de Iteraciones del Algoritmo de Ordenamiento\n')
plt.xlabel('n - Cantidad de elementos en LDE')
plt.ylabel('iteraciones(n) - Cantidad de Iteraciones ')
plt.plot(numeroElementos, vectorIteraciones, 'b')
 