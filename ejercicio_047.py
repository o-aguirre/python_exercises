#Hacer un menu de opciones que incluya la opcion de salir del programa

flag = True

while flag:
    opt = input('ingresa 1 para continuar: ')
    if opt != '1':
        flag = False