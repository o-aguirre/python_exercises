#Pide un numero y verifica si es positivo, negativo o cero.

try:
    num = int(input('Ingresa un numero: '))
    if num == 0:
        print('El numero ingresado es cero')
    elif num > 0:
        print('El numero ingresado es positivo')
    elif num < 0:
        print('El numero ingresado es negativo')
except:
    print('Debes ingresar un numero')


