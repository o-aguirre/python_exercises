# Elimina duplicados de una lista

lista = [1, 1, 2, 2, 3]
new_lista = []

for i in lista:
    if i not in new_lista:
        new_lista.append(i)

print(new_lista)

# otra forma
new_lista = list(set(lista))
print(new_lista)