# -*- coding: utf-8 -*-
"""
Created on Mon Nov 1 14:45:46 2022

@author: Andres
"""
from os import remove
f1 = "particion_1.txt"
f2 = "particion_2.txt"
def auxiliar_particionar_archivo(archivo_original):
    """ Particiona un archivo en dos archivos auxiliares armando lineas con
    numeros ordenados de menor a mayor. La alternancia entre un archivo u otro
    se produce cuando se corta la secuencia "de menor a mayor" leido en el archivo original

    Args:
        archivo_original (file)
    Returns:
        ordenado (bool)
            valor booleano que indica que como no se realizó ninguna 
            alternancia entre los archivos auxiliar, entonces , el archivo original 
            se encontraba ordenado
    """
    
    ordenado = True
    archivo_aux_seleccionado = f1
    
    with  open(f1,'a') as archivo_auxiliar_1:
        with  open(f2,'a') as archivo_auxiliar_2:
   
        
            actual = archivo_original.readline()
            siguiente = archivo_original.readline()    
    
            if actual != "" and siguiente != "":
                    while actual != "":
                        
                        if archivo_aux_seleccionado == f1:
                            archivo_auxiliar_1.write(actual)
                       
                        if archivo_aux_seleccionado == f2:
                            archivo_auxiliar_2.write(actual)
                
            
                        if actual > siguiente and siguiente != "":
                            archivo_aux_seleccionado = auxiliar_intercambiar_archivo_selecionado(archivo_aux_seleccionado)
                            ordenado = False
                
                        actual = siguiente
            
                        if actual != "":
                            siguiente = archivo_original.readline()
            
    return ordenado
     #else posible excep  
        
def auxiliar_fusionar_archivos(archivo_original):
    """ Fusiona dos archivos auxiliares reescribiendo el archivo original.
    Los datos en este se colocan comparando cada dato de una secuencia ordenada del
    archivo_auxiliar_1  y archivo_auxiliar_2 hasta que no queden datos en ninguno.
    Args:
        archivo_original (file)
    
    """
    f1 = "particion_1.txt"
    f2= "particion_2.txt"
    with  open(f1,'r') as archivo_auxiliar_1:
        with  open(f2,'r') as archivo_auxiliar_2:
            
            dato_actual_en_1 = archivo_auxiliar_1.readline()
            dato_siguiente_en_1 = archivo_auxiliar_1.readline()
            
            dato_actual_en_2 = archivo_auxiliar_2.readline()
            dato_siguiente_en_2 = archivo_auxiliar_2.readline()
            
            if dato_actual_en_1 != "" and dato_actual_en_2 != "":

                while dato_actual_en_1 != "" and dato_actual_en_2 != "":
                    
                    if dato_actual_en_1 < dato_actual_en_2:
                        archivo_original.write( dato_actual_en_1 )
                        
                        if dato_siguiente_en_1 < dato_actual_en_1 or dato_siguiente_en_1 == "":
                            while dato_siguiente_en_2 != "" and dato_actual_en_2 < dato_siguiente_en_2:
                                archivo_original.write( dato_actual_en_2)
                                dato_actual_en_2 = dato_siguiente_en_2
                                dato_siguiente_en_2 = archivo_auxiliar_2.readline()
                                
                            archivo_original.write( dato_actual_en_2)
                            dato_actual_en_2 = dato_siguiente_en_2
                            if dato_actual_en_2 != "":
                               dato_siguiente_en_2 = archivo_auxiliar_2.readline()                       
                                
                        dato_actual_en_1 = dato_siguiente_en_1
                        if dato_actual_en_1 != "":
                            dato_siguiente_en_1 = archivo_auxiliar_1.readline()
                        

                    if dato_actual_en_2 < dato_actual_en_1:
                        archivo_original.write( dato_actual_en_2 )
                        
                        if dato_siguiente_en_2 < dato_actual_en_2 or dato_siguiente_en_2 == "":
                            while dato_siguiente_en_1 != "" and dato_actual_en_1 < dato_siguiente_en_1:
                                archivo_original.write( dato_actual_en_1)
                                dato_actual_en_1 = dato_siguiente_en_1
                                dato_siguiente_en_1 = archivo_auxiliar_1.readline()

                            archivo_original.write( dato_actual_en_1)
                            dato_actual_en_1 = dato_siguiente_en_1
                            if dato_actual_en_1 != "":
                                dato_siguiente_en_1 = archivo_auxiliar_1.readline()
                                
                                
                        dato_actual_en_2 = dato_siguiente_en_2
                        if dato_actual_en_2 != "":
                            dato_siguiente_en_2 = archivo_auxiliar_2.readline()
                        
                    if dato_actual_en_2 == dato_actual_en_1:
                        archivo_original.write( dato_actual_en_1 )
                        archivo_original.write( dato_actual_en_2 )
                        
                        dato_actual_en_1 = dato_siguiente_en_1
                        if dato_actual_en_1 != "":
                            dato_siguiente_en_1 = archivo_auxiliar_1.readline()
                            
                        dato_actual_en_2 = dato_siguiente_en_2
                        if dato_actual_en_2 != "":
                            dato_siguiente_en_2 = archivo_auxiliar_2.readline()
                            
            if dato_actual_en_1 == "":
                 while dato_actual_en_2 != "" :
                     archivo_original.write( dato_actual_en_2)
                     dato_actual_en_2 = dato_siguiente_en_2
                     if dato_actual_en_2 != "":
                        dato_siguiente_en_2 = archivo_auxiliar_2.readline()
                        
            if dato_actual_en_2 == "":
                 while dato_actual_en_1 != "" :
                     archivo_original.write( dato_actual_en_1)
                     dato_actual_en_1 = dato_siguiente_en_1
                     if dato_actual_en_1 != "":
                        dato_siguiente_en_1 = archivo_auxiliar_1.readline()  


def auxiliar_intercambiar_archivo_selecionado(archivo_aux_seleccionado):
    
    """ Compara e intercambia el valor del string archivo_aux_seleccionado por las 
    opciones  particion_1 y particion_2

    Args:
        archivo_aux_seleccionado (str)
    Returns:
        (str)
    """
    
    
    if archivo_aux_seleccionado == f1:
        return f2
        
    if archivo_aux_seleccionado == f2:
        return f1
        
def ordenar_externamente_mezcla_natural(ruta_y_nombre_del_archivo_original):
    """ Ordena los datos de menor a mayor de un archivo en disco haciendo uso de
    dos archivos auxiliares y el algoritmo de mezcla natural,
    para ello divide y fusiona criteriosamente los archivos hasta que
    se logre el orden de los datos

    Args:
        ruta_y_nombre_del_archivo_original (str)

    """

    esta_ordenado = False 
    
    while not esta_ordenado:
        with  open(ruta_y_nombre_del_archivo_original,'r') as archivo_original:
            esta_ordenado = auxiliar_particionar_archivo(archivo_original)

        if not esta_ordenado:
            with  open(ruta_y_nombre_del_archivo_original,'w') as archivo_original:
                auxiliar_fusionar_archivos(archivo_original)
        
            
            with  open(f1,'w') as archivo_aux_1:
                pass
               
            with  open(f2,'w') as archivo_aux_2:
                pass  
            
    # remove(f1) 
    # remove(f2)  
                
