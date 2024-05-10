# Invertir una cadena

txt = input('Ingresa un texto: ')
largo_txt = len(txt) - 1

for i in txt:
    print(txt[largo_txt], end='')
    largo_txt -= 1

# 2da forma de lograrlo
txt_2 = input('Ingresa un texto: ')
inverted_txt = txt_2[::-1]
print(inverted_txt)
