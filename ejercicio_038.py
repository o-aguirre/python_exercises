#Determina si un numero es divisible entre 5 y 7

num = int(input('Ingresa un numero: '))

if num % 5 == 0 and num % 7 == 0:
    print('El numero es divisible entre 5 y 7')
else:
    print('El numero no es divisible entre 5 y 7')