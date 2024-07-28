#Calcular el IMC e interpretarlo

weight = int(input('Ingresa tu peso: '))
height = float(input('Ingresa tu altura en metros: '))

imc = weight / (height ** 2)

if imc < 18.5:
    print('Bajo peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Normal')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidad')