# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:23:51 2022

@author: alumno
"""
from modulos.NodoArbol import NodoArbol
 

class ArbolAVL(): 
    def __init__(self):
        self.raiz = None
        self.tamano = 0
        self.factorEquilibrio = 0
        
    @property            
    def tamano(self):
        """ Devuelve el la cantidad de nodos del arbol """
        return self._tamano
    
    @tamano.setter
    def tamano(self, value):
        self._tamano = value
    
    def agregar(self,clave,valor):
        """ Agrega un nodo al arbol """
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1
        
    def _agregar(self,clave,valor,nodoActual):
        """ Metodo auxiliar y recursivo para encontrar la posicion en donde 
        insertar el nodo """
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo:
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho:
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)
            
    def eliminarCargaUtil(self,clave):
        """Elimina la carga util del nodo """
        it = iterador(self)
        for i in it:
            if i.clave ==clave:
                i.cargaUtil =None
        
        
    
    def actualizarEquilibrio(self,nodo):
        """El metodo compruema primero si el nodo actual requiere un reequilibrio
        , si es el caso reequilibra y no requiere hacer otra accion. 
        si NO necesita reequilibrio entonces se ajuta el factor de equilibrio del 
        padre Si el factor de equilibrio del padre no es cero, entonces el algoritmo
        continúa ascendiendo en el árbol, hacia la raíz"""
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo:
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho:
                    nodo.padre.factorEquilibrio -= 1
    
            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    
    def reequilibrar(self,nodo):
        """Aqui se realiza las rotaciones correspondientes debido al desequilibrio"""
        if nodo.factorEquilibrio < 0:
               if nodo.hijoDerecho.factorEquilibrio > 0:
                  self.rotarDerecha(nodo.hijoDerecho)
                  self.rotarIzquierda(nodo)
               else:
                  self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
               if nodo.hijoIzquierdo.factorEquilibrio < 0:
                  self.rotarIzquierda(nodo.hijoIzquierdo)
                  self.rotarDerecha(nodo)
               else:
                  self.rotarDerecha(nodo)
    
    def obtener(self,clave):
        """ Devuelve la carga util del nodo"""
        if self.raiz:
            res = self._obtener(clave,self.raiz)
            if res:
                   return res.cargaUtil
            else:
                   return None
        else:
            return None
    
    def _obtener(self,clave,nodoActual):
        """ Devuelve el nodo, en funcion a la clave que se le pasa """
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)

#--------------------------- ROTACIONES --------------------------------------------
    def rotarIzquierda(self,rotRaiz):
        """ Realiza una rotacion simple hacia la izquierda """
        nuevaRaiz = rotRaiz.hijoDerecho
        
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz:
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo:
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
        
        
    def rotarDerecha(self, rotRaiz):
        """ Realiza una rotacion simple hacia la derecha """
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if rotRaiz.padre is None:
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            elif rotRaiz.esHijoDerecho:
                rotRaiz.padre.hijoDerecho = nuevaRaiz

        nuevaRaiz.hijoDerecho = rotRaiz
        # rotRaiz.padre = nuevaRaiz
        rotRaiz.factorE = rotRaiz.factorEquilibrio +1 - min(0,nuevaRaiz.factorEquilibrio)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(0,rotRaiz.factorEquilibrio)

    
#-------------------------------------------------------------------------------------
    
       
    def eliminar(self,clave):
        """elimina un nodo del arbol """
        if self.tamano > 1:
           nodoAEliminar = self._obtener(clave,self.raiz)
           if nodoAEliminar:
               self.remover(nodoAEliminar)
               self.tamano = self.tamano-1
           else:
               raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
           self.raiz = None
           self.tamano = self.tamano - 1
        else:
           raise KeyError('Error, la clave no está en el árbol')
    
    def remover(self,nodoActual):
        if nodoActual.esHoja: #hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneHijos: #interior
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil
            # self.reequilibrar(nodoActual)
    
        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo:
                if nodoActual.esHijoIzquierdo:
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho:
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                       nodoActual.hijoIzquierdo.cargaUtil,
                                       nodoActual.hijoIzquierdo.hijoIzquierdo,
                                       nodoActual.hijoIzquierdo.hijoDerecho)
                # self.reequilibrar(nodoActual)

            else:
                if nodoActual.esHijoIzquierdo:
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho:
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                       nodoActual.hijoDerecho.cargaUtil,
                                       nodoActual.hijoDerecho.hijoIzquierdo,
                                       nodoActual.hijoDerecho.hijoDerecho)
                # self.reequilibrar(nodoActual)

            
    
    def __delitem__(self,clave):
       self.eliminar(clave)
                    
    @property
    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano
    
    def __setitem__(self,c,v):
        self.agregar(c,v)
       
    def __getitem__(self,clave):
       return self.obtener(clave)

    def __contains__(self,clave):
        """Es para sobrecargar el operador in, si un elemento 
        pertenece o no  """
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False
        
    def inorden(self,nodo):
        if nodo != None:
            self.inorden(nodo.hijoIzquierdo)
            print(nodo)
            self.inorden(nodo.hijoDerecho)
    
class iterador():
    def __init__(self,arbol,claveInicial= None,claveFin = None):
        
        self.parar = False
        # self._arbol = arbol
        if claveFin != None:
            self.nodoFin = arbol._obtener(claveFin,arbol.raiz)
        else:
            self.nodoFin = arbol.raiz
            
            while self.nodoFin!= None:
                self.nodoFin = self.nodoFin.encontrarSucesor()
        
        if claveInicial == None:
            self.nodoinicio = arbol.raiz
            self.nodoinicio = self.nodoinicio.encontrarMin()
        else:
            self.nodoinicio =arbol._obtener(claveInicial, arbol.raiz)


        
    def __iter__(self):
        return self
    
    def __next__(self):
        salida = self.nodoinicio 
                    
        if salida == None or self.parar == True :
            raise StopIteration
        
        if self.nodoinicio == self.nodoFin:
            self.parar = True
            
        self.nodoinicio = self.nodoinicio.encontrarSucesor()
    
        return salida


        
    
    
    
    
    
    
    