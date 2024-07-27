#Pide un numero y comprueba si el numero es par o impar utilizando if y modulo

try:
    num = int(input('Ingresa un numero: '))
    if num % 2 == 0:
        print('El numero ingresado es par')
    else:
        print('El numero ingresado es impar')
except:
    print('Debes ingresar un numero')