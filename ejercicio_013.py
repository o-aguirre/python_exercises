# Reemplaza un caracter en una cadena

string = input('Ingresa un texto: ')
new_string = ''

for i in range(len(string)):
    if i % 2 != 0:
        new_string += '#'
    else:
        new_string += string[i]

print(new_string)

# Otra forma

string_2 = input('Ingresa un texto: ')
new_string_2 = string_2.replace('o', '0')
print(new_string_2)