# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:08:43 2022

@author: Andres Venialgo
"""
from modulos.Arbol_AVL import ArbolAVL
from modulos.Arbol_AVL import iterador
from modulos.NodoArbol import NodoArbol

from datetime import datetime 
class TemperaturasDB():
    def __init__(self):
        self.arbol = ArbolAVL()
       
        
        

    def guardar_temperatura(self, fecha, temperatura):
        """guarda la medida de temperatura asociada a la fecha """
        aux = fecha.replace('/', '-')
        fecha = datetime.strptime(aux, "%d-%m-%Y").date()
        
        self.arbol.agregar(temperatura, fecha)
        
        
    
    def devolver_temperatura(self, fecha):
        """devuelve la medida de temperatura en la fecha determinada """
        return self.arbol.obtener(fecha)
    
        
    
    def max_temp_rango(self, fecha1, fecha2):
        """devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive
            (fecha1 < fecha2). """
        pass

    
    def min_temp_rango(self, fecha1, fecha2):
        """ devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive
            (fecha1 < fecha2). """
        pass
    
    def temp_extremos_rango(self, fecha1, fecha2):
        """devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 
            inclusive (fecha1 < fecha2). """
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2)
    
    def borrar_temperatura(self, fecha):
        """ recibe una fecha y elimina del árbol la medición correspondiente a esa 
            fecha. """
        self.arbol.eliminar(fecha)
    
    
    def mostrar_temperaturas(self, fecha1, fecha2):
        """fecha2): muestra por consola un listado de las mediciones de temperatura
            en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura 
            ºC”, ordenado por fechas. """
        pass
    
    
    def mostrar_cantidad_muestras(self):
        """ muestra por consola la cantidad de muestras de la BD"""
        self.arbol.inorden(self.arbol.raiz)
        pass
            
            
if __name__ == "__main__":
    a = TemperaturasDB()

   # CASO MAS FACIL----------------  
    # a.guardar_temperatura(10, "c")
    # a.guardar_temperatura(20,"b")
    
    # a.guardar_temperatura(30, "d")
    # a.guardar_temperatura(40, "e" )
    # a.guardar_temperatura(40, "z" )

    # a.guardar_temperatura(40, "g" )
    
    # a.mostrar_cantidad_muestras()
#--------------------------------------------------

 
    a.guardar_temperatura( 22, "14/07/2000")
    a.guardar_temperatura( 30, "1/02/2000")
    a.guardar_temperatura( 35, "24/04/2000")
    
    a.guardar_temperatura(12, "17/02/2028")
    a.guardar_temperatura(25, "22/04/2020")
    # a.guardar_temperatura(32, "12/05/2004")
    # a.guardar_temperatura(40, "15/02/2022")
    # a.guardar_temperatura(23, "30/03/2028")
    # a.guardar_temperatura(12, "14/05/2007")
    # a.guardar_temperatura(27, "6/04/2029")
    a.mostrar_cantidad_muestras()
    
    
    # b = "14/07/2000"
    # c = b.replace('/','-')
    # print(c)
    # fecha = datetime.strptime(c, "%d-%m-%Y")
    # print((fecha.date()))
    
    # b = "14/09/1999"
    # c = b.replace('/','-')
    # print(c)
    # fecha2 = datetime.strptime(c, "%d-%m-%Y")
    # print((fecha2.date()))
    
    # print( fecha2< fecha)
    
    
    # print(a.devolver_temperatura("1/02/00"))
          
    
    
    
       
    # 2017-04-20 25
    # 2017-05-04 32
    # 2017-02-22 40
    # 2017-03-28 23
    # 2017-05-07 12
    # 2017-04-29 27
    
    