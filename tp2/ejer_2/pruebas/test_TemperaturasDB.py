# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:25:32 2022

@author: Andres Venialgo
"""

from modulos.Temperaturas_DB import TemperaturasDB
import unittest
class Test_TemperaturasDB(unittest.TestCase):
    def setUp(self):
        self.DB = self.generarEjemplo()
        
        
    def generarEjemplo(self):
        """ Funcion auxiliar para generar un ejemplo"""
        temp = TemperaturasDB()
        temp.guardar_temperatura("14/07/2000",20)
        temp.guardar_temperatura("1/02/1999",45)
        temp.guardar_temperatura("24/04/2000",6)
        temp.guardar_temperatura("17/02/2028",43)
        temp.guardar_temperatura("22/04/2020",12)
        temp.guardar_temperatura("1/1/2044",25)
        temp.guardar_temperatura("12/05/2044",14)
        temp.guardar_temperatura("12/05/2004",25)        
        return temp
        
    def test_devolver_temperatura(self):
        """Compruebo si los me devuelve la temperatura asociada a una fecha """
        temp1 = self.DB.devolver_temperatura("1/1/2044")
        self.assertEqual(temp1, 25)
        
    def test_min_temp_rango(self):
        """ Pruebo si me devuelve el minimo valor de temperatura entre dos
        fechas """
        min_temp = self.DB.min_temp_rango("24/04/2000", "17/02/2028")
        self.assertEqual(min_temp, 6)
    
    def test_max_temp_rango(self):
        max_temp = self.DB.max_temp_rango("14/07/2000", "17/02/2028")
        self.assertEqual(max_temp, 43)
        
    def test_borrar_temperatura(self):
        """Compruebo que se elimina el valor de temperatura en la fecha indicada"""
        aux = self.DB
        aux.borrar_temperatura("22/04/2020")
        self.assertEqual(aux.devolver_temperatura("22/04/2020"), None)
        
    def test_temp_extremos_rango(self):
        """Compruebo la minima y maxima temperatura en un rango de fechas """
        min_temp,max_temp = self.DB.temp_extremos_rango("1/02/1999", "12/05/2044")
        self.assertEqual(max_temp,45 )
        self.assertEqual(min_temp,6 )
    
        
if __name__ == "__main__":
    unittest.main()
#
