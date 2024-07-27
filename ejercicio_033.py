#Determina si un año es bisiesto
'''
-Divisible por 4
-No divisible por 100
-Divisible por 400
'''

year = int(input('Ingresa un año: '))

if year % 4 == 0 and year % 100 != 0:
    print('Año bisiesto')
else:
    print('no es año bisiesto')