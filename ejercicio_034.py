#Verifica si una cadena es mayor o igual a 10 caracteres

string = input('Ingresa un texto: ')

if len(string) == 10:
    print('La cadena contiene 10 caracteres')
if len(string) > 10:
    print('La cadena contiene mas de 10 caracteres')
else:
    print('La cadena contiene menos de 10 caracteres')