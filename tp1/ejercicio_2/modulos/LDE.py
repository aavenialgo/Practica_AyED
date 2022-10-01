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
    
        
    
    def esta_vacia(self):
        """ devuelve True si la lista esta vacía"""
        return self._cabeza == None
    
    
    def agregar(self,item):
        """Agrega un elemento al principio (cabeza) de la lista """
        temp= Nodo(item)
        
        if self.tamanio == 0:    
            self.cabeza = temp
            self.cola = temp
        else:
        
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
        """Agrega un nuevo itema a la lista en la posicion 'pos' """
        
        if pos < 0 or pos >= self.tamanio:
            raise IndexError("Posicion fuera de rango")
        else:
            nuevo = Nodo(item)
            temp=self.cabeza
            if self.tamanio == 0:
                self.cabeza = nuevo
                self.cola = nuevo
                
            elif pos == (self.tamanio-1) :
                self.cola.anterior.siguiente = nuevo
                nuevo.anterior=self.cola.anterior
                nuevo.siguiente= self.cola
                self.cola.anterior=nuevo
                
                
            elif pos == 0:
                nuevo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo
                self.cabeza= nuevo
                
            else:
                for it in range(pos-1):
                    temp = temp.siguiente
                
             
                nuevo.siguiente = temp.siguiente
                temp.siguiente.anterior = nuevo
                temp.siguiente = nuevo
                nuevo.anterior = temp 
                
            self.tamanio +=1

        
    
    def extraer(self, pos=None):
        """elimina y devuelve el ítem en "posición". Si no se 
        indica el parámetro posición o se ingresa -1, se elimina 
        y devuelve el último elemento de la lista, cualquier otro
        valor negativo lanzara una exception"""
        dato = 0

        if pos == None or pos == -1:
            pos = self.tamanio-1
        elif pos <-1 or pos >= self.tamanio:
            raise Exception("Posición no valida")
            
        if pos == 0:
           dato = self.cabeza
           self.cabeza = self.cabeza.siguiente
           self.cabeza.anterior = None
        elif pos == (self.tamanio -1):
            dato = self.cola
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        else:
            temp = self.cabeza
            for it in range(pos):
                temp = temp.siguiente
            dato = temp
            temp.anterior = temp.siguiente
            temp.siguiente = temp.anterior
        self.tamanio-=1
        return dato
    
    def copiar(self):
        """Realiza una copia de la lista elemento a elemento y
        devuelve una copia """
        lista_copiada = ListaDobleEnlazada()
        nodo = self.cabeza
        for i,nodo in enumerate(self) :
            lista_copiada.anexar(nodo.dato)
        return lista_copiada
           
    
    def ordenar(self): 
        """Ordena de menor a mayor """
        
        for i in range (self.tamanio,0, -1):
            if (i==1):
                break
            aux = self.cabeza
            pos_mayor = 1
            nodo_mayor = Nodo(-9999999)
            
            for j in range (1, i+1):
                
                if aux.dato >nodo_mayor.dato:
                    nodo_mayor = aux
                    pos_mayor = j
                if j == i:
                    if pos_mayor == 1:
                        self.cabeza = self.cabeza.siguiente
                        self.cabeza.anterior = None
                    elif pos_mayor != i:
                        nodo_mayor.anterior.siguiente = nodo_mayor.siguiente
                        nodo_mayor.siguiente.anterior = nodo_mayor.anterior
                    
                    if pos_mayor != i and i != self.tamanio :
                        aux.siguiente.anterior = nodo_mayor
                        nodo_mayor.anterior = aux
                        nodo_mayor.siguiente = aux.siguiente
                        aux.siguiente = nodo_mayor
                    elif pos_mayor != i and i == self.tamanio:
                        self.cola.siguiente = nodo_mayor
                        nodo_mayor.anterior = self.cola
                        self.cola = nodo_mayor
                        self.cola.siguiente = None
                aux = aux.siguiente
                    
                
    
    @property
    def tamanio(self):
        """getter de tamanio """
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self,item):
        """Setter de tamanio """
        self._tamanio = item 
        
    def __iter__(self):
        """metodo para iterar """
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente
            
            
    def esta_vacia(self):
        """Devuelve True si la lista esta vacia """
        return self.tamanio == 0
    
    def concatenar(self,p_lista):
        """Concatena al final la lista que se pasa por parametro a
        la lista actual """
        if  p_lista.tamanio != 0:
            temp = self.cola
            self.cola.anterior.siguiente = temp
            temp.anterior = self.cola.anterior
            
            p_lista.cabeza.anterior = temp
            temp.siguiente = p_lista.cabeza
            
                     
            self.cola = p_lista.cola
            p_lista.cola.anterior.siguiente = self.cola
            self.cola.anterior =  p_lista.cola.anterior
            self.tamanio = self.tamanio + p_lista.tamanio
            
        return self
            
            
    def invertir(self):
        """ Invierte el orden de los elementos de la lista"""
            
        temp = self.cabeza
        self.cabeza = self.cola
        self.cola = temp
        for i in range (self.tamanio-1):
            temp = temp.siguiente
            if i == 0:
                temp.anterior.siguiente = None

            else:
                temp.anterior.siguiente = temp.anterior.anterior
            temp.anterior.anterior = temp
        temp.siguiente = temp.anterior
        temp.anterior = None
        
         
        
    def __str__ (self):
        lista =[nodo for nodo in self ]
        return str(lista)
    
    
    def __getitem__(self, pos):
        nodo = self.cabeza
        for i,nodo in enumerate(self) :
            nodo.siguiente
            if i == pos:
                break
            
        dato = nodo.dato
        return dato


    def __add__(self, p_lista):
        nueva = self
        temp = nueva.cola 

        nueva.cola.anterior.siguiente = temp
        temp.anterior = nueva.cola.anterior
        temp.siguiente = p_lista.cabeza
        p_lista.cabeza.anterior = temp

        nueva.cola = p_lista.cola
        p_lista.cola.anterior.siguiente = nueva.cola
        nueva.tamanio = nueva.tamanio + p_lista.tamanio
        
        return nueva
    
    
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



    


    

    