# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:08:43 2022

@author: Andres Venialgo
"""
from modulos.Arbol_AVL import ArbolAVL

class TemperaturasDB():
    def __init__(self):
        self.arbol = ArbolAVL()
        
        pass
    

    def guardar_temperatura(self, temperatura, fecha):
        """guarda la medida de temperatura asociada a la fecha """
        pass
    
    def devolver_temperatura(self, fecha):
        """devuelve la medida de temperatura en la fecha determinada """
        pass
    
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
        pass
    
    
    def mostrar_temperaturas(self, fecha1, fecha2):
        """fecha2): muestra por consola un listado de las mediciones de temperatura
            en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura 
            ºC”, ordenado por fechas. """
        pass
    
    
    def mostrar_cantidad_muestras(self):
        """ muestra por consola la cantidad de muestras de la BD"""
        return self.arbol.tamano
    

    
    