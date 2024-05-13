# Divide una cadena en una lista de sub-cadenas

txt = input('Ingresa un texto: ')

new_txt = []
for i in txt:
    new_txt.append(i)

print(new_txt)

# Segunda forma
txt_2 = input('Ingresa un texto : ')
new_txt_2 = txt_2.split()
print(new_txt_2)