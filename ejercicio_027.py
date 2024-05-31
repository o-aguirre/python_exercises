# Realiza operaciones básicas con conjuntos unión e intersección

conj_uno = {1, 2, 3}
conj_dos = {3, 4, 5}

union = conj_uno | conj_dos
interseccion = conj_uno & conj_dos
estricto = conj_uno ^ conj_dos
dif = conj_uno - conj_dos

print(union, interseccion, estricto, dif, sep='\n')
