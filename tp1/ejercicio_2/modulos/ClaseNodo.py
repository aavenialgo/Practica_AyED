# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:56:08 2022

@author: Julian Traversaro
"""

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior= None
    @property 
    def dato(self):
        return self._dato
    @property
    def siguiente(self):
        return self._siguiente
    
    @dato.setter
    def dato(self,nuevodato):
        self._dato = nuevodato
        
    @siguiente.setter
    def siguiente(self,nuevosiguiente):
        self._siguiente = nuevosiguiente
        
    @property
    def anterior(self):
        return self._anterior
    
    @anterior.setter
    def anterior(self,nuevodato):
        self._anterior=nuevodato
    
    def __str__(self):
        return str(self.dato)
    
    def __repr__(self)-> str:
        return str(self.dato)       
    
if __name__=='__main__':
    n=Nodo(2)
    print(n.dato)
    
   