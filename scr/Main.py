import os
import shelve
from juego import Juego
from tablero import Tablero

class SistemaDeJuego(object):
    def __init__(self):
        self.juego = None #contendra la instancia del juego en ejecucion
        
    def guardarJuego(self,nom_juego):    
        db = shelve.open("datos.dat")
        db[nom_juego] = self.getJuego()
        db.close()
        
    def recuperarJuego(self,nom_juego):
        db = shelve.open("datos.dat")
        return db[nom_juego]
        
    def inicializarJuego(self,game):
        self.juego =game
    
    def clear(self):
        os.system('cls') # Windows
        
    def getJuego(self):
        return self.juego
    
    def menuPrincipal(self):
        while True:
            try:
                self.clear()
                print("***************************")
                print("*     MENU PRINCIPAL      *")
                print("***************************")
                print("*1.Iniciar un nuevo juego *")
                print("*2.Modo de vidas estaticas*")
                print("*3.Guardar juego          *")
                print("*4.Cargar juego           *")
                print("*5.Salir                  *")
                print("***************************")
            
                opcionMenu = int(input("Ingrese una opcion: "))
                if opcionMenu==1:
                    try:
                        dim = int(input("Ingrese la dimension del tablero nxn: "))
                        if(dim<=0):
                            raise Exception("Dimension invalida")
                        tablero = Tablero(dim)
                        print("Seleccione el modo de juego: ")
                        print("1.Celulas al azar")
                        print("2.Inicializar celulas")
                        print("")
                        op = int(input("opcion: "))
                        if op == 1:
                            cantidad = int(input("Cuantas celulas vivas desea en el tablero?? :"))
                            if(cantidad<0):
                                raise Exception("cantidad de celulas vivas invalida")
                            tablero.agregarCelulasRandom(cantidad)
                            print("Modos de juego")
                            print("1.normal")
                            print("2.paso a paso")
                            print("3.hasta encontrar vida estatica u oscilacion")
                            mode = int(input(""))
                            if mode == 1:
                      
                                game = Juego("normal",tablero)
                                self.inicializarJuego(game)
                                self.getJuego().iniciar()
                            elif mode == 2:
                                game = Juego("paso a paso",tablero)
                                self.inicializarJuego(game)
                                self.getJuego().iniciarPasoAPaso()
                            elif mode == 3:
                                game = Juego("hasta vida estatica",tablero)
                                self.inicializarJuego(game)
                                self.getJuego().iniciarHastaVidaEstatica() 
                            
                        elif op == 2:
                            tablero.agregarCelulas()
                            print("Modos de juego")
                            print("1.normal")
                            print("2.paso a paso")
                            print("3.hasta encontrar vida estatica u oscilacion")
                            mode = int(input(""))
                            if mode == 1:
                                
                                game = Juego("normal",tablero)
                                self.inicializarJuego(game)
                                self.getJuego().iniciar()
                            elif mode == 2:
                                game = Juego("paso a paso",tablero)
                                self.inicializarJuego(game)
                                self.getJuego().iniciarPasoAPaso()
                            elif mode == 3:
                                game = Juego("hasta vida estatica",tablero)
                                self.inicializarJuego(game)
                                self.getJuego().iniciarHastaVidaEstatica() 
                            #j = Juego("normal",tablero)
                            #sistema.inicializarJuego(j) #carga en el sistema el juego actual
                           
                            #sistema.obtenerJuego().iniciarPasoAPaso()
                    except KeyboardInterrupt:
                        pass
                    except KeyError:
                        print("Error al crear trayecto,no existe una ruta")     
                    except Exception as e:
                        print("error:",e) 
                    
                elif opcionMenu==2:
                    try:
                        dim = int(input("Ingrese la dimension del tablero nxn: "))
                        if(dim<=0):
                            raise Exception("Dimension invalida")
                        tablero = Tablero(dim)
                        n = int(input("Ingrese cantidad de celdas vivas del patron: "))
                        if(n<=0):
                            raise Exception("Cantidad de celulas invalidas invalida")
                        game = Juego("modo vida estatica",tablero)
                        game.setN(n)
                        self.inicializarJuego(game)
                        #print("adasdas")
                        self.getJuego().iniciarModoVidaEstatica()
                    except ValueError:
                        print("Id Invalido,ingrese nuevamente")  
                    except KeyError:
                        print("Error al agregar ruta al trayecto,no existe una ruta")          
                    except Exception as e:
                        print("Se ha producido un error: ",e)
                elif opcionMenu==3:
                    try:
                        nom = input("Ingrese el nombre con el que desea guardar el juego?? :")
                        self.guardarJuego(nom)
                    
                    except KeyboardInterrupt:
                        pass   
                    except KeyError:
                        print("Error al concatenar trayectos,no existe una ruta")        
                    except ValueError:
                        print("Id Invalido,ingrese nuevamente")
                    except Exception as e:
                        print("Error: ",e)             
                        
                elif opcionMenu==4:
                    try:
                        nom = input("Ingrese el nombre del juego a recuperar!! :")
                        juego = self.recuperarJuego(nom)
                        self.inicializarJuego(juego)
                        modo = self.getJuego().getMod()
                        if(modo == "normal"):
                            self.getJuego().iniciar()
                        elif(modo == "paso a paso"):    
                            self.getJuego().iniciarPasoAPaso()
                        elif(modo == "hasta vida estatica"):    
                            self.getJuego().iniciarHastaVidaEstatica()   
                        elif(modo == "modo vida estatica"):    
                            self.getJuego().iniciarModoVidaEstatica()       
                    except KeyboardInterrupt:
                        pass
                    except ValueError:
                        print("Id Invalido,ingrese nuevamente")
                    except Exception:
                        print("Error",e)    
                
                elif opcionMenu==5:
                    pass
                    break    
                
            except KeyboardInterrupt :
                pass      
            except Exception:
                print("Se produjo un error,elija nuevamente")
            
            
if __name__ == '__main__':
    sistema = SistemaDeJuego()
    sistema.menuPrincipal()
    
    