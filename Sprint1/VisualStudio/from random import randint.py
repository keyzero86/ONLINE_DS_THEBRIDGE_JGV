from random import randint
# Genera un numero aleatorio del 1 al 5
random_number = randint(1, 5)

num_vidas = 5

print(random_number)

while (num_vidas >0):
    adivinar_num = input()
    print(type(random_number))
    try:
        print(type(int(adivinar_num)))
    except:
        print("Introduce un numero entero")
  
    else:
        if(int(adivinar_num) ==random_number):
            print("Numero adivinado")
            break
        else:
            print("MEEEEC!Error una vida menos")
            num_vidas = num_vidas -1