# Cuenta lasocurrencias de un caracter especifico en un cadena

txt = input('Ingresa un texto: ')
cont = 0

for i in range(len(txt)):
    if txt[i] == 'e':
        cont += 1

print(cont)

# 2da forma de lograrlo

txt_2 = input('Ingresa un texto: ')
cont_occ = txt_2.count('e')
print(cont_occ)