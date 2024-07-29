#Solicita al usuario ingresar un número n e imprime el factorial de ese numero

num = int(input('Ingresa un numero: '))
mult = 1

for i in range(num, 0, -1):
    mult *= i

print(f'El factorial de {num} es: {mult}')