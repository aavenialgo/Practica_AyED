# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:44:14 2022

@author: Andres Venialgo
"""
import unittest

# from modulos.NodoArbol import NodoArbol 
from modulos.Arbol_AVL import ArbolAVL
from modulos.Arbol_AVL import iterador

class Test_Arbol_AVL(unittest.TestCase):
    def setUp(self):
        self.arbol = ArbolAVL()
        self.arbolPrueba = ArbolAVL()

    def generar_arbol(self, tipo):
        """ Genera arboles de ejemplo"""
        arbolPrueba = ArbolAVL()  
        
        if tipo == 1: # Arbol desequilibrado a la derecha
            arbolPrueba.agregar('a',1)
            arbolPrueba.agregar('b',2)
            arbolPrueba.agregar('c',3)
        
        if tipo == 2: # Arbol desequilibrado a la izquierda
            arbolPrueba.agregar('c',1)
            arbolPrueba.agregar('b',2)
            arbolPrueba.agregar('a',3)
        
        if tipo == 3: # Arbol que tiene rotaciones doble izquierda derecha
            
            pass
           
        if tipo == 4: # Arbol que tiene rotaciones doble derecha izquierda
            pass
        
        if tipo == 5:# Ejemplo Pequeño
            arbolPrueba.agregar(10, "diez")
            arbolPrueba.agregar(20, "veinte")
            arbolPrueba.agregar(30, "treinta")
            
        if tipo == 6 :#Ejemplo para arbol facilmente desbalanceable
            aux = [15,10,20,2,12,19,14,21,18]
            for i in aux:
                arbolPrueba.agregar(i, i*5)                
                
        return arbolPrueba
    
    def test_rotarIzquierda(self):
        """ Prueba para rotacion hacia la izquierda """
        raiz = self.generar_arbol(1).raiz
        self.assertEqual(raiz.clave, 'b')
        self.assertEqual(raiz.hijoDerecho.clave, 'c')
        self.assertEqual(raiz.hijoIzquierdo.clave, 'a')
        
    def test_rotarDerecha(self):
        """ Prueba para rotacion hacia la derecha """
        raiz = self.generar_arbol(2).raiz
        self.assertEqual(raiz.clave, 'b')
        self.assertEqual(raiz.hijoDerecho.clave, 'c')
        self.assertEqual(raiz.hijoIzquierdo.clave, 'a')
    
    def test_obtener(self):
        """ Compruebo que la funcion obtener devuelva la carga util cuando le paso una clave """
        aux1 = ["diez","veinte","treinta"]
        arbolPrueba = self.generar_arbol(5)
        self.assertEqual(aux1[0], arbolPrueba.obtener(10))
        self.assertEqual(aux1[1], arbolPrueba.obtener(20))
        self.assertEqual(aux1[2], arbolPrueba.obtener(30))
    
    def test_eliminar(self):
        """ Prueba para eliminar un nodo del arbol """
        #Caso 1: Elimina y no provoca un desbalance en el arbol
        aux1 = self.generar_arbol(6)
        tamanio_aux1 = aux1.tamano
        aux1.eliminar(18)
        nuevoTamanio = aux1.tamano
    
        original = self.generar_arbol(6)
        self.assertNotEqual(aux1,original)
        self.assertNotEqual(tamanio_aux1, nuevoTamanio )
        
        # #Caso 2: El nodo eliminado provoca un desbalance
        aux2 = self.generar_arbol(6)
        aux2.eliminar(21) 
        # # Este eliminar provocara un desbalanze en el nodo con clave 20
        # # obligando a hacer una rotacion hacia la derecha 
        it = iterador(aux2,10)
        for nodo in it:
            # print(nodo)
            if nodo.clave == 20:
                print(nodo.hijoIzquierdo)
                print(nodo.padre)
        
        # print("tam ",aux2.tamano )                
            
        # print(aux3)
        # print(aux3.hijoDerecho)
        # print("Tamanio ",aux3.__len__())
        # # self.assertEqual(19, aux3.clave)
        # self.assertEqual(18, aux3.hijoIzquierdo.clave)
        # self.assertEqual(20, aux3.hijoDerecho.clave)
        

        
if __name__ == "__main__":
    
    unittest.main()