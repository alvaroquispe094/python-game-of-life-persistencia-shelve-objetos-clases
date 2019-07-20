import random

class Tablero(object):
   
    def __init__(self, dim):
        self.celulas = 0
        self.vidasEstaticas = []
        self.dim = dim
        self.tablero = []
        for x in range(dim):
            fila = []
            for y in range(dim):
                
                fila.append("-")
            self.tablero.append(fila) #inicializa el tablero con todas las celulas vacias
        
    
    def agregarCelulasRandom(self, cantidad):
        for i in range(cantidad):
            x,y = self.getRandom(self.dim)
            self.tablero[x][y] = "*"
    
    def agregarCelulas(self):
        while True:
            try:
                
                x = int(input("Ingrese la fila con rango entre [1,"+str(self.dim)+"]: "))
                y = int(input("Ingrese la columna con rango entre [1,"+str(self.dim)+"]: "))
                if(x<1 or x>self.dim ):
                    input("Posicion invalida, presione enter para continuar")
                    raise IndexError
                print("")
                print("Ingrese cualquier cosa menos un numero para finalizar")
                self.tablero[x-1][y-1] = "*"
            
            except IndexError:
                pass    
            except Exception:
                break   
            
    def borrarCelulas(self):
        while True:
            try:
                
                x = int(input("Ingrese la fila entre [0,"+str(self.dim)+"]: "))
                y = int(input("Ingrese la columna entre [0,"+str(self.dim)+"]: "))
                if(x<1 or x>self.dim ):
                    input("Posicion invalida, presione enter para continuar")
                    raise IndexError
                print("")
                print("Inrese cualquier cosa menos un numero para finalizar")
                self.tablero[x-1][y-1] = "-"
            
            except IndexError:
                pass    
            except Exception:
                break   
            #try:
            #    x = int(input("cordenada x rango entre [0,dim]"))
            #    y = int(input("cordenada y rango entre [0,dim]"))
            #    print("")
            #    print("Inrese cualquier cosa menos un numero para finalizar")
            #    self.tablero[x][y] = "-"
            #except Exception:
            #    break        
    
    def getRandom(self,dim):
        return random.randrange(dim),random.randrange(dim)
    
    def reiniciarTablero(self,dim):
        self.tablero = []
        for x in range(dim):
            fila = []
            for y in range(dim):
                
                fila.append("-")
            self.tablero.append(fila) #inicializa el tablero con todas las celulas vacias
    
    def estaVacio(self):
        vacio = True
        for x in range(self.dim):
            for y in range(self.dim):            
                if self.obtenerTablero()[x][y] != "-":
                    vacio = False 
        return vacio
    
    def obtenerTablero(self):
        return self.tablero
    
    def setTablero(self,t):
        self.tablero = t
    
    def iniciarPosicion(self,x,y):
        self.tablero[x][y] = "*"
    
    def obtenerDimension(self):
        return self.dim
    
    def obtenerPosicion(self,x,y):
        return self.tablero[x][y]