# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:02:04 2022

@author: venialgo Andres
"""

class MonticuloBinario():
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
    
    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2
              
    
    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    def hijoMin(self,p):
        """ """
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        else:
            if self.listaMonticulo[p*2] < self.listaMonticulo[p*2+1]:
                return p * 2
            else:
                return p * 2 + 1
    
    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    
    def __iter__(self):
        return iter(self.listaMonticulo)
    
    def __len__(self):
        return self.tamanoActual
    
    # @property
    # def tamanio(self):
    #     return self._tamanoActual
    
    # @tamanio.setter
    # def tamanio(self, value):
    #     self._tamanoActual = value
    #     pass
    


if __name__ == '__main__':
    a = MonticuloBinario()
    lista = [5, 9, 11, 14, 18, 19]
    a.construirMonticulo(lista)
    print("Tamaño ",a.tamanoActual)


      
    