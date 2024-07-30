#Simular un lanzamiento de una moneda

import random

moneda = random.randint(0, 1)
if moneda == 1:
    print('Cara')
else:
    print('Sello')