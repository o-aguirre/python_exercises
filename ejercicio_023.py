# Verifica si una palabra es un palíndromo

word = input('Ingresa una palabra: ')
new_word = ''

for i in range(len(word) - 1, -1, -1):
    new_word += word[i]

# Otra forma
# es_pa = word == word[::-1]

if word == new_word:
    print('Haz encontrado una palabra palíndroma')
else:
    print('No es una palabra palíndroma')