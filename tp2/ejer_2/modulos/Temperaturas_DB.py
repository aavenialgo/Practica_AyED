# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:08:43 2022

@author: Andres Venialgo
"""
from modulos.Arbol_AVL import ArbolAVL
from modulos.Arbol_AVL import iterador

from datetime import datetime 
class TemperaturasDB():
    def __init__(self):
        self.arbol = ArbolAVL()
       
        
        

    def guardar_temperatura(self, fecha, temperatura):
        """guarda la medida de temperatura asociada a la fecha """
        # aux = fecha.replace('/', '-')
        # fecha = datetime.strptime(aux, "%d-%m-%Y").date()
        fecha = self._convertir_fecha(fecha)
        self.arbol.agregar(fecha, temperatura)
        
    def _convertir_fecha(self,fecha):
        aux = fecha.replace('/', '-')
        fecha = datetime.strptime(aux, "%d-%m-%Y").date()
        return fecha
    
    def devolver_temperatura(self, fecha):
        """devuelve la medida de temperatura en la fecha determinada """
        fecha = self._convertir_fecha(fecha)
        return self.arbol.obtener(fecha)
    
           
    def max_temp_rango(self, fecha1, fecha2):
        """devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive
            (fecha1 < fecha2). """
        fecha1 = self._convertir_fecha(fecha1)
        temp1 = self.arbol.obtener(fecha1)
        
        fecha2 = self._convertir_fecha(fecha2)
        
        temperatura_maxima = temp1
        it = iterador(self.arbol,fecha1)
        for valor in it:
            if temperatura_maxima < valor.cargaUtil:
                temperatura_maxima = valor.cargaUtil
            
        return temperatura_maxima
            
    
    def min_temp_rango(self, fecha1, fecha2):
        """ devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive
            (fecha1 < fecha2). """
        fecha1 = self._convertir_fecha(fecha1)
        temp1 = self.arbol.obtener(fecha1)
        
        fecha2 = self._convertir_fecha(fecha2)
        
        temperatura_minima = temp1
        it = iterador(self.arbol,fecha1)
        for valor in it:
            if temperatura_minima > valor.cargaUtil:
                temperatura_minima = valor.cargaUtil
            
        return temperatura_minima
    
    def temp_extremos_rango(self, fecha1, fecha2):
        """devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 
            inclusive (fecha1 < fecha2). """
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1, fecha2)
    
    
    def borrar_temperatura(self, fecha):
        """ recibe una fecha y elimina del árbol la medición correspondiente a esa 
            fecha. """
        fecha = self._convertir_fecha(fecha)
        self.arbol.eliminarCargaUtil(fecha)
 
    
    def mostrar_temperaturas(self, fecha1, fecha2):
        """fecha2): muestra por consola un listado de las mediciones de temperatura
            en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura 
            ºC”, ordenado por fechas. """
        
        fecha1 = self._convertir_fecha(fecha1)
        fecha2 = self._convertir_fecha(fecha2)
        
        it = iterador(self.arbol,fecha1,fecha2)
        
        for valor in it:
            if valor.cargaUtil == None:
                print(valor.clave, "Sin datos de temperatura!")
            else:
                print(f"{valor}"+" °C")

    
    def mostrar_cantidad_muestras(self):
        """ muestra por consola la cantidad de muestras de la BD"""
        print(self.arbol.tamano)
        # return self.arbol.tamano
            
            

    
    

    
    