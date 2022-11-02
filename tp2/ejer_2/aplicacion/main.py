# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 00:17:32 2022

@author: Andres Venialgo
"""
from modulos.Temperaturas_DB import TemperaturasDB 

a = TemperaturasDB()


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



