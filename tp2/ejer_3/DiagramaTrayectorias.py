# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:23:31 2022

@author: Julian Traversaro
"""
from modulos.Grafo import Grafo
from modulos.Dijkstra import encontrarMinimoPrecio, encontrarMaximoPeso 

"""
Creamos un grafo con sus vertices como ciudades y sus aristas se conforman por el maximo peso transportable
"""
g=Grafo()
g1=Grafo()
lector_datos=[]
numero_ciudades=0
with open ('rutas.txt', 'r') as archivo:
    for linea in archivo:
        numero_ciudades+=1
        lector_datos.append(linea.split(','))
        
# Punto 1 encontrar el peso maximo que se pueda transportar 
#------------------------------------------------------------------------------     
#Se crea el grafo propiamente dicho y se grafica 
for ciudades in range(numero_ciudades):
    g.agregarArista(lector_datos[ciudades][0],lector_datos[ciudades][1], lector_datos[ciudades][2])
    

# for v in g:

#     for w in v.conexiones:

#         print("( %s , %s )" % (v.Id, w.Id))
        

peso_maximo=encontrarMaximoPeso(g, g.obtenerVertice('CiudadBs.As.'), g.obtenerVertice('Rosario') )
print(f'El maximo peso transportado ente CiudadBs.As. y Rosario es: {peso_maximo} ')

#Punto 2 encontrar el precio minimo para transportar la maxima carga 
#-----------------------------------------------------------------------------
#Se crea el grafo propiamente dicho y se grafica 
for ciudades in range(numero_ciudades):
    g1.agregarArista(lector_datos[ciudades][0],lector_datos[ciudades][1], lector_datos[ciudades][3])
    


minimo_precio=encontrarMaximoPeso(g1, g1.obtenerVertice('CiudadBs.As.'), g1.obtenerVertice('Rosario') )
print(f'El minimo precio para el maximo peso transportado ente CiudadBs.As. y Rosario es: {minimo_precio} ')
