# Invertir una cadena

txt = input('Ingresa un texto: ')
largo_txt = len(txt) - 1

for i in txt:
    print(txt[largo_txt], end='')
    largo_txt -= 1