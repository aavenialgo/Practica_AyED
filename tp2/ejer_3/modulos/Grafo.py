# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:23:09 2022

@author: Julian Traversaro
"""
from modulos.Vertice import Vertice
import numpy as np 

class Grafo:
    def __init__(self):
        self._listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self._listaVertices[clave] = nuevoVertice
        """
        Asigno a cada vertice una distancia infinita 
        """
        
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self._listaVertices:
            return self._listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self._listaVertices:
            nv = self.agregarVertice(de)
        if a not in self._listaVertices:
            nv = self.agregarVertice(a)
        self._listaVertices[de].agregarVecino(self._listaVertices[a], int(costo))

    def obtenerVertices(self):
        return self._listaVertices.keys()

    def __iter__(self):
        return iter(self._listaVertices.values())
    @property
    def listaDeVertices(self):
        return self._listaVertices
    
    
if __name__== '__main__':
    g=Grafo()
    for i in range (5):
        g.agregarVertice(i)
    g.listaDeVertices
    
    
    g.agregarArista(0,1,5)
    g.agregarArista(0,5,2)
    g.agregarArista(1,2,4)
    g.agregarArista(2,3,9)
    g.agregarArista(3,4,7)
    g.agregarArista(3,5,3)
    g.agregarArista(4,0,1)
    g.agregarArista(5,4,8)
    g.agregarArista(5,2,1)
    
    for v in g:
        for w in v.conexiones:
            print("( %s , %s )" % (v.Id, w.Id))