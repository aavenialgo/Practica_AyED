# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 07:55:31 2022

@author: Julian Traversaro
"""
import numpy as np 
class Vertice:
    def __init__(self,clave):
        """
        

        Parameters
        ----------
        clave : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self._id = clave
        self._conectadoA = {}
        self._distancia=0
        self._predecesor=0
    
    def agregarVecino(self,vecino,ponderacion=0):
        """
        

        Parameters
        ----------
        vecino : TYPE
            DESCRIPTION.
        ponderacion : TYPE, optional
            DESCRIPTION. The default is 0.

        Returns
        -------
        None.

        """
        self._conectadoA[vecino] = ponderacion

    def __str__(self):
        """
        

        Returns
        -------
        None.

        """
        return str(self._id) + ' conectadoA: ' + str([x._id for x in self._conectadoA])
    @property 
    def conexiones(self):
        """
        

        Returns
        -------
        None.

        """
        return self._conectadoA.keys()
    @property
    def Id(self):
        """
        

        Returns
        -------
        None.

        """
        return self._id
    
    def ponderacion(self,vecino):
        """
        

        Parameters
        ----------
        vecino : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        return self._conectadoA[vecino]
    
    @property
    def distancia(self):
        """
        

        Returns
        -------
        None.

        """
        return self._distancia
    
    #@distancia.setter
    def setDistancia(self, valor):
        """
        

        Parameters
        ----------
        valor : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self._distancia=valor
    
    def predecesor(self, predecesor):
        """
        

        Parameters
        ----------
        predecesor : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
    
        self._predecesor=predecesor
        
       
        