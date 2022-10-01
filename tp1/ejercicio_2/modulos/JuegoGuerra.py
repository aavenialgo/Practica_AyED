# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 19:00:13 2022

@author: Julian Traversaro
"""

from ColaDoble import ColaDoble
import random 
class JuegoGuerra:
    
    def __init__(self, valor_semilla):
        '''
        

        Returns
        Inicializo el juego, creo el maso de cartas de poquer "baraja", como una lista de python 
        por facilidad, luego la "barajo "
        -------
        None.

        '''
        self.maxima_cantidad_turnos=10000
        self.jugador_1=ColaDoble()
        self.jugador_2=ColaDoble()
        self.n_jugadores=2
        self.valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.palos = ['♠', '♥', '♦', '♣']
        self.semilla=valor_semilla
        self.barajar()
    
    def barajar(self):
        '''
        

        Returns
        Barajo las cartas creando todos los palos de la baraja 
        -------
        None.

        '''
        self.baraja=[]
        for x in self.valores:
            for y in self.palos:
                carta='{} {}'.format(x,y)
                self.baraja.append(carta)
        
        #print(self.baraja)
    @property
    def turnos_jugados(self):
        '''
         interpretacion del requerimiento de  testing    

        Returns
        -------
        None.

        '''
        pass
    
    @property
    def ganador(self):
        '''
        

        Returns
        interpretacion de requerimiento de testing 
        -------
        None.

        '''
        return self.jugador_ganador
    @property
    def empate(self):
        '''
        

        Returns
        requerimiento interpretado del testing provisto 
        -------
        None.

        '''
        return self._empate
    
    def iniciar_juego(self):
        '''
        

        Parameters
        iniciar_juego, inicia el juego de la guerra con un numero de partidas establecido
        y por defecto son 10 mil 
        este metodo llama a un metodo interno de la clase en el cual se implententa una interfas 'grafica'
        para transmitir por puerto serie 
        ----------
        turnos_de_juego : TYPE, optional
            DESCRIPTION. The default is 10000.
            
        Returns
        -------
        None.

        '''
        
        self._empate=False
        '''mezclo las cartas''' 
        
        random.seed(self.semilla)
        
        random.shuffle(self.baraja)
        self.baraja_mezclada=ColaDoble()
        for i in range (len(self.baraja)):
            self.baraja_mezclada.agregarFrente(self.baraja[i])
        for i in range(26):
            
            '''
            La primera carta es para el jugador 1, luego es eliminada de la baraja
            la segunda para el jugador 2, esto se repite hasta terminar el maso 
            busco y elimino de la baraja el primer elemento. En cambio cada jugador agrega al frente
            de su maso siendo las ultimas 2 cartas de la baraja las primeras de cada maso, antes de
            volver a mezclarse 
            '''
            
            """
            self.baraja.removerFrente() no funciona, pero el metodo de clase padre si 
            """
            self.jugador_1.agregarFrente(self.baraja_mezclada.extraer(0))
            
            self.jugador_2.agregarFrente(self.baraja_mezclada.extraer(0))
            
            
        self.n_cartas_jugador_1=len(self.jugador_1)
        self.n_cartas_jugador_2=len(self.jugador_2)
        print(self.jugador_1)
        
        print(self.jugador_2)
        
        '''
        Cuando cada jugador ya tiene sus cartas comienza el juego 
        '''
        i=0
        masos_no_nulos=lambda cartas_j1, cartas_j2: cartas_j1>=0 or cartas_j2>=0
        
        while i <self.maxima_cantidad_turnos:
            if self.n_cartas_jugador_1>=0 and self.n_cartas_jugador_2>=0:
                self.show(i+1,self.jugador_1.removerFrente(), self.jugador_2.removerFrente(), estado='en juego') 
            i=i+1
            
        if i<= self.maxima_cantidad_turnos and self.n_cartas_jugador_1 < self.n_cartas_jugador_2:
            self.jugador_ganador='jugador 2'
            print('***JUGADOR 2 GANA LA PARTIDA***')    
            
        elif i<= self.maxima_cantidad_turnos and self.n_cartas_jugador_1 > self.n_cartas_jugador_2:
            self.jugador_ganador='jugador 1'
            print('***JUGADOR 1 GANA LA PARTIDA***')  
        elif self.n_cartas_jugador_1 ==0:
            self.jugador_ganador='jugador 2'
            print('***JUGADOR 2 GANA LA PARTIDA***')
        elif self.n_cartas_jugador_2 ==0:
            self.jugador_ganador='jugador 1'
            print('***JUGADOR 1 GANA LA PARTIDA***')
            
            

            
        if i== self.maxima_cantidad_turnos and self.n_cartas_jugador_1 == self.n_cartas_jugador_2:
            self._empate=True
            print('EMPATE')
            
            



    def show(self,turno,carta_jugador_1, carta_jugador_2, estado= 'en juego'):
        '''
        

        Parameters
        Metodo de clase en el que se implemta interfaz grafica transparente al usuario
        se reciben las cartas 'boca arriba del turno' y dependiendo su valor se toman desiciones
        dentro de estas desiciones esta el aumentar y disminuir el numero de cartas dde los jugadores 
        ganadores y perdedores respectivamente, solicitar mas cartas para la situaCION 'GUERRA' y la misma
        accion para la 'segunda guerra'
        ----------
        turno : TYPE
            DESCRIPTION.
        carta_jugador_1 : TYPE
            DESCRIPTION.
        carta_jugador_2 : TYPE
            DESCRIPTION.
        estado : TYPE, optional
            DESCRIPTION. The default is 'en juego'.

        Returns
        -------
        None.

        '''   

        
        
        if carta_jugador_1 <= carta_jugador_2:
            print('------------------------')
            print(f'Turno: {turno}')
            print('Jugador 1: ' )
            print('-X '*(self.n_cartas_jugador_1-1))
            print (f'{carta_jugador_1 } {carta_jugador_2 }')
            print('-X '*(self.n_cartas_jugador_2-1))
            
            print('Jugador 2 ')
            print('------------------------')
            self.n_cartas_jugador_1 =self.n_cartas_jugador_1-1
            self.n_cartas_jugador_2=self.n_cartas_jugador_2+1
            
            self.jugador_2.agregarFinal(carta_jugador_1)
            self.jugador_2.agregarFinal(carta_jugador_2)
           
            print(self.n_cartas_jugador_1)
            print(self.n_cartas_jugador_2)
        elif carta_jugador_1 >= carta_jugador_2:
            print('------------------------')
            print(f'Turno: {turno}')
            print('Jugador 1: ' )
            print('-X '*(self.n_cartas_jugador_1-1))
            print (f'{carta_jugador_1 } {carta_jugador_2 }')
            print('-X '*(self.n_cartas_jugador_2-1))
            
            print('Jugador 2 ')
            print('------------------------')
            self.n_cartas_jugador_2 =self.n_cartas_jugador_2-1
            self.n_cartas_jugador_1=self.n_cartas_jugador_1+1
            
            self.jugador_1.agregarFinal(carta_jugador_2)
            self.jugador_1.agregarFinal(carta_jugador_1)
            
            print(self.n_cartas_jugador_1)
            print(self.n_cartas_jugador_2)
            
        elif carta_jugador_1 == carta_jugador_2:
            print('------------------------')
            print(f'Turno: {turno}')
            print('Jugador 1: ' )
            print('-X '*(self.n_cartas_jugador_1-5))
            print (f'{carta_jugador_1 } {carta_jugador_2 }')
          
            self.botin_jugador1=[]
            self.botin_jugador2=[]
            for i in range(4):
                self.botin_jugador1.append(self.jugador_1.extraer(0))
                self.botin_jugador2.append(self.jugador_2.extraer(0))
                
            guerra_1=self.jugador_1.extraer(0) 
            guerra_2=self.jugador_2.extraer(0)
            print('-X '*6 + f' {guerra_1} {guerra_2 }')
            print('-X '*(self.n_cartas_jugador_2-5))
            
            print('Jugador 2 ')
            print('------------------------')
            
            
            print(self.n_cartas_jugador_1)
            print(self.n_cartas_jugador_2)
            if guerra_1 <=guerra_2:

               
                self.jugador_2.agregarFinal(carta_jugador_1)
                self.jugador_2.agregarFinal(carta_jugador_2)
             
                
                for i in range(4):
                    self.jugador_2.agregarFrente(self.botin_jugador1[i])
                    self.jugador_2.agregarFrente(self.botin_jugador2[i])
                
                self.jugador_2.agregarFinal(guerra_1)
                self.jugador_2.agregarFinal(guerra_2)
                
                self.n_cartas_jugador_1 =self.n_cartas_jugador_1-5
                self.n_cartas_jugador_2=self.n_cartas_jugador_2+10
                
            elif guerra_2 <=guerra_1:
                self.jugador_1.agregarFinal(carta_jugador_1)
                self.jugador_1.agregarFinal(carta_jugador_2)
                for i in range(4):
                    self.jugador_1.agregarFrente(self.botin_jugador1[i])
                    self.jugador_1.agregarFrente(self.botin_jugador2[i])
                

                self.jugador_1.agregarFinal(guerra_1)
                self.jugador_1.agregarFinal(guerra_2)
                
                self.n_cartas_jugador_2 =self.n_cartas_jugador_2-5
                self.n_cartas_jugador_1=self.n_cartas_jugador_1+10
          
            elif guerra_1 == guerra_2:
                print('------------------------')
                print(f'Turno: {turno}')
                print('Jugador 1: ' )
                print('-X '*(self.n_cartas_jugador_1-5))
                print (f'{carta_jugador_1 } {carta_jugador_2 }')
                self.botin_jugador1_1=[]
                self.botin_jugador2_1=[]
                for i in range(4):
                    self.botin_jugador1_1.append(self.jugador_1.extraer(0))
                    self.botin_jugador2_1.append(self.jugador_2.extraer(0))
                    
                guerra_1_1=self.jugador_1.extraer(0) 
                guerra_2_1=self.jugador_2.extraer(0)
                
                print('-X '*6 + f' {guerra_1} {guerra_2 }')
                print(f'{guerra_1_1} {guerra_2_1}')
                print('-X '*(self.n_cartas_jugador_2-5))
                
                print('Jugador 2 ')
                print('------------------------')
                print(self.n_cartas_jugador_1)
                print(self.n_cartas_jugador_2)
                
                if guerra_1_1 <=guerra_2_1:
                    
                    
                    self.jugador_2.agregarFinal(carta_jugador_1)
                    self.jugador_2.agregarFinal(carta_jugador_2)
                    for i in range(4):
                        self.jugador_2.agregarFrente(self.botin_jugador1[i])
                        self.jugador_2.agregarFrente(self.botin_jugador2[i])
                    
                    
                    for i in range(4):
                        self.jugador_2.agregarFrente(self.botin_jugador1[i])
                        self.jugador_2.agregarFrente(self.botin_jugador2[i])
                    
                    self.jugador_2.agregarFinal(guerra_1)
                    self.jugador_2.agregarFinal(guerra_2)
                    
                    for i in range(4):
                        self.jugador_2.agregarFrente(self.botin_jugador1_1[i])
                        self.jugador_2.agregarFrente(self.botin_jugador2_1[i])
                    
                    self.jugador_2.agregarFinal(guerra_1_1)
                    self.jugador_2.agregarFinal(guerra_2_1)
                    
                    
                    self.n_cartas_jugador_1 =self.n_cartas_jugador_1-9
                    self.n_cartas_jugador_2=self.n_cartas_jugador_2+18
                    
                elif guerra_2 <=guerra_1:
                    self.jugador_1.agregarFinal(carta_jugador_1)
                    self.jugador_1.agregarFinal(carta_jugador_2)
                    for i in range(4):
                        self.jugador_1.agregarFrente(self.botin_jugador1[i])
                        self.jugador_1.agregarFrente(self.botin_jugador2[i])
                    self.jugador_1.agregarFinal(guerra_1)
                    self.jugador_1.agregarFinal(guerra_2)
                    for i in range(4):
                        self.jugador_1.agregarFrente(self.botin_jugador1_1[i])
                        self.jugador_1.agregarFrente(self.botin_jugador2_1[i])
                    
                    
                    self.jugador_1.agregarFinal(guerra_1_1)
                    self.jugador_1.agregarFinal(guerra_2_1)
                    self.n_cartas_jugador_2 =self.n_cartas_jugador_2-9
                    self.n_cartas_jugador_1=self.n_cartas_jugador_1+18
                
if __name__=='__main__':
    '''jugador 1 gana la partida en el turno 137'''
    guerra=JuegoGuerra(valor_semilla=167)
    guerra.iniciar_juego()
    
    
    