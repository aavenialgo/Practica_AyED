# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:35:25 2022

@author: Julian Traversaro
"""



import random
from ListaNoOrdenada import ListaNoOrdenada
class ColaDoble(ListaNoOrdenada):
       
    def __init__(self):
        '''
        Clase ColaDoble hereda metodos de Lista no ordenada
        Crea una cola doble nueva y vacía.
        Returns
        -------
        None.

        '''
        super().__init__()
    
    @property
    def tamanio(self):
        '''
        devuelve el número de ítems en la cola doble. No necesita parámetros y devuelve un entero.

        Returns
        -------
        None.

        '''
        return super().tamanio
    
    @property
    def estaVacia(self):
        '''
        
        comprueba si la cola doble está vacía. No necesita parámetros y devuelve un valor booleano.
        Returns
        -------
        TYPE
            Booleano.

        '''
        return super().esta_vacia
    
    def agregarFrente(self, item):
        '''
        
        añade un nuevo ítem al frente de la cola doble. Necesita el ítem y no devuelve nada.
        Parameters
        ----------
        item : TYPE
            Item es cualquier tipo de objeto que se desee agregar a la cola doble.

        Returns
        
        -------
        None.

        '''
        super().agregar(item)
    
    def agregarFinal(self, item):
        '''
        
        añade un nuevo ítem en el final de la cola doble. Necesita el ítem y no devuelve nada.
        Parameters
        ----------
        item : TYPE
            Item es cualquier tipo de objeto que se desee agregar a la cola doble..

        Returns
        -------
        None.

        '''
        super().anexar(item)
    
    def removerFrente(self):
        '''
        limina el ítem que está en el frente de la cola doble. No necesita parámetros 
        y devuelve el ítem.

        Returns
        -------
        TYPE
            el item eliminado puede ser cualquier tipo de objeto que haya sido añadido con 
            anteriorirdad a la cola doble.

        '''
        frente=0
        return super().extraer(posicion=frente)
    
    def removerFinal(self):
        '''
        elimina el ítem que está al final de la cola doble. No necesita parámetros y devuelve el ítem.

        Returns
        -------
        TYPE
            el item eliminado puede ser cualquier tipo de objeto que haya sido añadido con 
            anteriorirdad a la cola doble.

        '''
        
        return super().extraer(posicion=self.tamanio)
    
                
    # def __getitem__(self, indice):
    #     return super().buscar(indice)
