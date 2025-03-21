import importlib
import variables
import tablero
import random

#Recarga los cambios del fichero varibles.py
importlib.reload(variables)
importlib.reload(tablero)


print("\033[32m---Inicio del Juego---")
#print('\033[32m Hello World but Red! \033[0m')
print("MENU:")
print("1. Empezar a Jugar")
print("2. Informacion")
print("0. Salir\033[0m")

def SubMenu1():
       print("\033[32m1. Para insertar barco Horinzontal")
       print("2. Para insertar barco Vertical\033[0m")
       #print("3. Mostrar Panel")
       eje = int(input())
       if eje == 1:
           print(" Horinzontal")
           eje = False
           print(" Cordenadas...")
           return eje
       elif eje ==2:
           print(" Vertical")
           eje =True
           print(" Cordenadas...")
           return eje
       #elif eje ==3:
          # t2jugador.PintarTablero()
          # SubMenu1()
               

Arranque = True
while Arranque == True:
    print("-----Estas en el Menú Principal----")
    evento1 = int(input())
    if evento1 == 2:
        print("     Dimension X: ",variables.DimensionX)
        print("     Dimension Y: ",variables.DimensionY)
    elif evento1 == 0:
        print("Cerrar")
        break
    elif evento1 == 1:
       print("---------A JUGAR!!!----------")
       print("      Vamos a poscionar los barcos.")

       t1 = tablero.tablero("CPU")   #Crear Tablero CPU

       ######
       #print("1.1. Para insertar barco Horinzontal")
       #print("1.2. Para insertar barco Vertical")
      # eje = int(input())
       #if eje == 1:
        #   print("Horinzontal")
       #    eje = False
       #    print("Cordenadas...")
       #elif eje ==2:
       #    print("Vertical")
       #    eje =True
       #    print("Cordenadas...")
        ######

       print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
       print("\nCPU:Colocando Barcos......")
       #BARCO 1 CPU
       randomX = random.randint(0, 9)
       randomY = random.randint(0, 9)
       t1.ColocarBarcoCPU(randomX ,randomY,4,False)
       #t1.PintarTablero()

        #BARCO 2 CPU
       randomX = random.randint(0, 9)
       randomY = random.randint(0, 9)
       t1.ColocarBarcoCPU(randomX ,randomY,4,False)
       #t1.PintarTablero()

        #BARCO 3 CPU
       randomX = random.randint(0, 9)
       randomY = random.randint(0, 9)
       t1.ColocarBarcoCPU(randomX ,randomY,3,False)
       #t1.PintarTablero()

        #BARCO 4 CPU
       randomX = random.randint(0, 9)
       randomY = random.randint(0, 9)
       t1.ColocarBarcoCPU(randomX ,randomY,2,False)
       #t1.PintarTablero()

        #BARCO 5 CPU
       randomX = random.randint(0, 9)
       randomY = random.randint(0, 9)
       t1.ColocarBarcoCPU(randomX ,randomY,1,False)

       t1.PintarTablero()




       
       print("\033[32m_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
       print("TURNO JUGADOR COLOCAR BARCOS")
       print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\033[0m")
       t2jugador = tablero.tablero("J1")   #Crear Tablero Jugador1

       print(t1.nombre)
       print(t2jugador.nombre)
    
       print("\n Colocar Barco Eslora 4 ")
       eje = SubMenu1()
       b4x = int(input())
       print(" Posicion X: ", b4x)
       b4y = int(input())
       print(" Posicion Y: ", b4y)
       t2jugador.ColocarBarco(b4x,b4y,4,eje)
       
       #t2jugador.PintarTablero()

       print("\n Colocar Barco Eslora 4b ")
       eje = SubMenu1()
       b2x = int(input())
       print(" Posicion X: ", b2x)
       b2y = int(input())
       print(" Posicion Y: ", b2y)
       t2jugador.ColocarBarco(b2x,b2y,4,eje)
       #t1.ColocarBarco(b2x,b2y,4,eje)
    
  
       #t2jugador.PintarTablero()
       print("Pulsa cualquir telca para continuar el juego...")
       input()
       #print("BARCO DE LA CPU............")
       TURNOS = 1
       while TURNOS < 4:
        print("\n#################################################")
        print("EMPIEZA EL TURNO Nº ", TURNOS)
        print("\n#################################################")
        # * Prueba disparo CPU  - FUNCIONA
        #t1.PintarTablero()
        t1.DispararBarcosCPU(t2jugador)
        t1.PintarTablero()




        #t1.PintarTablero()
         # * Prueba disparo JUGADOR - FUNCIONA

        print("\n JUGADOR -> CORDENADAS PARA DISPARAR:")
        print("X :")
        disparoX = int(input())
        print(disparoX)
        print("Y :")
        disparoY = int(input())
        print(disparoY)
        t2jugador.DispararBarcos(disparoX,disparoY,t1) 

        t2jugador.PintarTablero()

        TURNOS =TURNOS + 1

    ##### DISPARA CPU Seugndo disparo

       #t1.PintarTablero()
       #t1.DispararBarcosCPU(t2jugador)
       #t1.PintarTablero()


    #####



       #print("\n CORDENADAS PARA 2º DISPARAR:")
       #print("X :")
       #disparoX = int(input())
       #print(disparoX)
       #print("Y :")
       #disparoY = int(input())
       #print(disparoY)
       #t2jugador.DispararBarcos(disparoX,disparoY,t1) 

       #t1.DispararBarcos(disparoX,disparoY,t1)

       #t2jugador.PintarTablero()
       #t1.PintarTablero()
       print("#################FIN 4 TURNOS##############")
       

