# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:44:44 2022

@author: Julian Traversaro
"""

from modulos.Vertice import Vertice
from modulos.Grafo import Grafo 
from modulos.MonticuloBinario import MonticuloBinario
import numpy as np 


                
def encontrarMinimoPrecio(unGrafo, inicio, fin):
    """
    
    
    Parameters
    esta funcion implementa el algoritmo de Dijkstra directo, es decir la busqueda del camino minimo
    Inicialmente se determinan las distancias de todos los vertices al vertice de incio como distancias infinitas
    luego de esto mediante comparaciones  iterativas, se logra diagramar el camino optimo desde nuestro vertice
    de inicio hasta el vertice final 
    ----------
    unGrafo : TYPE
        DESCRIPTION.
    inicio : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    claves=list(unGrafo.obtenerVertices())
    
    for i in range(len(claves)):
        aux = unGrafo.obtenerVertice(claves[i])
        aux.setDistancia(np.inf)
    inicio.setDistancia(0)
    
    cp = MonticuloBinario()
    cp.construirMonticulo([(v.distancia,v) for v in unGrafo])
    while not cp.estaVacia():
        _, verticeActual = cp.eliminarMin()
        
        for verticeSiguiente in verticeActual.conexiones:
            nuevaDistancia = verticeActual.distancia + verticeActual.ponderacion(verticeSiguiente)
            
            if nuevaDistancia < verticeSiguiente.distancia:
                verticeSiguiente.setDistancia(nuevaDistancia)
                verticeSiguiente.predecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)
    return fin.distancia
                
def encontrarMaximoPeso(unGrafo, inicio, fin):
    """
    Esta funcion implementa el mismo algoritmo que el anteriormente mencionado, pero de forma inversa
    el vertice inicial tendra una distancia infinita en comparacion a los vertices vecinos
    de este modo se podra lograr una trayectoria que maximice las posibilidades entre los extremos 

    Parameters
    ----------
    unGrafo : TYPE
        DESCRIPTION.
    inicio : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    claves=list(unGrafo.obtenerVertices())
    
    for i in range(len(claves)):
        aux = unGrafo.obtenerVertice(claves[i])
        aux.setDistancia(0)
    inicio.setDistancia(np.inf)
    
    cp = MonticuloBinario()
    cp.construirMonticulo([(v.distancia,v) for v in unGrafo])
    
    while not cp.estaVacia():
        _, verticeActual = cp.eliminarMin()
        
        for verticeSiguiente in verticeActual.conexiones:
            nuevaDistancia = min(verticeActual.distancia, verticeActual.ponderacion(verticeSiguiente))
            
            if nuevaDistancia > verticeSiguiente.distancia:
                verticeSiguiente.setDistancia(nuevaDistancia)
                verticeSiguiente.predecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)
    
    return fin.distancia 
    
