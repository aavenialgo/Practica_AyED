# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:49:03 2022

@author: Julian Traversaro
"""
from modulos.Vertice import Vertice 


class MonticuloBinario():
    """
    Se modifica la clase Monticulo Binario para poder trabajar con pare clave valor necesarios para 
    la aplicacion
    """
    def __init__(self):
        """
        

        Returns
        -------
        None.

        """
        self.listaMonticulo = (0,0)
        self.tamanoActual = 0
        
    def estaVacia(self):
        """
        

        Returns
        -------
        None.

        """
        return self.tamanoActual == 0
    
    def insertar(self,k):
        """
        

        Parameters
        ----------
        k : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltArriba(self,i):
        """
        

        Parameters
        ----------
        i : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        while i // 2 > 0:
          if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
              
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2
    
    def infiltAbajo(self,i):
        """
        

        Parameters
        ----------
        i : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    def eliminarMin(self):
        """
        

        Returns
        -------
        None.

        """    
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado
    
    def hijoMin(self,p):
        """
        

        Parameters
        ----------
        p : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        """ """
        if p * 2 + 1 > self.tamanoActual:
            return p * 2
        
        else:
            if self.listaMonticulo[p*2][0] < self.listaMonticulo[p*2+1][0]:
                return p * 2
            else:
                return p * 2 + 1
    
    def decrementarClave(self, valor, nuevaClave):
        """
        

        Parameters
        ----------
        valor : TYPE
            DESCRIPTION.
        nuevaClave : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        hecho = False
        i=1
        clave=0
        while not hecho and i<=self.tamanoActual:
            if self.listaMonticulo[i][1]== valor:
                hecho =True 
                clave=i
            else:
                i=i+1
        if clave >0:
            self.listaMonticulo[clave]=(nuevaClave, self.listaMonticulo[clave][1])
            self.infiltArriba(clave)

    
    def construirMonticulo(self,unaTupla):
        """
        

        Parameters
        ----------
        unaTupla : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """    
        self.tamanoActual = len(unaTupla)
        self.listaMonticulo = [(0,0)]
        for dato in unaTupla:
            self.listaMonticulo.append(dato)
        i = len(unaTupla) // 2
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    
    def __contains__(self,vertice):
        """
        

        Parameters
        ----------
        vertice : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        for par in self.listaMonticulo:
            if par[1] ==vertice:
                return True 
        return False
    
    def devolverMinimo(self):
        """
        

        Returns
        -------
        None.

        """
        return self.listaMonticulo[1][1]
    
    
    def __iter__(self):
        """
        

        Returns
        -------
        None.

        """
        return iter(self.listaMonticulo)
    
    def __len__(self):
        """
        

        Returns
        -------
        None.

        """
        return self.tamanoActual
    
    def __str__(self):
        """
        

        Returns
        -------
        None.

        """
    
        lista=''
        for i in range(1, len(self.listaMonticulo)):
            lista+=str(self.listaMonticulo[i])+ ' '
        
        return lista
    

