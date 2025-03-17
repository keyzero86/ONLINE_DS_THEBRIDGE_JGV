
import numpy as np
import importlib
import barcos
import random
importlib.reload(barcos)

class tablero:
    nombre = ""
    tablero1 = 0
    tablero1disparar = 0
    #tablero1 = np.full([10,10]," ")
    Contarbarcos = 0
    BarcosPosCPU = []
    #tablero1 = np.full([10,10]," ",dtype= str)
    def __init__(self,nombre):
        self.nombre = nombre
        self.tablero1 = np.full([10,10]," ")
        self.tablero1disparar = np.full([10,10]," ")

    def Mostrar(self):
        print(self.nombre)
        print
        pass

    def PintarTablero(self):
        print("TABLERO: ",self.nombre)
        print(":##########################################:")
        print(self.tablero1)
        print(":------------------------------:")
        print(self.tablero1disparar)
        print(":##########################################:")
        pass
    
    def LeerTablero(self,buscar): #Lee el Tablero y busca lo que indiques por parametro, O=Barco X=Tocado ' '=Por Descubrir -=Agua
        print("Leer Tablero...")
        for i, fila in enumerate(self.tablero1):  # Recorre con índice de fila
           for j, elemento in enumerate(fila):  # Recorre con índice de columna
                if buscar == elemento:
                    print(f" Encontrado {elemento} en la posición ({i}, {j})")

                    ##añadir posiciones de barcos en una lista
                    ##self.BarcosPosCPU.append([i,j])
                    ##print("EJEMPLO DE LISTAAAAA: ",self.BarcosPosCPU)
        pass
        #tablero.tablero("Mapear").LeerTablero
    def DispararBarcos(self, DisX, DisY,otrotablero): 
        turno = False
        #for i, fila in enumerate(self.tablero1):  # Recorre con índice de fila ###CUIDADOOO
        #while turno == 0:
        for i, fila in enumerate(otrotablero.tablero1):  # Recorre con índice de fila
                for j, elemento in enumerate(fila):  # Recorre con índice de columna
                     if DisX == i and DisY == j and elemento == "O":
                        #self.tablero1[i][j] = "X"
                        self.tablero1disparar[i][j] = "X"
                        print(" --------------------------------[X]")
                        #otrotablero.tablero1[i][j]= "P"
                        ###otrotablero.tablero1[i][j] = "X"
                        print(" ---------")
                        print(" TOCADO!!")
                        print(" ---------")
                        turno = True
                        #break
                        #print("\n J1 Vuelve a Disparar:")
                        #print("Cordenada X Y ->")
                        #self.DispararBarcos(input(),input(),otrotablero) #cuidado...
                        #turno = 1
                     elif DisX == i and DisY == j and elemento == " ":
                        #self.tablero1[i][j] = "-"
                        self.tablero1disparar[i][j] = "-"
                        print(" ---------")
                        print(" AGUA!!")
                        print(" ---------")
                        print("\n Pasamos el turno...")
                        #turno = 1
        return turno
        #pass


    def DispararBarcosCPU(self,otrotablero): 
        turno = False

        DisX= random.randint(0, 9)
        DisY= random.randint(0, 9)
        print("CPU ............DISPARA A LA CORDENADA X:", DisX ," Y: ", DisY)

        #for i, fila in enumerate(self.tablero1):  # Recorre con índice de fila ###CUIDADOOO
        #while turno == 0:
        for i, fila in enumerate(otrotablero.tablero1):  # Recorre con índice de fila
                for j, elemento in enumerate(fila):  # Recorre con índice de columna
                     if DisX == i and DisY == j and elemento == "O":
                        #self.tablero1[i][j] = "X"
                        self.tablero1disparar[i][j] = "X"
                        print(" --------------------------------[X]")
                        #otrotablero.tablero1[i][j]= "P"
                        ###otrotablero.tablero1[i][j] = "X"
                        print(" ---------")
                        print(" CPU: TOCADO!!")
                        print(" ---------")
                        turno = True
                        #break
                        #print("\n J1 Vuelve a Disparar:")
                        #print("Cordenada X Y ->")
                        #self.DispararBarcos(input(),input(),otrotablero) #cuidado...
                        #turno = 1
                     elif DisX == i and DisY == j and elemento == " ":
                        #self.tablero1[i][j] = "-"
                        self.tablero1disparar[i][j] = "-"
                        print(" ---------")
                        print(" CPU:     AGUA!!")
                        print(" ---------")
                        print("\n Pasamos el turno...")
                        #turno = 1
        return turno
    
    def ColocarBarco(self, posX, posY, eslora,vertical):
        x=0
        activar=True
        for i in range(len(self.tablero1)):  # Recorre las filas
             for j in range(len(self.tablero1[i])):  # Recorre las columnas

                while x < eslora and activar == True:
                    print("Dentro Bucle ColocarBarco.......!")
                    if (posX + eslora > 10) or (posY + eslora > 10):
                        print(posX," Eslora fuera de Rango....")
                        if (posX + eslora > 10):
                            print(" Introduce una posicion X valida: ")
                            posX= int(input())
                            activar = False
                            break
                        if(posY + eslora > 10):
                            print(" Introduce una posicion Y valida: ")
                            posY= int(input())
                            activar = False
                            break

                    if (self.tablero1[posX + x][posY] != "O"):
                        if vertical == True and self.tablero1[posX + x][posY] == "O":
                            print(" ERRRO! Posicion ocupada por un barco: ", posX, " ",posY)
                            break
                        elif vertical == True and self.tablero1[posX + x][posY] != "O":
                            self.tablero1[posX + x][posY] = "O"                        
                        if vertical == False and self.tablero1[posX][posY + x] == "O":
                            print(" ERRRO! Posicion ocupada por un barco: ", posX, " ",posY)
                            break                       
                        elif vertical == False and self.tablero1[posX][posY + x] != "O":
                            self.tablero1[posX][posY + x] = "O"
                            print("Pinta - - - - -  0")
                    x = x + 1

                    if x == eslora:
                        self.LeerTablero("O")
                        self.Contarbarcos = self.Contarbarcos + 1
                        #print("Eslora: ",eslora)
                        if vertical == False:
                            print(" Posicion en ",posX,"-",posY," = Barco Nº", self.Contarbarcos ," con Eslora->", eslora)
                            #print("PosX: ", posX)
                            #print("PosY: ",posY)
                            #activar= False
                            break
                        else:
                            print(f" Posicion en [{posX}][{posY}] = Barco Nº {self.Contarbarcos}con Eslora->{eslora}")
                            #print("PosX: ", posX)
                            #print("PosY: ",posY)
                            #activar= False
                            break
                     
        pass

    def ComprobarBarcoCPU(self,posX,posY,eslora):
        while (posX + eslora > 10) or (posY + eslora > 10): #if
                print(posX," CPU - Eslora fuera de Rango....")
                if (posX + eslora > 10):
                    print(" CPU - Introduce una posicion X valida: ")
                    posX= random.randint(0, 9)
                    return posX
                    #activar = False
                    break
                elif(posY + eslora > 10):
                    print(" CPU - Introduce una posicion Y valida: ")
                    posY= random.randint(0, 9)
                    return posY
                    #activar = False
                    break
        
        

    def ColocarBarcoCPU(self, posX, posY, eslora,vertical):
        x=0
        activar=True
        print("CPU: Colocar Barco de eslora ->",eslora)
        print("CPU...",posX,"-",posY,"H")

        if vertical == False:

            for i in range(len(self.tablero1)):  # Recorre las filas
                for j in range(len(self.tablero1[i])):  # Recorre las columnas
                    #print("J=",j)
                    while x < eslora and activar == True:


                        if (posX > 10) or (posY + eslora > 10): # Quitar eslora en la PosX porque es horinzontal?
                            print(posX,"CPU: Eslora fuera de Rango....")
                            ###if (posX + eslora > 10):
                               ### print("CPU - Introduce una posicion X valida: ")
                                ###posX= random.randint(0, 9)
                                ###print(posX)

                            while(posY + eslora > 10): ###if
                                print("CPU - Introduce una posicion Y valida: ")
                                posY= random.randint(0, 9)
                                print("---------- Y: ",posY)
                                #activar = False
                                ###if (posY + eslora < 10):
                                    ###break

                       # if (self.tablero1[posX + x][posY] != "O") and ((posX + x) < 10) and (posY < 10):  #parece ser q solo controla el horizontal el vertical mal revisar
                            #g= 0
                            #f=0
                            #if vertical == True and self.tablero1[posX + x][posY] == "O": #falta ejecutar random de nuevo,probando
                                #if g == 0:
                                   # print(" CPU - ERRRO! Posicion ocupada por un barco: ", posX, " ",posY)
                                   # g=1
                                    #break
                            
                                #self.ComprobarBarcoCPU(posX,posY,eslora)  
                            
                                # break
                            #elif vertical == True and self.tablero1[posX + x][posY] != "O":
                               # self.tablero1[posX + x][posY] = "O" 
                            ######### cambio a partir de aqui para horizontales
                        #posiblebarco = 0
                        #control = False
                        Comprobador = 0 ###
                        Nocolocar = False
                        Contar=0
                        ###if x < eslora:
                        
                        while Comprobador < eslora:###
                            
                            if self.tablero1[posX][posY + Comprobador] == "O":
                                print("CPU - POSICION OCUPADA POR BARCO + ESLERA")
                                #control = True
                                #break
                                Nocolocar = True
                                #Comprobador = Comprobador + 1
                            else:
                                Contar = Contar +1
                                #Nocolocar = True
                                
                          #SEGUIR aqui hay que comprobar al colocar barco que comprueba posiciones de eslera si hay barcooo
                                #if Comprobador == (eslora -1) and Nocolocar == False:
                                if Nocolocar == False and Contar == (eslora): #!!!!-1 (ES UNA PRUEBA SINO QUITAR -1)
                                #if self.tablero1[posX][posY + x] != "O":
                                    k = 0
                                    while k < Contar:
                                        self.tablero1[posX][posY + k] = "O"
                                        print("COLOCADO EN: ", posX ,"-",posY)
                                        k = k+1
                                    break
                                    


                            if Nocolocar == True and Contar == (eslora) or (Contar == 0 and eslora ==1): #!!!!-1
                                print("EJECUTAR RANDOM POSICION QUE NO EXISTA BARCO")
                                while self.tablero1[posX][posY + eslora] == "O" and self.tablero1[posX][posY] == "O":
                                    posX= random.randint(0, 9)
                                    posY= random.randint(0, 9)

                                Comprobador = -1 ###
                                Nocolocar = False
                                Contar=0
                                ###break
                            Comprobador = Comprobador + 1
                            print("Comprobrador", Comprobador)


                            #eslora = eslora + 1
                            #if x == eslora:
                            #    break



                            #if vertical == False and self.tablero1[posX][posY + x] == "O":
                             #   if f == 0:
                             #       print(" CPU - ERRRO! Posicion ocupada por un barco: ", posX, " ",posY)
                             #       break                    
                            #elif vertical == False and self.tablero1[posX][posY + x] != "O":
                             #   self.tablero1[posX][posY + x] = "O"

                        x = x + 1

                        if x == eslora:
                            ####print("COLOCADO EN: ", posX ,"-",posY)
                            self.LeerTablero("O")
                            self.Contarbarcos = self.Contarbarcos + 1
                            #print("Eslora: ",eslora)
                            if vertical == False:
                                print(" Posicion en ",posX,"-",posY," = Barco Nº", self.Contarbarcos ," con Eslora->", eslora)
                                #print("PosX: ", posX)
                                #print("PosY: ",posY)
                                #activar= False
                                break
                            else:
                                print(f" Posicion en [{posX}][{posY}] = Barco Nº {self.Contarbarcos}con Eslora->{eslora}")
                                #print("PosX: ", posX)
                                #print("PosY: ",posY)
                                #activar= False
                                break
        elif vertical == True:
            print(vertical)

                    
    pass





"""""
        x=0
        while x < eslora:
            if (posX + eslora > 10) or (posY + eslora > 10):
                print(posX," Eslora fuera de Rango....")
                if (posX + eslora > 10):
                    print("Introduce una posicion X valida: ")
                    posX= int(input())
                    break
                if(posY + eslora > 10):
                    print("Introduce una posicion Y valida: ")
                    posY= int(input())
                    break

            if (posX < 0) and (posY < 0) or (posX > 10) and (posY > 10):
                print("Barco Fuera del Tablero....")
                break            



            if (posX + x > -1 and posX + x < 10) and (posY + x > -1 and posY + x< 10):
                if(self.tablero1[posX + x][posY] != "O"):
                    if vertical == True and self.tablero1[posX + x][posY] == "O":
                        print("ERRRO! Posicion ocupada por un barco: ", posX, " ",posY)
                        break
                    elif vertical == True and self.tablero1[posX + x][posY] != "O":
                        self.tablero1[posX + x][posY] = "O"

                    if vertical == False and self.tablero1[posX][posY + x] == "O":
                        print("ERRRO! Posicion ocupada por un barco: ", posX, " ",posY)
                        break                       
                    elif vertical == False and self.tablero1[posX][posY + x] != "O":
                        self.tablero1[posX][posY + x] = "O"
                
                    
            else:
                print("-------------->Fuera de RANGO....")
                break

            x = x + 1
            if x == eslora:
                self.LeerTablero("O")
                print("Eslora: ",eslora)
                if vertical == False:
                    print("PosX: ", posX)
                    print("PosY: ",posY)
                    break
                else:
                    print("PosX: ", posX)
                    print("PosY: ",posY)
                    break
            

        pass
"""""



