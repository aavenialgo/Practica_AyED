# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:02:26 2022

@author: Venialgo Andres
"""
# from nodo import Nodo
from time import sleep
class ListaDobleEnlazada:
    def __init__ (self):
        # self.__nodo = Nodo(dato_inicial)
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
        
    
    def estaVacia(self):
        return self._cabeza == None
    
    
    def agregar(self,item):
        """Agrega un elemento al principio (cabeza) de la lista """
        temp= Nodo(item)
        
        if self.tamanio == 0:    
            self.cabeza = temp
            self.cola = temp
        else:
        
            # temp = Nodo(item)
            temp.siguiente = self.cabeza
            self.cabeza.anterior = temp
            self.cabeza= temp
        self.tamanio+=1 
        
    def anexar(self, item):
        """ Agrega un elemento al final (cola) de la lista """
        temp = Nodo(item)
        
        if self.tamanio == 0:    
            self.cabeza = temp
            self.cola = temp
            
        else:
            self.cola.siguiente = temp
            temp.anterior = self.cola
            # temp.siguiente = None
            self.cola = temp
            
        self.tamanio +=1
        
    
    def insertar(self, pos, item):
        """Agrega un elemento en la posicion "pos" """
        
        nuevo = Nodo(item)
        temp = self.cabeza
        for it in range(pos-1):
            temp = temp.siguiente
        nuevo.siguiente = temp.siguiente
        temp.siguiente.anterior = nuevo
        temp.siguiente = nuevo
        nuevo.anterior = temp 
        self.tamanio +=1
        
    
    def extraer(self, pos ):
        dato = 0
        
        if pos == 0:
           dato = self.cabeza.dato
           self.cabeza = self.cabeza.siguiente
           self.cabeza.anterior = None
        elif pos == (self.tamanio -1):
            dato = self.cola.dato
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        else:
            temp = self.cabeza
            for it in range(pos-1):
                temp = temp.siguiente
            dato   = temp.dato
            temp.anterior.siguiente = temp.siguiente
            temp.siguiente.anterior = temp.anterior
        self.tamanio-=1
        return dato
           
    def concatenar(self,p_lista):
        """Concatena la lista que se pasa por parametro a la lista actual """
        if  p_lista.tamanio != 0:
            self.cola = p_lista.cabeza
            self.tamanio = self.tamanio + p_lista.tamanio
            
    
    def ordenar(self): 
        """Implementa un metodo de ordenamiento por insercion para ordenar la
        lista de menor a mayor """
        if self.cabeza != None:
            nodo = self.cabeza.siguiente
            
            # valor actual es nodo
            # una lista[pos-1] es nodo.anterior
            for indice in range(1,self.tamanio):
                pos = indice
                sleep(3)
                while nodo :
                    
                    print("nodo dato =", nodo)
                    if (nodo.anterior.dato > nodo.dato) and pos>0:
                        nodo = nodo.anterior
                        pos -= 1
                    
                nodo = nodo.siguiente
        nodo = self.cabeza.siguiente
        while nodo:
            
            while nodo:
                pass
            
   #     def ordenamientoPorInsercion(unaLista):
           # for indice in range(1,len(unaLista)):
        
           #   valorActual = unaLista[indice]
           #   posicion = indice
        
           #   while posicion>0 and unaLista[posicion-1]>valorActual:
           #       unaLista[posicion]=unaLista[posicion-1]
           #       posicion = posicion-1
        
           #   unaLista[posicion]=valorActual
    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self,item):
        self._tamanio = item 
        
    def __iter__(self):
        """metodo para iterar """
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente
            
            
    def esta_vacia(self):
        return self.tamanio == 0
        
    def __str__ (self):
        lista =[nodo for nodo in self ]
        return str(lista)
    
    
    
class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self,nuevodato):
        self._dato = nuevodato
    
    @property
    def siguiente(self):
        return self._siguiente

    
    @siguiente.setter
    def siguiente(self,nuevosiguiente):
        self._siguiente = nuevosiguiente
        
    @property
    def anterior(self):
        return self._anterior
    @anterior.setter
    def anterior(self, item):
        self._anterior = item
        
    def __str__(self):
        return  str(self.dato)
    
    def __repr__(self):
        return  str(self.dato)



        
if __name__ == '__main__':
    lista2= ListaDobleEnlazada()
    lista2.agregar(10)
    lista2.agregar(20)
    lista2.agregar(40)
    
    print(lista2)

    print("\nInserto el valor 30 en la pos 1")
    lista2.insertar(1,30)
    print(lista2)
    
    print("\nagrego el valor 50")
    lista2.agregar(50)
    print(lista2)
    
    print("\nextraigo el elemento 4")
    lista2.extraer(4)
    print (lista2)
    
    print("\nextraigo el primer elemento\n")
    lista2.extraer(0)
    print (lista2)

    print ("\nextraigo el ultimo elemento")
    lista2.extraer(lista2.tamanio-1)
    print (lista2)
    print()
    
    print("anexo 12")
    lista2.anexar(12)
    print(lista2)
    
    lista2.anexar(8)
    print(lista2)
    
    lista2.anexar(9)
    print(lista2)
    
    print()
    print("agrego")
    lista2.agregar(67)
    
    print(lista2)
    
    # print("\nordeno la lista")
    
    # lista2.ordenar()
    # print (lista2)

    