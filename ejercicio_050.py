#Mostrar los numeros del 1 al 100, pero reemplazando los multiplos de 3 
#por 'Fizz' y los multiplos de 5 por 'Buzz'. Los multiplos de ambos imprime 'Fizz-Buzz'

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz-Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)