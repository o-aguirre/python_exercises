# Ordena una lista de números de menor a mayor

lista = [2, 4, 3, 5, 1]
cambio = True

while cambio:
    cambio = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            cambio = True

print(lista)

# 2do método
lista_dos = [7, 9, 0, 6, 8]
lista_dos.sort()
print(lista_dos)