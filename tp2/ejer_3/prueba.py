# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:03:01 2022

@author: Andres Venialgo
"""

from modulos.Grafo import Grafo

from modulos.Dijkstra import *

g=Grafo()
for i in range (8):
    g.agregarVertice(i)
g.listaDeVertices


g.agregarArista('A','F',12)
g.agregarArista('A','C',24)
g.agregarArista('A','E',45)
g.agregarArista('F','C',4)
g.agregarArista('F','D',120)
g.agregarArista('C','E',11)
g.agregarArista('C','D',12)
g.agregarArista('C','B',22)
g.agregarArista('C','G',20)
g.agregarArista('D','H',29)
g.agregarArista('B','H',10)
g.agregarArista('B','D',31)
g.agregarArista('B','G',33)
g.agregarArista('G','H',17)

p = encontrarMinimoPrecio(g, g.obtenerVertice('A'), g.obtenerVertice('H'))
print(p)