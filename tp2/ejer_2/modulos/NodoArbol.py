# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:28:39 2022

@author: Andres Venialgo
"""

class NodoArbol:
    def __init__(self,clave,valor, izquierdo = None, derecho = None, padre = None):
         self.clave = clave
         self.cargaUtil = valor
         self.hijoIzquierdo = izquierdo
         self.hijoDerecho = derecho
         self.padre = padre
         self.factorEquilibrio = 0
         
    @property
    def factorEquilibrio(self):
        return self._factorEquilibrio
    
    @factorEquilibrio.setter
    def factorEquilibrio(self, value):
        self._factorEquilibrio = value
    @property
    def clave(self):
        return self._clave
    
    @clave.setter
    def clave(self,p_clave):
        self._clave = p_clave
        
    @property
    def cargaUtil(self):
        return self._cargaUtil
    
    @cargaUtil.setter 
    def cargaUtil(self,valor):
        self._cargaUtil = valor
        
    @property
    def padre(self):
        return self._padre
    @padre.setter
    def padre (self, p_padre):
        self._padre = p_padre
    
    @property
    def hijoIzquierdo(self):
        """ Devuelve hijo izquierdo """
        return self._hijoIzquierdo
    
    @hijoIzquierdo.setter
    def hijoIzquierdo(self,nueva_hoja):
        """ Setter de hijo izquierdo """
        self._hijoIzquierdo=nueva_hoja
    
    @property
    def hijoDerecho(self):
        """ Getter de hijo derecho """
        return self._hijoDerecho
     
    @hijoDerecho.setter
    def hijoDerecho(self,nueva_hoja):
        """ Setter de hijo derecho """
        self._hijoDerecho=nueva_hoja
    
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    
    #--------------------------------------------------------------------------
    """
    Para saber si es hijo derecho o hijo izquierdo utilizamos los nombres sucesor y 
    predecesor respectivamente.
    """
    @property
    def sucesor(self):
        """ Devuelve True si es hijo derecho """
        return self.padre and self.padre.hijoIzquierdo == self
    
    @property
    def predecesor(self):
        """Devuelve True si es hijo izquierdo """
        return self.padre and self.padre.hijoDerecho == self
    #--------------------------------------------------------------------------
    @property
    def esRaiz(self):
        return not self.padre
    @property
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    
    @property
    def tieneHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo
    
    @property
    def tieneHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo
    
    @property
    def tieneHijoDerecho(self):
        return self.hijoDerecho != None
    
    @property
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo != None
    
    
    
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
            
    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho:
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                   if self.esHijoIzquierdo():
                       suc = self.padre
                   else:
                       self.padre.hijoDerecho = None
                       suc = self.padre.encontrarSucesor()
                       self.padre.hijoDerecho = self
        return suc
    
    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo:
            actual = actual.hijoIzquierdo
        return actual    
    
    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                   self.padre.hijoIzquierdo = None
            else:
                   self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                   if self.esHijoIzquierdo():
                      self.padre.hijoIzquierdo = self.hijoIzquierdo
                   else:
                      self.padre.hijoDerecho = self.hijoIzquierdo
                   self.hijoIzquierdo.padre = self.padre
            else:
                   if self.esHijoIzquierdo():
                      self.padre.hijoIzquierdo = self.hijoDerecho
                   else:
                      self.padre.hijoDerecho = self.hijoDerecho
                   self.hijoDerecho.padre = self.padre

    def inorden(self,arbol):
        if arbol != None:
            self.inorden(arbol.hijoIzquierdo)
            print(arbol.raiz)
            self.inorden(arbol.hijoDerecho)   

    def __iter__(self):
       if self:
          if self.tieneHijoIzquierdo():
                 for elem in self.hijoIzquierdo:
                    yield elem
          yield self.clave
          if self.tieneHijoDerecho():
                 for elem in self.hijoDerecho:
                    yield elem
       else:
           raise StopIteration
    
    def __getitem__(self,clave):
        return self.obtener(clave)
    
    def __str__(self):
        return str(self.clave)+ ": " + str(self.cargaUtil)
    
if __name__ == '__main__':
    a = NodoArbol("manzana", 'roja')
    print(a)
    a.hijoIzquierdo= NodoArbol("banana", "amarilla")
    print(a.hijoIzquierdo)

    

        
        
        