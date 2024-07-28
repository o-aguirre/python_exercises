#Calcula el valor maximo entre 3 numeros

num1 = int(input('Ingresa un numero: '))
num2 = int(input('Ingresa un numero: '))
num3 = int(input('Ingresa un numero: '))

if num1 > num2 and num1 > num3:
    print('Primer valor es el mayor')
elif num2 > num1 and num2 > num3:
    print('Segundo valor es el mayor')
elif num3 > num2 and num3 > num1:
    print('Tercer valor es el mayor')

#Otra manera
maxim = max(num1, num2, num3)
print(maxim)