# -*- coding: utf-8 -*-
import os
import time
from tablero import Tablero
class Juego(object):
    def __init__(self, modo , tablero):
        
        self.mod = modo
        self.tablero = tablero
        self.gen = 0
        self.sleep = 0
        self.n = 0
    
    def setSleep(self,sleep): 
        self.sleep = sleep
    def getTablero(self):
        return self.tablero
        #def setTablero(self,matriz):
        #self.getTablero().setTablero() =
    def getMod(self):
        return self.mod    
    
    def setN(self,n):
        self.n = n
           
    def clear(self):
        os.system('cls')
    
    def dibujarTablero(self,dim):
        for x in range(dim):
            for y in range(dim):
                if self.getTablero().obtenerPosicion(x,y) == "-":
                    print(" -",end='')
                else:
                    print(" ■",end='') #caracter cuadrado que representa una celula viva
            print("\n",end='')        
                
    def analizarVecinos(self,dim):  
        copia_tablero = Tablero(dim)  
        for x in range(dim):
            for y in range(dim):
                cant_vecinos = self.obtenerCantidadVecinos(x,y,dim)
                if self.getTablero().obtenerPosicion(x,y) == "-":
                    if cant_vecinos == 3:
                        copia_tablero.obtenerTablero()[x][y] = "*"
                    else:
                        copia_tablero.obtenerTablero()[x][y] = "-"    
                else:
                    if cant_vecinos <2 or cant_vecinos>3:
                        copia_tablero.obtenerTablero()[x][y] = "-"
                    if cant_vecinos==2 or cant_vecinos==3:
                        copia_tablero.obtenerTablero()[x][y] = "*"
                        
        self.getTablero().setTablero(copia_tablero.obtenerTablero())   
    
    
    
    def copiarTablero(self,dim):
        copia_tablero = Tablero(dim)  
        for x in range(dim):
            for y in range(dim):
                copia_tablero.obtenerTablero()[x][y] = self.getTablero().obtenerPosicion(x,y)
        return copia_tablero        
             
    def shiftCopias(self,tableros,actual):
        copia_tableros  = tableros
        copia_tableros[0] = copia_tableros[1]
        copia_tableros[1] = copia_tableros[2]  
        copia_tableros[2] = actual
        return copia_tableros
    
    def esVidaEstatica(self,tableros,dim):
        tablero1 = tableros[0]
        tablero2 = tableros[1]
        actual = tableros[2]
        encontrado1 = True #para vida estatica
        encontrado2 = True #para oscilaciones nivel 2
        for x in range(dim):
            for y in range(dim):
                
                if actual.obtenerPosicion(x,y) != tablero2.obtenerPosicion(x,y):
                    encontrado1 = False
                    
        for x in range(dim):
            for y in range(dim):
                
                if actual.obtenerPosicion(x,y) != tablero1.obtenerPosicion(x,y):
                    encontrado2 = False            
        
        return encontrado1 or encontrado2
    
    def iniciarModoVidaEstatica(self):
        dim = self.tablero.obtenerDimension()
        self.getTablero().reiniciarTablero(dim)
        copia_tablero = Tablero(dim)
        cont = 0
        estaticas = 0
        for x in range(dim):
            for y in range(dim):
                copia_tablero.obtenerTablero()[x][y] = cont
                cont = cont +1
        self.clear()
        print("     muestra :",dim*dim,"   elementos: ",self.n,"     Control-c: volver al menu")
        self.dibujarTablero(dim)
        input("PRESIONE ENTER PARA COMENZAR")
    
        for tupla in self.combinations(range(dim*dim), self.n):
            self.getTablero().reiniciarTablero(dim) 
            self.gen = self.gen +1
            posiciones = []
            for num in tupla:
                #print(num)
                for x in range(dim):
                    for y in range(dim):
                        
                        if(copia_tablero.obtenerTablero()[x][y] == num):
                            
                            cordenadas = (x,y)
                            posiciones.append(cordenadas)
            """ barra"""
            
            for (x,y) in posiciones:
                self.getTablero().iniciarPosicion(x,y)
                
            
            
            actual_copia1 = self.copiarTablero(dim)
            self.analizarVecinos(dim)
            encontrado1 = True #para vida estatica
            for x in range(dim):
                for y in range(dim):
                
                    if actual_copia1.obtenerPosicion(x,y) != self.getTablero().obtenerPosicion(x,y) and encontrado1 == True:
                        encontrado1 = False
            
            
                        
            actual_copia2 = self.copiarTablero(dim)
            self.analizarVecinos(dim)
            #print(encontrado1)
            if(actual_copia2.estaVacio()):
                encontrado2 = False #para vida estatica
            else:
                encontrado2=True                        
            for x in range(dim):
                for y in range(dim):
                
                    if actual_copia2.obtenerPosicion(x,y) != self.getTablero().obtenerPosicion(x,y) and encontrado2 == True:
                        encontrado2 = False   
            
            
            
            actual_copia3 = self.copiarTablero(dim)
            self.analizarVecinos(dim)
            #print(encontrado2)
            if(actual_copia3.estaVacio()):
                encontrado3 = False #para vida estatica
            else:
                encontrado3=True  
            for x in range(dim):
                for y in range(dim):
                
                    if actual_copia3.obtenerPosicion(x,y) != self.getTablero().obtenerPosicion(x,y) and encontrado3 == True:
                        encontrado3 = False                 
            #print(encontrado3)
            
            actual_copia4 = self.copiarTablero(dim)
            self.analizarVecinos(dim)
            #print(encontrado1)
            if(actual_copia4.estaVacio()):
                encontrado4 = False #para vida estatica
            else:
                encontrado4=True                        
            for x in range(dim):
                for y in range(dim):
                
                    if actual_copia4.obtenerPosicion(x,y) != self.getTablero().obtenerPosicion(x,y) and encontrado4 == True:
                        encontrado4 = False   
            
            
            
            actual_copia5 = self.copiarTablero(dim)
            self.analizarVecinos(dim)
            #print(encontrado2)
            if(actual_copia5.estaVacio()):
                encontrado5 = False #para vida estatica
            else:
                encontrado5=True  
            for x in range(dim):
                for y in range(dim):
                
                    if actual_copia5.obtenerPosicion(x,y) != self.getTablero().obtenerPosicion(x,y) and encontrado5 == True:
                        encontrado5 = False 
            
                
            if(encontrado1 == True or encontrado2==True or encontrado3==True or encontrado4==True or encontrado5==True):
                self.getTablero().reiniciarTablero(dim)
                for (x,y) in posiciones:
                    self.getTablero().iniciarPosicion(x,y)
                estaticas = estaticas +1
                print("")
                print("Combinacion: ",self.gen,"   es vida estatica en [0-4] generaciones")
                
                self.dibujarTablero(dim)    
                
                       
            """for (x,y) in posiciones:
                self.getTablero().iniciarPosicion(x,y)    
            
            actual_copia1 = self.copiarTablero(dim)
            self.analizarVecinos(dim)
            encontrado1 = True #para vida estatica
            for x in range(dim):
                for y in range(dim):
                
                    if actual_copia1.obtenerPosicion(x,y) != self.getTablero().obtenerPosicion(x,y) and encontrado1 == True:
                        encontrado1 = False
            
            if(encontrado1 == True):
               
                estaticas = estaticas +1
                print("")
                print("Combinacion: ",self.gen)
                
                self.dibujarTablero(dim)
            """   
            time.sleep(self.sleep)
        print("Vidas estaticas: " ,estaticas,"                  ")  
        input("Se termino las combinaciones!!!")        
    
        
    def iniciarPasoAPaso(self):
        self.clear()
        dim = self.tablero.obtenerDimension()
        print("                   generacion: ",self.gen,"                     Control-c: volver al menu")
        #self.dibujarTablero(dim)
        
        while True:
            #self.gen = self.gen + 1
            self.clear()
            print("                    generacion: ",self.gen,"                     Control-c: volver al menu")
            self.dibujarTablero(dim)
            print("Seleccione una opcion: ")
            print("1.Agregar Celulas")
            print("2.Borrar celulas")
            print("3.Avanzar generacion")
            try:
                op = int(input("opcion: "))
                if op == 1:
                    self.getTablero().agregarCelulas()
                if op == 2:
                    self.getTablero().borrarCelulas()
                if op == 3:    
                #input("Presione enter")
                    self.analizarVecinos(dim)
                    self.gen = self.gen + 1
                    print("",end='')
                    print("\n",end='')
            except Exception:
                pass
            
    def iniciarHastaVidaEstatica(self):
        cont = 0
        dim = self.tablero.obtenerDimension()
        self.clear()
        print("                  generacion: ",self.gen,"                     Control-c: volver al menu")
        self.dibujarTablero(dim)
        input("PRESIONE ENTER PARA COMENZAR")
        tablero1 = self.copiarTablero(dim)
        tablero2 = self.copiarTablero(dim)
        actual = self.copiarTablero(dim)
        tableros = [tablero1,tablero2,actual]
        
        while True:
            #self.gen = self.gen +1
            actual = self.copiarTablero(dim)
            tableros  = self.shiftCopias(tableros, actual)
            encontrado = self.esVidaEstatica(tableros,dim) 
            if(encontrado == True and cont != 0):
                break
            self.clear()
            print("                  generacion: ",self.gen,"                             Control-c: volver al menu")
            """actual = self.copiarTablero(dim)
            tableros  = self.shiftCopias(tableros, actual)
            encontrado = self.esVidaEstatica(tableros,dim) 
            if(encontrado == True and cont != 0):
                break"""
            self.dibujarTablero(dim)
            time.sleep(self.sleep)
            self.analizarVecinos(dim)
            self.gen = self.gen +1
            """actual = self.copiarTablero(dim)
            tableros  = self.shiftCopias(tableros, actual)
            encontrado = self.esVidaEstatica(tableros,dim) 
            if(encontrado == True and cont != 0):
                break"""
            print("")
            #time.sleep(self.sleep)
            
            
            #self.analizarVecinos(dim)
            
            cont = cont +1
            print("\n",end='')     
        input("Juego finalizado!!!")
            
    def iniciar(self):
        dim = self.tablero.obtenerDimension()
        self.clear()
        print("                   generacion: ",self.gen,"                     Control-c: volver al menu")
        self.dibujarTablero(dim)
        input("PRESIONE ENTER PARA COMENZAR")
        
        while True:
            #self.gen = self.gen + 1
            #self.clear()
            #print("                                                              Control-c: volver al menu")
            #time.sleep(1)
            self.clear()
            print("                   generacion: ",self.gen,"                     Control-c: volver al menu")
            self.dibujarTablero(dim)
            time.sleep(self.sleep)
            self.analizarVecinos(dim)
            #enter = input("Presione enter")
            self.gen = self.gen + 1
            print("")
        
            print("\n",end='')        
                    
    
    
    def combinations(self,iterable, r):
        ''' combinations('ABCD', 2) --> AB AC AD BC BD CD
        combinations(range(4), 3) --> 012 013 023 123 
        La cantidad de combinaciones posibles es: N!/(N!*(N-r)!)
        donde N es la cantidad de elementos de iterable'''
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)
    
    def obtenerCantidadVecinos(self,x,y,dim):
        vecinos = 0
        """try:
            if(x-1<0 or x-1>=dim):
                raise IndexError
            elif(y-1<0 or y-1>=dim):
                raise IndexError
            
            if self.getTablero().obtenerPosicion(x-1,y-1) == "*":
                vecinos = vecinos + 1            
        except IndexError:
            print("Error: vecino fuera del rango del tablero")
        """
        if(x-1>=0 and x-1<dim) and (y-1>=0 and y-1<dim):
             
            if self.getTablero().obtenerPosicion(x-1,y-1) == "*":
                vecinos = vecinos + 1 
        
        
        if(x-1>=0 and x-1<dim) and (y>=0 and y<dim):
             
            if self.getTablero().obtenerPosicion(x-1,y) == "*":
                vecinos = vecinos + 1             
        
            #print("Error: vecino fuera del rango del tablero")
        
        
        if(x-1>=0 and x-1<dim) and (y+1>=0 and y+1<dim):

            if self.getTablero().obtenerPosicion(x-1,y+1) == "*":
                vecinos = vecinos + 1             
      
        
    
        if(x>=0 and x<dim) and (y+1>=0 and y+1<dim):
               
            if self.getTablero().obtenerPosicion(x,y+1) == "*":
                vecinos = vecinos + 1             

        
        
        if(x+1>=0 and x+1<dim) and (y+1>=0 and y+1<dim):
             
            if self.getTablero().obtenerPosicion(x+1,y+1) == "*":
                vecinos = vecinos + 1             

        
        
        if(x+1>=0 and x+1<dim) and (y>=0 and y<dim):
            
            if self.getTablero().obtenerPosicion(x+1,y) == "*":
                vecinos = vecinos + 1             
       
        
        
        if(x+1>=0 and x+1<dim) and (y-1>=0 and y-1<dim):
           
            if self.getTablero().obtenerPosicion(x+1,y-1) == "*":
                vecinos = vecinos + 1             
       
        
        
        if(x>=0 and x<dim) and (y-1>=0 and y-1<dim):
               
            if self.getTablero().obtenerPosicion(x,y-1) == "*":
                vecinos = vecinos + 1            
        
        
        return vecinos           