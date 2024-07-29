#Genera un numero aleatorio entre 1 y 10, luego pide al usuario adivinar el
#numero hasta que lo haga correctamente

import random

random_num = random.randint(1, 10)
trys = 0

while True:
    choice = int(input('Ingresa un numero: '))
    trys += 1
    if choice == random_num:
        print(f'Haz acertado! {choice} es el numero y te ha tomado {trys} intentos encontrarlo')
        break
    else:
        print('Intenta otra vez')