#Pide un caracter y determina si es una vocal

vocals = ['a', 'e', 'i', 'o', 'u']
caracter = input('Ingresa un caracter: ')

if caracter.lower() in vocals:
    print('Vocal')
else:
    print('Consonante')