# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:11:27 2022

@author: Julian Traversaro
"""

from ClaseNodo import Nodo

class ListaNoOrdenada:

    def __init__(self):
        '''
        

        Returns
        -------
        None.

        '''
        self.cabeza = None
        self.cola   = None
        self._n_nodos=0
        
    @property
    def esta_vacia(self):
        '''
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return self.cabeza == None
    
    @property
    def tamanio(self):
   
        return self._n_nodos
    
    
    def agregar(self,item):
        '''
        

        Parameters
        ----------
        item : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        
        temp = Nodo(item)
        if self.tamanio == 0:
           self.cabeza=temp
           self.cola=temp
           
        else: 
           temp.siguiente=self.cabeza
           self.cabeza.anterior=temp
           self.cabeza = temp 
        
        self._n_nodos=self._n_nodos+1
        
   
    def anexar(self, item):
        '''
        

        Parameters
        ----------
        item : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
    
        temp=Nodo(item)
        if self.tamanio == 0:
            self.cola=temp
            self.cabeza=temp
        else: 
            self.cola.siguiente=temp
            temp.anterior=self.cola
            
            self.cola=temp
        self._n_nodos=self._n_nodos+1      
    
    def insetar(self, posicion, item):
        '''
        

        Parameters
        ----------
        posicion : TYPE
            DESCRIPTION.
        item : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if posicion == 0:
            self.agregar(item)
        elif posicion == self.tamanio-1:
            temp=Nodo(item)
            self.cola.anterior.siguiente=temp
            temp.anterior=self.cola.anterior
            temp.siguiente=self.cola
            self.cola.anterior=temp
        else:
            nuevo=Nodo(item)
            temp=self.cabeza
            for i in range(posicion-1):
                temp=temp.siguiente

            nuevo.siguiente=temp.siguiente
            temp.siguiente.anterior=nuevo
            temp.siguiente=nuevo
            nuevo.anterior=temp

    
    
    def buscar(self,posicion):
        '''
        

        Parameters
        ----------
        posicion : TYPE
            DESCRIPTION.

        Returns
        -------
        item : TYPE
            DESCRIPTION.

        '''
        actual = self.cabeza
        try:
            for i in range(posicion):
                actual=actual.siguiente
            item=actual.dato
        except AttributeError: 
            print('No hay mas datos en la lista')
            
                                 
        return item   
   
    def copiar(self):
        lista_copiada=ListaNoOrdenada()
        aux=self.cabeza
        for i in range(self.tamanio):
            lista_copiada.anexar(aux)
            aux=aux.siguiente
        
        #lista_copiada=[nodo for nodo in self]
        
        return lista_copiada
        
    def extraer(self,posicion=-1):
        '''
        

        Parameters
        ----------
        posicion : TYPE, optional
            DESCRIPTION. The default is -1.

        Returns
        -------
        item_eliminado : TYPE
            DESCRIPTION.

        '''
        try: 
            self._n_nodos=self._n_nodos-1
            if self._n_nodos >=0:
                item_eliminado=self.buscar(posicion)
            else:
                item_eliminado=self.cabeza
            if posicion == 0:
                self.cabeza.anterior= None
                self.cabeza=self.cabeza.siguiente
            
            elif posicion == self.tamanio:
                self.cola=self.cola.anterior
                self.cola.siguiente=None
            else:
                 temp=self.cabeza 
                 for i in range(posicion):
                       temp=temp.siguiente
                 temp.siguiente.anterior=temp.anterior
                 temp.anterior.siguiente=temp.siguiente
                 temp.siguiente=None
                 temp.anterior=None
        except AttributeError:
            print('No se encontro item')
            
        
        return item_eliminado
            
            
    def __iter__(self):
        '''
        

        Yields
        ------
        nodo : TYPE
            DESCRIPTION.

        '''
        nodo=self.cabeza
        while nodo:
            yield nodo
            nodo=nodo.siguiente

    # def __setitem__(self,posicion, item):
    #         self.intesertar(posicion, item)
    
    def __len__(self):
        return self.tamanio
    
    def __str__(self):
        lista =[nodo for nodo in self ]
        return str(lista)
    
    def __rerpr__(self):
        
        return str(self)
    def invertir(self):
        pass
            
        
        
        


if __name__== '__main__':
    lista_0=ListaNoOrdenada()
    #print(lista_0.esta_vacia)
    
    for i in range(10):
        lista_0.anexar(i)
    
    # for nodo in lista_0:          
    #     print(nodo)
    # print()
    
    # lista_0.insetar(2, 'A')
    
    # for nodo in lista_0:          
    #     print(nodo)
    print(lista_0)
    item_extraido=lista_0.extraer(0)
    
    print('item extraido')
    print(item_extraido)
    item_extraido=lista_0.extraer(0)
    
    print('item extraido')
    print(item_extraido)
    
    print(lista_0)
    
    copia=lista_0.copiar()
    print(lista_0)
    print(type(lista_0))    
    print(type(copia))    
    
    # lista_0.invertir()
    # print(lista_0)
    
    