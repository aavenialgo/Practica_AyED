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
                self.cola.siguiente = nuevo
                nuevo.anterior = self.cola
                self.cola = nuevo
                
            elif pos == 0:
                nuevo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo
                self.cabeza= nuevo
                
            else:
                for it in range(pos-1):
                    temp = temp.siguiente
                
                # temp.siguiente = self.cabeza
                # self.cabeza.anterior = temp
                # self.cabeza= temp
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
            lista_copiada.anexar(nodo)
        return lista_copiada
           
    
    def ordenar(self): 
        """Implementa un metodo de ordenamiento por insercion para ordenar la
        lista de menor a mayor """
        #TODO Falta terminar 
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
    #TODO: consultar: p_lista es modificada en el 3er parrafo???
    # en caso de que si, esta mal?
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
            
    def invertir(self):
        """ Invierte el orden de los elementos de la lista"""
        temp = self.copiar()
        temp = self.cola
        invertida = ListaDobleEnlazada()
        while temp.anterior == None:
            invertida.anexar(temp)
            temp.anterior
            
        return invertida
        # for i, nodo in enumerate(temp):
        #     invertida.anexar(temp[])
        # pass
          
        
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


    #TODO si te fijas en el test_concantenar usa corchetes para acceder a los
    # datos, entonces hago el metodo magico para[] o devuelve una lista de python
    # el __add__ ? 
    def __add__(self, p_lista):
        #TODO: esta mal implementado,cambia la lista original en 
        # este caso, y no deberia ser asi
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



        
if __name__ == '__main__':
    lista2= ListaDobleEnlazada()
    lista2.agregar(111)
    lista2.agregar(10)
    lista2.insertar(0, 20)
    
##########################################################  
#   Prueba para demostrar que si inserta al final como correspode
#   y que hay que consultar por el test de insertar en los extremos.
#TODO: consultar

    lista2.insertar(lista2.tamanio-1,180)
    print(lista2)
    
    nodo_anterior = None
    nodo_actual = lista2.cabeza
    while nodo_actual.siguiente: 
        nodo_anterior = nodo_actual
        nodo_actual = nodo_actual.siguiente
        valor = nodo_anterior.dato
    
    print("valor= ", valor) # cuando muestra valor es el dato anterior y no el ultimo
    print()
# fin de la prueba 
#########################################################


########## PRUEBA: 
    copia = lista2.copiar()
    print("lista2: ", lista2.tamanio)
    print("copia: ", copia.tamanio)
    invertida = lista2.invertir()
    print(invertida)
    


    

    