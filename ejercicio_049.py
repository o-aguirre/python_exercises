#Simular un lanzamiento de dado hasta obtener un 6

import random
dado = 0

while dado != 6:
    dado = random.randint(1, 6)
    print(dado)