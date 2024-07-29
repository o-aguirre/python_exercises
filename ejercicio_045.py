#Imprime la tabla de multiplicar de un numero ingresado por el usuario

num = int(input('Ingresa un numero: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')