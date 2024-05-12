# Convierte un número decimal a uno entero

try:
    num = float(input('Ingresa un número: '))
except:
    print('err')

new_num = int(num)
print(new_num)