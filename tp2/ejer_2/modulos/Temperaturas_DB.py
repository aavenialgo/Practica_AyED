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
        return self.arbol.obtener(fecha)
    
        
    
    def max_temp_rango(self, fecha1, fecha2):
        """devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive
            (fecha1 < fecha2). """
        fecha1 = self._convertir_fecha(fecha1)
        temp1 = self.arbol.obtener(fecha1)
        #--------------------------------------
        fecha2 = self._convertir_fecha(fecha2)
        #------------------------------
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
        #--------------------------------------
        fecha2 = self._convertir_fecha(fecha2)
        #------------------------------
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
        # self.arbol.inorden(self.arbol.raiz)
        print(self.arbol.tamano)
            
            
if __name__ == "__main__":
    a = TemperaturasDB()
    
    

#--------------------------------------------------

 
    a.guardar_temperatura("14/07/2000",20)
    a.guardar_temperatura("1/02/2000",45)
    a.guardar_temperatura("24/04/2000",6)
    
    a.guardar_temperatura("17/02/2028",43)
    a.guardar_temperatura("22/04/2020",12)
    a.guardar_temperatura("12/05/2004",25)
    #--------------------------------------------------------------------
    print("\n------Cantidad de muestras-----------")
    a.mostrar_cantidad_muestras()
    #--------------------------------------------------------------------
    print("---Mostrar Temperaturas entre dos fechas---")
    a.mostrar_temperaturas("14/07/2000", "17/02/2028")
    #--------------------------------------------------------------------
    print("\n---Temperatura maxima entre dos rangos de fecha---")
    max_temp = a.max_temp_rango("1/02/2000", "17/02/2028")
    print("Maxima temperatura",max_temp)
    #--------------------------------------------------------------------
    print("\n---Temperatura minima entre dos rangos de fecha---")
    min_temp = a.min_temp_rango("1/02/2000", "17/02/2028")
    print("Minima temperatura",min_temp)
    #--------------------------------------------------------------------
    print("\n------temp_extremos_rango-------")
    maximo,minimo= a.temp_extremos_rango("1/02/2000", "17/02/2028")
    print(maximo,minimo)
    #--------------------------------------------------------------------
    print("\n----Eliminar Temperatura en una fecha-----")
    a.borrar_temperatura("14/07/2000")
    a.mostrar_temperaturas("1/02/2000", "17/02/2028")
    
    
    
       
    # 2017-04-20 25
    # 2017-05-04 32
    # 2017-02-22 40
    # 2017-03-28 23
    # 2017-05-07 12
    # 2017-04-29 27
    
    