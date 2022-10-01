# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:35:10 2022

@author: Julian Traversaro
"""
#%% variables globales 

#%%
"""
29/9/22 metodo dividir, divide correctamente 
"""        
def MezclaNatural(nombre):
    f1='particion_1.txt'
    f2='particion_2.txt'
    
    lectura=True
    n_lineas=0
    n_lineas_particion=0
    bandera_f1=True
    bandera_f2=True

    n_sublistas_f1=0
    n_sublistas_f2=0
    # mido el tamaño del archivo, no es la forma mas pythonista pero hay 
    #otras logicas mas importantes que resolver

    with open(nombre, 'r') as archivo_completo:
        for linea in archivo_completo:
            n_lineas+=1
    
    with open(nombre, 'r') as archivo_completo, open(f1, 'w') as particion1, open(f2,'w') as particion2:          
        aux=archivo_completo.readline()
        particion1.write(aux)  
        while n_lineas_particion <=n_lineas:
                n_lineas_particion+=1
                aux2=archivo_completo.readline()
                if aux <= aux2:
                    #estan ordenados
                    if bandera_f1:
                        particion1.write(aux2)
                        
                        aux=aux2
                    else:
                        particion2.write(aux2)
                        
                        aux=aux2
                elif aux >aux2:
                    
                    if bandera_f2:
                        particion2.write(aux2)
                        
                        aux=aux2
                        bandera_f1=False
                        bandera_f2=False
                        
                    elif bandera_f2==False:
                        particion1.write(aux2)
                        
                        aux=aux2
                        bandera_f1=True
                        bandera_f2=True
                        
    
                 
                    
                    
    #%%
    datos_mesclados='datos_mezclados.txt'
    n_sublistas_f1=0
    n_sublistas_f2=0
    lectura_mezcla=True
    f1_n_lineas=0
    f2_n_lineas=0
    f1_contador_lineas=0
    f2_contador_lineas=0
    auxiliar_f2=0
    auxiliar_f1=0
    
    
    mayor=0
    bandera_mayor=''
    bandera_menor=''
    volver_f2=False
    volver_f1=False
    
    
    with open(f1, 'r') as archivo_completo:
        for linea in archivo_completo:
            f1_n_lineas+=1
            
    with open(f2, 'r') as archivo_completo:
        for linea in archivo_completo:
            f2_n_lineas+=1
    
    with open(datos_mesclados, 'w') as archivo_mezclado, open(f1, 'r') as particion1, open(f2,'r') as particion2:    
        dato_f1=particion1.readline()
        dato_f2=particion2.readline()
        if dato_f1 <=dato_f2:
              n_sublistas_f1+=1
              mayor =dato_f2
              archivo_mezclado.write(dato_f1)
              
              
              bandera_mayor ='f2'
        else:
              n_sublistas_f2+=1
              mayor=dato_f1
              archivo_mezclado.write(dato_f2)
              
              
              bandera_mayor='f1'
        
        while f1_contador_lineas <=f1_n_lineas and f2_contador_lineas <=f2_n_lineas:
            f1_contador_lineas=f1_contador_lineas+1
            f2_contador_lineas=f2_contador_lineas+1
            
            if bandera_mayor =='f1':
               if volver_f1:
                    mayor=auxiliar_f1
                    volver_f1=False
                
               siguiente=particion1.readline()
               if siguiente >mayor:
                   archivo_mezclado.write(mayor)
                   
                   mayor=siguiente
               elif siguiente <=mayor:
                   volver_f1=True
                   auxiliar_f1=siguiente
               mayor=auxiliar_f1
               bandera_mayor='f2'
               
            elif bandera_mayor=='f2':
                if volver_f2:
                    
                    mayor=auxiliar_f2
                    volver_f2=False
                
                siguiente=particion2.readline()
                if siguiente> mayor:
                    archivo_mezclado.write(mayor)
                    mayor=siguiente
                    
                elif siguiente <=mayor:
                    volver_f2=True
                    auxiliar_f2=siguiente
                    bandera_mayor='f1' 
                    n_sublistas_f2+=1
                
if __name__=='__main__':
    nombre='datos.txt'
    MezclaNatural(nombre='datos.txt')
            
      
     
    
        