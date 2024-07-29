#Solicita al usuario ingresar un numero N y luego imprime la suma
# de todos los numeros desde 1 hasta n

num = int(input('Ingresa un numero: '))
sum = 0

for i in range(num + 1):
    sum += i

print('La suma total es ' , sum)